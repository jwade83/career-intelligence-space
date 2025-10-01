---
project: Career Intelligence Space
type: spec
status: draft
tags: [reality_check, operational_constraints, github_limitations, mobile_capabilities]
updated: 2025-09-30
---

# Reality Check - What's Live vs. Planned
**Status:** Draft - Operational Constraints Documentation  
**Date:** 2025-09-30

## 🎯 Purpose

This document provides a reality check on what's actually implemented vs. what's aspirational in the CIS mobile and automation systems. It addresses the operational constraints and limitations that caused real pain during implementation.

## ✅ What's Actually Live (Working Today)

### **Jobs Radar Intelligence System:**
- **GitHub Issue Templates** - Rich interactive templates with checkboxes and labels
- **Mobile Push Notifications** - Via GitHub Mobile App
- **Basic Comment Processing** - Manual comment codes (apply 1, research 2, snooze 3)
- **PR Generation** - Manual PR creation with basic automation
- **Issue Creation** - Automated issue creation via GitHub Actions

### **Field Agent Capture System:**
- **Capture Inbox** - Basic mobile capture interface
- **Template System** - Minimal capture templates
- **Automated Processing** - Basic GitHub Actions processing
- **File Structure** - Organized capture directory structure

## ❌ What's NOT Live (Aspirational/Backlog)

### **Over-Claimed Capabilities:**
- **❌ "100% offline capability"** - GitHub mobile has limited offline support
- **❌ "Voice/QR/GPS built-in"** - Not implemented, requires custom development
- **❌ "1-day deployment"** - Took multiple iterations and fixes
- **❌ "80-90% reductions"** - Aspirational metrics, not measured
- **❌ "Real-time validation"** - Not implemented
- **❌ "AI-powered data extraction"** - Not implemented

### **Missing Operational Features:**
- **❌ Auto-merge rules** - Checks don't always attach properly
- **❌ Idempotency handling** - Duplicate actions not handled
- **❌ Snooze state management** - No persistent snooze storage
- **❌ Attachment handling** - No size limits or EXIF scrubbing
- **❌ Token management** - No automated token rotation
- **❌ Noise management** - No auto-close or threshold rules

## 🚨 Operational Pain Points (Today's Reality)

### **1. Checks That Don't Attach / "Mergetate: Blocked"**
- **Problem:** GitHub Actions checks don't always attach to PRs
- **Workaround:** Tiny "no-op" commit to re-trigger checks
- **Missing:** Explicit auto-label/auto-merge rules
- **Need:** Path allowlist, required status checks list, precise error messages

### **2. YAML/Frontmatter Parse Errors**
- **Problem:** Comments and variants cause YAML parsing failures
- **Missing:** Hard-rail schema enforcement
- **Need:** Exact 4-key frontmatter, linter that strips stray keys, precise error text

### **3. Idempotency & State Management**
- **Problem:** Multiple comments, duplicate actions, re-submits not handled
- **Missing:** Deterministic job_id, comment de-duplication
- **Need:** "Already applied—ignored" receipts, stable ID mapping

### **4. Snooze Semantics**
- **Problem:** No persistent snooze state storage
- **Missing:** Where snooze_until lives and how next day's scan honors it
- **Need:** Tiny store (data/jobs/snoozed.jsonl) + filter rule in scanner

### **5. Index Stability**
- **Problem:** "apply 1" breaks when lists change
- **Missing:** Mapping comment indices to stable IDs
- **Need:** Render rows with stable IDs: `<company> — <title> 〔id: crmg-26-28〕`

### **6. Attachments from Mobile**
- **Problem:** No clear attachment handling rules
- **Missing:** Where images land, size limits, linking conventions
- **Need:** /09_FIELD/.../assets/ convention, auto-embed pattern, EXIF/GPS scrubbing

### **7. Secrets & Permissions**
- **Problem:** Token scope and permissions not clearly defined
- **Missing:** Exact GitHub Actions permissions, PAT storage, rotation
- **Need:** Least-privilege PAT guidance, secure storage, rotation procedures

### **8. Noise Management**
- **Problem:** No threshold rules or auto-close mechanisms
- **Missing:** Open-issue threshold, auto-close by EOD, watch settings
- **Need:** "Only open if IMMEDIATE ≥ 1," "HIGH in weekly roll-up," custom watch settings

