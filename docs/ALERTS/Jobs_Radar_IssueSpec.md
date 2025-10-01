---
project: Career Intelligence Space
type: spec
status: draft
tags: [jobs_radar, comment_grammar, receipts, idempotency, stable_ids]
updated: 2025-09-30
---

# Jobs Radar - Comment Grammar & Receipts Specification
**Status:** Draft - Operational Specification  
**Date:** 2025-09-30

## 🎯 Purpose

This document defines the authoritative comment grammar, receipt formats, and idempotency handling for the Jobs Radar Intelligence System. It addresses the operational pain points of duplicate actions, index stability, and clear user feedback.

## 📝 Comment Grammar (Authoritative)

### **Core Commands:**
```
apply <idx|id>          # Apply to job by index or stable ID
research <idx|id>       # Research job by index or stable ID  
snooze <idx|id> <Nd>    # Snooze job for N days
ignore <idx|id>         # Ignore job permanently
```

### **Examples:**
```
apply 1                 # Apply to first job in list
apply crmg-26-28        # Apply to job with stable ID
research 2              # Research second job
research liberty-255229 # Research job with stable ID
snooze 3 3d             # Snooze third job for 3 days
snooze bluestone-pt-30 7d # Snooze job for 7 days
ignore 4                # Ignore fourth job
```

### **Index vs. Stable ID:**
- **Index:** Position in current list (1, 2, 3, etc.) - can change if list updates
- **Stable ID:** Permanent identifier (crmg-26-28, liberty-255229) - never changes

## 🏷️ Stable ID Generation

### **Jobs Radar Stable IDs:**
```
hash(platform + title + company + city)
```

### **Examples:**
- **Platform:** MultifamilyNW
- **Title:** Maintenance Tech II  
- **Company:** CRMG
- **City:** Portland
- **Stable ID:** `crmg-26-28` (shortened hash)

### **Field Agent Stable IDs:**
```
YYYYMMDD_HHMM_LOC_TAG
```

### **Examples:**
- **Date:** 2025-09-30
- **Time:** 14:32
- **Location:** PDX-NE
- **Tag:** Plumbing
- **Stable ID:** `20250930_1432_PDX-NE_Plumbing`

## 📋 Receipt Examples

### **Successful Actions:**
```
✅ Applied to CRMG — Maintenance Tech II — $26-28/hr
   • Company research stub created: 06_COMPANY/CRMG/research.md
   • Negotiation tracker opened: 05_NEGOTIATION/CRMG.md
   • Follow-up scheduled: +3 days
   • PR #123 created with changes
```

```
✅ Research initiated for Liberty Group — Certified Maintenance Tech
   • Company research stub created: 06_COMPANY/Liberty/research.md
   • Added to weekly review list
   • PR #124 created with changes
```

```
✅ Snoozed Bluestone — PT Facilities Tech until 2025-10-03
   • Added to snooze store: data/jobs/snoozed.jsonl
   • Will reappear in scan on 2025-10-03
   • PR #125 created with changes
```

### **Idempotency Messages:**
```
ℹ️ CRMG — Maintenance Tech II already applied today — ignored
   • Previous action: 2025-09-30 08:15
   • No duplicate PR created
```

```
ℹ️ Liberty Group — Certified Maintenance Tech already researched — ignored
   • Previous action: 2025-09-30 08:20
   • No duplicate PR created
```

### **Error Messages:**
```
❌ Invalid command: "apply 5" — only 3 jobs in current list
   • Available indices: 1, 2, 3
   • Available IDs: crmg-26-28, liberty-255229, bluestone-pt-30
```

```
❌ Job not found: "apply xyz-123" — ID not in current scan
   • Available IDs: crmg-26-28, liberty-255229, bluestone-pt-30
```

```
❌ Processing failed: YAML validation error
   • Error: Missing required field 'company' in job data
   • PR #126 created with error details
   • Please try again or contact support
```

## 🔄 Idempotency Handling

### **Duplicate Action Prevention:**
1. **Check action history** - Look for previous actions on same job_id
2. **Time window** - Within 24 hours = duplicate, ignore
3. **Action type** - Same action type = duplicate, ignore
4. **Different action type** - Allow (e.g., research after apply)

