---
name: ai-legal-practice
description: Drafting + analysis workflow for attorneys: contract review, change-mapping, negotiation counter-language, redline package generation, research memos with citation verification, client communications, and policy/engagement-letter drafting. Requires attorney supervision; do not treat outputs as legal advice.
version: 0.2.0
---

# AI Legal Practice Skill

## Purpose

This skill encodes a practical “AI-first” legal workflow:

- **Triage fast** (including last-minute demands and aggressive markups)
- **Map changes across documents** (agreement ↔ schedules ↔ side letters ↔ emails)
- **Flag conflicts and knock-on effects**
- **Draft negotiation-ready counter-language**
- **Generate a response package** (revised document(s) + redline report + cover email)
- **Draft research memos** with built-in **anti-hallucination verification**
- **Draft client communications and policies** in a clear, pragmatic voice

This skill is designed to be used by (or under the supervision of) a **licensed attorney**.

## Safety and professional responsibility

1) **Not legal advice.** Output is draft work product; it must be reviewed and approved by a lawyer responsible for the matter.

2) **No hallucinated authorities.** For research tasks:
- Never invent case names, statutes, regulations, agency guidance, docket numbers, pin cites, or quotes.
- If you cannot verify an authority, label it **UNVERIFIED** and do not rely on it for conclusions.

3) **Confidentiality.**
- Treat all provided materials as confidential/privileged.
- Do not paste client-identifying facts into external systems unless the user explicitly indicates it is permitted.
- Follow the user’s organization policies for retention, training opt-out, and DPA/BAA requirements.

4) **Jurisdiction and scope.**
- Ask for jurisdiction or clearly state assumptions.
- If the user is not a lawyer, provide general educational information and recommend consulting counsel.

## When to use

Use this skill when the user is doing legal work such as:
- reviewing or negotiating contracts
- responding to demand letters and disputes based on contract language
- preparing closing sets and deliverables
- drafting client emails, board consents, policies, engagement letters
- preparing legal research memos that must be citation-accurate

## When NOT to use

Do not use this skill to:
- provide final legal conclusions without attorney review
- give jurisdiction-specific advice to non-lawyers
- produce filings without verification and compliance checks
- generate or rely on unverified citations

## Operating modes

Many agent environments have different interaction styles. Map this to your environment:

### Mode A — Interactive (chat)
Use for analysis, negotiation strategy, and drafting with the lawyer in the loop.

### Mode B — Workspace / batch (autonomous over files)
Use when the user points you at a folder and wants:
- a full redline package
- assembling closing deliverables
- bulk formatting/cleanup
- generating multiple drafts

### Mode C — Dev / automation (terminal access)
Use when you can run scripts to manipulate `.docx` or produce reports.

If you can’t run code, still follow the same workflow and produce structured drafts + instructions.

---

# Default intake (always do this first)

Collect or infer (and explicitly state) the following:

1) **Matter type**: services/SaaS, stock purchase, asset purchase, financing, employment, NDA, policy, dispute letter, etc.
2) **Side**: vendor/customer, buyer/seller, company/employee, licensor/licensee, plaintiff/defendant, etc.
3) **Leverage / objectives**: must-close vs. willing to walk; time pressure; reputational constraints.
4) **Risk posture**: conservative/balanced/aggressive; deal value and worst-case downside.
5) **Jurisdiction** (if relevant).
6) **Document set**: what is authoritative (agreement + exhibits/schedules + amendments + emails/side letters).
7) **Output requested**: issue-spotting only, negotiation language, redline package, memo, email, policy, etc.

If any items are missing, proceed using **explicit assumptions** and mark them as assumptions.

---

# Core workflow

## Phase 1 — Normalize the record

1) Identify all operative documents and their hierarchy:
- Agreement + exhibits/schedules
- Side letters / amendments (later-in-time controls for conflicts)
- Term sheet (if applicable)
- Markups / demand letter
- Email thread (facts and admissions)

2) Build a cross-reference map:
- defined terms
- section cross-references
- exhibits/schedules references
- “survival”, “materiality”, “knowledge” qualifiers

3) Flag “gotchas” early:
- conflicting definitions
- stale cross-references (e.g., Section numbers that no longer exist)
- inconsistent party names/entity types
- missing exhibits that are referenced but not included

## Phase 2 — Do the legal work

Select the correct playbook:

