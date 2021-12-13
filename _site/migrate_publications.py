#!/usr/bin/env python
"""
Migrate publication list from SE3 website here
Note: this script will overwrite current yml file
Usage:
step 1: download the publication from wordpress in bibtex(.bib) format
step 2: execute below command with the correct path to the downloaded file:
  python migrate_publications.py --bib-path "/Users/menglin/Projects/website_conctribution/teachpress_pub_23092021.bib"

# TODO: how to add new publications
"""
import argparse
import yaml


def _extract(line):
    key = line.split(" ")[0]
    if key == "year":
        prefix = key + "  = {"
    else:
        prefix = key + " = {"
    value = line.split(prefix)[-1].split("},")[0]
    return key, value


def parse_bibtex(args):
    # get a list of publication dict
    # - title: How Kondo-holes create intense nanoscale heavy-fermion hybridization disorder
  # image: dummy.png
  # description: ""
  # authors: MH Hamidian, AR Schmidt, IA Firmo, MP Allan, P Bradley, JD Garrett, TJ Williams, GM Luke, Y Dubi, AV Balatsky, JC Davis
  # link:
  #   url: http://www.pnas.org/content/108/45/18233
  #   display:  PNAS 108, 18233 (2011)
  # highlight: 0
  # news2:
    print("Step 1.1: Reading publications from {}".format(args.bib_path))

    with open(args.bib_path, "r") as f:
        lines = f.readlines()
    pub_list = []  # a list of dict
    pub_years = []

    previous_l = ""
    for line in lines:
        line = line.strip()
        if line.startswith("%") or len(line.strip()) == 0:
            continue

        if line.startswith("@"):
            # initialize a new dict
            pub_dict = {}
            pub_dict["pub_type"] = line.split("@")
            pub_dict["ref"] = line.split("{")[-1].split(",")[0]
            pub_dict["pub_type"] = line.split("@")[-1].split("{")[0]
        elif line.startswith("}"):
            pub_list.append(pub_dict)

        elif not line.endswith("},") and not line.startswith("keywords"):
            # which means this line is not finished
            previous_l = line
        else:
            # title, author, url, year, date, booktitle, address, note, and keywords
            if not line.endswith("},"):
                line = line + ","
            k, v = _extract(previous_l + line)
            previous_l = ""

            if k == "url":
                # TODO: may need to update url to other domain?
                pub_dict["link"] = {"url": v, "display": "PDF"}
            elif k == "author":
                v = v.replace("{", "")
                v = v.replace("}", "")
                v = v.replace("*", "\*")  # to properly disply * in markdown
                pub_dict[k] = v.replace(" and", ",")
            elif k == "note":
                pub_dict[k] = ", (" + v + ")"
            elif k == "abstract":
                continue
            elif k == "year":
                pub_years.append(v)
                pub_dict[k] = v
            else:
                pub_dict[k] = v

    pub_years = sorted(list(set(pub_years)), reverse=True)
    print("...parsed {} publications".format(len(pub_list)))

    print("Step 1.2: Unifying different pub_types for proper display")
    """
    author
    **title**
    venue, year, note
    link

    Following types are currently supported:
    {
    'inproceedings', 'conference', 'article','techreport',
    'book','inbook','incollection',
    'phdthesis', 'mastersthesis'
    }
    """
    unified_pub_list = []
    for pub_dict in pub_list:
        if "author" in pub_dict and "Belongie" not in pub_dict["author"]:
            print(pub_dict)
            continue

        p_type = pub_dict["pub_type"]
        if p_type == "conference" or p_type == "inproceedings":
            # venue = "{booktile / publisher}, {address}". e.g. CVPR, Salt Lake City, UT
            # if there is no venue provided, will raise error
            if "booktitle" in pub_dict:
                v_key = "booktitle"
            elif "publisher" in pub_dict:
                v_key = "publisher"
            else:
                raise ValueError("the conference bibtax does not contain booktitle or publisher information:\n", pub_dict)
            pub_dict["venue"] = pub_dict[v_key]

            if "address" in pub_dict:
                pub_dict["venue"] += ", {}".format(pub_dict["address"])

            pub_dict["venue"] += ", "

        elif p_type == "techreport":
            # venue = "{insitituion} ({number})" or "({number})" or " "

            if "institution" in pub_dict:
                venue_str = pub_dict["institution"]
            else:
                venue_str = ""

            if "number" in pub_dict:
                if len(venue_str) > 0:
                    venue_str += " "
                venue_str += "({})".format(pub_dict["number"])

            if len(venue_str) > 0:
                pub_dict["venue"] = venue_str + ", "
            else:
                pub_dict["venue"] = " "

        elif p_type == "article":
            # venue = "{journal/publisher}, {volumn} ({number})"
            # if there is no venue provided, will raise error
            if "journal" in pub_dict:
                venue_str = "{}".format(pub_dict["journal"])
            elif "publisher" in pub_dict:
                venue_str = "{}".format(pub_dict["publisher"])
            else:
                venue_str = ""

            if "volume" in pub_dict:
                venue_str += ", {}".format(pub_dict["volume"])
                if "number" in pub_dict:
                    venue_str += " ({})".format(pub_dict["number"])
            pub_dict["venue"] = venue_str + ", "

        elif p_type == "book" or p_type == "inbook":
            # "{booktitle}, {publisher}" or "{publisher}"
            if "booktitle" in pub_dict:
                venue_str = pub_dict["booktitle"]
            else:
                venue_str = ""

            if "publisher" in pub_dict:
                if len(venue_str) > 0:
                    venue_str += " "
                venue_str += pub_dict["publisher"]

            if len(venue_str) > 0:
                pub_dict["venue"] = venue_str + ", "
            else:
                pub_dict["venue"] = " "


        elif p_type == "incollection":
            # only one
            # Large-Scale Visual Geo-Localization, pp. 59-76, Springer, 2016.
            # "{booktitle}, pp. {pages}, {publisher}, "
            pub_dict["venue"] = "{}, pp. {}, {}, ".format(
                pub_dict["booktitle"],
                pub_dict["pages"],
                pub_dict["publisher"]
            )

        elif "thesis" in p_type:
            # Cornell University, 2014, (MEng Project Report).
            # {school}
            pub_dict["venue"] = "{}, ".format(pub_dict["school"])

        if "link" not in pub_dict:
            pub_dict["link"] = {"url": "", "display": "PDF"}
        unified_pub_list.append(pub_dict)

    print("...transformed {} publications".format(len(unified_pub_list)))
    return unified_pub_list, pub_years


def write_yaml(pub_list, pub_years):
    yml_path = "_data/publist.yml"

    with open(yml_path, 'w') as file:
        yaml.dump(pub_list, file)
    print("Step 2.1: written to {}".format(yml_path))

    yml_path = "_data/pubyears.yml"

    with open(yml_path, 'w') as file:
        yaml.dump(pub_years, file)
    print("Step 2.2: written to {}".format(yml_path))


def main():
    parser = argparse.ArgumentParser(description='Publication migration parser')
    parser.add_argument('--bib-path', default="", type=str,
                        help='Path to the txt file downloaded from SE3 website')
    args = parser.parse_args()

    pub_list, pub_years = parse_bibtex(args)
    write_yaml(pub_list, pub_years)


if __name__ == '__main__':
    main()