### **Implementation:**
```python
def check_idempotency(job_id, action, timestamp):
    # Check if same action within 24 hours
    recent_actions = get_recent_actions(job_id, timestamp - 24*3600)
    
    for recent in recent_actions:
        if recent.action == action:
            return {
                "status": "duplicate",
                "message": f"ℹ️ {job_id} already {action}ed today — ignored",
                "previous_action": recent.timestamp
            }
    
    return {"status": "new", "message": "✅ Processing..."}
```

## 📊 Snooze State Management

### **Snooze Store Schema:**
```json
{
  "job_id": "crmg-26-28",
  "until": "2025-10-03",
  "snoozed_at": "2025-09-30T14:32:00Z",
  "reason": "waiting_for_license"
}
```

### **Snooze Filter Rule:**
```python
def filter_snoozed_jobs(jobs, snooze_store):
    active_jobs = []
    
    for job in jobs:
        if job.job_id in snooze_store:
            snooze_until = snooze_store[job.job_id]["until"]
            if datetime.now() < snooze_until:
                continue  # Skip snoozed job
        
        active_jobs.append(job)
    
    return active_jobs
```

## 🎯 Index Stability Solution

### **Render Format:**
```
1. CRMG — Maintenance Tech II — $26-28/hr 〔id: crmg-26-28〕
2. Liberty Group — Certified Maintenance Tech — $28-30/hr 〔id: liberty-255229〕
3. Bluestone — PT Facilities Tech — $24-26/hr 〔id: bluestone-pt-30〕
```

### **Command Support:**
- **Index commands:** `apply 1`, `research 2`, `snooze 3 3d`
- **ID commands:** `apply crmg-26-28`, `research liberty-255229`
- **Mixed commands:** `apply 1` and `research liberty-255229` in same comment

### **Index Mapping:**
```python
def map_index_to_id(index, job_list):
    if 1 <= index <= len(job_list):
        return job_list[index - 1].stable_id
    else:
        raise ValueError(f"Invalid index: {index}")
```

## 🔧 Error Handling

### **Validation Rules:**
1. **Index bounds** - Must be 1 ≤ index ≤ list_length
2. **Stable ID format** - Must match expected pattern
3. **Action validity** - Must be apply/research/snooze/ignore
4. **Snooze duration** - Must be positive integer + 'd'

### **Error Response Format:**
```
❌ <Error Type>: <Description>
   • <Helpful context>
   • <Available options>
   • <Next steps>
```

### **Common Error Scenarios:**
- **Invalid index:** "apply 5" when only 3 jobs
- **Invalid ID:** "apply xyz-123" when ID doesn't exist
- **Invalid action:** "delete 1" when action not supported
- **Invalid duration:** "snooze 1 3x" when format incorrect
- **Processing failure:** YAML validation, file system errors

## 📱 Mobile Optimization

### **Comment Creation:**
- **Voice-to-text** - Use device's voice-to-text for comments
- **Quick replies** - Pre-defined comment templates
- **Auto-complete** - Suggest job IDs and actions
- **Error prevention** - Validate before sending

### **Receipt Display:**
- **Push notifications** - Immediate receipt via GitHub mobile
- **Rich formatting** - Emojis and formatting for clarity
- **Action links** - Direct links to created PRs and files
- **Status updates** - Real-time status in issue comments

## 🎯 Success Metrics

### **Comment Processing:**
- **Response time:** ≤30 seconds from comment to receipt
- **Success rate:** ≥95% successful processing
- **Error rate:** ≤5% processing failures
- **Idempotency:** 100% duplicate prevention

### **User Experience:**
- **Command clarity:** 100% of commands parse correctly
- **Receipt clarity:** 100% of receipts provide actionable feedback
- **Error recovery:** 100% of errors provide clear next steps
- **Mobile compatibility:** 100% of features work on GitHub mobile

---

## 🎯 Key Takeaways

1. **Stable IDs prevent index drift** - Always show both index and stable ID
2. **Idempotency prevents duplicates** - Check action history before processing
3. **Clear receipts build confidence** - Provide detailed feedback and next steps
4. **Error handling guides users** - Always provide helpful context and options

---

*Jobs Radar Comment Grammar & Receipts Specification - Career Intelligence Space*
*Status: Draft - Operational Specification*
