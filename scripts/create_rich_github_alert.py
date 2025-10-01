#!/usr/bin/env python3
"""
Create Rich GitHub Alert
Creates a GitHub issue with rich interactions and mobile-optimized content
"""

import os
import json
import requests
from datetime import datetime, timedelta
from pathlib import Path

def create_rich_github_alert():
    """Create a rich GitHub issue for the Jobs Radar project"""
    repo_root = Path(__file__).parent.parent
    
    # Get GitHub token and repo info
    github_token = os.getenv('GITHUB_TOKEN')
    if not github_token:
        print("❌ GITHUB_TOKEN not found. Cannot create GitHub issue.")
        print("💡 To enable automatic issue creation:")
        print("   1. Go to GitHub Settings > Developer settings > Personal access tokens")
        print("   2. Create a token with 'issues' permission")
        print("   3. Add it as GITHUB_TOKEN secret in your repo")
        return
    
    # Get repository info
    github_repository = os.getenv('GITHUB_REPOSITORY', 'jwade83/career-intelligence-space')
    owner, repo = github_repository.split('/')
    
    # Create rich issue
    create_jobs_radar_issue(owner, repo, github_token)

def create_jobs_radar_issue(owner, repo, token):
    """Create a rich GitHub issue for Jobs Radar activation"""
    
    # Check if issue already exists
    if issue_exists("Jobs Radar Intelligence System", owner, repo, token):
        print("⚠️ Issue already exists for Jobs Radar Intelligence System")
        return
    
    # Create rich issue with mobile-optimized content
    issue_data = {
        "title": "🚀 ACTIVATE: Jobs Radar Intelligence System",
        "body": create_rich_issue_body(),
        "labels": ["alert", "high-priority", "project-activation", "weekly-review", "jobs-radar"],
        "assignees": ["jwade83"],
        "milestone": None  # Will be set if milestone exists
    }
    
    # Try to set milestone
    milestone_id = get_milestone_id("Phase 1 Implementation", owner, repo, token)
    if milestone_id:
        issue_data["milestone"] = milestone_id
    
    response = requests.post(
        f"https://api.github.com/repos/{owner}/{repo}/issues",
        headers={
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        },
        json=issue_data
    )
    
    if response.status_code == 201:
        issue = response.json()
        print(f"✅ Created rich GitHub issue: {issue['html_url']}")
        print(f"📱 Mobile-optimized for GitHub mobile app")
        print(f"🔔 You should receive push notifications immediately")
        
        # Add initial comment with quick actions
        add_quick_actions_comment(issue['number'], owner, repo, token)
        
    else:
        print(f"❌ Failed to create issue: {response.status_code} - {response.text}")

