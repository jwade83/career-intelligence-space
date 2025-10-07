# CIS Mobile Field Capture Workflow - Design Iteration v2

## 🎯 Workflow Overview

**Objective**: Streamlined mobile field capture system for TikTok content → CIS field cases using AI-assisted processing.

**Total Time Target**: 2-3 minutes end-to-end
**Platforms**: TikTok → Transcription Tool → ChatGPT Mobile → GitHub Copilot Mobile

## 📋 Complete 5-Step Workflow

### **Step 1: Content Discovery** ✅ TESTED
- **Platform**: TikTok
- **Action**: View content, identify valuable coaching/behavioral insights
- **Output**: Screenshot + mental note of key content
- **Status**: Working (manual process)

### **Step 2: Text Extraction** ✅ TESTED
- **Platform**: External transcription tool (unspecified)
- **Action**: Generate transcript from TikTok video
- **Output**: Full text transcript
- **Status**: Working (user confirmed)

### **Step 3: Context Preparation** ✅ TESTED
- **Platform**: Manual preparation
- **Action**: Combine screenshot + transcript for ChatGPT input
- **Output**: Formatted input for ChatGPT
- **Status**: Working (user confirmed)

### **Step 4: AI Analysis & Structuring** 🔄 CURRENTLY TESTING
- **Platform**: ChatGPT Mobile
- **Input**: Screenshot description + transcript
- **Action**: Analyze content, extract insights, generate structured template
- **Output**: GitHub Copilot-ready template
- **Status**: Template designed, needs testing

### **Step 5: Repository Integration** ✅ PARTIALLY TESTED
- **Platform**: GitHub Copilot Mobile Browser
- **Input**: ChatGPT-generated template
- **Action**: Create file, commit to repository
- **Output**: Committed field case in `00_SANDBOX/agent_inbox/`
- **Status**: Basic file creation works, template execution needs testing

## 🧪 Testing Status

### **Completed Tests**
1. **Mobile GitHub Copilot Basic Capability** ✅
   - **Result**: Successfully created files, branches, commits
   - **Evidence**: `test_mobile_copilot.md` file created
   - **Branch**: `copilot/create-test-mobile-copilot-file`
   - **Key Finding**: Mobile Copilot can handle complex operations

2. **Transcription Tool Integration** ✅
   - **Result**: User confirmed working
   - **Status**: No issues reported
   - **Key Finding**: External tool integration successful

### **Current Testing Phase**
**Priority 2: ChatGPT Mobile Template Generation**
- **Objective**: Validate ChatGPT can generate GitHub Copilot-ready templates
- **Focus**: Analysis and structuring, not transcript copying
- **Template**: Designed for mobile optimization

### **Pending Tests**
1. **ChatGPT Template Execution** ❓
   - **Test**: ChatGPT output → GitHub Copilot execution
   - **Status**: Ready to test
   - **Dependency**: Current ChatGPT template testing

2. **End-to-End Workflow** ❓
   - **Test**: Complete 5-step process with real content
   - **Status**: Waiting for ChatGPT template validation
   - **Dependency**: All individual components working

## 📝 Current ChatGPT Template Design

### **Input Format**
```
Screenshot: [Brief description of key visual elements]
Transcript: [Full transcript from your tool]

Analyze this content and extract the core coaching principle, behavioral routine, or strategic insight. Focus on what's actionable and valuable for career development, not entertainment value.
```

