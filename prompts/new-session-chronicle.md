# New Session Chronicle — Pipeline from Downloads → 08_CHRONICLE

You are operating on my local Mac with terminal access.

Goal: Pipeline two chat exports from ~/Downloads into the repo as Chronicles with compliant frontmatter, then PR with auto-merge.

FILES IN ~/Downloads:
- "ChatGPT-Pilot project migration.txt"
- "cursor_summarize_repository_functionali.md"

STEPS (do these exactly; report each step):

PHASE 0 — Locate repo root
- Check which path exists and use it as REPO_ROOT:
  1) /Users/johnwade/Desktop/career-intelligence-space/career-intelligence-space
  2) /Users/johnwade/Desktop/career-intelligence-space
- Ensure "$REPO_ROOT/08_CHRONICLE" exists; create if missing.

PHASE 1 — Copy + rename from Downloads
- DATE=$(date +%Y%m%d)
- Copy (not move) the two files from ~/Downloads into "$REPO_ROOT/08_CHRONICLE", preserving originals in Downloads. Use safe quoting for spaces.
- Rename inside 08_CHRONICLE to:
  - ${DATE}_ChatGPT-Pilot-Migration.md
  - ${DATE}_Cursor-Repo-Summary.md

PHASE 2 — Add YAML frontmatter (gate compliant)
For each of the two new files, ensure a YAML frontmatter block is the very first thing in the file (no backticks, no code fences). If frontmatter is missing, prepend exactly:

---
project: Career Intelligence Space
type: log
status: matured
tags: [chronicle, chat, migration]
updated: YYYY-MM-DD
---

- Set updated to today's date in local time (YYYY-MM-DD).
- Preserve the exported content exactly below the frontmatter.
- Do not remove the exported headers or change the dialogue content.
- After editing, show me a short diff preview for each file.

PHASE 3 — Commit → branch → PR
- Stage only these two files under 08_CHRONICLE.
- Commit with: 
  "chronicle: add ${DATE} ChatGPT and Cursor session logs"
- Create a new branch named:
  "chronicle/${DATE}-chat-logs"
- Push to origin, open a Pull Request, enable auto-merge (squash).
- If checks are missing or pending, trigger our `recheck` workflow or re-run failed jobs.

PHASE 4 — Status summary
- Print:
  - PR URL
  - Required checks states (gate, links)
  - Whether auto-merge is enabled
  - Which REPO_ROOT path was used
  - Exact filenames created

If any file is not found in ~/Downloads, pause and ask me whether to skip that one or provide the correct filename.