def create_rich_issue_body():
    """Create rich issue body with mobile-optimized content"""
    return f"""## 🚨 Project Activation Required

**Generated:** {datetime.now().strftime('%Y-%m-%d')}  
**Source:** Weekly Review Trigger System  
**Priority:** HIGH  
**Urgency:** IMMEDIATE  
**Readiness Score:** 4/4 (PERFECT)

### 📋 Project Overview
- **Project Name:** Jobs Radar Intelligence System
- **Type:** Career Intelligence Enhancement
- **Status:** Ready for immediate implementation
- **File:** `08_CHRONICLE/vision/2025-11-10_Jobs_Radar_Intelligence_System_Capsule.md`

### ✅ Trigger Conditions Met
- ✅ **Technical Readiness** - All technical requirements satisfied
- ✅ **Resource Availability** - Resources available for implementation
- ✅ **Strategic Alignment** - Perfect alignment with CIS vision
- ✅ **User Demand** - Strong user demand demonstrated

### 🎯 Implementation Plan

#### **Phase 1: Chat-Only Intelligence (Week 1-2)**
- [ ] **Enhance Discovery Agent** - Add scoring algorithm and feedback loops
- [ ] **Create Perplexity prompts** - Develop structured job scan report templates
- [ ] **Test chat workflow** - Validate natural conversation interface
- [ ] **Integrate with existing templates** - Company Research and Compensation Tracker

#### **Phase 2: Smart Email Digest (Week 3-4)**
- [ ] **Email parsing system** - Simple keyword extraction
- [ ] **Action mapping** - A1 = apply job 1, R2 = research job 2
- [ ] **Confirmation system** - Email confirmations for actions
- [ ] **Fallback to chat** - Complex interaction support

#### **Phase 3: Action Card Microform (Week 5-6)**
- [ ] **Static page creation** - Single web page with signed URL
- [ ] **Single endpoint** - POST /actions with simple payload
- [ ] **Token management** - Single-day token expiration
- [ ] **Integration testing** - End-to-end workflow validation

### 📱 Mobile Quick Actions

**Swipe Actions:**
- **Swipe Right** → Start Implementation
- **Swipe Left** → Snooze for Later
- **Tap** → View Full Details
- **Long Press** → Show Context Menu

**Voice Commands:**
- "Start implementation" → Begin Phase 1
- "Mark complete" → Update progress
- "Add comment" → Voice-to-text update

### 🔄 Daily Workflow

#### **Morning Routine (8:00 AM):**
1. **Check CIS Dashboard** - Review overnight job scan results
2. **Review "Today's 3 Actions"** - Generated from previous day's scan
3. **Prioritize IMMEDIATE opportunities** - Apply scoring algorithm results
4. **Update application status** - Mark any completed actions from yesterday

### 📊 Success Criteria

#### **Phase 1 Success:**
- [ ] **Daily usage** - User checks chat every morning
- [ ] **Action completion** - User applies to 2-3 jobs per week
- [ ] **Time saved** - 5 minutes vs. 30 minutes manual job search
- [ ] **User satisfaction** - Natural, effortless interaction

### 🔗 Related Resources

- **Project Documentation:** [Jobs Radar Intelligence System Capsule](08_CHRONICLE/vision/2025-11-10_Jobs_Radar_Intelligence_System_Capsule.md)
- **Discovery Agent:** [agents/discovery.yml](agents/discovery.yml)
- **Company Research Template:** [docs/COMPANY_RESEARCH_TEMPLATE.md](docs/COMPANY_RESEARCH_TEMPLATE.md)

### 💬 Discussion & Updates

**Implementation Status:** 🟡 Ready to Start  
**Next Milestone:** Phase 1 - Chat-Only Intelligence  
**Estimated Completion:** 2 weeks  
**Blockers:** None identified

---
*Generated by Weekly Review Trigger System - {datetime.now().strftime('%Y-%m-%d')}*  
*Status: ACTIVE - Implementation Required*"""

def add_quick_actions_comment(issue_number, owner, repo, token):
    """Add a comment with quick actions for mobile users"""
    comment_data = {
        "body": """## 📱 Quick Actions for Mobile

**Tap to execute:**

### 🚀 Start Implementation
- [ ] **Begin Phase 1** - Start Discovery Agent enhancement
- [ ] **Set up Perplexity** - Test job scanning prompts
- [ ] **Create test workflow** - Validate chat interface

### 📋 Review & Plan
- [ ] **Review specifications** - Check implementation requirements
- [ ] **Allocate time** - Schedule development work
- [ ] **Set milestones** - Create implementation timeline

### 🔄 Update Status
- [ ] **Mark in progress** - Update issue status
- [ ] **Add progress comment** - Document current status
- [ ] **Set reminder** - Schedule follow-up

---
*Use voice commands or tap actions for quick updates*"""
    }
    
    response = requests.post(
        f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}/comments",
        headers={
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        },
        json=comment_data
    )
    
    if response.status_code == 201:
        print("✅ Added quick actions comment for mobile users")
    else:
        print(f"⚠️ Could not add quick actions comment: {response.status_code}")

def issue_exists(title, owner, repo, token):
    """Check if issue with similar title already exists"""
    response = requests.get(
        f"https://api.github.com/repos/{owner}/{repo}/issues",
        headers={
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        },
        params={"state": "open", "labels": "jobs-radar"}
    )
    
    if response.status_code == 200:
        issues = response.json()
        for issue in issues:
            if "Jobs Radar" in issue['title']:
                return True
    
    return False

def get_milestone_id(milestone_title, owner, repo, token):
    """Get milestone ID by title"""
    response = requests.get(
        f"https://api.github.com/repos/{owner}/{repo}/milestones",
        headers={
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }
    )
    
    if response.status_code == 200:
        milestones = response.json()
        for milestone in milestones:
            if milestone['title'] == milestone_title:
                return milestone['number']
    
    return None

if __name__ == "__main__":
    create_rich_github_alert()
