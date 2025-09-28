---
project: Career Intelligence Space
type: spec
status: matured
tags: [prompts, macros, pr, automation, troubleshooting]
updated: 2025-09-27
---

# PR: Stuck Checks Fixer (Gate/Links/Update)

You are my repo-aware fixer. We have a PR failing 3 checks:
1) frontmatter-required / gate
2) pr-auto-enable-automerge / enable
3) pr-update-branch / update

Do the following, in order, and show a short diagnosis summary before you apply patches:

PHASE 1 — DIAGNOSE
A1) Inspect these files (open and read):
   - .github/workflows/*.yml
   - .github/scripts/pr_health.py (and any other scripts referenced by workflows)
   - docs/ONTOLOGY.yml (or similarly named file defining allowed enums)
   - docs/SETUP_Cursor.md
   - docs/CURSOR_PLAYBOOK.md
A2) From the code, identify EXACT enum requirements for the YAML frontmatter:
   - required keys (project, type, status, tags, updated)
   - allowed values for project/type/status
   - formatting rules (--- without code fences; date format; list format; no indentation traps)
A3) Identify link rules mentioned in our gate (e.g., "docs/ links are relative /(path), no (../docs…)") and check both files for violations.

PHASE 2 — PATCH (frontmatter + links)
B1) For docs/SETUP_Cursor.md and docs/CURSOR_PLAYBOOK.md:
   - Ensure frontmatter is the very first lines in the file with only triple dashes, no backticks.
   - Conform each key to the exact enums you found. If project must be a slug, use "career-intelligence-space".
   - Use a valid type from the enum (likely "docs"); do NOT invent a new type like "setup" if it's not in the enum.
   - status should be one of the allowed values (e.g., "active" or "draft")—pick the correct one based on ONTOLOGY.yml.
   - updated should be YYYY-MM-DD (ISO date). Use today's date in local time.
   - Keep tags as a YAML list (e.g., [cursor, ide, setup, workflow, ci]).
B2) Fix any link-format violations required by the gate rules across those files (relative links policy).
B3) Propose a single patch (diff) that updates both files. Show me the diff.

PHASE 3 — VALIDATE LOCALLY (if possible)
C1) If pr_health.py can be run locally without extra secrets, run it against the changed docs to sanity-check the frontmatter and link rules. If it requires args, infer from the script.
C2) Report the results briefly.

PHASE 4 — COMMIT + REBASE + PUSH
D1) Stage all modified files.
D2) Commit with:
    "docs: compliance - conform frontmatter and doc link rules"
D3) Bring the current branch up to date with origin/main so the 'pr-update-branch' check passes:
    - Fetch origin
    - Rebase or merge origin/main into this branch (prefer rebase if clean; otherwise merge)
    - Push the updated branch (force-with-lease only if rebase was used and is safe)
   Explain which strategy you used and why.

PHASE 5 — AUTO-MERGE CHECK
E1) Open the PR and confirm whether auto-merge is enabled. If the "pr-auto-enable-automerge" workflow requires a label or other signal (e.g., specific title/prefix), infer from .github/workflows and apply it:
    - If a label is required, add it to the PR.
    - If a title prefix or comment trigger is required, update title or post the comment.
E2) If auto-merge must be toggled via the GitHub UI and cannot be toggled from code, post a concise checklist comment on the PR with the exact one-click action I need to take.

PHASE 6 — STATUS
F1) Summarize:
    - The exact enum rules you enforced
    - What changed in each file
    - Whether local validation (if any) passed
    - Whether the branch is now up-to-date
    - Whether auto-merge is enabled or what manual action is pending
