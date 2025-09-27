---
project: Career Intelligence Space
type: capsule
status: matured
tags: [ci, gates, branch_protection, linkcheck, frontmatter, pr_route]
updated: 2025-09-26
---
# CI Gates & Merge Path Hardening

## PRs & changes
- PR #10–#11: aligned required contexts to **links** and **gate**; fixed PR-trigger expectations; added `pr_health.py` and PR route doc.
## Incidents & fixes
- BLOCKED merges with “green jobs” → runs were `workflow_dispatch` (don’t satisfy protection) and/or name mismatches.
## Outcome
- Branch protection: strict=true, enforce_admins=true; contexts: links, gate.
- Reliable PR route ritualized.
