---
project: Career Intelligence Space
type: strategic_vision_capsule
status: pending
tags: [cis, vision, strategic_analysis, jobs_radar, career_intelligence, automation, perplexity_integration]
updated: 2025-11-10
capsule_type: strategic_innovation_analysis
analysis_date: 2025-11-10
category: strategic_design_philosophy
sentiment: breakthrough_innovation
stage: "B → C Evolution"
priority: high
implementation_readiness: medium
---

# Jobs Radar Intelligence System
**Primary:** Automated Career Opportunity Discovery and Action Intelligence  
**Secondary:** Chat-First Job Market Intelligence with Perplexity Integration  
**Tertiary:** Streamlined User Experience for Daily Career Opportunity Management  
**Quaternary:** CIS Enhancement for Action-Execution-Intelligence Ecosystem  
**Date:** 2025-11-10  
**Status:** Strategic Vision Capsule (Pending Implementation)

---

## 🎯 Purpose

Transform the ChatGPT-proposed "jobs radar" concept into a streamlined, chat-first career intelligence system that enhances existing CIS capabilities. This capsule documents the strategic analysis, design evolution, and implementation roadmap for creating an effortless daily job market intelligence workflow.

---

## 🌐 Strategic Context

**Current State:** CIS operates as Stage B Quality Gatekeeper with comprehensive career intelligence frameworks but lacks automated job market scanning and action intelligence.

**Vision State:** CIS evolves to include automated job market intelligence with chat-first interaction, leveraging existing Perplexity capabilities and CIS infrastructure for seamless daily career opportunity management.

**Evolution Path:** Stage B (Quality Gatekeeper) → Stage C (External Intelligence Integration) → Stage D (Full Action-Execution-Intelligence Ecosystem)

---

## 📊 Strategic Assessment: A+ Breakthrough Innovation

### **Core Innovation: Chat-First Career Intelligence**
The critical insight: **leverage existing chat behavior** rather than creating new interfaces, transforming job search from manual process to conversational intelligence.

**Key Design Principles:**
- **Chat-first interaction** - natural conversation with existing ChatGPT/Perplexity
- **Progressive enhancement** - start simple, evolve based on usage
- **CIS integration** - enhance existing frameworks rather than create parallel systems
- **Streamlined workflow** - 2-minute daily check-in with maximum intelligence

---

## 🚀 Design Evolution: From Complex to Streamlined

### **Original ChatGPT Proposal (Complex)**
- Multiple interfaces (chat, email, action card, dashboard)
- Complex JSON payloads and GitHub API integration
- Heavy automation with n8n flows and auto-merge rules
- Multiple failure paths and maintenance overhead

### **Streamlined CIS Enhancement (Simple)**
- **Single interface** - chat handles 90% of interactions
- **Leverage existing infrastructure** - Discovery Agent, Strategic Lenses, Chronicle
- **Progressive enhancement** - add complexity only when needed
- **Minimal maintenance** - uses existing CIS automation

---

## 🎯 Implementation Roadmap

### **Phase 1: Chat-Only Intelligence (Start Here)**
**Timeline:** 1-2 weeks  
**Complexity:** Low  
**User Experience:** Natural conversation with existing ChatGPT/Perplexity

**Core Workflow:**
```
You: "What's new in the job market?"
CIS: "Found 3 IMMEDIATE opportunities:
1. CRMG — Maint Tech II — $26-28/hr — Why: work-order tech + electrical
2. Liberty — Certified Maint Tech — $28-30/hr — Why: HVAC track  
3. Bluestone — PT Facilities Tech — $24-26/hr — Why: part-time fit

Reply: apply 1, research 2, snooze 3d 3"

You: "apply 1, research 2, snooze 3d 3"
CIS: "Done. Applied to CRMG, created Liberty research stub, snoozed Bluestone until Friday. Check your email for confirmation."
```

**Technical Implementation:**
- Enhance existing Discovery Agent with scoring algorithm
- Create Perplexity prompts for structured job scan reports
- Integrate with existing Company Research Template and Compensation Tracker
- Use existing Chronicle structure for job scan reports

