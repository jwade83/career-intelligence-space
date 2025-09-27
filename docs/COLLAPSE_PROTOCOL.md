---
project: Career Intelligence Space
type: memo
status: matured
tags: [collapse, protocol, ritual]
updated: 2025-09-26
---
# Collapse Protocol — re-prime and recover fast

## When to use
- Context loss, instruction dilution, drift, or blocked merges that don’t make sense.

## Ritual (2 minutes)
1. Paste the **Session Header** template (see `../02_TEMPLATES/SESSION_HEADER.txt`).
2. Re-read: `./CONTRIBUTING.md`, `./AUTOMATION.md`, `./reflexive/PR_ROUTE.md`, `./Golden_Rules.md`
3. If working on a PR:
   - `gh pr merge <#> --squash --auto`
   - `python3 .github/scripts/pr_health.py <#>`
   - If **MISSING contexts** → push a no-op commit to the PR branch.
   - If **strict block** → Update Branch API for that PR.
4. Log the incident briefly in a capsule or decision note if it changed rules or process.

## Signals to watch
- “MISSING contexts”, `merge=BLOCKED` with green-looking jobs
- Linkcheck failures from `](docs/...)` inside `docs/`
- Front-matter failures (missing keys, fenced FM, invalid enums)
