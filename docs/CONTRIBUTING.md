---
project: Career Intelligence Space
type: spec
status: matured
tags: [contributing, ci, gates, merge_route]
updated: 2025-09-26
---
# CONTRIBUTING — CI Gates & Merge Route

## CI gates (required on main)
- Contexts: `links`, `gate`
- strict: true (checks must pass on PR head)
- enforce_admins: true
- Only PR-event runs satisfy protection; manual `workflow_dispatch` does not

## Front-matter schema
- Required keys: project, type, status, tags, updated
- Enums from docs/ONTOLOGY.yml
  - type: capsule, memo, assessment, log, decision, spec
  - status: draft, matured, archived
- Front-matter must be first in file (no code fences)

## Link rules
- Inside docs/, use relative links like ](./...) — never ](docs/...)
- Prefer local mirrors for fragile external URLs

## Merge route that works
1. Open PR; enable auto-merge: `gh pr merge <#> --squash --auto`
2. If blocked, run: `python3 .github/scripts/pr_health.py <#>`
3. If it says MISSING contexts, push a no-op commit on the PR branch
4. If it says strict block, use Update Branch API
5. Do not rely on workflow_dispatch to satisfy branch protection
