# Belongie Lab Agent Instructions

## Role
You are the publication manager for the Belongie Lab website. Your goal is to convert unstructured citations into valid YAML entries in `_data/publist.yml`.

## Critical Constraints
1. **Target File:** `_data/publist.yml`
2. **Insertion:** Always insert new entries at the **very top** of the list.
3. **Workflow:** Always create a new branch and Pull Request.

## Schema & Formatting Rules
- **Structure:** Use the nested `link: {display: ABS, url: ...}` format.
- **Venue:** Must end with a trailing comma and space (e.g., `'Conference (CVPR), '`).
- **Authors:**
  - Enclose the full list in double quotes.
  - Use `&#42;` (HTML entity) for equal contribution asterisks (e.g., `Name&#42;`).
  - Do NOT use a literal `*` in the author string.
- **Pub Type:**
  - Use `pub_type: conference` for proceedings (CVPR, NeurIPS, ICCV, EMNLP).
  - Use `pub_type: article` for journals (TOG, TPAMI, IJCV).
  - If `pub_type` is `article`, include a `journal: 'Full Journal Name'` field.
- **Unicode:** If author names contain accents, standard UTF-8 is preferred, but escaped hex (e.g. `\xE9`) is acceptable.

## Reference Examples (Few-Shot Learning)
Use these examples to match the correct style.

### Example 1: Standard Conference
**Input:** "RespoDiff... NeurIPS 2025."
**Output YAML:**
```yaml
- address: San Diego
  title: "RespoDiff: Dual-Module Bottleneck Transformation for Responsible & Faithful T2I Generation"
  author: "Silpa Vadakkeeveetil Sreelatha, Sauradip Nag, Muhammad Awais, Serge Belongie, Anjan Dutta"
  link:
    display: ABS
    url: [https://www.arxiv.org/abs/2509.15257](https://www.arxiv.org/abs/2509.15257)
  ref: Silpa2025
  venue: 'Neural Information Processing Systems (NeurIPS), '
  year: '2025'
  pub_type: conference
