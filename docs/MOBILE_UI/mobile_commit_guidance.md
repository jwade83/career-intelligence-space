---
project: Career Intelligence Space
type: guide
status: active
tags: [mobile_ui, commit_guidance, mobile_copilot, structured_commits]
updated: '2025-10-03'
---

# Mobile Commit Guidance

## 🎯 Overview

This guide provides comprehensive commit message guidance for mobile users of the Career Intelligence Space repository. It ensures consistent, structured commit messages across all environments while maintaining mobile-specific provenance tracking.

## 📱 Mobile Commit Message Format

### **Required Structure**
```
type(scope): description

[Optional body with more details]

Source-Provenance: [source_details]
Mobile-Context: [mobile_specific_info]
```

### **Mobile-Specific Requirements**
- **Source-Provenance**: Always required for mobile captures
- **Mobile-Context**: Required for mobile field captures
- **Device Tracking**: Include device type and capture method
- **Template Reference**: Link to template used if applicable

## 🔧 Environment-Specific Guidance

### **1. Local IDE (VS Code) - Automated**
**Best Practice**: Use VS Code with Copilot commit message generation

**Setup**:
- Install VS Code with GitHub Copilot
- Repository includes `.vscode/settings.json` with commit instructions
- Copilot will automatically generate structured commit messages

**Usage**:
1. Stage your changes: `git add .`
2. Use Copilot's "Generate Commit Message" button
3. Review and adjust if needed
4. Commit: `git commit -m "[generated message]"`

**Example Generated Message**:
```
feat(mobile-copilot): add compliance checklist to mobile guide

- Add comprehensive mobile compliance checklist
- Include frontmatter validation steps
- Add mobile-specific requirements
- Create quality assurance guidelines

Source-Provenance: VS Code Copilot
Mobile-Context: device=iPhone, method=mobile_copilot_chat, template=basic_field_capture
```

### **2. GitHub Web Editor - Manual**
**Limitation**: No native Copilot commit generation in web editor

**Workaround**: Use mobile commit templates from README

**Usage**:
1. Copy appropriate template from README
2. Customize placeholders
3. Paste into commit message field
4. Submit commit

**Available Templates**:
- **Basic Mobile Capture**: `feat(mobile-copilot): add [description]`
- **Technical Analysis**: `feat(mobile-copilot): add technical analysis of [topic]`
- **Meta Insight**: `feat(mobile-copilot): add meta insight on [topic]`

### **3. Mobile GitHub Copilot Chat - Conversational**
**Best Practice**: Use Copilot Chat for content generation, then manual commit

**Usage**:
1. Use Copilot Chat to generate content
2. Let Copilot create files automatically
3. Use mobile commit templates for commit messages
4. Include mobile context in commit

**Example Workflow**:
1. **Copilot Chat**: "Create a new mobile field capture file..."
2. **File Created**: Copilot creates file with proper frontmatter
3. **Commit Message**: Use mobile template with mobile context
4. **Submit**: Commit with structured message

## 📋 Mobile Commit Templates

### **Basic Field Capture**
```
feat(mobile-copilot): add [description]

Source-Provenance: Mobile GitHub Copilot
Mobile-Context: device=[device_type], method=mobile_copilot_chat, template=basic_field_capture
```

### **Technical Analysis**
```
feat(mobile-copilot): add technical analysis of [topic]

Source-Provenance: Mobile GitHub Copilot
Mobile-Context: device=[device_type], method=mobile_copilot_chat, template=technical_analysis
```

### **Meta Insight**
```
feat(mobile-copilot): add meta insight on [topic]

Source-Provenance: Mobile GitHub Copilot
Mobile-Context: device=[device_type], method=mobile_copilot_chat, template=meta_insight
```

### **Systems Documentation**
```
feat(mobile-copilot): add systems documentation for [system]

Source-Provenance: Mobile GitHub Copilot
Mobile-Context: device=[device_type], method=mobile_copilot_chat, template=systems_doc
```

### **Template Updates**
```
template(mobile): enhance [template_name] template

Source-Provenance: Mobile GitHub Copilot
Mobile-Context: device=[device_type], method=mobile_copilot_chat, template=[template_name]
```

