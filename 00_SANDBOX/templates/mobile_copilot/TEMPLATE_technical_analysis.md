---
project: Career Intelligence Space
type: template
status: active
tags: [mobile_copilot, template, technical_analysis, prompt]
updated: '2025-10-03'
---

# Mobile Copilot Technical Analysis Template

## 🎯 Purpose

This template provides a standardized prompt for technical analysis using mobile GitHub Copilot Chat Assistant. It ensures consistent frontmatter compliance and comprehensive technical content structure.

## 📋 Template

```
Create a new file in 00_SANDBOX/systems/ called [filename].md with the following structure:

---
project: Career Intelligence Space
type: mobile_copilot_technical_analysis
status: active
tags: [mobile_copilot, technical_analysis, [specific_tags]]
source: mobile_github_copilot
captured_at: '2025-10-03'
initiated_by: mobile_user
mobile_device: [device_type]
analysis_depth: [depth_level]
---

# [Technical Analysis Title]

## Executive Summary
[Brief overview of the technical analysis and key findings]

## Technical Context
[Background information and technical environment]

## Analysis Methodology
[Approach and methods used for the analysis]

## Key Findings
### Finding 1: [Title]
- **Impact**: [High/Medium/Low]
- **Technical Details**: [Specific technical information]
- **Recommendations**: [Actionable technical recommendations]

### Finding 2: [Title]
- **Impact**: [High/Medium/Low]
- **Technical Details**: [Specific technical information]
- **Recommendations**: [Actionable technical recommendations]

## Technical Recommendations
- [ ] [Priority 1 recommendation]
- [ ] [Priority 2 recommendation]
- [ ] [Priority 3 recommendation]

## Implementation Considerations
- **Technical Complexity**: [Low/Medium/High]
- **Resource Requirements**: [Specific requirements]
- **Timeline**: [Estimated implementation time]
- **Dependencies**: [Technical dependencies]

## Risk Assessment
- **Technical Risks**: [Identified technical risks]
- **Mitigation Strategies**: [Risk mitigation approaches]
- **Monitoring Requirements**: [Technical monitoring needs]

## Next Steps
- [ ] Review technical analysis
- [ ] Validate technical recommendations
- [ ] Plan implementation approach
- [ ] Execute technical improvements

## Technical Notes
[Additional technical context or considerations]
```

## 🔧 Usage Instructions

### **Step 1: Customize Placeholders**
- Replace `[filename]` with descriptive technical filename
- Replace `[Technical Analysis Title]` with specific analysis title
- Replace `[specific_tags]` with relevant technical tags
- Update `captured_at` date
- Set `[device_type]` (iPhone, Android, iPad)
- Set `[depth_level]` (preliminary, standard, comprehensive)

### **Step 2: Add Technical Content**
- Fill in Executive Summary with key findings
- Add Technical Context and background
- Describe Analysis Methodology used
- List Key Findings with impact levels
- Provide Technical Recommendations
- Include Implementation Considerations
- Assess Technical Risks and mitigation

### **Step 3: Submit**
- Copy the complete prompt
- Paste into mobile GitHub Copilot Chat
- Review generated technical content
- Submit for processing

## 📱 Mobile Default Values Guide

### **Technical Analysis Defaults**
```yaml
# Mobile Technical Analysis Defaults
initiated_by: mobile_user
mobile_device: [device_type]  # e.g., "iPhone", "Android", "iPad"
analysis_depth: standard  # preliminary, standard, comprehensive
capture_method: mobile_copilot_chat
technical_focus: [domain]  # e.g., "systems", "architecture", "performance"
```

### **Technical-Specific Tags**
```yaml
# Common technical analysis tags
tags: [mobile_copilot, technical_analysis, [domain], [complexity], [urgency]]
# Examples:
# [mobile_copilot, technical_analysis, systems, high_complexity, immediate]
# [mobile_copilot, technical_analysis, architecture, medium_complexity, standard]
```

## 📊 Quality Checklist

### **Frontmatter Validation**
- [ ] `project: Career Intelligence Space`
- [ ] `type: mobile_copilot_technical_analysis`
- [ ] `status: active`
- [ ] `tags: [mobile_copilot, technical_analysis, [specific_tags]]`
- [ ] `source: mobile_github_copilot`
- [ ] `captured_at: 'YYYY-MM-DD'`
- [ ] `initiated_by: mobile_user`
- [ ] `mobile_device: [device_type]`
- [ ] `analysis_depth: [depth_level]`

### **Content Validation**
- [ ] Clear technical title
- [ ] Comprehensive executive summary
- [ ] Well-structured technical findings
- [ ] Actionable technical recommendations
- [ ] Proper technical risk assessment
- [ ] Implementation considerations included

## 🎯 Best Practices

### **Technical Content Guidelines**
- **Be Specific**: Include concrete technical details
- **Impact Assessment**: Always include impact levels
- **Actionable Recommendations**: Provide specific technical actions
- **Risk Awareness**: Identify and address technical risks
- **Implementation Focus**: Consider practical implementation

### **Mobile Optimization**
- **Concise Technical Language**: Use clear, precise technical terms
- **Structured Findings**: Use consistent format for findings
- **Visual Hierarchy**: Use headers and bullet points effectively
- **Mobile Readability**: Ensure content is readable on mobile screens

---

**This template ensures consistent, high-quality technical analysis using mobile GitHub Copilot Chat Assistant.**