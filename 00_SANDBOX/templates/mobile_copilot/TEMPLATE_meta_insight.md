---
project: Career Intelligence Space
type: template
status: active
tags: [mobile_copilot, template, meta_insight, prompt]
updated: '2025-10-03'
---

# Mobile Copilot Meta Insight Template

## 🎯 Purpose

This template provides a standardized prompt for meta insight tracking using mobile GitHub Copilot Chat Assistant. It ensures consistent frontmatter compliance and structured insight capture.

## 📋 Template

```
Create a new file in 00_SANDBOX/meta_insights/ called [filename].md with the following structure:

---
project: Career Intelligence Space
type: mobile_copilot_meta_insight
status: active
tags: [mobile_copilot, meta_insight, [specific_tags]]
source: mobile_github_copilot
captured_at: '2025-10-03'
initiated_by: mobile_user
mobile_device: [device_type]
insight_type: [insight_category]
confidence_level: [confidence]
---

# [Meta Insight Title]

## Insight Overview
[Brief description of the meta insight and its significance]

## Context & Background
[Background information and context for the insight]

## Key Observations
### Observation 1: [Title]
- **Pattern**: [Identified pattern or trend]
- **Evidence**: [Supporting evidence or data]
- **Implications**: [What this means for the project]

### Observation 2: [Title]
- **Pattern**: [Identified pattern or trend]
- **Evidence**: [Supporting evidence or data]
- **Implications**: [What this means for the project]

## Meta Analysis
### Pattern Recognition
- **Primary Pattern**: [Main pattern identified]
- **Secondary Patterns**: [Additional patterns]
- **Pattern Strength**: [Strong/Medium/Weak]

### Insight Quality
- **Confidence Level**: [High/Medium/Low]
- **Evidence Quality**: [Strong/Moderate/Weak]
- **Replicability**: [High/Medium/Low]

## Strategic Implications
### Immediate Impact
- **Short-term Effects**: [Immediate implications]
- **Action Items**: [Specific actions needed now]

### Long-term Implications
- **Strategic Direction**: [Long-term strategic implications]
- **Future Considerations**: [Things to monitor over time]

## Recommendations
- [ ] [Priority 1 recommendation based on insight]
- [ ] [Priority 2 recommendation based on insight]
- [ ] [Priority 3 recommendation based on insight]

## Follow-up Actions
- [ ] Validate insight with additional data
- [ ] Share insight with relevant stakeholders
- [ ] Monitor for pattern continuation
- [ ] Update strategic planning based on insight

## Meta Notes
[Additional meta-level observations or considerations]
```

## 🔧 Usage Instructions

### **Step 1: Customize Placeholders**
- Replace `[filename]` with descriptive insight filename
- Replace `[Meta Insight Title]` with specific insight title
- Replace `[specific_tags]` with relevant insight tags
- Update `captured_at` date
- Set `[device_type]` (iPhone, Android, iPad)
- Set `[insight_category]` (strategic, operational, tactical)
- Set `[confidence]` (high, medium, low)

### **Step 2: Add Insight Content**
- Fill in Insight Overview with key findings
- Add Context & Background information
- List Key Observations with patterns and evidence
- Provide Meta Analysis of patterns and quality
- Include Strategic Implications
- Add specific Recommendations
- Plan Follow-up Actions

### **Step 3: Submit**
- Copy the complete prompt
- Paste into mobile GitHub Copilot Chat
- Review generated insight content
- Submit for processing

## 📱 Mobile Default Values Guide

### **Meta Insight Defaults**
```yaml
# Mobile Meta Insight Defaults
initiated_by: mobile_user
mobile_device: [device_type]  # e.g., "iPhone", "Android", "iPad"
insight_type: strategic  # strategic, operational, tactical
confidence_level: medium  # high, medium, low
capture_method: mobile_copilot_chat
insight_scope: [scope]  # e.g., "project", "system", "process"
```

### **Insight-Specific Tags**
```yaml
# Common meta insight tags
tags: [mobile_copilot, meta_insight, [domain], [type], [confidence]]
# Examples:
# [mobile_copilot, meta_insight, strategic, high_confidence, immediate]
# [mobile_copilot, meta_insight, operational, medium_confidence, standard]
```

## 📊 Quality Checklist

### **Frontmatter Validation**
- [ ] `project: Career Intelligence Space`
- [ ] `type: mobile_copilot_meta_insight`
- [ ] `status: active`
- [ ] `tags: [mobile_copilot, meta_insight, [specific_tags]]`
- [ ] `source: mobile_github_copilot`
- [ ] `captured_at: 'YYYY-MM-DD'`
- [ ] `initiated_by: mobile_user`
- [ ] `mobile_device: [device_type]`
- [ ] `insight_type: [insight_category]`
- [ ] `confidence_level: [confidence]`

### **Content Validation**
- [ ] Clear insight title
- [ ] Comprehensive overview
- [ ] Well-structured observations
- [ ] Strong meta analysis
- [ ] Strategic implications included
- [ ] Actionable recommendations
- [ ] Follow-up actions planned

## 🎯 Best Practices

### **Meta Insight Guidelines**
- **Pattern Focus**: Look for patterns and trends
- **Evidence-Based**: Support insights with evidence
- **Strategic Thinking**: Consider broader implications
- **Actionable**: Provide specific recommendations
- **Follow-up**: Plan for insight validation and application

### **Mobile Optimization**
- **Concise Insights**: Keep insights focused and clear
- **Structured Format**: Use consistent observation format
- **Visual Hierarchy**: Use headers and bullet points effectively
- **Mobile Readability**: Ensure content is readable on mobile screens

---

**This template ensures consistent, high-quality meta insight capture using mobile GitHub Copilot Chat Assistant.**