### **Mobile Workflow Changes**
```
workflow(mobile-ui): improve [workflow_component]

Source-Provenance: Mobile GitHub Copilot
Mobile-Context: device=[device_type], method=mobile_copilot_chat, template=workflow_guide
```

## 🎯 Mobile-Specific Commit Guidelines

### **Device Context Requirements**
- **iPhone**: `device=iPhone`
- **Android**: `device=Android`
- **iPad**: `device=iPad`
- **Unknown**: `device=mobile_device`

### **Capture Method Tracking**
- **Mobile Copilot Chat**: `method=mobile_copilot_chat`
- **Mobile Browser**: `method=mobile_browser`
- **Mobile App**: `method=mobile_app`
- **Voice Input**: `method=voice_input`

### **Template Reference**
- **Basic Field Capture**: `template=basic_field_capture`
- **Technical Analysis**: `template=technical_analysis`
- **Meta Insight**: `template=meta_insight`
- **Systems Documentation**: `template=systems_doc`

### **Source Provenance Options**
- **Mobile GitHub Copilot**: `Source-Provenance: Mobile GitHub Copilot`
- **Mobile Browser**: `Source-Provenance: Mobile Browser`
- **Mobile App**: `Source-Provenance: Mobile App`
- **Voice Input**: `Source-Provenance: Voice Input`

## 📊 Quality Standards

### **Commit Message Quality**
- **Clarity**: Clear, descriptive messages
- **Consistency**: Follow format exactly
- **Completeness**: Include all required fields
- **Context**: Provide sufficient detail

### **Mobile Optimization**
- **Device Awareness**: Include device context
- **Method Tracking**: Specify capture method
- **Template Reference**: Link to templates used
- **Compliance**: Ensure mobile-specific requirements

### **Provenance Tracking**
- **Source Identification**: Always specify source
- **Method Documentation**: Include capture method
- **Context Preservation**: Maintain mobile context
- **Audit Trail**: Enable complete traceability

## 🔧 Troubleshooting Common Issues

### **Missing Mobile Context**
- **Issue**: Commit message lacks mobile context
- **Solution**: Add Mobile-Context field with device and method
- **Prevention**: Use mobile commit templates

### **Incorrect Source Provenance**
- **Issue**: Wrong or missing source provenance
- **Solution**: Use correct source for your environment
- **Prevention**: Follow environment-specific guidance

### **Template Mismatch**
- **Issue**: Commit message doesn't match template used
- **Solution**: Ensure template reference matches actual template
- **Prevention**: Use exact template names

### **Format Inconsistency**
- **Issue**: Commit message doesn't follow conventional format
- **Solution**: Use structured format with type(scope): description
- **Prevention**: Follow mobile commit templates exactly

## 🎯 Best Practices Summary

### **Before Committing**
1. **Choose Template**: Select appropriate mobile commit template
2. **Customize Placeholders**: Replace [description], [device_type], etc.
3. **Check Format**: Ensure conventional commit format
4. **Verify Context**: Include mobile context and provenance

### **During Commit**
1. **Use Templates**: Copy from README or this guide
2. **Customize Content**: Replace placeholders with actual values
3. **Check Compliance**: Ensure all required fields included
4. **Review Message**: Verify clarity and completeness

### **After Commit**
1. **Verify Format**: Check commit message follows format
2. **Check Context**: Ensure mobile context included
3. **Validate Provenance**: Confirm source provenance correct
4. **Learn & Improve**: Apply lessons to future commits

## 🔗 Related Resources

### **Commit Documentation**
- **Repository Instructions**: [.github/copilot-instructions.md](../../.github/copilot-instructions.md)
- **VS Code Settings**: [.vscode/settings.json](../../.vscode/settings.json)
- **Mobile Templates**: [Mobile Templates](.)

### **Mobile Workflow**
- **Mobile Guide**: [Mobile Copilot Guide](./mobile_copilot_field_capture_guide.md)
- **Complete Workflow**: [Mobile Workflow Guide](./mobile_workflow_complete.md)
- **Onboarding**: [Mobile Onboarding Guide](./mobile_user_onboarding.md)

---

**This mobile commit guidance ensures consistent, high-quality commit messages across all mobile environments while maintaining complete provenance tracking and mobile-specific context.**
