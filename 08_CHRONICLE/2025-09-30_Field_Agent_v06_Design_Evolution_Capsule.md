---
project: Career Intelligence Space
type: implementation_capsule
status: completed
tags: [cis, field_agent, mobile_ui, github_native, design_evolution, v06]
updated: 2025-09-30
capsule_type: design_evolution
analysis_date: 2025-09-30
category: system_design
sentiment: highly_insightful
implementation_readiness: high
priority: high
---

# Field Agent v0.6 - Design Evolution & GitHub-Native Strategy
**Primary:** From Structure-First to Dump-First Mobile Capture
**Secondary:** GitHub-Native Mobile UI/UX Design Philosophy
**Tertiary:** Technical Architecture & Implementation Roadmap
**Date:** 2025-09-30
**Status:** Design Complete - Ready for Implementation

## 🎯 Design Evolution Summary

The Field Agent system evolved from a complex, structure-first approach to a streamlined, dump-first, GitHub-native mobile capture system. This evolution was driven by real-world field testing that revealed critical friction points in the original design.

## 🔍 Original Field Agent Problems (ChatGPT Postmortem)

### **High-Friction Capture Process:**
- **Too many required fields** at capture time (client, location, task type, parts, notes, images, links)
- **Context switching** between Chat ↔ Terminal/Cursor ↔ GitHub PRs ↔ phone photos
- **Naming anxiety** - uncertainty about file paths/frontmatter
- **Parse/merge fatigue** - YAML comments or frontmatter drift → CI failures
- **No "one-button finish"** - no dopamine hit, just more steps

### **Root Cause: Structure-First Approach**
- **Schema demanded too much upfront** instead of allowing dump-first, structure-later
- **Optimized for machines, not field reality**
- **Frontmatter complexity** with optional fields and comments
- **No hard rails** for mobile editing

## 🚀 Field Agent v0.6 Design Philosophy

### **Core Principle: Dump-First, Structure-Later**
- **Two-field capture:** (a) voice/photo/note, (b) 1-tap task tag
- **Minimal frontmatter:** exactly 4 keys, no comments
- **Deterministic naming:** `/09_FIELD/YYYYMMDD_HHMM_{loc}_{task}/capture.md`
- **Immediate receipt:** "Saved + PR #123 opened"

### **GitHub-Native Strategy:**
- **"Mobile-first ≠ native app build"** - GitHub mobile + Issue templates + comment listeners deliver 80% of value
- **"Keep everything CI-side"** - Maintains automation benefits without exploding complexity
- **"Jobs Radar as proofed pattern"** - Use successful GitHub-native approach as template

## 🔧 Technical Architecture

### **Interaction Surfaces:**
1. **Chat-first (fastest):** `/field` command + attachments + "Submit"
2. **Email fallback:** email photos + one-line subject
3. **GitHub Issue (optional):** native mobile push notifications

### **File Structure:**
```
/09_FIELD/20250930_1432_PDX-NE_Plumbing/capture.md
/09_FIELD/20250930_1432_PDX-NE_Plumbing/assets/IMG_0001.jpg
```

### **Minimal Frontmatter (4 keys only):**
```yaml
---
run_id: 2025-09-30T14:32-07:00
tag: Plumbing
loc: PDX-NE
status: draft
---
```

### **Body Auto-Generated:**
```markdown
## Dump
- Voice note: transcript...
- Photo: ![IMG_0001.jpg](assets/IMG_0001.jpg)
- Quick note: "Toilet fill valve bypassed; recommend retrofit"

## Later-structure (agent can backfill)
- Parts: (blank)
- Time: (blank)
- Outcome: (blank)
```

## 📱 Mobile Experience Design

### **Friction Budget:**
- **≤ 60 seconds** per capture on site
- **≤ 1 tap + 1 send + 1 submit**
- **Offline support** with queued local saves

### **Mobile-First Features:**
- **Zero desktop dependency** - Works from any device
- **Minimal cognitive load** - Just capture and save
- **Auto-processing** - Harness compliance handled automatically
- **Traceability** - Complete audit trail maintained

## 🎯 Implementation Roadmap

### **Phase 1: Core GitHub-Native Systems (Week 1-2)**
- **Field Agent v0.6** - Dump-first capture system
- **Issue Template** - "Field Capture (Dump)" template
- **Mobile Workflow** - Attach photos + one-liner + pick tag
- **Comment Submit** - `submit` comment triggers workflow

### **Phase 2: Enhanced Features (Week 3-4)**
- **Action Card Microform** - Optional web interface
- **Advanced Mobile Features** - Voice memo, GPS tagging (behind toggles)

### **Phase 3: Stretch Features (Later)**
- **AI-Powered Intelligence** - Smart data extraction
- **Advanced Integrations** - Email-to-issue, SMS capture

## 📊 Success Metrics

### **Field Agent v0.6 Success Criteria:**
- **≤ 60 seconds** per capture on site
- **≤ 1 tap + 1 send + 1 submit** workflow
- **100% offline capability** with sync when online
- **95% successful ingestion** rate

### **Acceptance Gates:**
- **≤ 60s** to capture + submit
- **Zero frontmatter errors** - Hard-rail schema works
- **Images linked and viewable** - Asset management works
- **If misses twice in a week → fix workflow, don't add features**

## 🔍 Key Insights & Lessons Learned

### **What Works:**
- **GitHub-native features** for UI/UX
- **Mobile-first design** with native app integration
- **Clear action moments** with immediate feedback
- **Automated processing** to handle complexity
- **Dump-first, structure-later** approach

### **What Doesn't Work:**
- **Structure-first capture** systems
- **Complex frontmatter** requirements
- **Context switching** between multiple tools
- **No clear "finish" moment**
- **Optimizing for machines over field reality**

### **Strategic Alignment:**
- **CIS Vision** - Directly supports Action-Execution-Intelligence Ecosystem
- **User Experience** - Chat-first, mobile-optimized approach
- **Technical Architecture** - Leverages existing GitHub infrastructure
- **Scalability** - Foundation for advanced automation features

## 🚨 Risk Management & Guardrails

### **Privacy & Security:**
- **CI repo private** - Never public
- **No tenant names/addresses in filenames** - Privacy protection
- **Sensitive details in body text only** - Proper data handling

### **Data Management:**
- **Stable IDs** - `YYYYMMDD_HHMM_loc_tag` for field captures
- **Noise reduction** - Only open Issues when needed
- **Auto-close by EOD** - Prevent issue accumulation

### **Error Handling:**
- **Hard-rail frontmatter** - Exact 4 keys, no optional fields
- **Path allowlist** - Only allowed directories
- **Precise failure messages** - Clear feedback when CI lints trip

---

## 🎯 Next Steps

### **Immediate Actions:**
1. **Create Field Agent v0.6 specification** - Detailed technical spec
2. **Design Issue templates** - "Field Capture (Dump)" template
3. **Plan 7-day pilot** - Test system in parallel with Jobs Radar
4. **Document acceptance criteria** - Clear success/failure metrics

### **Documentation Needs:**
- **`/docs/AGENTS/field_agent_v06_spec.md`** - Complete specification
- **`/docs/MOBILE_UI/`** - Mobile UI/UX requirements
- **GitHub Issues** - Actionable implementation tasks
- **Task Queue** - Agent-executable tasks

---

*Field Agent v0.6 Design Evolution - Career Intelligence Space*
*Status: Design Complete - Ready for Implementation*