### **Phase 2: Smart Email Digest (Weekend Project)**
**Timeline:** 2-3 weeks  
**Complexity:** Medium  
**User Experience:** Proactive intelligence with email-first interaction

**Core Workflow:**
```
Morning Email (8:00 AM):
Subject: CIS Jobs Radar — 3 IMMEDIATE, 5 HIGH

IMMEDIATE (3):
1. CRMG — Maint Tech II — $26-28/hr — Why: work-order tech + electrical
2. Liberty — Certified Maint Tech — $28-30/hr — Why: HVAC track
3. Bluestone — PT Facilities Tech — $24-26/hr — Why: part-time fit

Quick Actions:
- Reply "A1" to apply to #1
- Reply "R2" to research #2  
- Reply "S3-3d" to snooze #3 for 3 days

Or open chat for full interaction.
```

**Technical Implementation:**
- Email parsing for simple keyword extraction
- Action mapping (A1 = apply job 1, R2 = research job 2)
- Same backend infrastructure as Phase 1
- Confirmation email system

### **Phase 3: Action Card Microform (Nice-to-Have)**
**Timeline:** 4-6 weeks  
**Complexity:** Medium-High  
**User Experience:** Visual interface for bulk actions

**Core Workflow:**
```
Single Web Page:
Jobs Radar — Tue, 8:01 AM • Portland

IMMEDIATE (3):
[Company] [Title] [Pay] [Posted] [Why Fit] [Action Dropdown]
CRMG     Maint Tech II  $26-28/hr  2h ago  work-order tech  [Apply ▼]
Liberty  Certified Maint $28-30/hr 4h ago  HVAC track      [Research ▼]
Bluestone PT Facilities $24-26/hr 1d ago  part-time fit   [Snooze ▼]

[Submit Actions] [View HIGH (5)] [Open Chat]
```

**Technical Implementation:**
- Static page with signed URL (token expires same day)
- Single endpoint POST /actions with simple payload
- Reuses chat infrastructure
- No authentication required

---

## 🔧 Technical Architecture

### **Core Components**
1. **Enhanced Discovery Agent** - existing `agents/discovery.yml` with scoring algorithm
2. **Perplexity Integration** - structured prompts for job market intelligence
3. **Strategic Lens Application** - existing 5-lens framework for opportunity assessment
4. **Chronicle Integration** - existing `08_CHRONICLE/` structure for reports
5. **Feedback Loop Architecture** - existing metrics framework for outcome tracking

### **Data Flow**
```
Perplexity Job Scan → CIS Processing → Chat Interface → User Actions → Repo Updates → Email Confirmation
```

### **Integration Points**
- **Discovery Agent** - foundation for job scanning and scoring
- **Company Research Template** - auto-generated research stubs
- **Compensation Tracker** - salary benchmarking and negotiation prep
- **Strategic Lenses** - consistent opportunity evaluation
- **Chronicle System** - audit trail and historical tracking

---

## 📊 Success Metrics

### **Phase 1 Success Criteria**
- **Daily usage** - user checks chat every morning
- **Action completion** - user applies to 2-3 jobs per week
- **Time saved** - 5 minutes vs. 30 minutes manual job search
- **User satisfaction** - natural, effortless interaction

### **Phase 2 Success Criteria**
- **Email engagement** - user reads and acts on morning digest
- **Quick reply usage** - user uses email commands for simple actions
- **Fallback to chat** - user uses chat for complex interactions
- **Proactive intelligence** - system reaches out to user

### **Phase 3 Success Criteria**
- **Bulk actions** - user processes multiple opportunities at once
- **Visual preference** - user prefers action card over chat for complex decisions
- **Workflow efficiency** - user completes daily job review in under 2 minutes
- **System adoption** - user relies on system for career opportunity management

---

## 🎯 Key Design Principles

### **✅ What Makes It Streamlined**
- **Single interface** - chat handles 90% of interactions
- **Progressive enhancement** - add complexity only when needed
- **Leverage existing tools** - no new apps or dashboards
- **Simple data flow** - chat → backend → repo → email

