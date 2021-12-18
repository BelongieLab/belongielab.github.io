# FAQ
## How to add new publications?

The main files to modify for new publications are: [`_data/publist.yml`](https://github.com/BelongieLab/belongielab.github.io/blob/main/_data/publist.yml) and [`_data/pubyears.yml`](https://github.com/BelongieLab/belongielab.github.io/blob/main/_data/pubyears.yml). 

**Step 1**: Append new publication to [`_data/publist.yml`](https://github.com/BelongieLab/belongielab.github.io/blob/main/_data/publist.yml). Each publication will be displayed as:

```markdown
author
**title**
venue year. / venue year note.
link
```

The required keys for each publication are: 

| Name   | Note for proper display                                      | Example                                                      |
| ------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| author | Each name follows: `"{first_name} {last_name}"`;  <br />Names are seperated with `", "`; <br />Equal contribution: pls add `"\*"` after name. | `"Katie Luo\*, Guandao Yang\*, Wenqi Xian, Harald Haraldsson, Bharath Hariharan, Serge Belongie"` |
| title  |                                                              | `"Stay Positive: Non-Negative Image Synthesis for Augmented Reality"` |
| venue  | Follow the format: `"{venue_str}, "`; <br />See table below for specifications of different publication types;<br />Set to " " if there is nothing to add here. | `"Computer Vision and Pattern Recognition (CVPR), Virtual, "` |
| year   |                                                              | `'2021'`                                                     |
| note   | Follow the format:  `, (note_str)`<br />Leave this field out if there is nothing to add here. | `', (Oral, *Equal Contribution)'`                            |
| link   | Follow the format: `{"url": url_str, "display": "PDF"}`;<br />`url_str = ""` if there is no pdf. |                                                              |



| Publication type            | Venue = `"{venue_str}, "`                                    | Example                                                      |
| --------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| conference or inproceedings | `venue_str = "{booktitle/publisher}, {address}"`  or `"{booktitle/publisher}"` | `"International Conference on Computer Vision (ICCV), Virtual, "` |
| techreport                  | `venue_str = "{institution} ({number})"`  or  `"({number})"` | `"(CS2007-090), "`                                           |
| article                     | `venue_str = "{journal/publisher}, {volumn} ({number})"`  or  `"{journal/publisher}, {volumn}"`  or `"{journal/publisher}"` | `"IEEE Transactions on Pattern Analysis and Machine Intelligence, 24 (4), "` |
| book or inbook              | `venue_str = "{booktitle}, {publisher}"`  or  `"{publisher}"` | `"Methods of Microarray Data Analysis II Kluwer Academic, "` |
| incollection                | `venue_str = "{booktitle}, pp. {pages}, {publisher}"`        | `"Large-Scale Visual Geo-Localization, pp. 59-76, Springer, "` |
| thesis                      | `venue_str = "{school}"`                                     | `"Cornell University, "`                                     |

**Step 2**: If the year of the publication is different from all the previous ones, please append the new year to [`_data/pubyears.yml`](https://github.com/BelongieLab/belongielab.github.io/blob/main/_data/pubyears.yml).