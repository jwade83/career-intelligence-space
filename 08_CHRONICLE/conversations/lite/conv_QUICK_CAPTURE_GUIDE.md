---
project: Career Intelligence Space
type: conversation_archive_lite
status: active
tags:
- conversation_archive
- lite
- field_agent
- mobile_note
updated: '2025-09-30'
conversation_date: '2025-09-30'
participants:
- user
- field_agent
conversation_id: conv_QUICK_CAPTURE_GUIDE
timezone: America/Los_Angeles
related: []
capture_metadata:
  original_capture_id: QUICK_CAPTURE_GUIDE
  capture_type: mobile_note
  processed_at: '2025-09-30T09:21:23.005488'
  source_file: 08_CHRONICLE/capture_inbox/QUICK_CAPTURE_GUIDE.md
---

# Mobile Note — Lite Archive

## Summary
- **Captured:** Unknown date
- **Type:** Mobile Note
- **Source:** Field Agent Mobile Capture

## Content
# Quick Capture Guide

## Method 1: Ultra-Simple Template (Easiest)

1. **Copy this template** and paste it into a new file:
```markdown
---
project: Career Intelligence Space
type: mobile_capture
status: raw
tags: [mobile_capture, field_agent, quick_note]
captured_at: 2025-11-10
capture_type: quick_note
source: github_mobile
---

# Quick Note

## Content
[Just type your content here]

---
**Field Agent Quick Capture**
```

2. **Only change**:
   - The date in `captured_at: 2025-11-10`
   - Your content in the `## Content` section

## Method 2: Voice-to-Text Integration

1. **Use your phone's voice-to-text** to dictate content
2. **Copy the text** into the template above
3. **Commit the file**

## Method 3: Photo + Text

1. **Take a photo** of notes, whiteboard, etc.
2. **Save photo** to your device
3. **Create capture file** with:
   ```markdown
   ## Content
   ![Photo](your_photo.jpg)
   
   [Add any additional notes here]
   ```

## Method 4: Quick Script (Desktop)

If you're on desktop, you can use:
```bash
python3 scripts/quick-capture.py "Your content here"
```

## Auto-Processing

All captures are automatically:
- ✅ Processed by Field Agent workflow
- ✅ Scanned for PII
- ✅ Converted to lite archives
- ✅ Added to conversation history

## Tips

- **Keep it simple** - just capture the essence
- **Use voice-to-text** for longer content
- **Take photos** for visual information
- **Don't worry about formatting** - the system handles it


## Next Steps
- [ ] Review and refine content
- [ ] Add to Decision Log if strategic
- [ ] Link to related archives
- [ ] Archive or promote to full conversation

---

**Traceability**
- conversation_id: conv_QUICK_CAPTURE_GUIDE
- decision_log: docs/decision-log.md (search for the conversation_id)
- chronicle_path: 08_CHRONICLE/conversations/lite/
- schema_version: v1
- original_capture_id: QUICK_CAPTURE_GUIDE
