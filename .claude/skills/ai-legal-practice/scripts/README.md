# Scripts

These helpers are optional. They are designed to be small, readable, and safe.

## Requirements

```bash
pip install python-docx
```

(If your agent environment already has `python-docx`, you can skip.)

## 1) Extract a document outline (headings)

```bash
python docx_extract_outline.py path/to/Agreement.docx > outline.json
```

Outputs JSON including detected headings and their paragraph indices.

## 2) Generate an HTML redline report (Original vs Revised)

```bash
python docx_redline_report.py Original.docx Revised.docx --out Redline.html
```

Open `Redline.html` in a browser.

### Notes / limitations
- The redline is a text-level comparison (paragraph-based). It is not native Word tracked changes.
- If you need native tracked changes, use Word **Review → Compare** on Original vs Revised (see `../references/redline_workflow.md`).
