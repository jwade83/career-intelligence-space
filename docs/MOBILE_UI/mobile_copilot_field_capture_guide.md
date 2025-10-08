---
project: Career Intelligence Space
type: spec
status: active
tags: [mobile_copilot, field_capture, user_guide, mobile_ui, github_native]
updated: '2025-10-03'
---

# Mobile Copilot Field Capture Guide

## 🎯 Overview

This guide explains how to use GitHub Copilot Chat Assistant on mobile devices to capture field intelligence directly into the Career Intelligence Space repository. This capability enables sophisticated content generation and file creation from your mobile device.

## 📱 Prerequisites

### **Required Setup**
- **Mobile device** with internet connection
- **GitHub account** with repository access
- **Mobile browser** (Safari, Chrome, etc.)
- **GitHub Copilot** access (Pro/Pro+/Enterprise)

### **Access Method**
- **✅ Use**: Mobile browser → github.com → Copilot Chat Assistant
- **❌ Avoid**: GitHub Mobile App (limited file creation capabilities)

## ✅ Mobile Compliance Checklist

### **Before Submitting Any Mobile Capture:**

#### **Frontmatter Validation**
- [ ] `project: Career Intelligence Space`
- [ ] `type: mobile_copilot_field_capture` (or appropriate type)
- [ ] `status: active`
- [ ] `tags: [mobile_copilot, field_capture, [specific_tags]]`
- [ ] `source: mobile_github_copilot`
- [ ] `captured_at: 'YYYY-MM-DD'` (current date)

#### **Content Validation**
- [ ] Clear and descriptive title
- [ ] Well-structured content with proper markdown
- [ ] Relevant tags (2-3 specific tags beyond mobile_copilot)
- [ ] Actionable next steps included
- [ ] File placed in correct directory (00_SANDBOX/agent_inbox/)

#### **Mobile-Specific Requirements**
- [ ] Filename follows convention: `YYYY-MM-DD_descriptive_name.md`
- [ ] Content is mobile-optimized (concise, bullet points)
- [ ] No sensitive information (PII, confidential data)
- [ ] Proper markdown formatting for mobile readability

## 🚀 Quick Start

### **Step 1: Access Repository**
1. Open mobile browser
2. Navigate to `github.com/jwade83/career-intelligence-space`
3. Tap "Copilot" button (if available) or open Copilot Chat

### **Step 2: Use Prompt Templates**
Copy and paste one of the provided prompt templates (see Templates section below)

### **Step 3: Review and Submit**
1. Review generated content
2. Copilot will create a new branch
3. Files will be committed automatically
4. Review the PR when ready

## 📋 Prompt Templates

### **Basic Field Capture**
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

[Content here]

## Next Steps
- [ ] Review content
- [ ] Validate frontmatter
- [ ] Process through workflow
```

### **Technical Analysis**
```
Create a technical analysis file in 00_SANDBOX/systems/ called [filename].md with comprehensive analysis of [topic], including:

1. System components and relationships
2. Data flow patterns
3. Integration points
4. Scalability considerations
5. Security implications

Use proper CIS frontmatter with type: systems and include detailed technical content.
```

### **Meta Insight Tracking**
```
Create a meta insight file in 00_SANDBOX/meta_insights/ called [filename].md documenting insights about [topic], including:

1. Pattern recognition
2. System behavior analysis
3. Process optimization opportunities
4. Future development implications

Use proper CIS frontmatter with type: meta_insight_tracking and include detailed analysis.
```

## 🎯 Best Practices

### **Prompt Quality**
- **Be specific**: Include exact file paths and directory structure
- **Use templates**: Copy from provided templates for consistency
- **Include context**: Reference repository structure and existing content
- **Specify frontmatter**: Explicitly request CIS-compliant metadata

### **Content Quality**
- **Review before submit**: Check generated content for accuracy
- **Validate frontmatter**: Ensure all required fields are present
- **Check formatting**: Verify markdown formatting is correct
- **Test links**: Ensure any links work properly

### **Mobile Optimization**
- **Use mobile browser**: Avoid GitHub Mobile App for file creation
- **Keep prompts concise**: Mobile typing is more challenging
- **Use templates**: Pre-written prompts reduce typing
- **Test connectivity**: Ensure stable internet connection

## 🔧 Troubleshooting

### **Common Issues**

#### **"File not created"**
- **Cause**: Using GitHub Mobile App instead of mobile browser
- **Solution**: Switch to mobile browser and github.com

#### **"Frontmatter errors"**
- **Cause**: Incomplete or incorrect frontmatter in prompt
- **Solution**: Use provided templates with complete frontmatter

#### **"Permission denied"**
- **Cause**: Insufficient repository permissions
- **Solution**: Verify repository access and permissions

#### **"Content quality issues"**
- **Cause**: Vague or incomplete prompts
- **Solution**: Use detailed, specific prompts with clear instructions

### **Quality Validation**

#### **Frontmatter Checklist**
- [ ] `project: Career Intelligence Space`
- [ ] `type: [appropriate_type]`
- [ ] `status: [draft|active|matured]`
- [ ] `tags: [array_of_tags]`
- [ ] `updated: 'YYYY-MM-DD'`

#### **Content Checklist**
- [ ] Clear title and structure
- [ ] Relevant and accurate content
- [ ] Proper markdown formatting
- [ ] Appropriate directory placement
- [ ] Cross-references work correctly

## 📊 Success Metrics

### **Quality Indicators**
- **Frontmatter compliance**: 100% of required fields present
- **Content accuracy**: Relevant and well-structured content
- **Directory placement**: Files in correct locations
- **Cross-references**: Links and references work properly

### **Usage Patterns**
- **Frequency**: Regular mobile copilot usage
- **Content types**: Variety of content types generated
- **Integration**: Seamless integration with existing workflows
- **User satisfaction**: Positive feedback on mobile experience

## 🔄 Integration with Existing Systems

### **Field Agent v0.6**
- **Complementary**: Mobile copilot for complex content, Field Agent for simple capture
- **Shared standards**: Common frontmatter and processing protocols
- **Unified analytics**: Combined usage tracking and analysis

### **Barometer Review System**
- **Content review**: Mobile copilot content included in barometer reviews
- **Quality assessment**: Regular evaluation of mobile copilot content
- **Process improvement**: Use insights for system evolution

## 📚 Additional Resources

### **Related Documentation**
- [Mobile UI Gap Analysis](../MOBILE_UI/mobile_ui_gap_analysis.md)
- [Field Agent v0.6 Specification](../AGENTS/field_agent_v06_complete.md)
- [CIS Ontology](../ONTOLOGY.yml)
- [Frontmatter Requirements](../Golden_Rules.md)

### **Template Library**
- [Basic Field Capture Templates](.)
- [Technical Analysis Templates](.)
- [Meta Insight Templates](.)

---

**This guide provides everything needed to successfully use mobile GitHub Copilot Chat Assistant for field capture in the Career Intelligence Space repository.**
