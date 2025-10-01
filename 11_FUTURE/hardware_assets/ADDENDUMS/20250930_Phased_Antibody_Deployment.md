---
project: Career Intelligence Space
type: future_spec
status: deferred
tags: [harness, phased_deployment, roadmap]
updated: 2025-09-30
review_date: 2026-01-15
schema_version: v1
id: FUTURE_ADDENDUM_PHASED_DEPLOYMENT
---

# Phased Antibody Deployment — Minimum Viable Immunity

## Phase 1 (Week 1): Keystone Immunity

**Goal:** Prevent cascade collapse at keystone, establish immune system foundation

**Deploy:**
- Ontology.yml + blocking linter (keystone antibody)
- Charter.yml with hard constraints (boundary definition)
- Basic externalization enforcement (constitutional law via Decision Log presence check)
- Link/Anchor checker + Stable ID registry (C4 guard v1)

**Acceptance Gates:**
- CI fails on synonym drift (ontology enforcement)
- CI fails on missing decision ID (externalization enforcement)
- CI fails on unresolved links (reference stability)

**Resource Cost:** ~20 hours

**MVI Achieved:**
- ✅ Cascade prevention at keystone (C3)
- ✅ Goal stability through constraints (C5)
- ✅ Memory preservation through externalization (C6/C7)
- ❌ Still vulnerable: C1/C2 (context saturation), C4 (partial)

**Survival Time:** 3-6 months before collapse risk critical

---

## Phase 2 (Week 2): Provenance & Recovery

**Goal:** Enable reconstruction and recovery, reduce permanent collapse risk

**Deploy:**
- Decision Log schema + enforcement (provenance)
- Reconstruction tests in CI (validate decision context)
- Checkpoint system with recovery metadata (recovery infrastructure)
- Tag + rollback dry-run procedures
- Context Pack generator v1 (entropy reduction)

**Acceptance Gates:**
- Reconstruction test passes for all decisions
- Rollback dry-run succeeds from latest checkpoint
- Context packs generate within token limits
- Zero duplicate information in context packs

**Resource Cost:** ~24 hours

**Requires:** MVI-1 hardware (VPS + n8n + Chroma)

**MVI Enhanced:**
- ✅ Previous protections maintained
- ✅ Provenance reconstruction enabled (C6)
- ✅ Recovery from failures possible (C6/C7)
- ✅ Context entropy reduced (C1/C2)
- ❌ Still vulnerable: C4 (full reference stability), proactive hardening

**Survival Time:** 12+ months before collapse risk critical

---

## Phase 3 (Week 3): Antifragility

**Goal:** Proactive hardening, cascade detection, complete immunity

**Deploy:**
- Cascade sensors for C1-C7 pairs (early warning)
  - C3→C2: Detect synonym creep breaking prompts
  - C4→C6: Detect reference ambiguity destroying provenance
  - C2→C5: Detect instruction dilution causing goal drift
- Stress test suite (deliberate immune testing)
  - Synonym injection test
  - Reference ambiguity test
  - Orphan decision test
- Weekly metrics dashboard (system hardening measurement)

**Acceptance Gates:**
- All three cascade sensors detect injections
- Weekly stress tests run automatically
- Report generated with pass/fail metrics
- At least one deliberate injection caught per cycle

**Resource Cost:** ~16 hours

**Requires:** MVI-1 hardware + monitoring infrastructure

**Complete Immunity Achieved:**
- ✅ All C1-C7 collapse risks addressed
- ✅ Cascade detection and prevention
- ✅ Proactive hardening through stress
- ✅ Measurable antifragility

**Survival Time:** Indefinite - system hardens from exposure

---

## Total Resource Investment

**Complete Deployment:** ~60 hours over 3 weeks
**Minimum Viable Immunity (Phase 1 only):** ~20 hours over 1 week

---

## Critical Sequencing Rules

### Rule 1: Ontology MUST Be First
**Why:** It's the keystone. Without stable vocabulary:
- Decision log terms drift
- Charter constraints become ambiguous
- Context packs reference wrong definitions
- **CANNOT SKIP OR DEFER**

### Rule 2: Charter Enables Enforcement
**Why:** Without defined constraints:
- No basis for blocking violations
- Enforcement mechanisms have no authority
- Goal creep undermines all antibodies
- **CANNOT SKIP OR DEFER**

### Rule 3: Externalization Before Decision Log
**Why:** Decision log IS externalization
- Must enforce externalization doctrine first
- Then structure it with decision log
- Order matters for enforcement

### Rule 4: Decision Log Before Checkpoints
**Why:** Checkpoints preserve context
- Context comes from decision log
- Checkpoints without context = useless
- Recovery requires reconstruction capability

### Rule 5: Context Packs Before Stress Tests
**Why:** Stress tests need scoped context
- Can't test "dump everything" prompts effectively
- Need controlled injection to measure cascade
- Context packs enable precise testing

---

## Degraded Operations Plan

### If Only Phase 1 Possible (Emergency MVI):

**Deploy Immediately:**
1. Minimal Ontology - Lock 10 critical terms only
2. Basic Linter - Block obvious synonym drift
3. Charter Constraints - 3-5 non-negotiables only
4. Externalization Hook - Block empty decision commits

**Acceptance:**
- System vulnerable to C1/C2/C4 collapse
- BUT: Cascade prevention at keystone (C3)
- BUT: Goal stability maintained (C5)
- BUT: Memory preservation enforced (C6/C7)

**Survival Time:** 3-6 months before collapse risk critical

---

### If Phase 1 + 2 Possible (Strong MVI):

**Additional Protection:**
- Provenance reconstruction enabled
- Recovery from failures possible
- Context entropy reduced

**Acceptance:**
- System vulnerable to C4 (reference drift)
- BUT: Can recover from most failures
- BUT: Can reconstruct most decisions

**Survival Time:** 12+ months before collapse risk critical

---

## Key Principle

> **Each phase must be COMPLETE before the next.**
> 
> **No partial antibodies. No "we'll finish it later."**
> 
> **Each phase achieves MVI or doesn't deploy at all.**

---

**This bridges Harness doctrine (complete immunity required) with operational reality (phased deployment necessary) while maintaining the existential framing.**

