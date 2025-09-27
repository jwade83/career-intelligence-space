---
project: Career Intelligence Space
type: spec
status: matured
tags: [transcripts, howto, docs]
updated: 2025-09-27
---
# Transcripts — Upload, Access, Policy

## Upload (one command)
- Put your export anywhere, then run:
  - `bin/cis-add-transcript "$HOME/Downloads/<export>.md"`

## Access
- Browse: `99_LOGS/transcripts/INDEX.md` (auto-updated on PRs touching transcripts).
- Link from capsules using relative links to the `.txt`.

## Policy
- Raw transcripts are `.txt` to avoid CI linkcheck noise.
- Markdown docs (capsules, memos, decisions) stay `.md` and must pass gates.