### **9. Observability & Success Metrics**
- **Problem:** No counters or roll-ups to prove system works
- **Missing:** Metrics collection and failure analysis
- **Need:** Tiny metrics.json or weekly capsule showing #alerts, #actions, #PRs merged, failure causes

### **10. CI ↔ MP Boundary**
- **Problem:** No clear guardrail between CI and Master Portfolio
- **Missing:** Explicit reminder that none of this promotes to MP
- **Need:** "CI-only paths" allowlist, manual MP promotion process

## 🔧 GitHub Mobile Limitations (Reality Check)

### **What GitHub Mobile Actually Provides:**
- **Basic offline viewing** - Can view issues without internet
- **Push notifications** - Real-time alerts for issues and PRs
- **Photo attachments** - Can attach photos to issues
- **Comment creation** - Can create and edit comments
- **Basic issue management** - Can create, edit, and close issues

### **What GitHub Mobile Does NOT Provide:**
- **True offline editing** - Limited offline capabilities
- **Native camera integration** - Must use device's photo picker
- **GPS tagging** - No location services integration
- **Voice recording** - No native voice memo capability
- **Barcode scanning** - No QR/barcode scanning
- **Advanced file management** - Limited file organization

## 📊 Realistic Success Metrics (Measured, Not Aspirational)

### **Jobs Radar (Current Reality):**
- **Issue Creation Time:** ~2 minutes (manual process)
- **Mobile Accessibility:** 80% (GitHub mobile app limitations)
- **Automation Level:** 40% (basic automation, manual intervention required)
- **User Satisfaction:** "Looks pretty good" (positive but not quantified)

### **Field Agent (Target Reality):**
- **Capture Time:** Target ≤60s (not yet achieved)
- **Processing Success:** Target 95% (not yet measured)
- **Offline Capability:** Target basic offline (GitHub mobile limitations)
- **Error Rate:** Target ≤5% (not yet measured)

## 🎯 Corrected Implementation Priorities

### **High Priority (Fix Real Pain Points):**
1. **Auto-merge rules** - Fix checks not attaching
2. **Idempotency handling** - Prevent duplicate actions
3. **Snooze state management** - Persistent snooze storage
4. **Attachment handling** - Size limits and EXIF scrubbing
5. **Error handling** - Precise error messages and recovery

### **Medium Priority (Enhance Existing):**
1. **Token management** - Secure storage and rotation
2. **Noise management** - Threshold rules and auto-close
3. **Observability** - Metrics collection and analysis
4. **Index stability** - Stable ID mapping
5. **Frontmatter validation** - Hard-rail schema enforcement

### **Low Priority (Future Enhancements):**
1. **Voice recording** - Custom mobile app development
2. **GPS tagging** - Location services integration
3. **Barcode scanning** - QR/barcode scanning
4. **AI processing** - Intelligent data extraction
5. **Advanced automation** - Complex workflow automation

## 🚨 Guardrails & Constraints

### **GitHub-Native Limitations:**
- **No custom mobile app** - Must work within GitHub's mobile interface
- **Limited offline capabilities** - GitHub mobile has basic offline support only
- **No native device features** - Camera, GPS, voice require custom development
- **API rate limits** - GitHub API has usage restrictions
- **Permission constraints** - Limited by GitHub's permission model

### **CI-Only Boundary:**
- **No MP promotion** - All automation stays in CI, manual promotion to Master Portfolio
- **Path allowlist** - Only specific directories can be modified
- **Content restrictions** - No sensitive data in filenames or public areas
- **Review requirements** - All changes require review before merge

## 📋 Next Steps (Reality-Based)

### **Immediate Actions:**
1. **Fix auto-merge issues** - Implement proper check attachment
2. **Add idempotency handling** - Prevent duplicate actions
3. **Implement snooze storage** - Persistent state management
4. **Add attachment rules** - Size limits and privacy protection
5. **Improve error handling** - Clear error messages and recovery

### **Documentation Updates:**
1. **Remove over-claims** - Update capsules to reflect reality
2. **Add operational constraints** - Document GitHub limitations
3. **Create troubleshooting guides** - Common issues and solutions
4. **Add metrics collection** - Measure actual performance
5. **Document guardrails** - CI boundaries and restrictions

---

## 🎯 Key Takeaway

**The systems work, but they're not as automated or capable as initially claimed. Focus on fixing the real operational pain points before adding new features. GitHub-native approach is solid, but acknowledge its limitations.**

---

*Reality Check - Career Intelligence Space*
*Status: Draft - Operational Constraints Documentation*
