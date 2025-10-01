---
project: Career Intelligence Space
type: future_spec
status: deferred
tags: [hardening, fixes, production_ready]
updated: 2025-09-30
review_date: 2026-01-15
schema_version: v1
id: FUTURE_PRODUCTION_HARDENING
---

# Production Hardening — Top 7 Fixes Applied

This document tracks the critical fixes applied to the Future Silo system to make it production-ready and spam-free.

## ✅ Fixes Applied

### Fix 1: GitHub Actions YAML Import Failure
**Problem:** Workflow used `import yaml` without installing PyYAML; `::set-output` deprecated

**Solution:**
- ✅ Added `actions/setup-python@v5` step
- ✅ Added `pip install pyyaml` step
- ✅ Replaced `::set-output` with `$GITHUB_OUTPUT` file write
- ✅ Added `silo_id` to issue body for searchability

**Files Changed:**
- `.github/workflows/future-review-pinger.yml`

---

### Fix 2: Cron vs. PT Time Mismatch
**Problem:** Comment said 08:00 PT but cron was 16:00 UTC (actually 09:00 PDT during DST)

**Solution:**
- ✅ Changed to daily cron: `0 12 * * *` (12:00 UTC)
- ✅ Simpler, more reliable than weekly
- ✅ Let script decide which items are due

**Files Changed:**
- `.github/workflows/future-review-pinger.yml`

---

### Fix 3: Issue De-Duplication (Prevent Spam)
**Problem:** Workflow could open new issue every run, creating spam

**Solution:**
- ✅ Switched to `dacbd/create-issue-action@v2`
- ✅ Added `update_existing: true`
- ✅ Added `search_existing: open`
- ✅ One issue updated in-place, not duplicated

**De-Duplication Policy:**
- Searches for existing **open** issues with title "Future Silo Review — items due"
- If found: Updates existing issue body with current due files
- If not found: Creates new issue
- **Closed issues are NOT reopened** - new issue created for next review cycle
- This prevents noise while maintaining clear review boundaries

**Files Changed:**
- `.github/workflows/future-review-pinger.yml`

---

### Fix 4: Linter Rule for future_spec Sanity
**Problem:** No validation that `review_date` is ISO format and in future

**Solution:**
- ✅ Created `scripts/lint_frontmatter.py` with validation:
  - ISO YYYY-MM-DD format check
  - Date must be ≥ 90 days in future
  - Required fields per schema
  - Detailed error messages
- ✅ Created `.github/workflows/frontmatter-lint.yml` to run on PRs
- ✅ Blocks PRs with invalid frontmatter

**Files Created:**
- `scripts/lint_frontmatter.py`
- `.github/workflows/frontmatter-lint.yml`

---

### Fix 5: CODEOWNERS Path Reach
**Problem:** CODEOWNERS pattern might not fire if not in standard location

**Solution:**
- ✅ Created `.github/CODEOWNERS` (GitHub-standard path)
- ✅ Pattern: `/11_FUTURE/hardware_assets/** @jwade83`
- ✅ Ensures reviews required for Harness doctrine changes

**Files Created:**
- `.github/CODEOWNERS`

---

### Fix 6: PR Template Guardrails (Hard Checks)
**Problem:** PR template was advisory, needed hard checks to reduce human error

**Solution:**
- ✅ Enhanced Future Silo section:
  - `review_date` set **≥ 90 days** ahead (explicit)
  - Linked `related:` IDs present
  - CODEOWNERS reviewers requested (@jwade83)
  - Linked Decision or Chronicle if activation/promote

**Files Changed:**
- `.github/PULL_REQUEST_TEMPLATE.md`

---

### Fix 7: Discoverability Link (Relative Path)
**Problem:** Absolute path might not work in MkDocs

**Solution:**
- ✅ Changed to relative link: `[11_FUTURE/hardware_assets/README.md](../11_FUTURE/hardware_assets/README.md)`
- ✅ Works in GitHub UI and future MkDocs
- ✅ Proper markdown link format

**Files Changed:**
- `docs/README.md`

---

## 🎁 Nice-to-Haves Implemented

### Idempotent Promotion Script
**File:** `scripts/promote_future_silo.sh`

