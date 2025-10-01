---
project: Career Intelligence Space
type: decision_log
status: active
tags: [decisions, provenance, harness]
updated: 2025-09-30
---

# Decision Log

This document maintains a chronological record of significant architectural and strategic decisions for the Career Intelligence Space project.

## About This Log

**Purpose:** Preserve decision context, rationale, and reversibility for future reference and reconstruction.

**Format:** Each decision entry includes:
- Decision statement
- Rationale
- Alternatives considered
- Reversibility assessment
- Success criteria
- Related artifacts

---

## Decisions

### 2025-09-30 — Create Future Silo for Hardware/Asset Roadmap

- **Decision:** Create `/11_FUTURE/hardware_assets/` silo for deferred hardware/asset roadmap planning
- **Rationale:** 
  - Preserve detailed Harness doctrine and hardware roadmap without cluttering active docs
  - Prevent collapse of nuanced planning through structured preservation
  - Enable time-deferred activation with complete context preservation
- **Alternatives:**
  - Keep in active docs (rejected: premature, clutters active work)
  - Delete and recreate when needed (rejected: context loss, collapse risk)
  - Store in Chronicle only (rejected: no recall automation, hard to discover)
- **Reversibility:** High — can promote to active docs or archive to Chronicle
- **Success Criteria:**
  - Automated review triggers on schedule
  - Complete context preserved for activation
  - Discoverable but not intrusive
  - No drift or entropy over time
- **Related:** 
  - FUTURE_HARDWARE_ASSETS_HOME
  - HARNESS_ADDENDUM_HARDWARE_ASSET_ROADMAP
  - Future Review Pinger workflow

---

## Template for Future Activation Decision

### [DATE] — Activate Hardware/Asset Roadmap

- **Decision:** Promote `/11_FUTURE/hardware_assets/` → `docs/architecture/harness/hardware/`
- **Rationale:** Triggers met (capture latency + rehydration metrics)
- **Alternatives:** Maintain batch-only GitHub Actions (rejected: latency)
- **Reversibility:** High — rollback to FUTURE and tags
- **Success Criteria:** P95 text capture→PR ≤ 60s; weekly stress tests green
- **Related:** FUTURE_HARDWARE_ASSETS_HOME, HARNESS_ADDENDUM_HARDWARE_ASSET_ROADMAP

---

*For decision record template, see: `99_LOGS/decision_template.md`*

