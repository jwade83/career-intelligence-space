---
project: Career Intelligence Space
type: spec
status: matured
tags: [automation, ci, checks, invariants]
updated: 2025-09-26
---
# AUTOMATION — Checks, triggers, schema

## Required status checks (main)
contexts:
  - links
  - gate
strict: true
enforce_admins: true

## Workflows
linkcheck:
  trigger: pull_request (also push, workflow_dispatch allowed but not counted by protection)
  context_name: links
frontmatter_required:
  trigger: pull_request
  context_name: gate

## Front-matter schema (enforced)
required_keys: [project, type, status, tags, updated]
type_enum: [capsule, memo, assessment, log, decision, spec]
status_enum: [draft, matured, archived]
project_enum: [Career Intelligence Space]

## Known pitfalls
- docs/ internal links must be relative (./), not prefixed with docs/
- external chat/share links should be mirrored locally
