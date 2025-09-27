---
project: Career Intelligence Space
type: capsule
status: matured
tags: [reflexive, rollup, weekly, metrics]
updated: 2025-09-26
---
# Weekly Reflexive Rollup — 2025-W39 (Sep 22–Sep 28, 2025)
## Repo health signals
- Branch protection: contexts [links, gate]; strict: true; admins enforced: true
- Invariants audit last run: not run yet

## Merged PRs this week
- #7 — chore: noop change to trigger linkcheck & tag-drift-warn (by @jwade83) — 2025-09-26 — `chore/test-ci-workflows` — https://github.com/jwade83/career-intelligence-space/pull/7
- #2 — docs(chronicle): add PR tracking line to Week-0 Chronicle (by @jwade83) — 2025-09-25 — `retrofill-week0-followup` — https://github.com/jwade83/career-intelligence-space/pull/2
- #6 — Chronicle: Week-1 retrofill stub (by @jwade83) — 2025-09-25 — `week1-chronicle` — https://github.com/jwade83/career-intelligence-space/pull/6
- #3 — Chronicler Retrofill — Add Forensic Backfill Log (v0.1) (by @jwade83) — 2025-09-25 — `backfill-log-fix` — https://github.com/jwade83/career-intelligence-space/pull/3
- #5 — Docs: link Forensic Backfill Log v0.2 (by @jwade83) — 2025-09-25 — `index-v0.2` — https://github.com/jwade83/career-intelligence-space/pull/5
- #4 — Chronicler Retrofill Week 0 — Verified SHAs, Notices, Frontmatter, Exchange Blocks (by @jwade83) — 2025-09-25 — `forensic-backfill-v0.2` — https://github.com/jwade83/career-intelligence-space/pull/4
- #10 — test(frontmatter): add file without front-matter (by @jwade83) — 2025-09-27 — `chore/frontmatter-proof` — https://github.com/jwade83/career-intelligence-space/pull/10
- #11 — chore: remove frontmatter proof file (by @jwade83) — 2025-09-27 — `chore/cleanup-frontmatter-proof` — https://github.com/jwade83/career-intelligence-space/pull/11
- #8 — docs(D5): add human↔machine handshake memo; update CONTRIBUTING (by @jwade83) — 2025-09-27 — `chore/handshake-memo` — https://github.com/jwade83/career-intelligence-space/pull/8
- #12 — docs(ci): add CONTRIBUTING, AUTOMATION, PR template, and warn-only invariants audit (by @jwade83) — 2025-09-27 — `chore/docs-kit` — https://github.com/jwade83/career-intelligence-space/pull/12
- #13 — ci(audit): ensure invariants audit is warn-only and gh-native (by @jwade83) — 2025-09-27 — `chore/audit-warn-only` — https://github.com/jwade83/career-intelligence-space/pull/13
- #14 — capsule: add 2025-09-26 ChatGPT Penne session + index (passes gates) (by @jwade83) — 2025-09-27 — `feat/penne-capsule` — https://github.com/jwade83/career-intelligence-space/pull/14
- #15 — docs-rules add golden rules, collapse protocol, session header, and strengthen PR template (by @jwade83) — 2025-09-27 — `chore/golden-rules` — https://github.com/jwade83/career-intelligence-space/pull/15
- #16 — feat/chronicle bundle 20250926 (by @jwade83) — 2025-09-27 — `feat/chronicle-bundle-20250926` — https://github.com/jwade83/career-intelligence-space/pull/16
- #17 — feat/add confirm repo transcript (by @jwade83) — 2025-09-27 — `feat/add-confirm-repo-transcript` — https://github.com/jwade83/career-intelligence-space/pull/17
- #18 — capsule: add local transcript link to Penne capsule (by @jwade83) — 2025-09-27 — `fix/penne-transcript-link` — https://github.com/jwade83/career-intelligence-space/pull/18

## Incidents & fixes (notable)
- Ensured required contexts exactly match `links` and `gate`; only PR-event runs satisfy protection.
- Added `pr_health.py` to print missing contexts/strict actions and established the PR route ritual.
- Patched invariants audit to warn-only and use `gh api` (no external deps).
- Resolved a front-matter miss on `08_CHRONICLE/INDEX.md` that blocked a capsule.

## Rituals & next actions
- Keep using the auto-merge + `pr_health.py` merge path.
- Mirror fragile external links locally before referencing them in capsules.
- If audit warns about FM or `docs/` link anti-patterns, queue a housekeeping PR.

## Pointers
- Golden Rules: ../docs/Golden_Rules.md
- Collapse Protocol: ../docs/COLLAPSE_PROTOCOL.md
- PR Route: ../docs/reflexive/PR_ROUTE.md
