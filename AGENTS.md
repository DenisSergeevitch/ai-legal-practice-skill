# AGENTS.md

## Purpose

This repository packages one portable skill, `ai-legal-practice`, for multiple agent ecosystems.

The goal is to keep one canonical skill source, mirror it into the platform-specific folders, and publish a clean public repository that is safe to share.

## Repository Layout

Canonical source:

- `skills/ai-legal-practice/`

Mirrors for specific ecosystems:

- `.claude/skills/ai-legal-practice/`
- `.github/skills/ai-legal-practice/`

Top-level docs:

- `README.md` is the human-facing repo overview
- `LICENSE` is the repo license
- `AGENTS.md` is the build and publishing guide for agents working in this repo

## Source Of Truth

Always treat `skills/ai-legal-practice/` as the source of truth.

Rules:

1. Make content changes in `skills/ai-legal-practice/` first.
2. After editing the canonical skill, sync the same changes into `.claude/skills/ai-legal-practice/` and `.github/skills/ai-legal-practice/`.
3. Do not treat mirror folders as authoritative.
4. Before committing, verify the canonical folder and both mirrors are aligned.

If only one copy is updated, the repo is incomplete.

## How We Build Skills

This repo is for a real reusable skill, not loose notes.

Each skill should follow this structure:

- `SKILL.md` for the actual agent instructions
- `references/` for detailed materials that should be loaded only when needed
- `scripts/` for deterministic helper utilities
- `examples/` for small prompt examples when they make the skill easier to apply

Working rules:

1. Keep `SKILL.md` lean and procedural. Put long supporting material into `references/`.
2. Put durable, repeatable logic into scripts instead of rewriting it in chat every time.
3. Keep examples short and sanitized.
4. Prefer practical workflows, checklists, and output formats over theory.
5. Do not add client documents, privileged material, secrets, tokens, or personal data.

## SKILL.md Standards

`SKILL.md` should be the minimum complete instruction set needed for the agent to do the job well.

Expected qualities:

- Clear trigger description in frontmatter `name` and `description`
- Strong statement of scope
- Safety boundaries where needed
- Default intake requirements
- Step-by-step workflow
- Explicit output formats where consistency matters
- References to `references/` or `scripts/` only when they materially help

Avoid:

- Bloated background explanation
- Duplicating full reference content inside `SKILL.md`
- Repo maintenance notes that belong in `AGENTS.md`
- Human marketing copy

## Scripts And References

Use `scripts/` when reliability matters more than prose.

Use `references/` when the material is useful but too large or too specific to keep in `SKILL.md`.

Rules:

1. Scripts should have narrow, obvious purposes.
2. Script names should describe the output they produce.
3. Reference files should be directly discoverable from `SKILL.md`.
4. Keep sample inputs and outputs sanitized.

## README Standards

`README.md` is for humans deciding whether to use the repo. It is not the place for agent-only operating rules.

The README should usually include:

1. What the skill does in plain language
2. Who it is for
3. Important safety or professional-use disclaimer
4. Repo layout and which folder is canonical
5. Installation or copy paths for supported agent ecosystems
6. A few realistic usage examples
7. Optional scripts overview if scripts are included
8. License

README guidance:

- Keep it concise and concrete
- Describe outcomes, not internal brainstorming
- Prefer real use cases over generic feature lists
- Mention if the skill output requires human review
- Update the README when folder layout, install path, or supported ecosystems change

Do not turn the README into a changelog or a long design memo.

## Publishing Rules

This repository is intended to be publishable, including as a public GitHub repo, but only after a safety check.

Before publishing or pushing significant changes:

1. Verify the canonical skill and both mirrors match
2. Remove `.DS_Store` and other junk files
3. Confirm there are no secrets, API keys, private client facts, privileged documents, or identifying matter details
4. Confirm examples and references are safe to publish
5. Confirm `README.md`, `LICENSE`, and `AGENTS.md` are present and accurate

Visibility rule:

- Do not change repository visibility without explicit user confirmation

If the user asks to publish:

1. Commit coherent changes
2. Push the current branch
3. If needed, create or update the remote
4. Only change public/private status if the user explicitly asked for that action

## Git Workflow

Default workflow:

1. Edit the canonical skill first
2. Sync mirrors
3. Review diff for all three copies
4. Commit with a message that describes the skill change
5. Push to the configured remote

Prefer small commits when updating instructions, references, or scripts.

## Quality Bar

A change is not complete unless:

- the canonical skill is correct
- both mirrors are synced
- the README still matches the repo
- the repo is safe to publish
- git status is clean after commit