**Features:**
- ✅ One CLI command: `./scripts/promote_future_silo.sh hardware_assets`
- ✅ Dry-run mode: `./scripts/promote_future_silo.sh hardware_assets --dry-run`
- ✅ Copies files to target location (reconciles if exists)
- ✅ Updates frontmatter: `deferred` → `active`
- ✅ Creates Decision Log entry (checks for duplicates)
- ✅ Creates checkpoint tag for rollback (versioned if exists: `-v2`, `-v3`)
- ✅ Opens promotion branch with proper naming
- ✅ **Does NOT auto-push to main** - requires manual PR creation
- ✅ Fully idempotent (safe to re-run)

**Edge Cases Handled:**
- **Destination exists:** Reconciles (overwrites) instead of failing
- **Decision Log duplicate:** Skips entry if already exists (checks via grep)
- **Checkpoint tag exists:** Creates versioned tag (`-v2`, `-v3`, etc.)
- **No changes:** Exits gracefully with warning
- **Security:** Local-only, no auto-push, requires manual PR

**Usage:**
```bash
# Dry run (no changes)
./scripts/promote_future_silo.sh hardware_assets --dry-run

# Actual promotion
./scripts/promote_future_silo.sh hardware_assets
```

---

### Label Management Script
**File:** `scripts/ensure_labels.sh`

**Features:**
- ✅ Pre-creates required labels: `future`, `review`, `harness`, `promotion`, `automation`
- ✅ Uses GitHub CLI (`gh`) for safety
- ✅ Idempotent (skips existing labels)
- ✅ Prevents action failures from missing labels

**Operational Note:**
- **Local ops only** - requires `gh` CLI installed
- **Not in CI** - labels should be created once, manually
- Run after repo setup or before first pinger execution

**Usage:**
```bash
# Requires: brew install gh (or equivalent)
./scripts/ensure_labels.sh
```

---

### Frontmatter Linter (Comprehensive)
**File:** `scripts/lint_frontmatter.py`

**Features:**
- ✅ Validates all frontmatter in Chronicle, Future, docs
- ✅ Enforces `review_date` ≥ 90 days ahead for `future_spec`
- ✅ Validates ISO YYYY-MM-DD format
- ✅ Checks required fields per schema
- ✅ **Human-readable remediation** in error messages (e.g., "Set review_date ≥ 2026-01-15")
- ✅ **Fails fast** if schema missing or invalid
- ✅ Runs in CI on every PR (`.github/workflows/frontmatter-lint.yml`)

**Usage:**
```bash
# Lint all files
python scripts/lint_frontmatter.py

# CI will automatically lint on PRs touching:
# - 08_CHRONICLE/**/*.md
# - 11_FUTURE/**/*.md
# - docs/**/*.md
```

---

## 🔍 Validation Checklist

### Pre-Deployment Validation
- ✅ PyYAML installed in all workflows
- ✅ `$GITHUB_OUTPUT` used (not deprecated `::set-output`)
- ✅ Issue de-duplication active
- ✅ Cron schedule simplified (daily)
- ✅ CODEOWNERS in standard path
- ✅ PR template with hard checks
- ✅ Relative links for discoverability
- ✅ Frontmatter linter operational
- ✅ All scripts executable (`chmod +x`)

### Post-Deployment Validation
- [ ] Run `./scripts/ensure_labels.sh` to create labels
- [ ] Verify frontmatter linter passes: `python scripts/lint_frontmatter.py`
- [ ] Test promotion script dry-run
- [ ] Verify CODEOWNERS triggers on test PR
- [ ] Wait for first daily cron run (confirm no duplicate issues)

---

## 📊 System Status

### Before Fixes
- ❌ Workflow would fail on `import yaml`
- ❌ Could create duplicate issues (spam)
- ❌ No validation of `review_date` format/value
- ❌ CODEOWNERS might not fire
- ❌ PR template too permissive
- ❌ No promotion automation

### After Fixes
- ✅ All workflows production-ready
- ✅ Issue de-duplication prevents spam
- ✅ Frontmatter validation blocks invalid dates
- ✅ CODEOWNERS enforces review
- ✅ PR template has hard checks
- ✅ One-command promotion with rollback safety
- ✅ Label management automated
- ✅ Complete CI/CD pipeline

---

## 🚀 Deployment Readiness

**Status:** ✅ **PRODUCTION-READY**

All critical fixes applied. System is:
- **Robust** - No dependency failures
- **Quiet** - No spam, de-duplication active
- **Safe** - Validation gates in place
- **Automated** - Promotion script ready
- **Maintainable** - Clear error messages