- **Playbook 1**: Rapid change-map + conflict scan (last-minute demand / markup)
- **Playbook 2**: Full contract review (severity + missing provisions + market sanity check)
- **Playbook 3**: Redline package generation (revised doc + redline report + cover email)
- **Playbook 4**: Real-time drafting stress test (avoid unintended concessions)
- **Playbook 5**: Research memo (parallel research + verification)
- **Playbook 6**: Client communications (clear risk framing)
- **Playbook 7**: Policy / engagement letter drafting (AI clause included)

## Phase 3 — Quality control before delivering

Run these checks:

1) **Internal consistency**
- defined terms used consistently
- cross-references resolve
- no contradictions created by proposed edits

2) **Scope and assumptions**
- assumptions are explicit
- jurisdiction identified or stated as assumed
- “not legal advice / needs review” where appropriate

3) **Citation integrity** (research outputs)
- every citation verified or labeled UNVERIFIED
- no fabricated quotes or pinpoint cites

4) **Client usability**
- BLUF summary
- clear recommendations
- “fight vs. concede” guidance where requested
- questions for client listed explicitly

---

# Playbook 1 — Rapid change-map + conflict scan (the “7 PM demand letter” scenario)

## Goal
Given a demand letter or proposed restructure, quickly:
- map each proposed change to existing terms
- identify contradictions with schedules/side letters
- spot internal conflicts created by proposed language
- produce negotiation-ready counter-positions

## Steps

1) **Extract proposed changes**
- List each requested change as a discrete item.
- If the change is embedded in narrative prose, rewrite it as: “Change X: [plain English].”

2) **Map to agreement**
For each change:
- current section(s) impacted
- related defined terms
- downstream sections that depend on it (indemnities, remedies, survival, closing conditions, etc.)

3) **Cross-document conflict scan**
Check whether the change contradicts:
- disclosure schedules (reps, exceptions, known issues)
- side letters/amendments
- fundamental reps section
- closing deliverables list
- any “no conflict / no adverse change” reps that the requesting party has already confirmed

4) **Knock-on effects**
Explicitly answer: “If we accept this, what breaks elsewhere?”
Common examples:
- adding an escrow condition changes “closing mechanics” and may affect termination rights
- widening indemnity carve-outs may conflict with limitation of liability
- changing deliverables can silently shift timing obligations and default triggers

5) **Output: counter-positions package**
Provide:
- severity rating per change (CRITICAL / HIGH / MEDIUM / LOW)
- why it matters, in deal terms
- proposed counter-language (or alternative formulations)
- tradeoffs: what we can concede vs. where to hold firm
- cross-references to the other side’s own documents where their request creates contradictions

## Output format (use this exact structure)

### Proposed Change 1 — [short title] — [SEVERITY]
- **What they want**:
- **Where it hits** (sections/defined terms):
- **What it does to risk**:
- **Conflicts / contradictions** (agreement ↔ schedules ↔ side letters):
- **Knock-on effects**:
- **Counter-position** (plain English):
- **Proposed counter-language** (draft clause text):
- **Negotiation note** (fight / concede / trade for X):
- **Questions for client**:

---

# Playbook 2 — Full contract review (severity + missing provisions + market sanity)

## Goal
Deliver a review that is immediately usable for negotiation:
- severity-rated issues
- market sanity check (where appropriate)
- missing-provisions checklist
- concrete counter-language

## Steps

1) Confirm perspective (e.g., “vendor with limited leverage; wants to close”).
2) Identify and prioritize the “risk movers”:
- indemnification scope + carve-outs
- limitation of liability (cap + exclusions)
- IP ownership/license scope
- data security, privacy, incident response
- termination rights + payment on termination
- assignment / change of control
- warranties, disclaimers, acceptance criteria
- remedies, specific performance, injunctive relief
- governing law / venue / arbitration
3) Run missing-provisions checklist (see `references/contract_review_checklist.md`).
4) Produce counter-language for high-severity items.
5) Provide a “concession map”: what can be given, and what to ask for in return.

## Output format (use this exact structure)

## BLUF
- **Top 3–5 issues** (one line each)
- **Deal context assumptions**
- **Overall posture recommendation** (aggressive/balanced/conservative)

## Issues (severity-rated)

### [CRITICAL] Issue — [short title]
- **Location**:
- **What the clause does now**:
- **Why it matters** (practical + legal):
- **Market sanity check** (if applicable):
- **Cross-impacts**:
- **Proposed counter-language**:
- **Fallback positions** (Option A / B / C):
- **Trade suggestions**:
- **Questions for client**:

(Repeat for HIGH / MEDIUM / LOW)

