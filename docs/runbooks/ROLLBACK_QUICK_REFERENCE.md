# Rollback Quick Reference
**Context:** Quick reference guide for Stage B rollback procedures in the Career Intelligence Space (CIS).

**Purpose:** Provide immediate access to rollback commands and procedures during emergency situations.

---

## 🚨 Emergency Rollback Commands

### **Level 1: Disable Single Workflow**
```bash
# Disable specific workflow
./scripts/rollback/workflow-disable.sh frontmatter-validation "High false positive rate"

# Manual disable
mv .github/workflows/frontmatter-validation.yml .github/workflows/frontmatter-validation.yml.disabled
```

### **Level 2: Enable Bypass for PR**
```bash
# Add bypass label to PR
gh pr edit [PR_NUMBER] --add-label "bypass-safeguard"

# Remove bypass label
gh pr edit [PR_NUMBER] --remove-label "bypass-safeguard"
```

### **Level 3: Gradual Rollback**
```bash
# Edit config to reduce strictness
vim prompts/strategic_lenses/config.yml

# Change enforcement levels:
# level: strict → lenient
# frontmatter_validation: block → warn_only
# promotion_gates: required → optional
```

### **Level 4: Complete Stage Reversion**
```bash
# Emergency stage reversion
./scripts/rollback/stage-reversion.sh "Complete system failure - reverting to Stage A"

# Manual stage reversion
mv .github/workflows/*.yml .github/workflows/*.yml.disabled
git checkout stage-a-final -- prompts/strategic_lenses/config.yml
```

---

## 📊 Rollback Triggers & Thresholds

| Trigger | Threshold | Action | Authority |
|---------|-----------|--------|-----------|
| Velocity Drop | >50% | Workflow Disable | Automated |
| PR Failure Rate | >30% | Bypass Enable | Automated |
| Review Completion | <60% | Gradual Rollback | Manual |
| System Health | >3 failures/24h | Workflow Disable | Automated |
| User Frustration | Qualitative | Gradual Rollback | Manual |
| System Break | Any | Stage Reversion | Emergency |

---

## 🔍 Monitoring Commands

### **Check System Health**
```bash
# Check workflow runs
gh run list --limit 20

# Check PR status
gh pr list --state all --limit 20

# Check review completion
gh issue list --label "weekly-review" --state all
```

### **Manual Monitoring**
```bash
# Run rollback monitoring
gh workflow run rollback-monitoring.yml

# Check specific metrics
gh workflow run rollback-monitoring.yml -f check_type=pr_failure
```

---

## 📝 Documentation & Logging

### **Create Incident Log**
```bash
# Incident log location
08_CHRONICLE/incidents/$(date +%Y-%m-%d)_rollback-[TYPE].md

# Use issue template
gh issue create --template rollback-event.md
```

### **Update Documentation**
```bash
# Update rollback runbook
vim docs/runbooks/STAGE_B_ROLLBACK.md

# Update config
vim prompts/strategic_lenses/config.yml
```

---

## 🚀 Recovery Procedures

### **After Workflow Disable**
1. Monitor system for 24-48 hours
2. Conduct RCA
3. Fix underlying issue
4. Test improved workflow
5. Re-enable with monitoring

### **After Stage Reversion**
1. Immediate stakeholder notification
2. 24-hour system monitoring
3. Comprehensive RCA within 48 hours
4. Stage B redesign planning
5. Gradual re-implementation

---

## 📞 Emergency Contacts

- **System Owner:** jwade83
- **Emergency Escalation:** [TO_BE_DEFINED]
- **Documentation:** `docs/runbooks/STAGE_B_ROLLBACK.md`

---

## ⚡ Quick Decision Matrix

| Situation | Rollback Level | Time to Execute | Recovery Time |
|-----------|----------------|-----------------|---------------|
| Single workflow issue | Level 1 | 2 minutes | 1-2 weeks |
| Multiple PRs blocked | Level 2 | 1 minute | 1-3 days |
| System friction | Level 3 | 5 minutes | 1-2 weeks |
| Complete failure | Level 4 | 10 minutes | 1-3 months |

---

**Last Updated:** 2025-11-10  
**Version:** 1.0.0  
**Next Review:** After first rollback event
