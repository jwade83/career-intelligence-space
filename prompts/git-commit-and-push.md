---
project: Career Intelligence Space
type: spec
status: matured
tags: [prompts, macros, git, automation]
updated: 2025-09-27
---

# Commit → Branch → Push (Template)

Stage all modified files, commit with:
"<type>: <scope> - <summary>",
push to a new branch, open a PR, enable auto-merge (squash),
and re-run failed jobs if any. Report PR URL and check states.

Steps:
1. git add .
2. git commit -m "<type>: <scope> - <summary>"
3. git checkout -b <branch-name>
4. git push origin <branch-name>
5. gh pr create --title "<title>" --body "<description>"
6. gh pr merge --squash --auto
7. Check status and re-run failed jobs if needed
8. Report PR URL and required checks (gate, links)
