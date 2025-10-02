---
project: Career Intelligence Space
type: spec
status: matured
tags: ['docs']
updated: 2025-10-02
---

# D5 — Human↔Machine Handshake (Why linkcheck matters)

**Intent:** Make every human contribution produce a *machine-verifiable state change*.

## Two languages
- **Human talk:** capsules, memos, decisions, quick notes.
- **Computer talk:** folders, frontmatter, links, CI gates, indexes.

## Handshake
A change is “real” when machines can traverse it:
- Links resolve (no orphans/404s).
- Frontmatter present (structured fields).
- Artifacts indexed/addressable.
- Weekly rollup sees it (metrics move).

## Guardrails
- **Blocking:** linkcheck (must pass to merge).
- **Advisory:** tag-drift warn.
- (Soon) frontmatter-required; ontology drift.

## Conventions
- Links within `docs/` → use `./relative`.
- Cross-tree links → repo-root: `/path/to/file.md`.
- Match **filename case** exactly.
