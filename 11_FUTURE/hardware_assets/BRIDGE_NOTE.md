---
project: Career Intelligence Space
type: future_spec
status: deferred
tags: [harness, bridge_note, doctrine, collapse_prevention]
updated: 2025-09-30
review_date: 2026-01-15
schema_version: v1
id: FUTURE_BRIDGE_NOTE_HARDWARE
related:
  - /11_FUTURE/hardware_assets/20250930_Hardware_Asset_Roadmap.md
---

# Bridge Note: Harness Principles vs. Cursor Framing

**Purpose:**  
This note reconciles the Cursor-framed review of our GitHub scaffolding with the deeper Harness intent. Cursor's framing is useful but flattens systemic risks into checklists. The Harness view treats collapse risks as *failure modes* with interdependencies, and antibodies as *operating doctrines* rather than optional patches.

---

## 1. Collapse Risks as Failure Modes, Not Checkboxes
- **Cursor framing:** C1–C7 as discrete risks, mapped to repo features.
- **Harness framing:** Risks interlock and compound.  
  - Example: C3 vocabulary drift → C2 instruction dilution → C4 reference ambiguity → C6 evidence entropy.  
  - Collapse is usually *cascading*, not isolated.

---

## 2. Externalized Memory as the Primary Defense
- **Cursor framing:** Repo as "memory bank."
- **Harness framing:** **Nothing important lives only in chat.** Repo scaffolding is not a convenience but a non-negotiable survival principle.  

---

## 3. Ontology as Keystone Antibody (C3)
- **Cursor framing:** Ontology.yml suggested, linter optional.
- **Harness framing:** Vocabulary drift is the keystone collapse vector.  
  - Antibody = enforced ontology + linter that *blocks drift at commit*.  
  - Without this, all downstream collapse risks re-emerge.

---

## 4. Decision Log & Provenance (C6)
- **Cursor framing:** Missing but "some context lost."  
- **Harness framing:** Lack of provenance = existential failure.  
  - If decisions and rationales can't be reconstructed, the system is untrustworthy.  
  - Antibody = immutable decision log with reversibility notes.

---

## 5. Checkpoints as Recovery Anchors (C6/C7)
- **Cursor framing:** Git commits as snapshots.  
- **Harness framing:** Explicit checkpoints are annotated *anchors* designed for recovery.  
  - Purpose = fast rollback and time-travel, not just git history.

---

## 6. Context Packs as Controlled Injections (C1/C2)
- **Cursor framing:** Automation for prompts.  
- **Harness framing:** Controlled scope is the point.  
  - Context packs = compressed, role-specific capsules to *reduce entropy*.  
  - Rule: never dump everything, always load scoped packs.

---

## 7. Charter as Constraint Ledger (C5)
- **Cursor framing:** North star / mission doc.  
- **Harness framing:** Charter = **non-negotiable constraint ledger**.  
  - Defines what cannot be bent, even if expedient.  
  - More like guardrails than mission statements.

---

## 8. Antifragility Principle
- **Cursor framing:** Repo provides memory + continuity.  
- **Harness framing:** System must get stronger under stress.  
  - Linter errors, QA failures, and flagged PII are *positive stressors*.  
  - Feedback loops are deliberately designed to harden the system.

---

## 9. Synthesis
- **Cursor Review:** 70% of Harness scaffolding already active (docs, chronicle, validation).  
- **Harness View:** Remaining 30% (Charter, Ontology, Context Packs, Decision Log, Checkpoints) are not "nice to haves" but essential antibodies against systemic collapse.  

---

## 10. Actionable Next Steps
1. **Charter.yml** → lock non-negotiable rules.  
2. **Ontology.yml + linter** → enforce vocab stability.  
3. **Context packs** → modular scoped prompts.  
4. **Decision Log** → immutable rationale tracking.  
5. **Checkpoint tags** → recovery anchors with metadata.  

---

**Key Insight:**  
Cursor shows *what's been built*. Harness shows *why it must exist and how it survives collapse*. This Bridge Note ensures both frames remain visible: the practical GitHub scaffolding and the systemic Harness antibodies.

---

