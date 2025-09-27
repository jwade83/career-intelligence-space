---
project: Career Intelligence Space
type: spec
status: matured
tags: [rules, golden, ci, gates]
updated: 2025-09-26
---
# Golden Rules — CI gates, merge path, and link hygiene

## Required checks on main
- contexts: `links`, `gate`
- strict: true
- enforce_admins: true
- Only **PR-event** runs satisfy protection (pull_request or a push to the PR branch). Manual `workflow_dispatch` runs do **not**.

## Front-matter requirements (blocking)
- Must be the first thing in every changed `.md` file (no code fences).
- Required keys: `project`, `type`, `status`, `tags`, `updated`
- Enums from `./ONTOLOGY.yml`
  - type: `capsule`, `memo`, `assessment`, `log`, `decision`, `spec`
  - status: `draft`, `matured`, `archived`
- `updated`: ISO date (YYYY-MM-DD)

## Link rules (linkcheck)
- Inside `docs/`, use **relative links** like `](./file.md)` — never `](docs/...)`.
- Prefer local mirrors for fragile external URLs.

## Merge route that always works
1. Open PR and enable auto-merge: `gh pr merge <#> --squash --auto`
2. Run: `python3 .github/scripts/pr_health.py <#>`
3. If it says **MISSING contexts** → push a tiny no-op commit on the PR branch.
4. If it says **strict block** → run Update Branch API.
5. Do not rely on `workflow_dispatch` to satisfy branch protection.

## Pointers
- CONTRIBUTING: `./CONTRIBUTING.md`
- Automation spec: `./AUTOMATION.md`
- Ontology enums: `./ONTOLOGY.yml`
- PR route: `./reflexive/PR_ROUTE.md`
- Collapse Protocol: `./COLLAPSE_PROTOCOL.md`
