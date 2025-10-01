---
project: Career Intelligence Space
type: future_spec
status: deferred
tags: [harness, triggers, roadmap]
updated: 2025-09-30
review_date: 2026-01-15
schema_version: v1
id: FUTURE_HARDWARE_ASSETS_TODOS
---

# Triggers & TODOs — When to Promote From FUTURE

## Activation Triggers (any one)
- P95 **text capture → PR** exceeds 60s for 2 consecutive weeks.
- ≥3 PII false-positive/unresolved events per week block workflows.
- Median **rehydration time** > 5 min across a sprint.
- Context packs hit **recall deficits** (C1/C2) in 3+ weekly tasks.
- Dedicated always-on node (VPS/mini PC) becomes available (<$10/mo).

## Next Actions
1. Open a Decision Log entry ("Activate Hardware/Asset Roadmap").
2. Promote Roadmap & Addendums to `docs/architecture/harness/hardware/`.
3. Create checkpoint tag and run rollback dry-run.
4. Chronicle an activation note linking Decision & checkpoint.

## Owners
- **Architect:** Charter/Ontology/auth changes
- **Librarian:** IDs, link/anchor registry, Chronicle
- **Ops:** n8n/VPS, secrets, CI wiring