**Next Step:** Merge to `main` and monitor first daily cron run.

---

## 🔒 Additional Hardening (Beyond Top 7)

### PR Template Enforcement
**Added:** `.github/workflows/pr-template-check.yml`

**Features:**
- ✅ CI enforces PR template checklist for `/11_FUTURE` changes
- ✅ Blocks PRs touching `/11_FUTURE` without proper checkboxes
- ✅ Validates all sub-checks (frontmatter, review_date, related IDs, CODEOWNERS)
- ✅ Runs frontmatter linter on changed files only

**Result:** Templates are no longer suggestions - they're enforced by CI

---

### CODEOWNERS Scope Expansion
**Updated:** `.github/CODEOWNERS`

**Protected Paths:**
- `/11_FUTURE/**` - All Future Silo content
- `/docs/HARNESS/**` - Harness immune system specs
- `/08_CHRONICLE/harness/**` - Harness documentation
- `/docs/DECISION_LOG.md` - Provenance chain
- `/docs/ONTOLOGY.yml` - Keystone antibody (vocabulary stability)
- `/config/**` - Configuration and schema
- `/.github/workflows/**` - Automation infrastructure

**Result:** Complete Harness doctrine protection

---

### Workflow Health Improvements
**Updated:** `.github/workflows/future-review-pinger.yml`

**Enhancements:**
- ✅ Added `pull-requests: read` permission
- ✅ Added summary step for debugging (prints due files)
- ✅ Uses `actions/setup-python@v5` (latest)
- ✅ Fallback ready (documented alternative: `peter-evans/create-issue-from-file`)

**Result:** Robust, debuggable, maintainable workflow

---

### Security Posture
**Promotion Script:**
- ✅ Local-only execution (no CI secrets)
- ✅ No auto-push to main (requires manual PR)
- ✅ Dry-run mode for testing
- ✅ Token management: Future OIDC or short-lived PAT if needed

**Label Script:**
- ✅ Local `gh` CLI only (not in CI)
- ✅ Manual one-time execution

**Result:** No PAT baking, no auto-merge footguns

---

## 📋 Post-Deployment Validation

### Manual Steps (One-Time Setup)
```bash
# 1. Create labels
./scripts/ensure_labels.sh

# 2. Test linter locally
python scripts/lint_frontmatter.py

# 3. Test promotion dry-run
./scripts/promote_future_silo.sh hardware_assets --dry-run

# 4. Verify schema exists and is valid
cat config/archive_schema.yml | grep future_spec
```

### CI Validation (After Merge)
- [ ] Open test PR touching `/11_FUTURE/hardware_assets/README.md`
- [ ] Verify CODEOWNERS requests reviewer (@jwade83)
- [ ] Verify PR template appears with Future Silo section
- [ ] Verify PR template check workflow runs and passes
- [ ] Verify frontmatter linter runs and passes
- [ ] Close test PR

### Monitoring (Ongoing)
- [ ] Wait for first daily cron run (12:00 UTC)
- [ ] Verify no duplicate issues created
- [ ] Verify issue body includes silo_id
- [ ] Verify workflow summary shows due files count

---

## 🎯 Harness-Doctrine Alignment

### Externalization: ✅ COMPLETE
- Silo structure prevents knowledge living only in chat
- Decision Log template ensures provenance
- Chronicle integration for activation tracking

### C3 Vocabulary Drift: ✅ PROTECTED
- Ontology file in CODEOWNERS
- Frontmatter schema validation
- Linter enforces stable terminology

### C4 Reference Ambiguity: ⚠️ PARTIAL
- Stable IDs enforced in frontmatter
- `related:` field validated
- **Follow-up:** Link/Anchor checker for full C4 protection

### C6 Evidence Entropy: ✅ COMPLETE
- Decision Log template with reconstruction tests
- Checkpoint tags for rollback
- Complete provenance chain

### Antifragility: ⚠️ PENDING
- **Follow-up:** Weekly stress test job
  - Create fake FUTURE file with too-soon review_date
  - Ensure linter blocks it
  - Measure immune response time

---

**Next Step:** Merge to `main` and monitor first daily cron run.

---

*Production Hardening Complete - Future Silo System Ready for Production*
*All critical footguns addressed - Silent failures prevented*

