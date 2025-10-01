---
project: Career Intelligence Space
type: spec
status: draft
tags: [snooze, state_management, persistent_storage, filter_rules]
updated: 2025-09-30
---

# Snooze Semantics - Persistent State Management
**Status:** Draft - Snooze State Specification  
**Date:** 2025-09-30

## 🎯 Purpose

This document defines how snooze state is managed in the Jobs Radar system, including where snooze_until lives, how the next day's scan honors it, and the implementation of the tiny store with filter rules.

## 📊 Snooze Store Schema

### **File Location:**
```
data/jobs/snoozed.jsonl
```

### **Schema:**
```json
{
  "job_id": "crmg-26-28",
  "until": "2025-10-03",
  "snoozed_at": "2025-09-30T14:32:00Z",
  "reason": "waiting_for_license",
  "original_priority": "IMMEDIATE",
  "snoozed_by": "jwade83"
}
```

### **Field Definitions:**
- **job_id:** Stable job identifier (hash of platform+title+company+city)
- **until:** Date when job should reappear (YYYY-MM-DD format)
- **snoozed_at:** Timestamp when snooze was applied (ISO 8601)
- **reason:** Optional reason for snoozing (for context)
- **original_priority:** Priority level when snoozed (IMMEDIATE/HIGH/MEDIUM)
- **snoozed_by:** User who applied the snooze

## 🔄 Snooze Filter Rule Implementation

### **Scanner Integration:**
```python
def filter_snoozed_jobs(jobs, snooze_store_path="data/jobs/snoozed.jsonl"):
    """
    Filter out jobs that are currently snoozed
    """
    # Load snooze store
    snoozed_jobs = load_snooze_store(snooze_store_path)
    
    # Get current date
    today = datetime.now().date()
    
    # Filter active jobs
    active_jobs = []
    for job in jobs:
        if job.job_id in snoozed_jobs:
            snooze_until = datetime.strptime(snoozed_jobs[job.job_id]["until"], "%Y-%m-%d").date()
            if today < snooze_until:
                # Job is still snoozed
                continue
            else:
                # Snooze period expired, remove from store
                remove_from_snooze_store(job.job_id, snooze_store_path)
        
        active_jobs.append(job)
    
    return active_jobs

def load_snooze_store(snooze_store_path):
    """
    Load snooze store from JSONL file
    """
    snoozed_jobs = {}
    
    if not os.path.exists(snooze_store_path):
        return snoozed_jobs
    
    with open(snooze_store_path, 'r') as f:
        for line in f:
            if line.strip():
                snooze_entry = json.loads(line)
                snoozed_jobs[snooze_entry["job_id"]] = snooze_entry
    
    return snoozed_jobs

def remove_from_snooze_store(job_id, snooze_store_path):
    """
    Remove expired snooze entry from store
    """
    # Read all entries
    entries = []
    with open(snooze_store_path, 'r') as f:
        for line in f:
            if line.strip():
                entry = json.loads(line)
                if entry["job_id"] != job_id:
                    entries.append(entry)
    
    # Write back without the expired entry
    with open(snooze_store_path, 'w') as f:
        for entry in entries:
            f.write(json.dumps(entry) + '\n')
```

## 📝 Snooze Command Processing

### **Command Format:**
```
snooze <idx|id> <Nd>
```

### **Examples:**
```
snooze 1 3d        # Snooze first job for 3 days
snooze crmg-26-28 7d  # Snooze job for 7 days
snooze 2 1d        # Snooze second job for 1 day
```

### **Processing Logic:**
```python
def process_snooze_command(job_id, duration_str, user_id="jwade83"):
    """
    Process snooze command and update snooze store
    """
    # Parse duration
    duration_days = parse_duration(duration_str)  # "3d" -> 3
    
    # Calculate until date
    until_date = (datetime.now() + timedelta(days=duration_days)).strftime("%Y-%m-%d")
    
    # Create snooze entry
    snooze_entry = {
        "job_id": job_id,
        "until": until_date,
        "snoozed_at": datetime.now().isoformat(),
        "reason": "user_requested",
        "original_priority": get_job_priority(job_id),
        "snoozed_by": user_id
    }
    
    # Add to snooze store
    add_to_snooze_store(snooze_entry)
    
    return {
        "status": "success",
        "message": f"✅ Snoozed {job_id} until {until_date}",
        "until_date": until_date
    }

def parse_duration(duration_str):
    """
    Parse duration string like "3d", "7d", "1d"
    """
    if duration_str.endswith('d'):
        return int(duration_str[:-1])
    else:
        raise ValueError(f"Invalid duration format: {duration_str}")

def add_to_snooze_store(snooze_entry, snooze_store_path="data/jobs/snoozed.jsonl"):
    """
    Add snooze entry to store
    """
    # Ensure directory exists
    os.makedirs(os.path.dirname(snooze_store_path), exist_ok=True)
    
    # Append to JSONL file
    with open(snooze_store_path, 'a') as f:
        f.write(json.dumps(snooze_entry) + '\n')
```

## 🔍 Snooze State Queries

### **Check Snooze Status:**
```python
def get_snooze_status(job_id, snooze_store_path="data/jobs/snoozed.jsonl"):
    """
    Get current snooze status for a job
    """
    snoozed_jobs = load_snooze_store(snooze_store_path)
    
    if job_id not in snoozed_jobs:
        return {"status": "active", "message": "Job is not snoozed"}
    
    snooze_entry = snoozed_jobs[job_id]
    until_date = datetime.strptime(snooze_entry["until"], "%Y-%m-%d").date()
    today = datetime.now().date()
    
    if today < until_date:
        return {
            "status": "snoozed",
            "until": snooze_entry["until"],
            "reason": snooze_entry.get("reason", "user_requested"),
            "days_remaining": (until_date - today).days
        }
    else:
        return {"status": "expired", "message": "Snooze period has expired"}
```

