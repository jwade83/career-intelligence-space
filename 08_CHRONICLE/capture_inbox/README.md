---
project: Career Intelligence Space
type: capture_instructions
status: active
tags: [capture_inbox, field_agent, mobile_capture, instructions]
updated: 2025-11-10
timezone: "America/Los_Angeles"
---

# Field Agent Capture Inbox

This directory serves as the **mobile capture interface** for the Field Agent system, enabling real-world information capture without desktop dependency.

## 🎯 Purpose

Bridge the gap between **Harness infrastructure** (desktop) and **Field Agent scenarios** (mobile/remote) by providing a low-friction capture system that maintains Harness compliance.

## 📱 Mobile Capture Workflow

### Quick Capture (GitHub Mobile App)
1. **Open GitHub Mobile** app
2. **Navigate to** `08_CHRONICLE/capture_inbox/`
3. **Create new file** with naming convention: `raw_YYYYMMDD_HHMM.md`
4. **Use minimal template** (see below)
5. **Save and commit** - processing happens automatically

### Capture Types
- **`raw_YYYYMMDD_HHMM.md`** - General notes and thoughts
- **`raw_YYYYMMDD_HHMM_photo.md`** - Photo captures with descriptions
- **`raw_YYYYMMDD_HHMM_voice.md`** - Voice memo transcriptions
- **`raw_YYYYMMDD_HHMM_meeting.md`** - Meeting notes and insights

## 📋 Minimal Template

```yaml
---
capture_id: raw_20251110_2215
capture_type: mobile_note
capture_date: 2025-11-10
---

# Quick capture content here

## Context
- Where: [location/context]
- When: [time/urgency]
- Why: [importance/reason]

## Key Points
- Point 1
- Point 2
- Point 3

## Next Steps
- [ ] Action item 1
- [ ] Action item 2
```

## 🔄 Automated Processing

### GitHub Action Processing
- **Trigger:** Every 6 hours or on push to `capture_inbox/`
- **Process:** 
  1. Detect capture type from content/file name
  2. Generate conversation_id from capture_id
  3. Backfill full Harness frontmatter
  4. Move to `08_CHRONICLE/conversations/lite/`
  5. Run QA gates (linter, PII scanner)
  6. Create PR for review

### Quality Gates
- **Frontmatter validation** - Ensures Harness compliance
- **PII scanning** - Protects sensitive information
- **Schema compliance** - Maintains archive standards
- **Traceability** - Preserves capture chain of custody

## 🎯 Field Agent Scenarios

### On-the-Go Capture
- **Conference insights** - Quick notes during talks
- **Networking conversations** - Key points and follow-ups
- **Research discoveries** - Links and findings
- **Strategic thoughts** - Ideas and connections

### Mobile-First Features
- **Zero desktop dependency** - Works from any device
- **Minimal cognitive load** - Just capture and save
- **Auto-processing** - Harness compliance handled automatically
- **Traceability** - Complete audit trail maintained

## 📊 Success Metrics

### Capture Efficiency
- **Time to capture** - <30 seconds from idea to saved
- **Processing success** - >95% successful ingestion
- **QA compliance** - 100% Harness schema compliance
- **Traceability** - 100% capture ID preservation

### Field Agent Effectiveness
- **Mobile usage** - Regular capture from mobile devices
- **Information retention** - Reduced "dispatch mode" entropy
- **Harness integration** - Seamless promotion to archives
- **Real-world validation** - Proven utility in field scenarios

## 🔧 Troubleshooting

### Common Issues
- **Frontmatter errors** - Use minimal template exactly
- **Processing delays** - Check GitHub Actions status
- **QA failures** - Review linter output in PR
- **Mobile editing** - Use GitHub Mobile app for best experience

### Support
- **Documentation:** `docs/runbooks/harness/archive-lint-failures.md`
- **QA System:** `make qa` for local validation
- **Schema Reference:** `config/archive_schema.yml`
- **Decision Log:** `docs/decision-log.md`

---

**Field Agent Status:** ✅ **OPERATIONAL**  
**Last Updated:** 2025-11-10  
**Next Review:** Weekly
