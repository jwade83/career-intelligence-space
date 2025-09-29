#!/bin/bash
# Stage Reversion Script for Complete Stage B Rollback
# Usage: ./scripts/rollback/stage-reversion.sh [reason]

set -e

REASON="$1"
TIMESTAMP=$(date +%Y-%m-%d_%H-%M-%S)

if [ -z "$REASON" ]; then
    echo "Usage: $0 <reason>"
    echo "Example: $0 'Complete system failure - reverting to Stage A'"
    exit 1
fi

echo "🚨 STAGE REVERSION INITIATED"
echo "📝 Reason: $REASON"
echo "⚠️ This will disable ALL Stage B components and revert to Stage A"

# Confirm with user
read -p "Are you sure you want to proceed with Stage B reversion? (yes/no): " confirm
if [ "$confirm" != "yes" ]; then
    echo "❌ Stage reversion cancelled"
    exit 1
fi

# Create rollback log entry
LOG_DIR="08_CHRONICLE/incidents"
LOG_FILE="$LOG_DIR/${TIMESTAMP}_rollback-stage-reversion.md"

mkdir -p "$LOG_DIR"

cat > "$LOG_FILE" << EOF
---
project: Career Intelligence Space
type: rollback_incident
status: active
tags: [rollback, stage_reversion, stage_b, emergency, incident]
updated: $(date +%Y-%m-%d)
rollback_type: stage_reversion
reason: $REASON
timestamp: $TIMESTAMP
---

# Rollback Incident - Stage B Reversion

**Date:** $(date +%Y-%m-%d)
**Time:** $(date +%H:%M:%S)
**Rollback Type:** Stage Reversion (Complete)
**Reason:** $REASON
**Severity:** EMERGENCY

## Actions Taken
- [ ] All Stage B workflows disabled
- [ ] Stage A configuration restored
- [ ] Rollback incident logged
- [ ] Stakeholders notified

## Workflows Disabled
EOF

echo "🔄 Disabling Stage B workflows..."

# List of Stage B workflows to disable
STAGE_B_WORKFLOWS=(
    "frontmatter-validation"
    "workflow-validation"
    "promotion-gates"
    "weekly-lens-reminder"
    "pr-failure-systems-engineer"
)

DISABLED_COUNT=0
for workflow in "${STAGE_B_WORKFLOWS[@]}"; do
    WORKFLOW_FILE=".github/workflows/${workflow}.yml"
    DISABLED_FILE=".github/workflows/${workflow}.yml.disabled"
    
    if [ -f "$WORKFLOW_FILE" ]; then
        echo "  - Disabling: $workflow"
        mv "$WORKFLOW_FILE" "$DISABLED_FILE"
        echo "- [x] \`$WORKFLOW_FILE\` → \`$DISABLED_FILE\`" >> "$LOG_FILE"
        ((DISABLED_COUNT++))
    else
        echo "  - Not found: $workflow (may already be disabled)"
        echo "- [ ] \`$WORKFLOW_FILE\` (not found)" >> "$LOG_FILE"
    fi
done

echo "✅ Disabled $DISABLED_COUNT Stage B workflows"

# Restore Stage A configuration
echo "🔄 Restoring Stage A configuration..."

# Update config.yml to Stage A settings
cat > "prompts/strategic_lenses/config.yml" << 'EOF'
---
# Strategic Lenses Configuration
# Career Intelligence Space (CIS) Consultant Lens System
project: Career Intelligence Space
type: configuration
status: active
updated: 2025-09-29
tags: [cis, config, strategic_lenses, consultant_system]
---

# Lens System Status
system_status: active  # active | inactive | maintenance
activation_date: 2025-09-29
version: 1.0.0

# Individual Lens Controls
lenses:
  strategic_analyst:
    status: active
    priority: high
    use_cases: [weekly_reviews, milestone_assessments, strategic_planning]
  
  project_manager:
    status: active
    priority: high
    use_cases: [task_breakdown, timeline_planning, resource_allocation]
  
  systems_engineer:
    status: active
    priority: medium
    use_cases: [technical_bottlenecks, workflow_optimization, automation_gaps]
  
  productivity_coach:
    status: active
    priority: medium
    use_cases: [momentum_assessment, energy_management, workflow_optimization]
  
  venture_designer:
    status: active
    priority: low
    use_cases: [opportunity_mapping, market_positioning, competitive_analysis]

