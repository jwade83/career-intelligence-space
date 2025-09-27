---
project: Career Intelligence Space
type: spec
status: matured
tags: [automation, ci, babysitter, norms]
updated: 2025-09-27
---

# Automation Norms & Babysitters

## Protected Branch Policy (main)
- Required contexts: `links`, `gate`.
- Require up-to-date before merge; admins enforced.
- All updates to `main` arrive via PR with auto-merge armed.

## PR Route That Works (always)
- Create + arm auto-merge:  
  `gh pr create --fill && gh pr merge --squash --auto`
- Checks slow to attach? The PR babysitter will push a no-op commit to the PR branch. Manual fallback if ever needed:  
  `printf '\n' >> README.md && git add README.md && git commit -m "chore(ci): retrigger" && git push`
- Keep PRs boring: don’t merge until `links` and `gate` are green; auto-merge will complete on its own.

## Babysitters (installed)
- [`../.github/workflows/pr-babysitter.yml`](../.github/workflows/pr-babysitter.yml)  
  Auto no-op commit to PR branch if required contexts haven’t attached (starts PR-event checks).
- [`../.github/workflows/pr-update-branch.yml`](../.github/workflows/pr-update-branch.yml)  
  Auto “Update branch” when PR is behind `main`.
- [`../.github/workflows/pr-auto-enable-automerge.yml`](../.github/workflows/pr-auto-enable-automerge.yml)  
  Auto-enable **squash** auto-merge on PR open/reopen/ready.
- [`../.github/workflows/linkcheck-rerun-on-transient.yml`](../.github/workflows/linkcheck-rerun-on-transient.yml)  
  Auto re-run `linkcheck` once on transient web errors (429/5xx/timeouts). Real broken links still block.
- [`../.github/workflows/update-migration-map.yml`](../.github/workflows/update-migration-map.yml)  
  Generated “migration map” changes are proposed via a bot PR (no direct push to protected `main`).

## Transcripts: Upload, Index, Policy
- Upload one-liner: `bin/cis-add-transcript "$HOME/Downloads/<export>.md"`  
  Writes `.txt` to `99_LOGS/transcripts/`, opens PR, arms auto-merge, retriggers checks.
- Policy: raw transcripts are `.txt` to avoid linkcheck noise; narrative docs stay `.md` and must pass gates.
- Auto-index: [`../.github/workflows/transcripts-index.yml`](../.github/workflows/transcripts-index.yml) builds `INDEX.md` on transcript PRs.  
  Browse: [`../99_LOGS/transcripts/INDEX.md`](../99_LOGS/transcripts/INDEX.md)
- Guard: [`../.github/workflows/transcripts-ban-md.yml`](../.github/workflows/transcripts-ban-md.yml) blocks `.md` under `99_LOGS/transcripts/**`.

## Front-matter & Link Gates (what they enforce)
- Front-matter required keys for `.md`: `project`, `type`, `status`, `tags`, `updated` (ISO date).
- `linkcheck` validates Markdown links; transcripts `.txt` are excluded by design.

## Optional Quality-of-Life
- `gh alias set pra 'pr create --fill && pr merge --squash --auto'`
- `gh alias set prn 'api repos/:owner/:repo/pulls/$(gh pr view --json number --jq .number)/update-branch || true'`

## Changelog
- 2025-09-27: Added PR babysitters pack; transcripts route; auto-index; policy; this page.
