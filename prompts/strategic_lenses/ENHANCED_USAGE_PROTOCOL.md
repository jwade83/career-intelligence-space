---
project: Career Intelligence Space
type: enhanced_protocol
status: active
tags: [cis, strategic_lenses, enhanced_protocol, stage_framework, metrics]
updated: 2025-09-29
version: "1.1.0"
---

# Enhanced Strategic Consultant Lenses Usage Protocol

**Version:** 1.1.0 (2025-09-29)  
**Status:** Active - Stage A Implementation  
**Framework:** ChatGPT Enhanced with CIS Integration

---

## 🎯 Purpose

This enhanced protocol integrates ChatGPT's stage-based framework with our existing CIS strategic consultant lenses system. The lenses serve as both **operational tools** (repeatable prompts) and **strategic consultants** (perspectives on system health), ensuring consistent, measurable, and phased implementation aligned with CIS maturity.

---

## 🧭 Core Principles

1. **Consistency over novelty** – Better to run fewer lenses regularly than many lenses sporadically
2. **Structured derivatives** – Each lens produces outputs that feed into chronicles, assessments, or repo hygiene artifacts
3. **Stage-based growth** – Lenses scale from internal scaffolding to external dashboards only once metrics validate their value
4. **Antifragility** – Failures or workflow breaks are opportunities to trigger a lens, capture the learning, and reinforce the system
5. **No collapse** – Canonical prompts, frontmatter, and version control protect lens integrity across tools

---

## 📋 Enhanced Lens Triggers & Usage

| Lens                | Primary Use                  | Trigger Points                                    | Output Placement                        | Stage A Metrics |
|---------------------|------------------------------|--------------------------------------------------|-----------------------------------------|-----------------|
| **Strategic Analyst** | Big-picture project review   | Weekly reviews, milestone checks, quarterly retros | `/08_CHRONICLE/weekly/` entries          | % weeks with reviews |
| **Project Manager**   | Task-level clarity & risk    | Weekly reviews, sprint planning, blockers         | `/08_CHRONICLE/weekly/` entries          | % weeks with PM analysis |
| **Systems Engineer**  | Repo/automation health       | PR failure, sync drift, automation outage         | `/08_CHRONICLE/incidents/` or `/docs/runbooks/` | # incidents → fixes |
| **Productivity Coach**| Momentum & focus             | Daily check-ins, when noticing focus drift        | `/08_CHRONICLE/daily/` or personal tracker | % days with momentum check |
| **Venture Designer**  | Future opportunities & scaling| Quarterly reviews, roadmap planning               | `/08_CHRONICLE/quarterly/` entries       | % quarters with market analysis |

---

## ⏳ Stage Framework Implementation

### **Stage A – Internal Review (Current)**
**Duration:** Minimum 6 weeks  
**Success Criteria:**
- Consistent usage across all lens types
- Outputs logged in appropriate chronicle subdirectories
- First metrics collected and baseline established
- No public visibility

**Implementation:**
- Lenses run in chronicle workflows (weekly/daily/incident)
- Success = consistent usage, outputs logged, first metrics collected
- Maintain existing CIS automation and workflows

### **Stage B – Quality Gatekeeper (Next)**
**Trigger:** After 6 weeks of stable Stage A usage  
**Success Criteria:**
- Lenses become part of promotion path
- Artifacts must pass relevant lens checks before "matured"
- Metrics tracked: % of artifacts reviewed with lenses
- % of incidents resulting in new safeguards

**Implementation:**
- GitHub automation triggers specific lenses
- Quality gates for chronicle promotion
- Incident response protocols with lens integration

### **Stage C – External Dashboard (Future)**
**Trigger:** After 4-6 cycles of stable Stage B use  
**Success Criteria:**
- Lens outputs rendered on GitHub Pages
- Lenses double as public-facing documentation
- CIS health and trajectory visible externally

**Implementation:**
- GitHub Pages integration
- Public dashboard development
- External value demonstration

---

## 📊 Success Metrics Framework

