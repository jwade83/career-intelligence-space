---
project: Career Intelligence Space
type: spec
status: active
tags: [harness, immune_system, collapse_prevention, future_development]
updated: 2025-09-30
---

# Harness: LLM Collapse Prevention Immune System

## 🎯 Purpose

The **Harness** is an immune system designed to prevent LLM project collapse (C1-C7 failure modes) through enforced antibodies, not optional best practices. This directory contains the future-facing specifications for the complete Harness system, which requires external assets (hardware + services) not yet deployed.

## 🛡️ What is the Harness?

**From ChatGPT Harness Development:**

> "LLM projects collapse because finite context + statelessness + human inconsistency create saturation, dilution, drift, ambiguity, creep, entropy, and fragmentation (C1–C7). The only durable answer is infrastructure that constrains and externalizes memory with enforcement—your Harness—so the system stays reliable as it scales in time, people, and artifacts."

**The Harness is:**
- **Not a feature wishlist** - It's an immune system
- **Not optional enhancements** - It's survival infrastructure
- **Not additive scaffolding** - It's a complete defense system
- **Not reactive patches** - It's proactive hardening

## 🧬 The Seven Collapse Risks (C1-C7)

### **C1. Context Saturation**
- **Symptom:** Prompts exceed practical window or bury key constraints
- **Mechanism:** Important items get truncated or drowned in noise
- **Antibody:** Context packs with scoped, role-specific bundles

### **C2. Instruction Dilution**
- **Symptom:** Outputs follow shape but miss spirit
- **Mechanism:** Conflicting prompts; model averages incompatible asks
- **Antibody:** Charter with enforced constraints, context packs

### **C3. Vocabulary Drift** (KEYSTONE RISK)
- **Symptom:** Terms mutate until definitions blur
- **Mechanism:** Paraphrase + summarization + synonym creep
- **Antibody:** Ontology.yml + blocking linter

### **C4. Reference Ambiguity**
- **Symptom:** Vague callbacks produce wrong references
- **Mechanism:** No stable IDs or canonical links
- **Antibody:** Stable ID registry + link/anchor checker

### **C5. Goal Creep**
- **Symptom:** Outputs chase adjacent goals while abandoning north star
- **Mechanism:** No charter + change log
- **Antibody:** Charter.yml with constraint ledger

### **C6. Evidence Entropy**
- **Symptom:** Can't reconstruct why a decision was made
- **Mechanism:** Mutable docs, missing checkpoints, no rationale
- **Antibody:** Decision Log + checkpoints with recovery metadata

### **C7. Thread Fragmentation**
- **Symptom:** Critical context scattered across apps
- **Mechanism:** Parallel conversations without chronicle layer
- **Antibody:** Chronicle system + externalization enforcement

## 🧪 Cascade Dynamics

**Collapse is not linear - it's cascading:**

```
C3 vocabulary drift
  ↓
C2 instruction dilution
  ↓
C4 reference ambiguity
  ↓
C6 evidence entropy
  ↓
SYSTEM COLLAPSE (unrecoverable)
```

**Without keystone antibody (Ontology), entire system erodes.**

## 🛡️ The Seven Antibodies (Non-Negotiable)

### **1. Charter.yml** (Prevents C5)
**What:** Non-negotiable constraint ledger
**Not:** Mission statement or guidelines
**Enforcement:** Violations blocked at commit
**Status:** 🔴 NOT DEPLOYED

### **2. Ontology.yml + Linter** (Prevents C3 - KEYSTONE)
**What:** Canonical term definitions with blocking enforcement
**Not:** Suggested vocabulary guidelines
**Enforcement:** CI fails on synonym drift
**Status:** 🔴 NOT DEPLOYED

### **3. Decision Log** (Prevents C6)
**What:** Immutable rationale tracking with reversibility notes
**Not:** Optional documentation
**Enforcement:** Reconstruction tests must pass
**Status:** 🔴 NOT DEPLOYED

### **4. Checkpoints** (Prevents C6/C7)
**What:** Recovery anchors with rollback procedures
**Not:** Git commits with better messages
**Enforcement:** Rollback tests must pass
**Status:** 🔴 NOT DEPLOYED

### **5. Context Packs** (Prevents C1/C2)
**What:** Scoped, role-specific prompt bundles
**Not:** Prompt templates
**Enforcement:** Never dump everything
**Status:** 🔴 NOT DEPLOYED

### **6. Externalization Enforcement** (Prevents C6/C7)
**What:** Constitutional law - nothing lives only in chat
**Not:** Workflow best practice
**Enforcement:** Audit reports flag violations
**Status:** 🟡 PARTIAL (manual process)

### **7. Cascade Sensors** (Prevents compound failure)
**What:** Early warning for C3→C2, C4→C6, C2→C5
**Not:** Error logging
**Enforcement:** Weekly stress tests required
**Status:** 🔴 NOT DEPLOYED

## 🏗️ Current CIS Status vs. Full Harness

