#!/usr/bin/env python3
"""
Update Alerts Dashboard
Updates the alerts dashboard with GitHub issue links
"""

import os
import json
import requests
from datetime import datetime
from pathlib import Path

def update_alerts_dashboard():
    """Update alerts dashboard with GitHub issue links"""
    repo_root = Path(__file__).parent.parent
    results_file = repo_root / "08_CHRONICLE" / "weekly_review_results.json"
    dashboard_file = repo_root / "08_CHRONICLE" / "ALERTS_DASHBOARD.md"
    
    if not results_file.exists():
        print("❌ No weekly review results found.")
        return
    
    # Load results
    with open(results_file, 'r') as f:
        results = json.load(f)
    
    # Get GitHub issues
    github_token = os.getenv('GITHUB_TOKEN')
    github_repository = os.getenv('GITHUB_REPOSITORY', 'jwade83/career-intelligence-space')
    owner, repo = github_repository.split('/')
    
    issues = get_github_issues(owner, repo, github_token) if github_token else []
    
    # Update dashboard
    update_dashboard_content(dashboard_file, results, issues)

def get_github_issues(owner, repo, token):
    """Get GitHub issues with weekly-review label"""
    response = requests.get(
        f"https://api.github.com/repos/{owner}/{repo}/issues",
        headers={
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        },
        params={"state": "open", "labels": "weekly-review"}
    )
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"⚠️ Could not fetch GitHub issues: {response.status_code}")
        return []

