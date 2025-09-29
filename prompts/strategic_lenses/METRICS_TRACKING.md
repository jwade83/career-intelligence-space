---
project: Career Intelligence Space
type: metrics_tracking
status: active
tags: [cis, strategic_lenses, metrics, tracking, stage_framework]
updated: 2025-09-29
version: "1.0.0"
---

# Strategic Lenses Success Metrics Tracking

## Overview
This document defines the metrics tracking system for the Strategic Consultant Lenses framework, implementing ChatGPT's stage-based progression with measurable success criteria.

---

## 📊 Metrics Framework

### **Stage A Metrics (Internal Review)**

#### **Coverage Metrics**
- **Weekly Coverage:** % of weeks with Strategic Analyst + Project Manager reviews
- **Daily Coverage:** % of days with Productivity Coach momentum checks  
- **Incident Coverage:** % of incidents triggering Systems Engineer analysis
- **Quarterly Coverage:** % of quarters with Venture Designer market analysis

#### **Consistency Metrics**
- **Cross-Tool Consistency:** % of lens outputs matching structure across ChatGPT, Perplexity, Cursor
- **Protocol Adherence:** % of lens usage following established protocols
- **Quality Standards:** % of lens outputs meeting quality criteria

#### **Antifragility Metrics**
- **Incident Resolution:** # of Systems Engineer-triggered incidents leading to permanent fixes
- **Learning Capture:** % of failures resulting in improved processes
- **System Reinforcement:** # of new safeguards implemented from lens insights

---

## 📈 Tracking Implementation

### **Weekly Metrics Collection**

#### **Coverage Tracking**
```yaml
week: "2025-W40"
date_range: "2025-09-29 to 2025-10-05"
coverage:
  strategic_analyst: true
  project_manager: true
  systems_engineer: false
  productivity_coach: 3/7  # 3 out of 7 days
  venture_designer: false
coverage_percentage: 60%  # 3 out of 5 lenses used
```

#### **Quality Tracking**
```yaml
quality_metrics:
  protocol_adherence: 100%  # All lenses followed protocols
  output_structure: 100%    # All outputs matched expected format
  actionability: 85%        # 85% of insights were actionable
  integration: 100%         # All outputs integrated with chronicle
```

#### **Value Tracking**
```yaml
value_metrics:
  decisions_clarified: 3    # Number of decisions made clearer
  blockers_resolved: 1      # Number of blockers resolved
  processes_improved: 2     # Number of process improvements
  insights_generated: 8     # Number of new insights
```

### **Monthly Metrics Summary**

#### **Trend Analysis**
```yaml
month: "2025-09"
trends:
  coverage_trend: "increasing"  # up/down/stable
  quality_trend: "stable"
  value_trend: "increasing"
  consistency_trend: "stable"
```

#### **Stage Progression**
```yaml
stage_assessment:
  current_stage: "A"
  weeks_in_stage: 4
  readiness_for_stage_b: 75%  # Based on metrics
  key_improvements_needed: ["incident_coverage", "daily_consistency"]
```

---

## 🎯 Success Thresholds

### **Stage A Success Criteria**
- **Coverage:** ≥80% weekly coverage for Strategic Analyst + Project Manager
- **Consistency:** ≥90% protocol adherence across all lens usage
- **Quality:** ≥85% of outputs meeting quality standards
- **Duration:** Minimum 6 weeks of consistent usage

### **Stage B Readiness Criteria**
- **Coverage:** ≥90% weekly coverage for all applicable lenses
- **Consistency:** ≥95% protocol adherence
- **Quality:** ≥90% of outputs meeting quality standards
- **Antifragility:** ≥50% of incidents resulting in process improvements
- **Duration:** 6+ weeks of stable Stage A performance

### **Stage C Readiness Criteria**
- **Coverage:** ≥95% coverage across all lens types
- **Consistency:** ≥98% protocol adherence
- **Quality:** ≥95% of outputs meeting quality standards
- **Value:** Measurable improvement in decision quality and process efficiency
- **Duration:** 4-6 cycles of stable Stage B performance

---

## 📋 Metrics Collection Process

### **Daily Collection**
1. **Productivity Coach Usage** - Track daily momentum checks
2. **Incident Triggers** - Log any Systems Engineer lens triggers
3. **Quality Assessment** - Quick quality check of any lens outputs

### **Weekly Collection**
1. **Coverage Assessment** - Which lenses were used this week
2. **Quality Review** - Assess output quality and protocol adherence
3. **Value Assessment** - Track decisions, blockers, and improvements
4. **Trend Analysis** - Compare to previous weeks

### **Monthly Collection**
1. **Comprehensive Review** - Full metrics analysis
2. **Stage Assessment** - Evaluate readiness for next stage
3. **Improvement Planning** - Identify areas for enhancement
4. **Reporting** - Generate metrics summary for review

---

## 🔧 Implementation Tools

### **Metrics Collection Template**
```markdown
## Weekly Metrics - Week of YYYY-MM-DD

### Coverage
- [ ] Strategic Analyst
- [ ] Project Manager  
- [ ] Systems Engineer
- [ ] Productivity Coach (days: ___/7)
- [ ] Venture Designer

### Quality
- [ ] Protocol Adherence: ___%
- [ ] Output Structure: ___%
- [ ] Actionability: ___%
- [ ] Integration: ___%

### Value
- Decisions Clarified: ___
- Blockers Resolved: ___
- Processes Improved: ___
- Insights Generated: ___

### Notes
[Any observations or improvements needed]
```

### **Automated Tracking**
- **GitHub Issues** - Create issues for metrics collection
- **Workflow Triggers** - Automated reminders for metrics collection
- **Dashboard Updates** - Regular updates to metrics dashboard

---

## 📊 Reporting Framework

### **Weekly Reports**
- **Coverage Summary** - Which lenses were used
- **Quality Assessment** - How well protocols were followed
- **Value Highlights** - Key insights and improvements
- **Trend Indicators** - Progress toward stage goals

### **Monthly Reports**
- **Comprehensive Analysis** - Full metrics review
- **Stage Assessment** - Readiness for next stage
- **Improvement Recommendations** - Areas for enhancement
- **Success Celebration** - Achievements and milestones

### **Quarterly Reports**
- **Strategic Review** - Long-term trends and patterns
- **Framework Evolution** - How the system has improved
- **Future Planning** - Next stage preparation
- **Value Demonstration** - ROI and impact assessment

---

## 🚀 Next Steps

### **Immediate (This Week)**
1. **Begin Metrics Collection** - Start tracking with current lens usage
2. **Establish Baseline** - Record current state for comparison
3. **Create Collection Process** - Implement daily/weekly collection routines

### **Short-term (Next 4 Weeks)**
1. **Refine Metrics** - Adjust based on initial collection experience
2. **Improve Collection** - Streamline data gathering process
3. **Analyze Trends** - Identify patterns and improvement areas

### **Medium-term (Next 8 Weeks)**
1. **Automate Collection** - Implement automated metrics gathering
2. **Create Dashboard** - Visual representation of metrics
3. **Prepare Stage B** - Use metrics to prepare for next stage

---

*Metrics Tracking System v1.0.0*
*Updated: 2025-09-29*
