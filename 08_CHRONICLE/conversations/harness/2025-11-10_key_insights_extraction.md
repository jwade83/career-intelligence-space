---
project: Career Intelligence Space
type: insights_extraction
status: active
tags: [insights, harness, key_decisions, strategic_analysis, collapse_risks]
updated: 2025-11-10
conversation_id: "conv_2025_11_10_harness_architecture"
extraction_date: "2025-11-10"
timezone: "America/Los_Angeles"
captured_at_utc: "2025-11-10T15:30:00Z"
related:
  - "2025-11-10_full_conversation_archive.md"
  - "2025-11-10_implementation_analysis.md"
---

# Key Insights from Harness Architecture Conversation

## Strategic Insights

### 1. Timing is Critical
- **Current system is working** - Stage B + career intelligence artifacts delivering value
- **Harness is premature** - Solving problems we don't have yet
- **Focus on validation** - Prove current system works before adding complexity

### 2. Implementation Strategy
- **80/20 rule applies** - 80% of benefits with repo-native components
- **Incremental approach** - Start simple, add complexity as needed
- **External services as upgrades** - Not required dependencies

### 3. Risk Management
- **Avoid scope creep** - Don't repeat the technical automation mistake
- **Maintain career focus** - Harness should serve career intelligence mission
- **Preserve system stability** - Don't destabilize working system

## Technical Insights

### 1. Architecture Design
- **Each component is an antibody** - Matched to specific collapse risks
- **Antifragility by design** - System gets stronger from failures
- **Externalized memory** - Not dependent on token limits

### 2. Implementation Approach
- **Repo-native first** - Leverage GitHub's native capabilities
- **External services second** - Only when needed for scale
- **Automation as enforcement** - GitHub Actions for rule enforcement

### 3. Documentation Strategy
- **Comprehensive but organized** - Structured for future reference
- **Implementation-ready** - Clear criteria and procedures
- **Conversation preservation** - Full context maintained

## Harness Features → Collapse Risk Mapping Matrix

| Harness Component | Primary Risk | Secondary Risk | Tertiary Risk | Detection Signal | Implementation Priority |
|------------------|--------------|----------------|---------------|------------------|----------------------|
| **Ontology.yml** | C3 (Vocabulary Drift) | C4 (Reference Ambiguity) | C2 (Instruction Dilution) | Term mismatch vs. Ontology linter | Phase 1 - High |
| **Context Packs** | C1 (Context Saturation) | C2 (Instruction Dilution) | C3 (Vocabulary Drift) | >3 pastebacks per session | Phase 1 - High |
| **Decision Log** | C4 (Reference Ambiguity) | C5 (Goal Creep) | C6 (Evidence Entropy) | "As we discussed before" without reference | Phase 1 - High |
| **Checkpoints** | C6 (Evidence Entropy) | C7 (Thread Fragmentation) | C4 (Reference Ambiguity) | Cannot find previous decisions | Phase 1 - Medium |
| **Chronicle** | C7 (Thread Fragmentation) | C4 (Reference Ambiguity) | C5 (Goal Creep) | Same topic spread across >2 threads | Phase 1 - Medium |
| **Agents (Roles)** | C2 (Instruction Dilution) | C5 (Goal Creep) | C7 (Thread Fragmentation) | Mixed instructions in single prompt | Phase 2 - Medium |
| **Automation Layer** | C1 (Context Saturation) | C3 (Vocabulary Drift) | C6 (Evidence Entropy) | Manual context rebuilding needed | Phase 2 - High |

## Collapse Risk Neutralization Strategy

### **C1 - Context Saturation**
- **Primary Solution:** Context Packs (lean, targeted context injection)
- **Secondary Solution:** Automation Layer (automated context pack building)
- **Detection Signal:** >3 pastebacks per session, window > X tokens
- **Implementation:** Phase 1 - High priority

### **C2 - Instruction Dilution**
- **Primary Solution:** Agents (Roles) - clear role definitions
- **Secondary Solution:** Context Packs (bounded, focused instructions)
- **Detection Signal:** Mixed instructions in single prompt
- **Implementation:** Phase 2 - Medium priority

### **C3 - Vocabulary Drift**
- **Primary Solution:** Ontology.yml (stable terminology)
- **Secondary Solution:** Automation Layer (vocabulary linting)
- **Detection Signal:** Term mismatch vs. Ontology linter
- **Implementation:** Phase 1 - High priority

### **C4 - Reference Ambiguity**
- **Primary Solution:** Decision Log (explicit rationale)
- **Secondary Solution:** Chronicle (human-readable references)
- **Detection Signal:** "As we discussed before" without reference
- **Implementation:** Phase 1 - High priority

### **C5 - Goal Creep**
- **Primary Solution:** Decision Log (documented scope)
- **Secondary Solution:** Agents (Reviewer role)
- **Detection Signal:** Scope changes without explicit decision
- **Implementation:** Phase 1 - High priority

### **C6 - Evidence Entropy**
- **Primary Solution:** Checkpoints (immutable snapshots)
- **Secondary Solution:** Decision Log (provenance preservation)
- **Detection Signal:** Cannot find previous decisions
- **Implementation:** Phase 1 - Medium priority

### **C7 - Thread Fragmentation**
- **Primary Solution:** Chronicle (narrative continuity)
- **Secondary Solution:** Checkpoints (milestone anchoring)
- **Detection Signal:** Same topic spread across >2 threads in 72h
- **Implementation:** Phase 1 - Medium priority

## Decision Framework

### When to Implement Harness
1. **Current system validated** through real usage
2. **Specific pain points identified** that Harness solves
3. **Resource availability** for implementation
4. **Clear success metrics** defined

### Implementation Priority
1. **Phase 1:** Repo-native components (80% of benefits)
2. **Phase 2:** Borderline components (intelligence layer)
3. **Phase 3:** External services (strategic upgrades)

## Key Takeaways
- **Harness is valuable** but timing is everything
- **Current system priority** - Validate before adding complexity
- **Comprehensive documentation** - Preserve all analysis for future use
- **Strategic patience** - Wait for the right moment to implement
- **Collapse risk mapping** - Each component targets specific failure modes
- **Antifragility by design** - System gets stronger from failures
- **Externalized memory** - Not dependent on token limits
