#!/usr/bin/env python3
"""
Create Weekly Review Alert
Generates a visible alert file for weekly review results
"""

import os
import json
from datetime import datetime, timedelta
from pathlib import Path

def create_weekly_alert():
    """Create a visible weekly review alert"""
    repo_root = Path(__file__).parent.parent
    results_file = repo_root / "08_CHRONICLE" / "weekly_review_results.json"
    
    if not results_file.exists():
        print("❌ No weekly review results found. Run weekly_review_trigger.py first.")
        return
    
    # Load results
    with open(results_file, 'r') as f:
        results = json.load(f)
    
    # Create alert filename
    today = datetime.now().strftime("%Y-%m-%d")
    alert_file = repo_root / "08_CHRONICLE" / "weekly" / f"{today}_weekly_review_trigger_alert.md"
    
    # Generate alert content
    alert_content = generate_alert_content(results, today)
    
    # Write alert file
    with open(alert_file, 'w') as f:
        f.write(alert_content)
    
    print(f"✅ Weekly review alert created: {alert_file}")
    print(f"📊 Projects evaluated: {results['projects_evaluated']}")
    print(f"🚀 Projects ready: {len(results['projects_ready'])}")
    print(f"💡 Recommendations: {len(results['recommendations'])}")

def generate_alert_content(results, date):
    """Generate alert content based on results"""
    
    # Count projects ready for activation
    projects_ready = len(results['projects_ready'])
    projects_evaluated = results['projects_evaluated']
    
    # Determine alert priority
    if projects_ready > 0:
        priority = "high"
        urgency = "immediate"
        alert_icon = "🚨"
    else:
        priority = "medium"
        urgency = "normal"
        alert_icon = "📋"
    
    content = f"""---
project: Career Intelligence Space
type: alert
status: active
tags: [weekly_review, trigger_alert, project_activation]
updated: {date}
alert_type: project_activation
priority: {priority}
urgency: {urgency}
---

# {alert_icon} Weekly Review Trigger Alert - Project Activation Required

**Date:** {date}  
**Alert Type:** Project Activation Required  
**Priority:** {priority.upper()}  
**Urgency:** {urgency.upper()}

---

## 🎯 ALERT SUMMARY

**{projects_ready} PROJECT{'S' if projects_ready != 1 else ''} READY FOR IMMEDIATE ACTIVATION**  
**{projects_evaluated} PROJECT{'S' if projects_evaluated != 1 else ''} EVALUATED**  
**{len(results['priority_changes'])} PRIORITY CHANGE{'S' if len(results['priority_changes']) != 1 else ''}**

---

## 🚀 IMMEDIATE ACTION REQUIRED

"""
    
    # Add projects ready for activation
    if results['projects_ready']:
        for project in results['projects_ready']:
            project_name = project['project']
            if project_name == 'Unknown':
                project_name = "Jobs Radar Intelligence System"  # Default name
            
            content += f"""### **{project_name} - ACTIVATE NOW**
- **Readiness Score:** {project['readiness_score']}/4 (PERFECT)
- **Status:** Ready for immediate implementation
- **File:** `{project['file'].split('/')[-1]}`

#### **Trigger Conditions Met:**
"""
            for condition, met in project['trigger_conditions'].items():
                status = "✅" if met else "❌"
                condition_name = condition.replace('_', ' ').title()
                content += f"- {status} **{condition_name}** - {'Satisfied' if met else 'Not met'}\n"
            
            content += "\n#### **Recommended Actions:**\n"
            content += "1. **Review implementation requirements** - Check Phase 1 specifications\n"
            content += "2. **Allocate resources and timeline** - Schedule implementation work\n"
            content += "3. **Begin Phase 1 implementation** - Start chat-only intelligence system\n"
            content += "4. **Set up monitoring and feedback loops** - Track progress and outcomes\n\n"
    else:
        content += "No projects ready for immediate activation at this time.\n\n"
    
    # Add additional recommendations
    content += "## 📋 ADDITIONAL RECOMMENDATIONS\n\n"
    
    if results['recommendations']:
        for rec in results['recommendations']:
            if rec['recommendation'] != 'activate_project':
                project_name = rec['project']
                if project_name == 'Unknown':
                    project_name = "Research Task"
                
                content += f"""### **{project_name} - {rec['recommendation'].replace('_', ' ').title()}**
- **Readiness Score:** {rec['readiness_score']}/4 ({'High' if rec['readiness_score'] >= 3 else 'Moderate' if rec['readiness_score'] >= 2 else 'Low'})
- **Status:** {rec['recommendation'].replace('_', ' ').title()}
- **Action:** Review and take appropriate action\n\n"""
    else:
        content += "No additional recommendations at this time.\n\n"
    
    # Add next steps
    content += f"""## 🔄 NEXT STEPS

### **Immediate (This Week):**
1. **Review this alert** - Assess all recommendations
2. **Activate ready projects** - Begin implementation of high-readiness projects
3. **Review pending projects** - Address moderate-readiness items

### **This Month:**
1. **Monitor progress** - Track implementation milestones
2. **Gather feedback** - Collect user feedback on new features
3. **Plan next phase** - Prepare for future enhancements

---

## 📊 SYSTEM STATUS

### **Projects Evaluated:** {projects_evaluated}
- **Vision Capsules:** {len([p for p in results['projects_ready'] if 'vision' in p['file']])}
- **Task Queue Items:** {projects_evaluated - len([p for p in results['projects_ready'] if 'vision' in p['file']])}

### **Readiness Distribution:**
- **Ready for Activation:** {projects_ready} ({int(projects_ready/projects_evaluated*100) if projects_evaluated > 0 else 0}%)
- **Needs Review:** {projects_evaluated - projects_ready} ({int((projects_evaluated - projects_ready)/projects_evaluated*100) if projects_evaluated > 0 else 0}%)
- **Maintain Status:** 0 (0%)

### **Priority Changes:** {len(results['priority_changes'])}
- {'No priority changes recommended at this time.' if len(results['priority_changes']) == 0 else 'Priority changes recommended - see details above.'}

---

## 🔔 ALERT NOTIFICATION

**This alert was generated by the Weekly Review Trigger System**  
**Next Review:** {(datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d')} (Next Friday)  
**Alert Status:** ACTIVE - Requires user action  
**Dismissal:** Mark as resolved when all recommendations are addressed

---

## 📁 RELATED FILES

- **Full Results:** `08_CHRONICLE/weekly_review_results.json`
- **Trigger Script:** `scripts/weekly_review_trigger.py`
- **Alert History:** `08_CHRONICLE/weekly/` (previous alerts)

---

*Weekly Review Trigger Alert - Career Intelligence Space*  
*Generated: {date}*  
*Status: ACTIVE - Action Required*"""
    
    return content

if __name__ == "__main__":
    create_weekly_alert()
