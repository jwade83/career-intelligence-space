# Promotion Gates - Stage B Quality Gatekeeper
**Context:** Defines the promotion path for artifacts through maturity levels with lens-gated quality checks.

**Purpose:** Ensure artifacts meet quality standards before promotion, with strategic lens reviews as part of the promotion process.

---

## Artifact Maturity Levels

### **Level 1: Draft**
**Status:** `draft`  
**Description:** Initial creation, work in progress  
**Requirements:** Basic frontmatter, no quality gates

### **Level 2: In Review**
**Status:** `in-review`  
**Description:** Ready for lens review and quality assessment  
**Requirements:** Complete frontmatter, ready for Strategic Analyst + Project Manager review

### **Level 3: Matured**
**Status:** `matured`  
**Description:** Quality-assured, lens-reviewed, ready for use  
**Requirements:** Passed lens review, meets quality standards

### **Level 4: Promoted**
**Status:** `promoted`  
**Description:** Production-ready, externally validated  
**Requirements:** Additional validation, stakeholder approval

---

## Promotion Gate Requirements

### **Draft → In Review**
**Gate:** Basic Quality Check  
**Requirements:**
- [ ] Valid YAML frontmatter
- [ ] Complete content structure
- [ ] Proper file naming convention
- [ ] Appropriate tags assigned

**Automation:** Frontmatter validation GitHub Action

### **In Review → Matured**
**Gate:** Strategic Lens Review  
**Requirements:**
- [ ] Strategic Analyst lens review completed
- [ ] Project Manager lens review completed
- [ ] Quality standards met
- [ ] No critical issues identified

**Process:** Manual lens application + quality assessment

### **Matured → Promoted**
**Gate:** Stakeholder Validation  
**Requirements:**
- [ ] External stakeholder review (if applicable)
- [ ] Production readiness confirmed
- [ ] Documentation complete
- [ ] Integration tested

**Process:** Manual stakeholder review + final validation

---

## Lens Review Requirements by Artifact Type

### **Chronicle Entries (08_CHRONICLE/)**
**Required Lenses:** Strategic Analyst + Project Manager  
**Review Focus:**
- Strategic Analyst: Big-picture value, alignment with goals
- Project Manager: Timeline, dependencies, resource allocation

### **Documentation (docs/)**
**Required Lenses:** Strategic Analyst + Systems Engineer  
**Review Focus:**
- Strategic Analyst: Strategic value, clarity, completeness
- Systems Engineer: Technical accuracy, workflow integration

### **Templates (02_TEMPLATES/)**
**Required Lenses:** Strategic Analyst + Productivity Coach  
**Review Focus:**
- Strategic Analyst: Template value, reusability
- Productivity Coach: Usability, workflow efficiency

### **Research (03_RESEARCH/)**
**Required Lenses:** Strategic Analyst + Venture Designer  
**Review Focus:**
- Strategic Analyst: Research quality, strategic insights
- Venture Designer: Market relevance, opportunity assessment

### **Tools (04_TOOLS/)**
**Required Lenses:** Systems Engineer + Project Manager  
**Review Focus:**
- Systems Engineer: Technical implementation, integration
- Project Manager: Usability, maintenance requirements

---

## Promotion Gate Automation

### **Automated Gates**
```yaml
automated_gates:
  frontmatter_validation:
    trigger: "PR creation or update"
    check: "Valid YAML frontmatter"
    action: "Block PR if invalid"
    bypass: "bypass-safeguard label"
  
  naming_convention:
    trigger: "File creation"
    check: "Proper naming convention"
    action: "Warning comment"
    bypass: "Manual override"
```

### **Manual Gates**
```yaml
manual_gates:
  lens_review:
    trigger: "Status change to in-review"
    requirement: "Strategic lens reviews completed"
    action: "Manual verification required"
    documentation: "Lens review results in PR comments"
  
  stakeholder_approval:
    trigger: "Status change to promoted"
    requirement: "Stakeholder review completed"
    action: "Manual approval required"
    documentation: "Approval recorded in issue/PR"
```

---

## Promotion Workflow

### **Step 1: Create Artifact (Draft)**
```bash
# Create new artifact with proper frontmatter
touch new-artifact.md
# Add frontmatter with status: draft
# Commit and push
```

