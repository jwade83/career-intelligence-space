---
name: Stage B Rollback Event
about: Document and track a Stage B rollback event for audit and learning purposes
title: "Rollback Event - [TYPE] - [DATE]"
labels: rollback, incident, stage-b
assignees: jwade83
---

# Stage B Rollback Event Report

## Rollback Summary
**Date:** [YYYY-MM-DD]  
**Time:** [HH:MM]  
**Rollback Type:** [ ] Workflow-Level [ ] Selective Bypass [ ] Gradual Rollback [ ] Stage Reversion  
**Decision Authority:** [ ] Automated [ ] Manual [ ] Emergency  
**Duration:** [ESTIMATED_DURATION]

## Trigger Analysis
**Primary Trigger:** [SELECT_ONE]
- [ ] Velocity drop >50%
- [ ] PR failure rate >30%
- [ ] Review completion <60%
- [ ] System health degradation
- [ ] User frustration
- [ ] Quality degradation
- [ ] System untrust
- [ ] System break
- [ ] Critical blocking
- [ ] Other: [DESCRIBE]

**Quantitative Evidence:**
```
[PASTE_METRICS_OR_SCREENSHOTS]
```

**Qualitative Evidence:**
```
[DESCRIBE_USER_FEEDBACK_OR_OBSERVATIONS]
```

## Actions Taken
**Rollback Level:** [LEVEL_1-4]  
**Specific Actions:**
- [ ] Workflow disabled: [WORKFLOW_NAME]
- [ ] Bypass label applied: [PR_NUMBER]
- [ ] Config updated: [CONFIG_CHANGES]
- [ ] Stage A restored: [RESTORATION_STEPS]

**Commands Executed:**
```bash
[PASTE_ACTUAL_COMMANDS_RUN]
```

**Verification Steps:**
- [ ] [VERIFICATION_STEP_1]
- [ ] [VERIFICATION_STEP_2]
- [ ] [VERIFICATION_STEP_3]

## Impact Assessment
**Pre-Rollback State:**
- Active PRs: [COUNT]
- Workflow Status: [STATUS]
- User Activity: [LEVEL]
- System Performance: [METRICS]

**Post-Rollback State:**
- Active PRs: [COUNT]
- Workflow Status: [STATUS]
- User Activity: [LEVEL]
- System Performance: [METRICS]

**Measured Impact:**
- Development Velocity: [BEFORE] → [AFTER]
- PR Success Rate: [BEFORE] → [AFTER]
- User Satisfaction: [BEFORE] → [AFTER]
- System Stability: [BEFORE] → [AFTER]

## Root Cause Analysis
**What Went Wrong:**
```
[DETAILED_DESCRIPTION_OF_FAILURE]
```

**Why Did It Go Wrong:**
```
[ANALYSIS_OF_UNDERLYING_CAUSES]
```

**How Was It Detected:**
```
[DETECTION_METHOD_AND_TIMING]
```

**What Could Have Prevented It:**
```
[PREVENTION_STRATEGIES]
```

## Lessons Learned
**Key Insights:**
- [INSIGHT_1]
- [INSIGHT_2]
- [INSIGHT_3]

**Process Improvements:**
- [IMPROVEMENT_1]
- [IMPROVEMENT_2]
- [IMPROVEMENT_3]

**Future Preventions:**
- [PREVENTION_1]
- [PREVENTION_2]
- [PREVENTION_3]

## Recovery Planning
**Immediate Actions:**
- [ ] [IMMEDIATE_ACTION_1]
- [ ] [IMMEDIATE_ACTION_2]
- [ ] [IMMEDIATE_ACTION_3]

**Recovery Timeline:**
- **Week 1:** [RECOVERY_STEP_1]
- **Week 2:** [RECOVERY_STEP_2]
- **Week 3:** [RECOVERY_STEP_3]

**Stage B Retry Planning:**
- **When to Retry:** [TIMELINE]
- **What to Change:** [MODIFICATIONS]
- **How to Monitor:** [ENHANCED_MONITORING]

## Documentation Updates
**Files Modified:**
- [ ] `docs/runbooks/STAGE_B_ROLLBACK.md`
- [ ] `prompts/strategic_lenses/config.yml`
- [ ] `.github/workflows/[WORKFLOW_NAME].yml`
- [ ] `08_CHRONICLE/incidents/[INCIDENT_FILE].md`

**Chronicle Entry:**
- [ ] Incident log created: `08_CHRONICLE/incidents/[DATE]_rollback-[TYPE].md`
- [ ] RCA documented
- [ ] Recovery plan recorded
- [ ] Lessons learned integrated

## Follow-up Actions
**Immediate (24 hours):**
- [ ] [FOLLOW_UP_1]
- [ ] [FOLLOW_UP_2]

**Short-term (1 week):**
- [ ] [FOLLOW_UP_3]
- [ ] [FOLLOW_UP_4]

**Long-term (1 month):**
- [ ] [FOLLOW_UP_5]
- [ ] [FOLLOW_UP_6]

## Stakeholder Communication
**Notifications Sent:**
- [ ] [STAKEHOLDER_1]: [NOTIFICATION_METHOD]
- [ ] [STAKEHOLDER_2]: [NOTIFICATION_METHOD]

**Communication Log:**
```
[LOG_OF_ALL_COMMUNICATIONS]
```

## Antifragility Integration
**How This Rollback Strengthens the System:**
```
[DESCRIPTION_OF_SYSTEM_IMPROVEMENTS]
```

**New Safeguards Implemented:**
- [ ] [NEW_SAFEGUARD_1]
- [ ] [NEW_SAFEGUARD_2]

**Enhanced Monitoring:**
- [ ] [ENHANCED_MONITOR_1]
- [ ] [ENHANCED_MONITOR_2]

---

## Rollback Event Checklist
- [ ] Rollback executed successfully
- [ ] Verification completed
- [ ] Impact assessed
- [ ] RCA conducted
- [ ] Lessons learned documented
- [ ] Recovery plan created
- [ ] Stakeholders notified
- [ ] Chronicle entry created
- [ ] Follow-up actions scheduled
- [ ] Antifragility improvements identified

---

**Rollback Event ID:** [GENERATE_UNIQUE_ID]  
**Reported By:** [NAME]  
**Reviewed By:** [NAME]  
**Status:** [ ] Open [ ] In Progress [ ] Resolved [ ] Closed
