---
project: Career Intelligence Space
type: memo
status: draft
tags: [process, pr_route]
updated: 2025-09-26
---

# PR route that always works

1) Create PR
2) Enable auto-merge
3) Run pr_health to see what’s missing
4) If it says “MISSING contexts”, push a no-op commit
5) If it says strict block, run update-branch
6) Auto-merge lands when checks attach

Commands:

git checkout -b feat/my-change
git add -A && git commit -m "feat: my change" && git push -u origin feat/my-change
gh pr create --fill
PR=$(gh pr view --json number --jq .number)
gh pr merge "$PR" --squash --auto
python3 .github/scripts/pr_health.py "$PR"
