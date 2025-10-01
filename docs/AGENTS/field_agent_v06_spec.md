---
project: Career Intelligence Space
type: spec
status: draft
tags: [field_agent, mobile_capture, github_native, v06, specification]
updated: 2025-09-30
---

# Field Agent v0.6 - Technical Specification
**Version:** 0.6  
**Status:** Draft - Ready for Implementation  
**Date:** 2025-09-30

## 🎯 Overview

Field Agent v0.6 is a dump-first, GitHub-native mobile capture system designed for field work scenarios. It leverages GitHub Issues, mobile app integration, and automated processing to provide a streamlined capture experience with minimal friction.

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

### **Frontmatter Schema (4 keys only):**
```yaml
---
run_id: 2025-09-30T14:32-07:00
tag: Plumbing
loc: PDX-NE
status: draft
---
```

## 📱 Mobile Workflow

### **Step 1: Create Issue**
- **Template:** "Field Capture (Dump)"
- **Location:** GitHub Mobile App
- **Action:** Create new issue from template

### **Step 2: Capture Content**
- **Photos:** Attach multiple photos directly to issue
- **Text:** Add quick note in issue body
- **Tag:** Select from predefined tag list (Plumbing, Electrical, Mounting, Smart-Home, Appliance, General)

### **Step 3: Submit**
- **Comment:** `submit` comment triggers processing
- **Processing:** GitHub Action creates files and PR
- **Receipt:** Bot posts confirmation with PR link

## 🔄 Automated Processing

### **GitHub Action Workflow:**
1. **Trigger:** Comment containing `submit` on Field Capture issue
2. **Extract Data:** Parse issue body, attachments, and tag
3. **Create Files:** Generate capture.md and move assets
4. **Generate PR:** Create PR with changes
5. **Post Receipt:** Bot confirms completion with PR link

### **Processing Logic:**
```python
def process_field_capture(issue_data):
    # Extract metadata
    tag = extract_tag(issue_data)
    location = extract_location(issue_data)
    timestamp = generate_timestamp()
    
    # Create file structure
    folder_name = f"{timestamp}_{location}_{tag}"
    create_folder(f"09_FIELD/{folder_name}")
    
    # Process attachments
    for attachment in issue_data.attachments:
        move_asset(attachment, f"09_FIELD/{folder_name}/assets/")
    
    # Generate capture.md
    generate_capture_file(issue_data, folder_name)
    
    # Create PR
    create_pr(folder_name)
    
    # Post receipt
    post_receipt(issue_data, pr_link)
```

## 📋 Issue Template Specification

### **Template Name:** "Field Capture (Dump)"
### **Labels:** `field-capture`, `mobile`, `v06`
### **Assignees:** `jwade83`
### **Projects:** `Field Agent`

### **Template Body:**
```markdown
## 📱 Field Capture - Dump First

**Location:** [Enter location - e.g., PDX-NE, Seattle-Downtown]
**Tag:** [Select one: Plumbing, Electrical, Mounting, Smart-Home, Appliance, General]

## 📸 Photos
[Attach photos directly to this issue]

## 📝 Quick Note
[Add your quick note here]

## 🏷️ Tag Selection
- [ ] Plumbing
- [ ] Electrical  
- [ ] Mounting
- [ ] Smart-Home
- [ ] Appliance
- [ ] General

## ✅ Submit
Comment `submit` when ready to process
```

## 🔧 Implementation Details

### **GitHub Action Configuration:**
```yaml
name: Field Agent v0.6 Processing
on:
  issue_comment:
    types: [created]

jobs:
  process-field-capture:
    if: contains(github.event.comment.body, 'submit')
    runs-on: ubuntu-latest
    steps:
      - name: Process Field Capture
        uses: ./.github/actions/field-agent-processor
        with:
          issue_number: ${{ github.event.issue.number }}
          repository: ${{ github.repository }}
```

### **File Generation Logic:**
```python
def generate_capture_file(issue_data, folder_name):
    frontmatter = {
        "run_id": generate_run_id(),
        "tag": issue_data.tag,
        "loc": issue_data.location,
        "status": "draft"
    }
    
    body = f"""# Field Capture - {issue_data.tag}

## Dump
- Photos: {len(issue_data.attachments)} attached
- Note: {issue_data.note}
- Location: {issue_data.location}
- Time: {issue_data.timestamp}

## Later-structure (agent can backfill)
- Parts: (blank)
- Time: (blank)
- Outcome: (blank)
- Client: (blank)
"""
    
    write_file(f"09_FIELD/{folder_name}/capture.md", frontmatter, body)
```

## 📊 Success Metrics

### **Performance Targets:**
- **Capture Time:** ≤ 60 seconds per capture
- **Processing Time:** ≤ 30 seconds from submit to receipt
- **Success Rate:** ≥ 95% successful processing
- **Error Rate:** ≤ 5% frontmatter or processing errors

### **Acceptance Criteria:**
- **Mobile Usability:** Works seamlessly on GitHub Mobile App
- **Offline Support:** Queues captures when offline, processes when online
- **File Integrity:** All assets properly linked and accessible
- **PR Generation:** Clean, reviewable PRs with proper commit messages

## 🚨 Error Handling

### **Common Error Scenarios:**
1. **Missing Tag:** Default to "General" with warning
2. **Missing Location:** Default to "Unknown" with warning
3. **No Photos:** Process text-only capture
4. **Processing Failure:** Post error message with retry option

### **Error Messages:**
```python
ERROR_MESSAGES = {
    "missing_tag": "⚠️ No tag selected. Defaulting to 'General'.",
    "missing_location": "⚠️ No location specified. Defaulting to 'Unknown'.",
    "processing_failed": "❌ Processing failed. Please try again or contact support.",
    "success": "✅ Field capture processed successfully! PR #123 created."
}
```

## 🔗 Integration Points

### **CIS Integration:**
- **Chronicle System:** Captures become part of 08_CHRONICLE
- **Agent System:** Field captures feed into existing agent workflows
- **Automation:** Integrates with existing GitHub Actions

### **Future Enhancements:**
- **Email Integration:** Email-to-issue capture
- **Voice Memos:** Voice-to-text processing
- **GPS Tagging:** Automatic location detection
- **AI Processing:** Intelligent data extraction

---

*Field Agent v0.6 Technical Specification - Career Intelligence Space*
*Status: Draft - Ready for Implementation*