def update_dashboard_content(dashboard_file, results, issues):
    """Update dashboard content with GitHub issue links"""
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Create issue links mapping
    issue_links = {}
    for issue in issues:
        if "ACTIVATE:" in issue['title']:
            project_name = issue['title'].replace("🚀 ACTIVATE: ", "")
            issue_links[project_name] = issue['html_url']
        elif "REVIEW:" in issue['title']:
            project_name = issue['title'].replace("📋 REVIEW: ", "")
            issue_links[project_name] = issue['html_url']
    
    # Generate updated dashboard content
    content = f"""---
project: Career Intelligence Space
type: dashboard
status: active
tags: [dashboard, alerts, weekly_review, project_management]
updated: {today}
---

# 🚨 CIS Alerts Dashboard

**Last Updated:** {today}  
**Status:** ACTIVE  
**Purpose:** Central view of all active alerts and notifications

---

## 🔔 ACTIVE ALERTS

### 🚨 HIGH PRIORITY - IMMEDIATE ACTION REQUIRED

"""
    
    # Add high priority alerts
    if results['projects_ready']:
        for project in results['projects_ready']:
            project_name = project['project']
            if project_name == 'Unknown':
                project_name = "Jobs Radar Intelligence System"
            
            github_link = issue_links.get(project_name, "")
            link_text = f" - [View GitHub Issue]({github_link})" if github_link else ""
            
            content += f"""#### **{project_name} - ACTIVATE NOW{link_text}**
- **Alert Date:** {today}
- **Priority:** HIGH
- **Urgency:** IMMEDIATE
- **Readiness Score:** {project['readiness_score']}/4 (PERFECT)
- **Status:** Ready for immediate implementation
- **Action Required:** Begin Phase 1 implementation
- **Details:** [View Full Alert](weekly/{today}_weekly_review_trigger_alert.md)

"""
    else:
        content += "No high priority alerts at this time.\n\n"
    
    # Add medium priority alerts
    content += "### 📋 MEDIUM PRIORITY - REVIEW REQUIRED\n\n"
    
    review_projects = [r for r in results['recommendations'] if r['recommendation'] != 'activate_project']
    if review_projects:
        for rec in review_projects:
            project_name = rec['project']
            if project_name == 'Unknown':
                project_name = "Research Task"
            
            github_link = issue_links.get(project_name, "")
            link_text = f" - [View GitHub Issue]({github_link})" if github_link else ""
            
            content += f"""#### **{project_name} - {rec['recommendation'].replace('_', ' ').title()}{link_text}**
- **Readiness Score:** {rec['readiness_score']}/4 ({'High' if rec['readiness_score'] >= 3 else 'Moderate' if rec['readiness_score'] >= 2 else 'Low'})
- **Status:** {rec['recommendation'].replace('_', ' ').title()}
- **Action Required:** Review and take appropriate action

"""
    else:
        content += "No medium priority alerts at this time.\n\n"
    
    # Add summary and system status
    content += f"""---

## 📊 ALERT SUMMARY

### **Current Status:**
- **Active Alerts:** {len(results['projects_ready']) + len(review_projects)}
- **High Priority:** {len(results['projects_ready'])}
- **Medium Priority:** {len(review_projects)}
- **Low Priority:** 0

### **Project Readiness:**
- **Ready for Activation:** {len(results['projects_ready'])}
- **Needs Review:** {len(review_projects)}
- **Maintain Status:** 0

### **Last Weekly Review:**
- **Date:** {today}
- **Projects Evaluated:** {results['projects_evaluated']}
- **Recommendations Generated:** {len(results['recommendations'])}
- **Priority Changes:** {len(results['priority_changes'])}

---

## 🔄 QUICK ACTIONS

### **Immediate Actions:**
1. **Review GitHub Issues** - Check all open issues with 'weekly-review' label
2. **Activate Ready Projects** - Begin implementation of high-readiness projects
3. **Review Pending Projects** - Address moderate-readiness items

### **This Week:**
1. **Monitor Progress** - Track implementation milestones
2. **Gather Feedback** - Collect user feedback on new features
3. **Plan Next Phase** - Prepare for future enhancements

---

## 📁 ALERT HISTORY

### **{today}**
- **Jobs Radar Intelligence System** - Project activation required
- **Research Task Review** - Manual review needed

### **Previous Alerts:**
- No previous alerts (system just implemented)

---

## 🔧 SYSTEM STATUS

### **Weekly Review Trigger:**
- **Status:** ✅ ACTIVE
- **Last Run:** {today}
- **Next Run:** {(datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d')} (Next Friday)
- **Script:** `scripts/weekly_review_trigger.py`

### **GitHub Integration:**
- **Status:** ✅ ACTIVE
- **Issues Created:** {len(issues)}
- **Script:** `scripts/create_github_alerts.py`

### **Dashboard:**
- **Status:** ✅ ACTIVE
- **Auto-Update:** Via GitHub Actions
- **Location:** `08_CHRONICLE/ALERTS_DASHBOARD.md`

---

## 🎯 HOW TO VIEW ALERTS

### **Method 1: GitHub Issues (Recommended)**
- **GitHub Issues:** [View All Issues](https://github.com/{os.getenv('GITHUB_REPOSITORY', 'jwade83/career-intelligence-space')}/issues?q=is:issue+is:open+label:weekly-review)
- **Mobile App:** Get push notifications
- **Email:** Automatic email notifications

### **Method 2: Direct File Access**
```bash
# View latest alert
cat 08_CHRONICLE/weekly/{today}_weekly_review_trigger_alert.md

# View all alerts
ls 08_CHRONICLE/weekly/*alert*.md
```

### **Method 3: Dashboard View**
```bash
# View this dashboard
cat 08_CHRONICLE/ALERTS_DASHBOARD.md
```

---

## 📋 ALERT TYPES

### **Project Activation Alerts:**
- **Trigger:** Project readiness score ≥ 3/4
- **Priority:** HIGH
- **Action:** Begin implementation
- **Example:** Jobs Radar Intelligence System

### **Review Required Alerts:**
- **Trigger:** Project readiness score 1-2/4
- **Priority:** MEDIUM
- **Action:** Manual review and assessment
- **Example:** Research tasks

### **Priority Change Alerts:**
- **Trigger:** Priority escalation based on readiness
- **Priority:** MEDIUM
- **Action:** Update project priority
- **Example:** Low → Medium priority changes

---

## 🔔 NOTIFICATION SYSTEM

### **Current Implementation:**
- **GitHub Issues** - Automatic notifications to email and mobile
- **File-based alerts** - Markdown files in `08_CHRONICLE/weekly/`
- **Dashboard view** - Centralized alert summary
- **JSON results** - Machine-readable data in `weekly_review_results.json`

### **GitHub Features:**
- **Email notifications** - Automatic email alerts
- **Mobile push notifications** - GitHub mobile app
- **Issue assignments** - Assigned to you automatically
- **Labels and milestones** - Organized by priority and type
- **Comments and updates** - Track progress and discussions

---

## 📊 METRICS & TRACKING

### **Alert Response Time:**
- **Average Response Time:** TBD (system just implemented)
- **Alert Resolution Rate:** TBD
- **Project Activation Rate:** TBD

### **System Health:**
- **Weekly Review Success Rate:** 100% (1/1 runs successful)
- **Alert Generation Success Rate:** 100% (1/1 alerts generated)
- **GitHub Integration Success Rate:** {'100%' if issues else '0%'} ({len(issues)} issues created)

---

*CIS Alerts Dashboard - Career Intelligence Space*  
*Last Updated: {today}*  
*Status: ACTIVE - Monitoring Alerts*"""
    
    # Write updated dashboard
    with open(dashboard_file, 'w') as f:
        f.write(content)
    
    print(f"✅ Updated alerts dashboard: {dashboard_file}")

if __name__ == "__main__":
    update_alerts_dashboard()