### **❌ What Makes It Complex**
- **Multiple interfaces** - too many places to check
- **Complex authentication** - tokens, sessions, expiration
- **Heavy automation** - GitHub Actions, auto-merge, schema validation
- **Error handling** - multiple failure paths and recovery

---

## 🔄 Implementation Strategy

### **Start Simple (Phase 1)**
1. **Chat-only interface** - natural conversation with Perplexity
2. **Simple commands** - "apply 1, research 2, snooze 3d 3"
3. **Email confirmations** - audit trail without complexity
4. **Repo updates** - automatic, no user interaction required

### **Evolve Based on Usage (Phase 2)**
1. **Email digest** - if user finds themselves checking email first
2. **Quick replies** - if user wants faster email-based actions
3. **Smart notifications** - if user wants proactive alerts

### **Add Complexity Only When Needed (Phase 3)**
1. **Action Card** - if user needs visual interface for bulk actions
2. **Dashboard** - if user needs historical tracking and analytics
3. **Advanced automation** - if user needs complex workflow management

---

## 🎯 Risk Assessment

### **High-Risk Factors**
- **Perplexity API limitations** - rate limiting, data quality, access restrictions
- **User adoption** - new workflow may not fit existing habits
- **Maintenance overhead** - additional system to maintain and monitor
- **Data quality** - automated job scanning may produce inaccurate results

### **Risk Mitigation Strategies**
- **Start with manual prompts** - validate Perplexity capabilities before automation
- **Leverage existing behavior** - use chat interface user already uses daily
- **Minimal maintenance** - use existing CIS infrastructure and automation
- **Quality controls** - implement validation and feedback loops

---

## 📝 Next Steps

### **Immediate Actions (This Week)**
1. **Validate Perplexity capabilities** - test job board access and data quality
2. **Enhance Discovery Agent** - add scoring algorithm and feedback loops
3. **Create Perplexity prompts** - develop structured job scan report templates
4. **Test chat workflow** - validate natural conversation interface

### **Short-term Actions (Next Month)**
1. **Implement Phase 1** - chat-only intelligence system
2. **User testing** - validate workflow and gather feedback
3. **Refine scoring algorithm** - adjust based on user preferences and outcomes
4. **Documentation** - create user guide and technical specifications

### **Medium-term Actions (Next Quarter)**
1. **Implement Phase 2** - email digest and quick reply system
2. **Analytics integration** - track usage patterns and success metrics
3. **Strategic lens integration** - apply existing frameworks to job assessment
4. **Feedback loop implementation** - track application outcomes and market learning

---

## 🔮 Future Vision

### **Stage C: External Intelligence Integration**
- **Real-time job market intelligence** with automated scanning and scoring
- **Proactive opportunity alerts** based on user preferences and market changes
- **Integrated career pipeline** with application tracking and outcome analysis
- **Market learning system** that improves recommendations based on success patterns

### **Stage D: Full Action-Execution-Intelligence Ecosystem**
- **Autonomous career intelligence** that learns and adapts to user behavior
- **Predictive opportunity identification** using market trends and user patterns
- **Integrated negotiation support** with real-time salary benchmarking
- **Network intelligence** connecting opportunities with user's professional network

---

## 📋 Conclusion

The Jobs Radar Intelligence System represents a strategic enhancement to CIS that transforms job search from a manual, time-consuming process into an effortless, intelligent workflow. By leveraging existing chat behavior and CIS infrastructure, this system provides maximum value with minimal complexity.

The key to success is **starting simple** and **evolving based on actual usage patterns** rather than building a complex system upfront. The intelligence should feel **magical and effortless** rather than like managing a complex piece of machinery.

**Implementation Priority:** High  
**User Value:** Maximum  
**Technical Complexity:** Low-Medium  
**Maintenance Overhead:** Minimal  
**Strategic Alignment:** Perfect fit with CIS vision

---

*Jobs Radar Intelligence System - Career Intelligence Space*  
*Strategic Vision Capsule - 2025-11-10*  
*Status: Pending Implementation - Ready for Phase 1 Development*