### **List All Snoozed Jobs:**
```python
def list_snoozed_jobs(snooze_store_path="data/jobs/snoozed.jsonl"):
    """
    List all currently snoozed jobs
    """
    snoozed_jobs = load_snooze_store(snooze_store_path)
    today = datetime.now().date()
    
    active_snoozes = []
    for job_id, entry in snoozed_jobs.items():
        until_date = datetime.strptime(entry["until"], "%Y-%m-%d").date()
        if today < until_date:
            active_snoozes.append({
                "job_id": job_id,
                "until": entry["until"],
                "reason": entry.get("reason", "user_requested"),
                "days_remaining": (until_date - today).days
            })
    
    return active_snoozes
```

## 📊 Snooze Analytics

### **Weekly Snooze Report:**
```python
def generate_snooze_report(snooze_store_path="data/jobs/snoozed.jsonl"):
    """
    Generate weekly report of snooze activity
    """
    snoozed_jobs = load_snooze_store(snooze_store_path)
    
    # Count by reason
    reason_counts = {}
    for entry in snoozed_jobs.values():
        reason = entry.get("reason", "user_requested")
        reason_counts[reason] = reason_counts.get(reason, 0) + 1
    
    # Count by priority
    priority_counts = {}
    for entry in snoozed_jobs.values():
        priority = entry.get("original_priority", "UNKNOWN")
        priority_counts[priority] = priority_counts.get(priority, 0) + 1
    
    return {
        "total_snoozed": len(snoozed_jobs),
        "by_reason": reason_counts,
        "by_priority": priority_counts,
        "report_date": datetime.now().isoformat()
    }
```

## 🔧 Integration Points

### **Jobs Radar Scanner:**
```python
def run_jobs_scan():
    """
    Run daily jobs scan with snooze filtering
    """
    # Get raw job data
    raw_jobs = fetch_job_data()
    
    # Filter out snoozed jobs
    active_jobs = filter_snoozed_jobs(raw_jobs)
    
    # Process active jobs
    processed_jobs = process_jobs(active_jobs)
    
    # Generate report
    report = generate_jobs_report(processed_jobs)
    
    return report
```

### **Issue Creation:**
```python
def create_jobs_radar_issue(jobs):
    """
    Create Jobs Radar issue with snooze-aware job list
    """
    # Filter snoozed jobs
    active_jobs = filter_snoozed_jobs(jobs)
    
    # Only create issue if there are IMMEDIATE jobs
    immediate_jobs = [job for job in active_jobs if job.priority == "IMMEDIATE"]
    
    if len(immediate_jobs) >= 1:
        create_issue(immediate_jobs)
    else:
        # Log that no issue was created due to snooze filtering
        log_no_issue_created("All IMMEDIATE jobs are snoozed")
```

## 🎯 Snooze Receipt Examples

### **Successful Snooze:**
```
✅ Snoozed CRMG — Maintenance Tech II until 2025-10-03
   • Reason: waiting_for_license
   • Original priority: IMMEDIATE
   • Will reappear in scan on 2025-10-03
   • PR #127 created with snooze store update
```

### **Snooze Status Check:**
```
ℹ️ CRMG — Maintenance Tech II is snoozed until 2025-10-03
   • Reason: waiting_for_license
   • Days remaining: 3
   • Original priority: IMMEDIATE
```

### **Snooze Expired:**
```
ℹ️ CRMG — Maintenance Tech II snooze expired
   • Was snoozed until 2025-10-03
   • Now active and will appear in next scan
   • Removed from snooze store
```

## 🚨 Error Handling

### **Invalid Duration:**
```
❌ Invalid snooze duration: "3x"
   • Valid formats: 1d, 3d, 7d, 14d
   • Examples: snooze 1 3d, snooze crmg-26-28 7d
```

### **Job Not Found:**
```
❌ Job not found: "apply xyz-123"
   • Available IDs: crmg-26-28, liberty-255229, bluestone-pt-30
```

### **Snooze Store Error:**
```
❌ Failed to update snooze store
   • Error: Permission denied writing to data/jobs/snoozed.jsonl
   • Please check file permissions and try again
```

## 📱 Mobile Considerations

### **Snooze Interface:**
- **Quick durations** - Pre-defined buttons: 1d, 3d, 7d, 14d
- **Custom duration** - Text input for specific days
- **Reason selection** - Dropdown with common reasons
- **Confirmation** - Show until date before confirming

### **Snooze Management:**
- **View snoozed jobs** - List of currently snoozed jobs
- **Modify snooze** - Change duration or reason
- **Cancel snooze** - Remove from snooze store
- **Snooze history** - Track snooze patterns

---

## 🎯 Key Takeaways

1. **Persistent storage** - Snooze state survives across scans and restarts
2. **Automatic cleanup** - Expired snoozes are automatically removed
3. **Filter integration** - Scanner automatically respects snooze state
4. **Analytics ready** - Snooze data can be analyzed for patterns
5. **Mobile friendly** - Simple interface for snooze management

---

*Snooze Semantics - Career Intelligence Space*
*Status: Draft - Snooze State Specification*
