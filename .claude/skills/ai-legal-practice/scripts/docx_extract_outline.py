#!/usr/bin/env python3
"""
docx_extract_outline.py

Extract a simple outline from a .docx file:
- Heading paragraphs (based on style name like "Heading 1", "Heading 2", etc.)
- Paragraph index for each heading (0-based)
- Text preview

Usage:
  python docx_extract_outline.py path/to/file.docx > outline.json

Notes:
- This is a best-effort heuristic. Many legal docs use custom styles.
- If styles are non-standard, you can still use the "all_paragraphs" output.
"""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass, asdict
from typing import Any, List, Optional

try:
    from docx import Document  # type: ignore
except Exception as e:
    print("ERROR: python-docx is required. Install with: pip install python-docx", file=sys.stderr)
    raise


@dataclass
class Heading:
    index: int
    level: Optional[int]
    style: str
    text: str


def heading_level_from_style(style_name: str) -> Optional[int]:
    s = (style_name or "").strip().lower()
    # Common Word heading styles: "Heading 1", "Heading 2", etc.
    if s.startswith("heading"):
        parts = s.split()
        for p in parts:
            if p.isdigit():
                try:
                    return int(p)
                except ValueError:
                    pass
    return None


def main(argv: List[str]) -> int:
    if len(argv) != 2:
        print(__doc__.strip(), file=sys.stderr)
        return 2

    path = argv[1]
    doc = Document(path)

    headings: List[Heading] = []
    all_paragraphs: List[dict[str, Any]] = []

    for i, p in enumerate(doc.paragraphs):
        text = (p.text or "").strip()
        style_name = getattr(getattr(p, "style", None), "name", "") or ""
        level = heading_level_from_style(style_name)

        all_paragraphs.append(
            {
                "index": i,
                "style": style_name,
                "text": text,
            }
        )

        if level is not None and text:
            headings.append(Heading(index=i, level=level, style=style_name, text=text))

    out = {
        "file": path,
        "headings": [asdict(h) for h in headings],
        "all_paragraphs": all_paragraphs,
    }

    json.dump(out, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