# Usage Guidelines
usage_rules:
  - "Only use lenses when system_status is 'active'"
  - "Check individual lens status before application"
  - "Document lens usage in chronicle entries"
  - "Report issues or improvements via GitHub issues"

# Rollback Information
rollback:
  last_stable_version: "stage-a-final"
  rollback_instructions: "See docs/runbooks/STAGE_B_ROLLBACK.md for detailed procedures"
  emergency_contact: "jwade83"
  rollback_log: "08_CHRONICLE/incidents/"
EOF

echo "- [x] Stage A configuration restored" >> "$LOG_FILE"

# Complete the log file
cat >> "$LOG_FILE" << EOF

## Configuration Changes
- [x] \`prompts/strategic_lenses/config.yml\` restored to Stage A settings
- [x] All Stage B enforcement disabled
- [x] System status set to Stage A baseline

## Verification Steps
- [ ] Confirm all Stage B workflows disabled
- [ ] Verify Stage A functionality restored
- [ ] Check system stability
- [ ] Monitor for 24-48 hours
- [ ] Confirm no Stage B components active

## Recovery Planning
**Immediate Actions (24 hours):**
- [ ] Monitor system health
- [ ] Collect user feedback
- [ ] Assess rollback success

**Short-term (1 week):**
- [ ] Conduct comprehensive RCA
- [ ] Identify root causes
- [ ] Plan Stage B redesign

**Long-term (1 month):**
- [ ] Redesign Stage B components
- [ ] Implement enhanced monitoring
- [ ] Plan Stage B retry

## Stakeholder Communication
**Notifications Required:**
- [ ] Development team
- [ ] System users
- [ ] Management (if applicable)

**Communication Template:**
\`\`\`
STAGE B ROLLBACK NOTIFICATION

Date: $(date +%Y-%m-%d)
Time: $(date +%H:%M:%S)
Severity: EMERGENCY

The Career Intelligence Space (CIS) has been reverted from Stage B to Stage A due to:

$REASON

Actions Taken:
- All Stage B workflows disabled
- Stage A configuration restored
- System functionality verified

Impact:
- Development velocity should return to Stage A baseline
- All Stage B safeguards temporarily disabled
- Manual processes restored

Recovery Timeline:
- Immediate: System stability monitoring
- 1 week: Root cause analysis
- 1 month: Stage B redesign and retry

Contact: jwade83 for questions or concerns
\`\`\`

## Antifragility Integration
**How This Rollback Strengthens the System:**
- Identifies critical failure points in Stage B design
- Provides data for improved Stage B implementation
- Validates rollback procedures and automation
- Demonstrates system resilience and recovery capability

**New Safeguards to Implement:**
- [ ] Enhanced monitoring before Stage B retry
- [ ] Gradual rollout strategy
- [ ] Improved rollback triggers
- [ ] Better user communication

---
*Generated by Stage B rollback automation script*
EOF

echo "📄 Rollback log created: $LOG_FILE"

# Commit the changes
git add .github/workflows/*.disabled prompts/strategic_lenses/config.yml "$LOG_FILE"
git commit -m "rollback: complete Stage B reversion to Stage A

Reason: $REASON
Rollback Type: Stage Reversion (Complete)
Workflows Disabled: $DISABLED_COUNT
Incident Log: $LOG_FILE

This is an emergency Stage B rollback action.
See docs/runbooks/STAGE_B_ROLLBACK.md for procedures."

echo "✅ Stage B reversion completed successfully"
echo "📝 Changes committed to git"
echo "📄 Rollback log: $LOG_FILE"
echo "🚀 Ready to push: git push origin [branch-name]"
echo ""
echo "⚠️ IMPORTANT: Notify stakeholders immediately about this rollback"
echo "📋 Next steps: Monitor system health and conduct RCA within 24 hours"
