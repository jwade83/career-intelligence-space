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

## CI Checks & Auto-merge

### Required Status Checks (main branch)
- **links** - Link validation and checking
- **gate** - Frontmatter validation and schema compliance
- **strict: true** - All checks must pass on PR head
- **enforce_admins: true** - Even admins must pass checks

### Auto-merge Configuration
- **Label:** `auto-merge:candidate` - Enables automatic merging
- **Branch pattern:** `bot/{domain}-{yyyymmdd-hhmm}` - Bot-generated branches
- **Commit trailers:** 
  - `Affected-IDs: job-id-1, job-id-2` - Track affected job IDs
  - `Source: action-card` - Track action source

### Path Allowlist (CI-only)
- **Allowed paths:** 
  - `data/jobs/` - Job data and outcomes
  - `data/field/` - Field capture data
  - `08_CHRONICLE/` - Chronicle entries
  - `06_COMPANY/` - Company research stubs
  - `05_NEGOTIATION/` - Negotiation trackers
- **Blocked paths:** 
  - `05_ASSETS/` - Master Portfolio assets
  - `docs/` - Documentation (manual review required)

### "No-op" Re-run Pattern
When checks don't attach to PR:
1. **Push tiny commit** - Add empty line or comment
2. **Re-trigger checks** - Force GitHub Actions to re-run
3. **Verify attachment** - Confirm checks appear in PR
4. **Enable auto-merge** - If all checks pass

### Failure Messages (Copy-ready)
```
❌ Path not allowed: docs/example.md
   • Allowed paths: data/jobs/, data/field/, 08_CHRONICLE/, 06_COMPANY/, 05_NEGOTIATION/
   • Move file to allowed path or request manual review

❌ Frontmatter validation failed: Missing required key 'updated'
   • Required keys: project, type, status, tags, updated
   • Add missing key and try again

❌ Link validation failed: Broken link to docs/nonexistent.md
   • Fix broken link or remove reference
   • Use relative paths: ./file.md not docs/file.md

❌ Duplicate action detected: job-id-123 already processed
   • Previous action: 2025-09-30 14:32
   • No duplicate PR created
   • Check action history if needed
```

## Known pitfalls
- docs/ internal links must be relative (./), not prefixed with docs/
- external chat/share links should be mirrored locally
- Checks don't always attach to PRs - use "no-op" re-run pattern
- Auto-merge requires `auto-merge:candidate` label
- Path allowlist prevents accidental MP promotion
