# ✅ Merge Checklist — Main Branch (Harness Doctrine)

**Use this as a gate. Don't merge until all boxes are checked.**

## 1) PR Hygiene
- [ ] Title is clear and scoped (e.g., "Production Hardening + Doctrinal Correction")
- [ ] Description summarizes the change, links to addendum and hardening docs
- [ ] Linked items: issues/decisions/chronicle entries referenced
- [ ] Labels applied: `release`, `harness`, `future` (and others as relevant)
- [ ] Milestone (optional) set to current release

## 2) Files Changed (spot-check)
- [ ] `11_FUTURE/hardware_assets/ADDENDUMS/20251001_Final_Release_Adjustment.md` present
- [ ] `11_FUTURE/hardware_assets/PRODUCTION_HARDENING.md` updated and back-linked to addendum
- [ ] **Workflows present/pinned:**
  - [ ] `.github/workflows/future-review-pinger.yml` (with $GITHUB_STEP_SUMMARY, pinned actions)
  - [ ] `.github/workflows/frontmatter-lint.yml` (runs linter + tests)
  - [ ] `.github/workflows/pr-template-check.yml` (enforces template; bot allowlist)
  - [ ] `.github/workflows/link-anchor-check.yml` (lychee pinned to commit)
  - [ ] `.github/workflows/canary-stress-test.yml` (monthly canary)
- [ ] **Scripts have shebang + `set -euo pipefail`:**
  - [ ] `scripts/lint_frontmatter.py`
  - [ ] `scripts/validate_future_silo.sh`
  - [ ] `scripts/promote_future_silo.sh`
  - [ ] `scripts/ensure_labels.sh`
- [ ] `.github/CODEOWNERS` includes `/11_FUTURE/**` and other doctrine paths

## 3) Required Status Checks (in PR "Checks" tab)
- [ ] **Frontmatter Lint:** ✅ Passed
- [ ] **PR Template Check:** ✅ Passed (not skipped for human PRs)
- [ ] **Link/Anchor Check:** ✅ Passed
- [ ] **Linter Unit Tests (pytest):** ✅ Passed
- [ ] All checks green and branch up-to-date

## 4) Branch Protection (GitHub UI → Settings → Branches → main)
- [ ] "Require a pull request before merging" is **ON**
- [ ] "Require review from Code Owners" is **ON**
- [ ] "Require status checks to pass before merging" is **ON** with:
  - [ ] `lint` (frontmatter-lint.yml)
  - [ ] `lychee` (link-anchor-check.yml)
  - [ ] `check-template` (pr-template-check.yml)
- [ ] "Require branches to be up to date" is **ON**

## 5) Doctrinal Accuracy (no overclaim)
- [ ] PR description includes corrected status table:
  - C1/C2/C5 = ⚠️ PENDING
  - C3 = ⚠️ PARTIAL
  - C4/C6/C7/Antifragility = ✅ COMPLETE
- [ ] Addendum file referenced so future readers see correction source

## 6) Evidence & Debuggability
- [ ] Action logs show $GITHUB_STEP_SUMMARY sections rendered
- [ ] Example fix-it hints from linter visible in logs
- [ ] Canary job file exists and scheduled (1st of month)

## 7) Governance & Security
- [ ] No tokens/secrets added in scripts
- [ ] Promotion/labels scripts are local-only (or use OIDC)
- [ ] Actions pinned to commit SHAs (not moving tags)
- [ ] CODEOWNERS reviewers approved this PR

## 8) One-time Post-Merge Prep (will do immediately after merge)
- [ ] Run `./scripts/ensure_labels.sh` (local) to guarantee labels exist
- [ ] Trigger Future Silo Review Pinger once via "Run workflow" (manual smoke test)
- [ ] Confirm no duplicate issues and that silo_id/summary appear

## 9) Rollback Plan (Recovery anchor)
- [ ] Create checkpoint tag on merge commit:
  ```bash
  git tag checkpoint/final-release-2025-10-01
  git push origin checkpoint/final-release-2025-10-01
  ```
- [ ] Rollback documented in PRODUCTION_HARDENING.md:
  ```bash
  # Rollback
  git checkout checkpoint/final-release-2025-10-01
  ```
- [ ] Promotion script's tag collision policy documented (-v2, -v3)

## 10) Final Human Review
- [ ] All open review comments resolved
- [ ] No TODO or FIXME strings slipped into mainline
- [ ] Scope & impact acknowledged by reviewer(s)

---

## ⏭️ After Merge (quick follow-up)
- [ ] Verify first daily pinger run at 12:00 UTC posts clean summary
- [ ] Verify monthly canary runs on 1st and fails as designed
- [ ] Create tiny test PR touching `/11_FUTURE` to confirm CODEOWNERS + checks bite

---

**If all boxes are checked, you're green to Merge.** ✅