### **Step 2: Request Review (In Review)**
```bash
# Update status to in-review
# Create PR with lens review request
# Apply appropriate labels
```

### **Step 3: Lens Review Process**
```markdown
## Lens Review Request

**Artifact:** [ARTIFACT_NAME]
**Type:** [ARTIFACT_TYPE]
**Current Status:** in-review
**Target Status:** matured

### Required Lenses:
- [ ] Strategic Analyst
- [ ] Project Manager
- [ ] [ADDITIONAL_LENS_IF_NEEDED]

### Review Focus:
[SPECIFIC_REVIEW_AREAS]

### Quality Checklist:
- [ ] Content completeness
- [ ] Technical accuracy
- [ ] Strategic alignment
- [ ] Usability
```

### **Step 4: Quality Assessment**
```yaml
quality_criteria:
  content_quality:
    - Complete and accurate information
    - Clear structure and organization
    - Appropriate level of detail
  
  strategic_alignment:
    - Aligns with CIS goals
    - Provides clear value
    - Supports decision-making
  
  technical_quality:
    - Proper formatting
    - Valid references
    - Working examples
  
  usability:
    - Easy to understand
    - Practical application
    - Clear next steps
```

### **Step 5: Promotion Decision**
```markdown
## Promotion Assessment

**Artifact:** [ARTIFACT_NAME]
**Reviewer:** [REVIEWER_NAME]
**Date:** [DATE]

### Lens Review Results:
- **Strategic Analyst:** [APPROVED/REJECTED] - [COMMENTS]
- **Project Manager:** [APPROVED/REJECTED] - [COMMENTS]

### Quality Assessment:
- **Content Quality:** [SCORE/COMMENTS]
- **Strategic Alignment:** [SCORE/COMMENTS]
- **Technical Quality:** [SCORE/COMMENTS]
- **Usability:** [SCORE/COMMENTS]

### Promotion Decision:
- [ ] **APPROVED** - Promote to matured
- [ ] **REJECTED** - Return to draft with feedback
- [ ] **CONDITIONAL** - Approve with minor revisions

### Next Steps:
[SPECIFIC_ACTIONS_REQUIRED]
```

---

## Promotion Gate Monitoring

### **Metrics Tracking**
```yaml
promotion_metrics:
  total_artifacts: 0
  draft_artifacts: 0
  in_review_artifacts: 0
  matured_artifacts: 0
  promoted_artifacts: 0
  
  promotion_rates:
    draft_to_review: 0%
    review_to_matured: 0%
    matured_to_promoted: 0%
  
  lens_review_metrics:
    total_reviews_requested: 0
    reviews_completed: 0
    reviews_approved: 0
    reviews_rejected: 0
    review_completion_rate: 0%
```

### **Quality Indicators**
- **Promotion Rate:** % of artifacts successfully promoted
- **Review Completion:** % of lens reviews completed on time
- **Quality Score:** Average quality assessment score
- **Rejection Rate:** % of artifacts rejected during review

---

## Rollback Procedures for Promotion Gates

### **Gate Failure Response**
```yaml
gate_failure_response:
  frontmatter_validation_failure:
    action: "Block PR with clear error message"
    resolution: "Fix frontmatter and resubmit"
    escalation: "Manual bypass if legitimate edge case"
  
  lens_review_failure:
    action: "Return to draft status"
    resolution: "Address feedback and resubmit"
    escalation: "Alternative reviewer if needed"
  
  quality_assessment_failure:
    action: "Conditional approval with revisions"
    resolution: "Complete required changes"
    escalation: "Stakeholder review if needed"
```

### **Promotion Gate Rollback**
```bash
# Disable promotion gate automation
mv .github/workflows/promotion-gates.yml .github/workflows/promotion-gates.yml.disabled

# Revert to manual promotion process
# Update documentation
# Notify stakeholders
```

---

## Promotion Gate Success Criteria

### **Week 1-2 Targets**
- [ ] Promotion gate system operational
- [ ] First artifacts promoted through gates
- [ ] Lens review process established
- [ ] Quality metrics baseline established

### **Month 1 Targets**
- [ ] ≥85% promotion success rate
- [ ] ≤2 hours average review time
- [ ] ≥95% gate compliance rate
- [ ] ≥80% lens review completion rate

---

**Last Updated:** 2025-11-10  
**Version:** 1.0.0  
**Status:** Active - Stage B Implementation
