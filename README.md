# AI Legal Practice Skill (2026-style workflow)

This repo packages a **single agent skill** that encodes a practical, “small-firm-but-top-tier” legal workflow:
- severity-rated contract review
- last-minute demand letter / markup triage with cross-document conflict checks
- negotiation-ready counter-language
- redline package generation (revised .docx + human-readable redline report + optional Word *Compare* tracked-changes workflow)
- legal research memos with **anti-hallucination citation verification**
- client communications and policy/engagement-letter drafting

It is designed to be usable with **Claude Code / Claude Desktop skills**, **Codex-style agents**, and other agents that load `SKILL.md` instruction bundles.

> **Important**: This skill produces *draft* work product. It is not legal advice and is not a substitute for review by a licensed attorney. Always verify citations and confirm jurisdiction-specific requirements.

---

## What’s inside

- `skills/ai-legal-practice/` — canonical skill folder
- `.claude/skills/ai-legal-practice/` — same skill copied for Claude tooling
- `.github/skills/ai-legal-practice/` — same skill copied for GitHub/Codex-style discovery
- `scripts/` inside the skill — small helpers for docx outline extraction and redline reports

The scripts are optional; the skill also works in “no-tools” environments by producing structured drafts and checklists.

---

## Install

### Claude Code / Claude Desktop
Copy the folder into:
- `.claude/skills/ai-legal-practice/`

### Codex / GitHub skills
Copy the folder into:
- `.github/skills/ai-legal-practice/`

If your agent supports a different skills path, copy `skills/ai-legal-practice/` into that location.

---

## Use (examples)

### 1) Last-minute demand letter triage
Provide:
- the operative agreement(s)
- disclosure schedules / side letters / amendments (if any)
- the demand letter
- deal context (side, leverage, must-close vs. walk-away, key risk constraints)

Ask:
> “Map each proposed change against the current agreement and schedules. Flag contradictions, internal conflicts, and knock-on effects. Give severity ratings and counter-language.”

### 2) Full contract review from a specific side
Ask:
> “Review this services agreement from the vendor’s perspective. Flag risk shifts beyond market, missing provisions, and any definition/cross-reference issues. Provide severity ratings and counter-language.”

### 3) Produce a redline package
Ask:
> “Apply my selected positions to produce a revised .docx and a redline report. Include a clean cover email to opposing counsel.”

The skill will prefer:
1) produce a **revised .docx**, then
2) produce an **HTML redline report**, and
3) optionally instruct you to use Word’s **Compare** feature to generate official tracked changes.

---

## Scripts (optional)

From inside `skills/ai-legal-practice/scripts/`:

- `docx_extract_outline.py` — prints an outline (headings + paragraph indices) as JSON
- `docx_redline_report.py` — generates an HTML redline report comparing two `.docx` files

See `skills/ai-legal-practice/scripts/README.md`.

---

## License

MIT (see `LICENSE`).