### **ChatGPT Prompt Template**
```
Analyze this TikTok content and generate a CIS field case file for GitHub Copilot:

[PASTE SCREENSHOT DESCRIPTION AND TRANSCRIPT HERE]

Analyze the content and extract the core coaching principle, behavioral routine, or strategic insight. Then generate a file for GitHub Copilot to create with this exact format:

Create a new file in 00_SANDBOX/agent_inbox/ called 2025-10-06_[slug].md with this content:

---
project: Career Intelligence Space
type: field_case
status: active
tags: [field_capture, [content_type]]
source: tiktok
captured_at: '2025-10-06'
generator: chatgpt-mobile
---

# [Analyzed Title - Not Original Title]

## Field Data
- Core idea: [Your analysis of the main principle]
- Mechanism: [How the principle works - your analysis]
- When to apply: [When to use this - your analysis]

## Key Insight
> [Single sentence summary of the core insight - your analysis]

## Source Context
- Creator: @[handle]
- Link-id: [short_id]
- Content Type: [coaching_philosophy|behavioral_routine|strategic_insight]
- Original Title: [Original TikTok title]

## Analysis Notes
[Your analysis of what makes this valuable, what's unique, what's actionable]

## Artifacts
- Screenshot: /assets/field-cases/2025/10/[slug].png
- Transcript: /assets/field-cases/2025/10/[slug].txt

## Next Steps
- [ ] QC pass (frontmatter, links)
- [ ] Set status: in-review
```

## 🔧 Key Design Principles

### **Mobile-First Optimization**
- **Short Input**: Minimal placeholders, clear instructions
- **Copy-Paste Ready**: Complete template included
- **Error Prevention**: Exact file path, complete frontmatter
- **Self-Contained**: No external references needed

### **AI-Assisted Processing**
- **ChatGPT Role**: Analysis and structuring, not content copying
- **GitHub Copilot Role**: File creation and repository management
- **Human Role**: Content selection and quality control

### **Quality Assurance**
- **Built-in Validation**: Template ensures compliance
- **Professional Output**: Career intelligence focus, not entertainment
- **Structured Format**: Consistent field case format
- **Traceability**: Complete audit trail

## 📊 Success Metrics

### **Speed Benchmarks**
- **Content Discovery**: 30 seconds
- **Transcription**: 30 seconds
- **Context Preparation**: 30 seconds
- **ChatGPT Processing**: 30-60 seconds
- **GitHub Copilot**: 30-60 seconds
- **Total Time**: 2-3 minutes

### **Quality Standards**
- **Analysis Quality**: Professional insights, not entertainment
- **Template Compliance**: CIS ontology compliance
- **Mobile Execution**: Reliable mobile operations
- **Content Value**: Actionable career intelligence

## 🚨 Known Issues & Limitations

### **Mobile Constraints**
- **Network Dependency**: Requires stable connection
- **Input Length**: Mobile interface limitations
- **Browser Compatibility**: GitHub Copilot mobile browser requirements
- **File Operations**: Mobile file creation reliability

### **AI Processing Limitations**
- **ChatGPT Analysis**: Quality depends on input format
- **Template Generation**: Consistency needs validation
- **Content Classification**: Accuracy of insight extraction
- **Mobile Interface**: ChatGPT mobile limitations

## 🔄 Next Testing Steps

### **Immediate Priority**
1. **Test ChatGPT Template**: Validate analysis and structuring output
2. **Test Template Execution**: ChatGPT output → GitHub Copilot
3. **Validate End-to-End**: Complete workflow with real content

### **Success Criteria**
- [ ] ChatGPT generates professional analysis
- [ ] GitHub Copilot executes templates successfully
- [ ] Complete workflow under 3 minutes
- [ ] High-quality field cases produced

### **Failure Fallbacks**
- **Manual File Creation**: If GitHub Copilot fails
- **Desktop Processing**: If mobile limitations encountered
- **Simplified Templates**: If complex format fails
- **Offline Storage**: If network issues occur

## 📈 Workflow Evolution

### **Version 1**: Manual Process
- **Status**: Replaced
- **Issues**: Too slow, error-prone
- **Replaced By**: AI-assisted workflow

### **Version 2**: AI-Assisted (Current)
- **Status**: In testing
- **Focus**: Mobile optimization, AI integration
- **Target**: 2-3 minute total process

### **Future Versions**: Potential Enhancements
- **Automation**: Reduced manual steps
- **Quality Control**: Built-in validation
- **Integration**: Seamless platform connections
- **Scalability**: Batch processing capabilities

---

**This document represents the current state of the CIS Mobile Field Capture Workflow as of the latest design iteration. All components are designed for mobile-first, AI-assisted field capture with focus on speed, quality, and reliability.**
