---
project: Career Intelligence Space
type: stage_planning
status: draft
tags: [cis, strategic_lenses, stage_b, planning, automation]
updated: 2025-10-20
version: "1.0.0"
stage: "B"
prerequisite: "Stage A completion"
---

# Stage B Planning - Quality Gatekeeper

## Stage B Overview
**Activation:** After 6 weeks of stable Stage A use, meeting success criteria  
**Duration:** 4-6 cycles (4-6 weeks)  
**Goal:** Lenses become part of the promotion path for artifacts  
**Success Criteria:** % of artifacts reviewed with lenses; % of incidents resulting in new safeguards

---

## Stage B Framework

### **Purpose**
Lenses become part of the promotion path: artifacts must pass relevant lens checks before "matured."

### **Key Changes from Stage A**
- **Automated Triggers:** GitHub Actions trigger specific lenses
- **Promotion Gates:** Artifacts require lens review before promotion
- **Repo-wide Enforcement:** Safeguards work across all environments
- **Quality Metrics:** Track % of artifacts reviewed with lenses

### **Success Criteria**
- **Metrics Tracked:** % of artifacts reviewed with lenses; % of incidents resulting in new safeguards
- **Automation:** Optional GitHub automation triggers specific lenses
- **Visibility:** Internal, with potential for aggregated, anonymized metrics

---

## Stage B Implementation Plan

### **Phase 1: Repo-wide Safeguards (Week 1-2)**
**Goal:** Replace local-only safeguards with repo-wide enforcement

**Deliverables:**
1. **Frontmatter Validation GitHub Action** ✅ (Created)
   - Validates frontmatter on all chronicle files
   - Blocks PRs with invalid frontmatter
   - Provides clear error messages and guidance

2. **Workflow Validation GitHub Action** (Planned)
   - Validates workflow references point to existing workflows
   - Checks for naming consistency
   - Prevents broken automation

3. **Lens Integration GitHub Action** (Planned)
   - Automated lens triggering based on events
   - Result capture and chronicle integration
   - Quality metrics collection

### **Phase 2: Promotion Gates (Week 3-4)**
**Goal:** Lenses become part of artifact promotion path

**Deliverables:**
1. **Promotion Checklist GitHub Action**
   - Requires lens review before artifact promotion
   - Validates lens outputs meet quality standards
   - Tracks promotion metrics

2. **Quality Gatekeeper Workflow**
   - Automated quality checks for all artifacts
   - Lens-based validation for different artifact types
   - Promotion approval process

### **Phase 3: Metrics & Monitoring (Week 5-6)**
**Goal:** Comprehensive tracking and optimization

**Deliverables:**
1. **Metrics Dashboard**
   - % of artifacts reviewed with lenses
   - % of incidents resulting in new safeguards
   - Lens effectiveness tracking

2. **Automated Reporting**
   - Weekly lens usage reports
   - Quality trend analysis
   - Stage B readiness assessment

---

## Stage B GitHub Actions Architecture

### **1. Frontmatter Validation** ✅
```yaml
# .github/workflows/frontmatter-validation.yml
# Validates YAML frontmatter on chronicle files
# Triggers: PR, Push to main
# Blocks: Invalid frontmatter
```

### **2. Workflow Validation** (Planned)
```yaml
# .github/workflows/workflow-validation.yml
# Validates workflow references and naming
# Triggers: PR, Push to main
# Blocks: Broken references, inconsistent naming
```

### **3. Lens Integration** (Planned)
```yaml
# .github/workflows/lens-integration.yml
# Automated lens triggering and result capture
# Triggers: PR events, schedule, manual
# Outputs: Chronicle entries, metrics
```

### **4. Promotion Gates** (Planned)
```yaml
# .github/workflows/promotion-gates.yml
# Requires lens review before promotion
# Triggers: Promotion requests
# Validates: Lens outputs, quality standards
```

---

## Stage B Success Metrics

### **Coverage Metrics**
- **Artifact Review Coverage:** % of artifacts reviewed with lenses
- **Incident Response Coverage:** % of incidents triggering lens analysis
- **Promotion Gate Coverage:** % of promotions requiring lens review

### **Quality Metrics**
- **Lens Output Quality:** % of lens outputs meeting standards
- **Safeguard Effectiveness:** % of safeguards preventing issues
- **Process Adherence:** % of processes following Stage B protocols

### **Value Metrics**
- **Decisions Improved:** Count of decisions improved by lens analysis
- **Issues Prevented:** Count of issues prevented by safeguards
- **Process Optimizations:** Count of process improvements from lens insights

---

## Stage B Activation Criteria

### **Stage A Prerequisites**
- ✅ **6 weeks of stable Stage A use**
- ✅ **≥80% weekly coverage achieved**
- ✅ **≥90% protocol adherence maintained**
- ✅ **Antifragility principle validated**
- ✅ **Concrete safeguards implemented and verified**

### **Stage B Readiness Checklist**
- [ ] **Repo-wide Safeguards:** GitHub Actions replace local-only safeguards
- [ ] **Promotion Gates:** Lenses integrated into artifact promotion path
- [ ] **Quality Metrics:** Comprehensive tracking system operational
- [ ] **Automation:** Automated lens triggering and result capture
- [ ] **Documentation:** Stage B protocols and runbooks complete

---

## Stage B Risks & Mitigations

### **Risk 1: Over-automation**
**Mitigation:** Keep manual lens execution as primary, automation as support

### **Risk 2: Quality Gate Friction**
**Mitigation:** Clear guidelines, fast feedback, easy bypass for emergencies

### **Risk 3: Metrics Complexity**
**Mitigation:** Start simple, add complexity gradually based on value

### **Risk 4: Workflow Maintenance**
**Mitigation:** Comprehensive documentation, rollback procedures, monitoring

---

## Stage B Timeline

### **Week 1-2: Repo-wide Safeguards**
- Deploy frontmatter validation GitHub Action
- Create workflow validation GitHub Action
- Test repo-wide enforcement

### **Week 3-4: Promotion Gates**
- Implement promotion checklist GitHub Action
- Create quality gatekeeper workflow
- Test promotion path integration

### **Week 5-6: Metrics & Monitoring**
- Deploy metrics dashboard
- Implement automated reporting
- Assess Stage B readiness

---

## Stage C Preparation

### **Stage C Vision**
- **External Dashboard:** Lens outputs rendered on GitHub Pages
- **Public Visibility:** Analyst = status dashboard, Engineer = repo health
- **Documentation:** Lenses double as public-facing documentation

### **Stage C Prerequisites**
- 4-6 cycles of stable Stage B use
- Proven lens effectiveness and value
- Comprehensive metrics and monitoring
- Public communication strategy

---

*Stage B Planning Document - Version 1.0.0*  
*Generated using Strategic Consultant Lenses v1.1.0 - Stage A Framework*
