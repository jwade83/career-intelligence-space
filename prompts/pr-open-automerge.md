---
project: Career Intelligence Space
type: spec
status: matured
tags: [prompts, macros, pr, automation]
updated: 2025-09-27
---

# PR: Open + Auto-Enable (Squash) + Recheck

Open the current PR. 
- If "Update branch" is offered, do it.
- If any jobs are still red, click "Re-run failed jobs".
- Confirm auto-merge is enabled (squash). If not, enable it.
Report back which actions were taken.

Steps:
1. Check current PR status
2. Update branch if needed (gh api -X PUT repos/{owner}/{repo}/pulls/{pr}/update-branch)
3. Re-run failed jobs if any (gh run rerun <run-id>)
4. Enable auto-merge if not already enabled (gh pr merge <pr> --squash --auto)
5. Report final status and actions taken
