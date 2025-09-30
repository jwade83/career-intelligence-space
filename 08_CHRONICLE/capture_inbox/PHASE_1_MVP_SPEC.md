---
project: Career Intelligence Space
type: spec
status: draft
tags: [mvp, field_depository, mobile_capture, phase_1]
updated: 2025-11-10
---

# Phase 1 MVP: Field Depository System
**Status:** Minimum Deployable Spec - Achievable This Week

## 🎯 Core MVP Goal
**"Can I dictate into my phone and have it show up tomorrow as a lite archive with full schema compliance?"**

## ✅ What's Actually Possible Today

### **Single Persistent Capture File**
- **File:** `08_CHRONICLE/field/FIELD_NOTES.md`
- **Behavior:** Never resets completely, always ready for new content
- **Mobile UX:** Open file → dictate → commit → done

### **GitHub Mobile Workflow**
1. **Open** `FIELD_NOTES.md` in GitHub Mobile
2. **Tap** in content area
3. **Use native voice-to-text** (phone keyboard)
4. **Commit** with auto-generated message
5. **Done** - processing happens overnight

### **Nightly Processing Pipeline**
- **Trigger:** Schedule at 2 AM UTC daily
- **Process:** Move new content to timestamped captures
- **Generate:** Full Harness-compliant lite archives
- **Reset:** Input area for next day

## 🏗️ Technical Implementation

### **File Structure**
```
08_CHRONICLE/field/
├── FIELD_NOTES.md          # Persistent input file
├── processed/              # Nightly processed captures
└── README.md              # Usage guide
```

### **GitHub Actions Workflow**
```yaml
name: Field Notes Processor (Nightly)
on:
  schedule:
    - cron: '0 2 * * *'  # 2 AM UTC daily
  workflow_dispatch:
```

### **Processing Logic**
1. **Extract** new content from `FIELD_NOTES.md`
2. **Create** timestamped capture files
3. **Generate** lite archives with full frontmatter
4. **Reset** input area (preserve history)
5. **Commit** all changes

## 📱 Mobile User Experience

### **Daily Workflow**
1. **Morning:** Open `FIELD_NOTES.md`
2. **Throughout day:** Dictate thoughts/notes
3. **Evening:** Commit changes
4. **Next morning:** See processed archives

### **Voice-to-Text Tips**
- Use native phone keyboard voice feature
- Speak naturally with punctuation
- Edit after dictation if needed
- Don't worry about formatting

## 🔧 Implementation Steps

### **Step 1: Create Field Directory**
```bash
mkdir -p 08_CHRONICLE/field/processed
```

### **Step 2: Create Persistent Input File**
```markdown
---
project: Career Intelligence Space
type: field_notes
status: active
tags: [field_notes, mobile_capture, persistent]
updated: 2025-11-10
---

# Field Notes - Daily Capture

## Today's Notes
[Use voice-to-text here - speak your thoughts]

---

## Previous Days
[Previous notes will be archived here automatically]

---
**Field Agent Daily Capture - Always Ready**
```

### **Step 3: Create Nightly Processor**
```python
# scripts/field-notes-processor.py
# Processes FIELD_NOTES.md nightly
# Creates timestamped captures
# Generates lite archives
# Resets input area
```

### **Step 4: Create GitHub Actions Workflow**
```yaml
# .github/workflows/field-notes-nightly.yml
# Runs at 2 AM UTC daily
# Processes new content
# Generates archives
# Commits changes
```

## 📊 Success Metrics (Phase 1)

### **Functional Requirements**
- ✅ **Persistent input** - file never resets completely
- ✅ **Voice-to-text** - works with native mobile keyboard
- ✅ **Nightly processing** - content becomes lite archives
- ✅ **Full compliance** - passes all Harness quality gates
- ✅ **Zero templates** - no copy-paste required

### **Performance Targets**
- **Capture time:** < 60 seconds (dictate + commit)
- **Processing time:** < 5 minutes (nightly batch)
- **Compliance rate:** 100% (automated frontmatter)
- **Mobile compatibility:** 100% (GitHub Mobile app)

## 🚀 Phase 2+ Vision (Future)

### **Enhanced Mobile Integration**
- iOS Shortcuts → GitHub API
- Drafts app integration
- Android Tasker automation

### **Real-time Processing**
- Webhook triggers
- Sub-2-second response
- Live notifications

### **Intelligent Categorization**
- LLM-powered content analysis
- Auto-tagging and classification
- Context extraction

### **Advanced UX**
- Search and filter interface
- Mobile-optimized dashboard
- Offline sync capabilities

## 🎯 Why This Works

### **Realistic Scope**
- Uses existing GitHub Mobile capabilities
- Leverages current Harness architecture
- No external dependencies required

### **Immediate Value**
- Solves the "one-off file" problem
- Eliminates template copying
- Provides persistent capture point

### **Foundation for Growth**
- Proves the concept works
- Validates user workflow
- Enables data-driven Phase 2 decisions

---

**This MVP can be built and tested this week, while the S-tier vision remains intact for future phases.**