### **Coverage Metrics**
- **Weekly Coverage:** % of weeks with Strategic Analyst + Project Manager reviews logged
- **Daily Coverage:** % of days with Productivity Coach momentum checks
- **Incident Coverage:** % of incidents triggering Systems Engineer analysis
- **Quarterly Coverage:** % of quarters with Venture Designer market analysis

### **Antifragility Metrics**
- **Incident Resolution:** # of Systems Engineer-triggered incidents that led to permanent fixes
- **Learning Capture:** % of failures resulting in improved processes
- **System Reinforcement:** # of new safeguards implemented from lens insights

### **Consistency Metrics**
- **Cross-Tool Consistency:** Cross-tool lens outputs (ChatGPT, Perplexity, Cursor) match structure
- **Protocol Adherence:** % of lens usage following established protocols
- **Quality Standards:** % of lens outputs meeting quality criteria

### **Value Metrics**
- **Decision Clarity:** Evidence of clearer decisions from lens analysis
- **Stall Reduction:** Reduced time to resolution of blockers
- **Process Improvement:** Measurable workflow enhancements

---

## 🚀 Implementation Roadmap

### **Phase 1: Stage A Foundation (Weeks 1-6)**
1. **Week 1-2:** Implement new chronicle subdirectory structure
2. **Week 3-4:** Begin consistent lens usage with new structure
3. **Week 5-6:** Collect baseline metrics and establish patterns

### **Phase 2: Stage A Optimization (Weeks 7-12)**
1. **Week 7-8:** Refine protocols based on usage data
2. **Week 9-10:** Optimize lens combinations and triggers
3. **Week 11-12:** Prepare for Stage B transition

### **Phase 3: Stage B Preparation (Weeks 13-18)**
1. **Week 13-14:** Design quality gatekeeper protocols
2. **Week 15-16:** Implement GitHub automation triggers
3. **Week 17-18:** Test Stage B workflows

---

## 🛡️ Risk Mitigation

### **Repository Stability**
- **Gradual Migration:** New structure alongside existing
- **Backward Compatibility:** Existing workflows continue to function
- **Rollback Capability:** Easy reversion if issues arise

### **Automation Safety**
- **Workflow Updates:** Gradual enhancement of existing automation
- **Path Dependencies:** Maintain existing file locations
- **Testing:** Validate changes before full deployment

### **Quality Assurance**
- **Protocol Validation:** Test new protocols before implementation
- **Metrics Baseline:** Establish clear success criteria
- **Feedback Loops:** Regular assessment of system effectiveness

---

## 📋 Next Steps (2025 Q4)

### **Immediate (This Week)**
1. **Create Chronicle Subdirectories** - Implement new organizational structure
2. **Begin Stage A Usage** - Start consistent lens application
3. **Establish Metrics Baseline** - Begin collecting usage data

### **Short-term (Next 4 Weeks)**
1. **Maintain Stage A** for consistent usage and data collection
2. **Refine Protocols** based on real-world usage
3. **Prepare Stage B** quality gatekeeper design

### **Medium-term (Next 8 Weeks)**
1. **Implement Stage B** quality gatekeeper protocols
2. **Add GitHub Automation** for lens triggering
3. **Develop Metrics Dashboard** for tracking progress

---

## 🔧 Integration with Existing CIS

### **Chronicle System**
- **New Structure:** `/08_CHRONICLE/weekly/`, `/daily/`, `/incidents/`, `/quarterly/`
- **Existing Files:** Remain in current locations for backward compatibility
- **Index Updates:** Gradual migration of INDEX.md to handle both structures

### **Automation Workflows**
- **Existing Workflows:** Continue to function with current file locations
- **New Workflows:** Handle new subdirectory structure
- **Gradual Enhancement:** Update automation incrementally

### **Quality Standards**
- **Frontmatter:** Maintain existing CIS standards
- **Tagging:** Add new tags for enhanced framework
- **Status Values:** Ensure compatibility with existing values

---

*Enhanced Protocol v1.1.0 - Integrated with ChatGPT Stage Framework*
*Updated: 2025-09-29*
