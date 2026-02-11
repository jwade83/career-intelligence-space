---
project: Career Intelligence Space
type: spec
status: draft
tags: [field_agent, mobile_capture, github_native, v06, specification, implementation, hard_rails]
updated: 2025-10-07
---

# Field Agent v0.6 - Complete Specification
**Version:** 0.6  
**Status:** Draft - Ready for Implementation  
**Date:** 2025-10-07  
**Consolidated:** Technical Spec + Implementation Plan + Hard Rails

## 🎯 Overview

Field Agent v0.6 is a dump-first, GitHub-native mobile capture system designed for field work scenarios. It leverages GitHub Issues, mobile app integration, and automated processing to provide a streamlined capture experience with minimal friction.

This document consolidates the technical specification, implementation plan, and hard rails into a single comprehensive reference.

---

## 🔧 Technical Architecture

### **Core Components:**
1. **GitHub Issue Template** - "Field Capture (Dump)" template
2. **Mobile Workflow** - Photo + text + tag selection
3. **Comment Processing** - `submit` comment triggers workflow
4. **Automated Processing** - GitHub Actions for file creation and PR generation
5. **Receipt System** - Bot confirmation and PR links

### **File Structure:**
```
/09_FIELD/YYYYMMDD_HHMM_{loc}_{tag}/capture.md
/09_FIELD/YYYYMMDD_HHMM_{loc}_{tag}/assets/IMG_0001.jpg
/09_FIELD/YYYYMMDD_HHMM_{loc}_{tag}/assets/IMG_0002.jpg
```

---

## 🔧 Hard Rails Frontmatter Schema

### **Exact 4 Keys (Nothing Else):**
```yaml
---
run_id: 2025-09-30T14:32-07:00
tag: Plumbing
loc: PDX-NE
status: draft
---
```

### **Field Definitions:**
- **run_id:** ISO timestamp with timezone (YYYY-MM-DDTHH:MM:SS-HH:MM)
- **tag:** Single word category (Plumbing, Electrical, HVAC, etc.)
- **loc:** Location code (PDX-NE, PDX-SW, etc.)
- **status:** Always "draft" for new captures

### **Validation Rules:**
- **NO additional fields** - Only these 4 keys allowed
- **NO nested objects** - Flat structure only
- **NO arrays** - Single values only
- **NO comments** - Clean YAML only

---

## 📱 Mobile Workflow

### **Step 1: Create Issue**
- **Template:** "Field Capture (Dump)"
- **Location:** GitHub Mobile App
- **Action:** Create new issue from template

### **Step 2: Fill Template**
- **Photos:** Attach 1-5 photos
- **Description:** Brief text description
- **Tag:** Select from predefined list
- **Location:** Select from predefined list

### **Step 3: Submit**
- **Action:** Add comment "submit"
- **Trigger:** GitHub Actions workflow starts
- **Processing:** Automated file creation and PR generation

### **Step 4: Receipt**
- **Confirmation:** Bot comment with PR link
- **Review:** Check generated files
- **Merge:** Approve and merge PR

---

## 📋 Implementation Plan

### **Phase 1: Core Infrastructure (Week 1)**

#### **Issue #1: Field Agent v0.6 Issue Template**
- **Title:** "Create Field Agent v0.6 Issue Template"
- **Labels:** `field-agent-v06`, `issue-template`, `mobile`
- **Priority:** High
- **Assignee:** jwade83

**Description:**
Create a GitHub issue template for Field Agent v0.6 mobile capture workflow.

**Acceptance Criteria:**
- [ ] Template file created in `.github/ISSUE_TEMPLATE/`
- [ ] Template includes all required fields
- [ ] Template validates frontmatter schema
- [ ] Template includes mobile-optimized instructions

#### **Issue #2: GitHub Actions Workflow**
- **Title:** "Implement Field Agent v0.6 GitHub Actions Workflow"
- **Labels:** `field-agent-v06`, `github-actions`, `automation`
- **Priority:** High
- **Assignee:** jwade83

**Description:**
Create GitHub Actions workflow to process field capture submissions.

**Acceptance Criteria:**
- [ ] Workflow triggers on issue comment "submit"
- [ ] Workflow validates frontmatter schema
- [ ] Workflow creates directory structure
- [ ] Workflow generates capture.md file
- [ ] Workflow handles asset processing
- [ ] Workflow creates PR with generated files

### **Phase 2: Asset Processing (Week 2)**

#### **Issue #3: Asset Processing Pipeline**
- **Title:** "Implement Asset Processing Pipeline"
- **Labels:** `field-agent-v06`, `assets`, `processing`
- **Priority:** Medium
- **Assignee:** jwade83

**Description:**
Implement asset processing including EXIF scrubbing and privacy protection.

**Acceptance Criteria:**
- [ ] EXIF data removal from images
- [ ] Privacy protection for sensitive data
- [ ] Asset optimization and compression
- [ ] Proper asset directory structure

### **Phase 3: Testing & Validation (Week 3)**

#### **Issue #4: Field Agent v0.6 Testing**
- **Title:** "Comprehensive Testing of Field Agent v0.6"
- **Labels:** `field-agent-v06`, `testing`, `validation`
- **Priority:** Medium
- **Assignee:** jwade83

**Description:**
Test all aspects of Field Agent v0.6 workflow.

**Acceptance Criteria:**
- [ ] Mobile workflow testing
- [ ] GitHub Actions workflow testing
- [ ] Asset processing testing
- [ ] Error handling testing
- [ ] Performance testing

---

## 🛡️ Privacy & Security

### **EXIF Data Scrubbing:**
- **Remove:** GPS coordinates, device info, timestamps
- **Keep:** Image dimensions, color profile
- **Process:** All images before storage

### **Privacy Protection:**
- **No Personal Data:** Remove any personal information
- **Location Codes:** Use predefined location codes only
- **Asset Encryption:** Consider encryption for sensitive assets

---

## 📊 Success Metrics

### **Performance Targets:**
- **Capture Time:** < 2 minutes from start to submit
- **Processing Time:** < 5 minutes from submit to PR
- **Error Rate:** < 5% failed captures
- **User Satisfaction:** > 90% successful captures

### **Quality Metrics:**
- **Frontmatter Compliance:** 100% valid YAML
- **Asset Processing:** 100% EXIF scrubbed
- **File Structure:** 100% consistent directory structure

---

## 🔗 Related Documentation

### **Mobile Integration:**
- [Mobile UI Documentation Hub](../MOBILE_UI/README.md)
- [Mobile Workflow Complete](../MOBILE_UI/mobile_workflow_complete.md)
- [Mobile Copilot Field Capture Guide](../MOBILE_UI/mobile_copilot_field_capture_guide.md)

### **Technical References:**
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub Issue Templates](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests)
- [YAML Frontmatter Standards](../Golden_Rules.md)

---

*This consolidated specification provides everything needed to implement and maintain Field Agent v0.6, combining technical details, implementation planning, and operational constraints into a single reference document.*
