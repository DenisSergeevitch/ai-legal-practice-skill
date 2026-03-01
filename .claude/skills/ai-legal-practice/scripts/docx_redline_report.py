#!/usr/bin/env python3
"""
docx_redline_report.py

Generate an HTML "redline" report comparing two .docx files (Original vs Revised).

This is not native Word tracked changes; it is a paragraph/text-level diff
intended for quick review and negotiation packaging.

Usage:
  python docx_redline_report.py Original.docx Revised.docx --out Redline.html

Exit codes:
  0 success
  2 usage error
  1 runtime error
"""

from __future__ import annotations

import argparse
import difflib
import html
import sys
from pathlib import Path
from typing import List

try:
    from docx import Document  # type: ignore
except Exception:
    print("ERROR: python-docx is required. Install with: pip install python-docx", file=sys.stderr)
    raise


def extract_paragraph_lines(path: Path) -> List[str]:
    doc = Document(str(path))
    lines: List[str] = []
    for p in doc.paragraphs:
        t = (p.text or "").rstrip()
        # Keep blank lines to preserve spacing, but collapse runs of blanks later.
        lines.append(t)
    # Optional: trim trailing blank lines
    while lines and lines[-1] == "":
        lines.pop()
    return lines


def build_html_diff(original_lines: List[str], revised_lines: List[str], fromdesc: str, todesc: str) -> str:
    differ = difflib.HtmlDiff(tabsize=2, wrapcolumn=120)
    table = differ.make_table(
        fromlines=original_lines,
        tolines=revised_lines,
        fromdesc=html.escape(fromdesc),
        todesc=html.escape(todesc),
        context=True,
        numlines=2,
    )

    # Light CSS to make it readable
    css = """
    body { font-family: -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif; margin: 24px; }
    h1 { font-size: 18px; margin: 0 0 12px 0; }
    .meta { color: #444; margin-bottom: 16px; }
    table.diff { width: 100%; border-collapse: collapse; font-size: 12px; }
    .diff_header { background: #f0f0f0; }
    td, th { border: 1px solid #ddd; padding: 4px 6px; vertical-align: top; }
    .diff_add { background: #e6ffed; }
    .diff_sub { background: #ffeef0; }
    .diff_chg { background: #fff5b1; }
    """
    return f"""<!doctype html>
<html>
<head>
<meta charset="utf-8" />
<title>Redline report</title>
<style>{css}</style>
</head>
<body>
<h1>Redline report (Original vs Revised)</h1>
<div class="meta">
  <div><strong>Original:</strong> {html.escape(fromdesc)}</div>
  <div><strong>Revised:</strong> {html.escape(todesc)}</div>
  <div><strong>Notes:</strong> This is a text-level diff, not Word tracked changes.</div>
</div>
{table}
</body>
</html>
"""


def main(argv: List[str]) -> int:
    parser = argparse.ArgumentParser(description="Generate an HTML redline report comparing two .docx files.")
    parser.add_argument("original", type=Path, help="Path to Original.docx")
    parser.add_argument("revised", type=Path, help="Path to Revised.docx")
    parser.add_argument("--out", type=Path, required=True, help="Output HTML file path")
    args = parser.parse_args(argv[1:])

    if not args.original.exists():
        print(f"ERROR: original file not found: {args.original}", file=sys.stderr)
        return 1
    if not args.revised.exists():
        print(f"ERROR: revised file not found: {args.revised}", file=sys.stderr)
        return 1

    try:
        original_lines = extract_paragraph_lines(args.original)
        revised_lines = extract_paragraph_lines(args.revised)
        html_out = build_html_diff(
            original_lines=original_lines,
            revised_lines=revised_lines,
            fromdesc=str(args.original),
            todesc=str(args.revised),
        )
        args.out.write_text(html_out, encoding="utf-8")
        return 0
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