## Missing / weak provisions checklist
- List missing or unusually weak provisions and why they matter.

## Quick win edits
- Typos, definition fixes, cross-reference repairs, clarity edits.

---

# Playbook 3 — Redline package generation (revised doc + redline report + cover email)

## Goal
Produce a sendable negotiation package:
1) Revised document(s)
2) Redline report (human-readable)
3) Cover email to opposing counsel (or to client)

## Strategy for “tracked changes”
Many environments cannot reliably generate native Word tracked-changes markup. Use this robust path:

- Create a **revised `.docx`** that incorporates the selected edits.
- Create an **HTML redline report** comparing original vs revised.
- If the user needs “real” tracked changes, instruct them to run **Word → Review → Compare** on the two files to generate an official tracked-changes doc (see `references/redline_workflow.md`).

## Steps

1) Confirm the selected positions (which options to adopt).
2) Apply edits into a revised draft (preserve numbering/cross-refs as best as possible).
3) Generate:
- `Revised.docx`
- `Redline.html` (or `.md`)
- `Cover_Email.md`

If you have terminal access, use:
- `scripts/docx_redline_report.py` to generate the HTML redline.

---

# Playbook 4 — Real-time drafting stress test (avoid unintended concessions)

## Goal
While drafting a response letter/email, detect hidden concessions.

## Steps
For each draft paragraph:
1) Identify what the paragraph asserts, denies, or concedes.
2) Map it to the agreement sections it touches.
3) Ask: does this create any implied admission that harms another position?
4) Rewrite to preserve the intended argument while avoiding collateral damage.

## Output format
- **Paragraph**: [quote or summary]
- **Potential unintended implication**:
- **Risk** (LOW/MED/HIGH):
- **Safer rewrite**:
- **Notes**:

---

# Playbook 5 — Research memo with verification (anti-hallucination)

## Goal
Produce a memo that is usable in real practice:
- parallel research plan
- primary authority first
- explicit uncertainty flags
- built-in verification pass

## Steps

1) Build an issue tree (sub-questions).
2) For each sub-question, identify likely authorities:
- statutes + regs
- agency guidance
- case law
- enforcement actions / no-action letters (if relevant)
3) Research in parallel (separate sections per sub-topic).
4) Draft memo.
5) **Verification pass** (mandatory):
- For every citation: confirm the authority exists and supports the statement.
- If you cannot confirm, label it **UNVERIFIED** and do not use it for conclusions.
- Check for internal contradictions across memo sections.
- Provide confidence level per conclusion (HIGH/MED/LOW).

See `references/research_verification_protocol.md`.

## Output format

## Bottom line
- 3–7 bullets. Each bullet should be tied to verified authority or clearly labeled as interpretive.

## Background / facts (as provided)
- Separate facts from assumptions.

## Analysis
### Issue 1 — [question]
- **Answer (provisional)**:
- **Primary authority**:
- **Reasoning**:
- **Open questions / needs verification**:

(Repeat)

## Practical recommendations
- What to do next; what to avoid; escalation items.

## Authorities appendix
- List every authority cited with short description and verification status (VERIFIED / UNVERIFIED).

---

# Playbook 6 — Client communications (clear, usable, non-academic)

## Goal
Draft emails that clients can act on:
- concise summary
- risk framing
- decision points
- recommended next steps

See `references/client_email_style.md`.

## Output format

Subject: [clear, specific]

Hi [Name],

**Summary (1–3 bullets)**

**Key points**
- …

**Recommendations**
- …

**What I need from you**
- …

Best,
[Attorney name]

---

# Playbook 7 — Policy + engagement-letter drafting (including AI usage clause)

## Goal
Draft internal policies or engagement letter provisions that:
- frame AI as efficiency + quality support
- emphasize attorney supervision
- address confidentiality and provider data handling
- obtain client consent where appropriate

See `references/ai_usage_engagement_clause.md`.

---

# Tooling hooks (optional)

If you can run code:
- Use `scripts/docx_extract_outline.py` to generate a section outline for precise citations in your review.
- Use `scripts/docx_redline_report.py` to generate a redline report between two `.docx` files.

If you cannot run code:
- Still produce the revised text and a structured “changes by section” redline summary.

---

# Done criteria

A response is “done” when it includes:
- explicit perspective + assumptions
- severity-rated issues or change map (as requested)
- concrete counter-language for high-severity items
- cross-document conflict checks where multiple documents exist
- QC pass completed (consistency + citations where applicable)
- deliverables packaged (revised doc + redline report + cover email) when requested
