---
project: Career Intelligence Space
type: template
status: active
tags: [mobile_copilot, template, field_capture, prompt]
updated: '2025-10-03'
---

# Mobile Copilot Basic Field Capture Template

## 🎯 Purpose

This template provides a standardized prompt for basic field capture using mobile GitHub Copilot Chat Assistant. It ensures consistent frontmatter compliance and content structure.

## 📋 Template

```
Create a new file in 00_SANDBOX/agent_inbox/ called [filename].md with the following structure:

---
project: Career Intelligence Space
type: mobile_copilot_field_capture
status: active
tags: [mobile_copilot, field_capture, [specific_tags]]
source: mobile_github_copilot
captured_at: '2025-10-03'
---

# [Title]

## Overview
[Brief description of the capture]

## Content
[Main content here]

## Key Points
- [Point 1]
- [Point 2]
- [Point 3]

## Next Steps
- [ ] Review content
- [ ] Validate frontmatter
- [ ] Process through workflow
- [ ] Archive if complete

## Notes
[Additional notes or context]
```

## 🔧 Usage Instructions

### **Step 1: Customize Placeholders**
- Replace `[filename]` with descriptive filename
- Replace `[Title]` with appropriate title
- Replace `[specific_tags]` with relevant tags
- Update `captured_at` date

### **Step 2: Add Content**
- Fill in the Overview section
- Add main content in Content section
- List key points in Key Points section
- Add any additional notes

### **Step 3: Submit**
- Copy the complete prompt
- Paste into mobile GitHub Copilot Chat
- Review generated content
- Submit for processing

## 📱 Mobile Default Values Guide

### **Standard Mobile Provenance Fields**
```yaml
# Mobile Default Values (use these for consistency)
initiated_by: mobile_user
mobile_device: [device_type]  # e.g., "iPhone", "Android", "iPad"
prompt_template: basic_field_capture
capture_method: mobile_copilot_chat
connectivity: [connection_type]  # e.g., "wifi", "cellular", "offline_sync"
```

### **Device-Specific Defaults**
```yaml
# iPhone/iPad defaults
mobile_device: "iOS"
browser: "Safari"
capture_quality: "mobile_optimized"

# Android defaults  
mobile_device: "Android"
browser: "Chrome"
capture_quality: "mobile_optimized"

# Common mobile tags
tags: [mobile_copilot, field_capture, mobile_optimized, [specific_tags]]
```

### **Mobile-Specific Metadata**
```yaml
# Optional mobile enhancement fields
location_context: [if_relevant]  # e.g., "office", "field", "remote"
time_sensitivity: [urgency]  # e.g., "immediate", "standard", "batch"
capture_confidence: [quality]  # e.g., "high", "medium", "preliminary"
```

## 📊 Quality Checklist

### **Frontmatter Validation**
- [ ] `project: Career Intelligence Space`
- [ ] `type: mobile_copilot_field_capture`
- [ ] `status: active`
- [ ] `tags: [array_with_mobile_copilot]`
- [ ] `source: mobile_github_copilot`
- [ ] `captured_at: 'YYYY-MM-DD'`

### **Content Validation**
- [ ] Clear and descriptive title
- [ ] Well-structured content
- [ ] Relevant key points
- [ ] Actionable next steps
- [ ] Proper markdown formatting

## 🎯 Best Practices

### **Filename Conventions**
- Use descriptive, lowercase filenames
- Include date prefix: `YYYY-MM-DD_`
- Use underscores for spaces
- Keep under 50 characters

### **Tag Guidelines**
- Always include `mobile_copilot`
- Always include `field_capture`
- Add 2-3 specific tags
- Use lowercase with underscores

### **Content Guidelines**
- Be concise but comprehensive
- Use bullet points for lists
- Include actionable next steps
- Maintain professional tone

---

**This template ensures consistent, high-quality field capture using mobile GitHub Copilot Chat Assistant.**
