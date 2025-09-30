---
project: Career Intelligence Space
type: guide
status: active
tags: [guide, field_notes, mobile_capture]
updated: 2025-11-10
---

# Field Notes - Mobile Capture System

## 🎯 Purpose
**Persistent voice capture system for field agents** - no templates, no copying, just speak and commit.

## 📱 How to Use

### **Daily Workflow**
1. **Open** `FIELD_NOTES.md` in GitHub Mobile
2. **Tap** in the "Today's Notes" section
3. **Use voice-to-text** (native phone keyboard)
4. **Speak** your thoughts naturally
5. **Commit** the file
6. **Done!** Processing happens automatically

### **Voice-to-Text Tips**
- **Speak naturally** - don't worry about formatting
- **Use punctuation** - say "period", "comma", "new line"
- **Edit after** - you can always clean up the text
- **Keep it conversational** - this is for capturing thoughts

## 🔄 What Happens Automatically

### **Nightly Processing (2 AM UTC)**
- ✅ **New content** extracted from "Today's Notes"
- ✅ **Timestamped captures** created in `processed/`
- ✅ **Lite archives** generated with full Harness compliance
- ✅ **Input area** reset for next day
- ✅ **History preserved** in "Previous Days" section

### **Quality Gates**
- ✅ **Frontmatter validation** - ensures Harness compliance
- ✅ **PII scanning** - protects sensitive information
- ✅ **Schema compliance** - maintains data integrity
- ✅ **Traceability** - full audit trail from capture to archive

## 📁 File Structure

```
08_CHRONICLE/field/
├── FIELD_NOTES.md          # Your persistent input file
├── processed/              # Nightly processed captures
└── README.md              # This guide
```

## 💡 Usage Examples

### **Morning Standup Notes**
"Standup notes for November 10th. Key updates: finished the mobile capture system, need to test voice-to-text integration, blocked on GitHub API rate limits. Next steps: schedule demo with team, update documentation."

### **Client Meeting Notes**
"Client meeting with Acme Corp. Discussed project timeline, budget concerns, and technical requirements. They want to move forward with Phase 1 implementation. Action items: send proposal by Friday, schedule technical review next week."

### **Ideas and Insights**
"Random thought while walking: the field depository system could be extended to support photo captures with OCR. This would be useful for whiteboard notes and document scanning. Need to research OCR APIs and mobile integration."

## 🚀 Future Enhancements

### **Phase 2 (Coming Soon)**
- Real-time processing
- Mobile shortcuts integration
- Advanced categorization
- Search and filter interface

### **Phase 3 (Future)**
- AI-powered content analysis
- Cross-reference generation
- Notification system
- Advanced mobile UX

## 📞 Support

- **Issues:** Create GitHub issue for bugs or feature requests
- **Documentation:** See `docs/` directory for detailed guides
- **Architecture:** Check `08_CHRONICLE/vision/` for system design

---

**Ready to start capturing? Open `FIELD_NOTES.md` and start dictating!**