### **✅ What CIS Has (70% Foundation):**
- Chronicle system (partial C7 prevention)
- Documentation structure (scaffolding for antibodies)
- GitHub-native infrastructure (foundation for enforcement)
- Reality check documents (awareness of collapse risks)
- Operational specifications (implementation guidance)

### **🔴 What CIS Lacks (30% Critical Antibodies):**
- Charter.yml (C5 unprotected)
- Ontology.yml + Linter (C3 KEYSTONE missing)
- Decision Log (C6 vulnerable)
- Checkpoints (recovery impossible)
- Context Packs (C1/C2 at risk)
- Cascade Sensors (no early warning)
- Stress Tests (no proactive hardening)

## 🚧 Why This is Partitioned / Future-Facing

### **Hardware Dependencies:**

The complete Harness requires external assets not yet deployed:

1. **Always-on orchestrator** (n8n on VPS)
   - Enables continuous externalization enforcement
   - Required for: Real-time cascade detection

2. **Vector memory** (Chroma/Weaviate/Pinecone)
   - Enables context pack generation
   - Required for: C1/C2 prevention

3. **Transcription service** (whisper.cpp/API)
   - Enables voice capture → PR workflow
   - Required for: Field Agent mobile capture

4. **Decision Log DB** (SQLite/Airtable)
   - Enables provenance reconstruction
   - Required for: C6 prevention

**See:** `08_CHRONICLE/harness/HARNESS_ADDENDUM_HARDWARE_ASSET_ROADMAP.md`

## 📊 Phased Deployment Plan

### **Phase 1: Keystone Antibodies (Week 1)**
**Goal:** Minimum Viable Immunity (MVI)
**Deploy:**
- Ontology.yml + Blocking Linter (KEYSTONE)
- Charter.yml with Hard Constraints
- Basic Externalization Enforcement

**Acceptance:** CI blocks vocabulary drift, goal violations, non-externalized decisions

### **Phase 2: Recovery Infrastructure (Week 2)**
**Goal:** Enable reconstruction and recovery
**Deploy:**
- Decision Log Schema + Enforcement
- Checkpoint System with Recovery Metadata
- Context Pack Generator

**Requires:** MVI-1 hardware (VPS + n8n + Chroma)

### **Phase 3: Antifragility (Week 3)**
**Goal:** Proactive hardening
**Deploy:**
- Cascade Sensors for C1-C7 pairs
- Stress Test Suite
- Antifragility Metrics Dashboard

**Requires:** MVI-1 hardware + monitoring infrastructure

## 🎯 Key Principles

### **1. Antibodies are Non-Negotiable**
> "Every antibody is required. Failure to implement ANY ONE guarantees collapse through cascading failure across C1-C7."

### **2. Collapse is Cascading by Default**
> "Collapse doesn't happen gradually → it compounds exponentially. Early cascade detection is existential, not optional."

### **3. Externalization is Constitutional Law**
> "Nothing lives only in chat. Skipping externalization is not a workflow choice - it's a violation."

### **4. Ontology is Keystone**
> "Vocabulary drift cascades into EVERY other collapse risk. Without stable terms, the entire immune system fails."

### **5. Provenance is Existential**
> "A decision without provenance doesn't exist - it's a phantom that will cause collapse."

### **6. Antifragility Through Stress**
> "Don't just measure failure - deliberately induce stress to test immune response."

## 📚 Related Documentation

### **Harness Theory & Principles:**
- `08_CHRONICLE/harness/HARNESS_BRIDGE_NOTE.md` - Harness vs. Cursor framing
- `08_CHRONICLE/harness/HARNESS_ADDENDUM_HARDWARE_ASSET_ROADMAP.md` - Hardware requirements

### **Current CIS Implementation:**
- `docs/ALERTS/Reality_Check.md` - What's live vs. aspirational
- `docs/ALERTS/Jobs_Radar_IssueSpec.md` - Comment grammar & receipts
- `docs/ALERTS/Snooze.md` - State management
- `docs/AGENTS/Field_Agent_v06_Hard_Rails.md` - Hard-rail schemas
- `docs/AUTOMATION.md` - CI checks & auto-merge

### **Strategic Context:**
- `08_CHRONICLE/2025-09-30_Field_Agent_v06_Design_Evolution_Capsule.md` - Design evolution
- `08_CHRONICLE/2025-09-30_Jobs_Radar_Intelligence_System_Implementation_Capsule.md` - Implementation progress

## 🚨 Critical Understanding

**The Harness is not "nice to have" - it's survival infrastructure.**

Without it:
- C3 vocabulary drift cascades into C2/C4/C6
- C6 evidence entropy makes decisions unrecoverable
- C7 thread fragmentation destroys continuity
- C5 goal creep undermines all other protections
- System collapse is guaranteed within 3-6 months

**With partial deployment (MVI):**
- Collapse delayed to 12+ months
- Recovery possible from most failures
- But vulnerable to cascade events

**With complete deployment:**
- Collapse prevented indefinitely
- System hardens from stress
- Antifragility achieved

---

**The Harness is an immune system. Every antibody is required.** 🛡️🧬

