---
project: Career Intelligence Space
type: log
status: matured
tags: ['llm', 'streams', 'newsletter']
updated: 2025-10-02
---

## Highlights
- Outward-facing **newsletter/blog deliverables** defined with provenance.
- Platforms compared (GitHub Pages, Substack, Medium) → **Substack** chosen for speed.
- **Two-tier record** adopted: private hashed vault + public digest/newsletter.
- Pain points addressed: minimize copy/paste; standardize digests + action logs.
- **Traceability Matrix** mandated for each Chronicle.

## Decisions
- ✅ Substack as initial publishing channel.
- ✅ SHA-256 on each export + pointers in `POINTERS.md`.
- ✅ Matrix + redaction policy are mandatory.

## Notable insights (verbatim quotes ≤20 words, then anchor + why it matters)
- “Define deliverables clearly; readers must jump in mid-stream.” [L12] — Sets newsletter clarity bar.
- “Substack gives clean email + web with minimal setup.” [L18] — Fastest path to audience.
- “Two-tier model: vault (lossless) and digest (readable), linked by hash.” [L22] — Auditability + readability.
- “Avoid manual copy/paste; standardize digests + action logs.” [L28] — Repeatable, low-friction ops.
- “Chronicle ≠ raw log; it’s sourced narrative for outsiders.” [L40] — Focus on context, not transcripts.

## Actions requested
- [ ] Create digest + action log per critical session (owner: JW; cadence: per session)
- [ ] Draft Chronicle pilot issue referencing hash + sources
- [ ] Prepare Substack skeleton mapped to Chronicle sections

## Artifacts
- Pointer entry: `10_LLM_STREAMS/POINTERS.md` (this session)
- Vault: `vault://chatgpt/ChatGPT-Project newsletter strategy.md` (hashed)
