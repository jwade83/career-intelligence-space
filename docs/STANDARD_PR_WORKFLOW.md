---
project: Career Intelligence Space
type: spec
status: matured
tags: [workflow, pr, standard, team, adoption]
updated: 2025-11-10
adoption_status: active
---

# Standard PR Workflow - Team Adoption

**Status:** ✅ **ACTIVE** - This is the official PR workflow for all team members  
**Source:** Promoted from `docs/reflexive/PR_ROUTE.md` via Stage B Quality Gatekeeper  
**Adoption Date:** 2025-11-10

---

## 🎯 Standard PR Process

### **6-Step PR Workflow**
This is the **official workflow** that all team members must use for creating and managing pull requests.

#### **Step 1: Create PR**
```bash
git checkout -b feat/my-change
git add -A && git commit -m "feat: my change" && git push -u origin feat/my-change
gh pr create --fill
```

#### **Step 2: Enable Auto-Merge**
```bash
PR=$(gh pr view --json number --jq .number)
gh pr merge "$PR" --squash --auto
```

#### **Step 3: Check Health**
```bash
python3 .github/scripts/pr_health.py "$PR"
```

#### **Step 4: Fix Missing Contexts (if needed)**
```bash
git commit --allow-empty -m "fix: trigger checks"
git push
```

#### **Step 5: Update Branch (if needed)**
```bash
gh pr merge "$PR" --update-branch
```

#### **Step 6: Auto-Merge Completes**
When all checks pass, the PR will automatically merge.

---

## 🛠️ Troubleshooting Guide

### **Common Issues & Solutions**

#### **"MISSING contexts" Error**
- **Problem:** PR health check shows missing contexts
- **Solution:** Push a no-op commit to trigger checks
- **Command:** `git commit --allow-empty -m "fix: trigger checks" && git push`

#### **"strict block" Error**
- **Problem:** Branch protection requires update
- **Solution:** Update branch from main
- **Command:** `gh pr merge "$PR" --update-branch`

#### **Checks Not Attaching**
- **Problem:** GitHub Actions not running
- **Solution:** Use recheck workflow
- **Action:** Go to PR → Actions → Run workflow → recheck

#### **Auto-Merge Not Working**
- **Problem:** Auto-merge not enabled
- **Solution:** Enable in PR settings
- **Action:** PR page → Enable auto-merge (squash)

---

## 📊 Success Metrics

### **Target Improvements**
- **PR merge time reduction:** 50% faster
- **PR failure rate reduction:** 75% fewer failures
- **Team adoption rate:** 100% within 2 weeks

### **Current Status**
- **Adoption Rate:** 0% (baseline)
- **Average Merge Time:** TBD
- **Failure Rate:** TBD

---

## 🎯 Team Adoption Checklist

### **For Each Team Member:**
- [ ] **Learn the 6-step process** (memorize or bookmark)
- [ ] **Practice with test PR** (create and merge)
- [ ] **Use troubleshooting guide** when issues arise
- [ ] **Report any problems** to team lead
- [ ] **Track personal metrics** (merge time, failures)

### **For Team Lead:**
- [ ] **Train all team members** on new workflow
- [ ] **Monitor adoption metrics** weekly
- [ ] **Address adoption barriers** promptly
- [ ] **Refine workflow** based on feedback
- [ ] **Celebrate successes** and improvements

---

## 📚 Quick Reference

### **One-Liner Commands**
```bash
# Complete PR workflow
git checkout -b feat/my-change && git add -A && git commit -m "feat: my change" && git push -u origin feat/my-change && gh pr create --fill && PR=$(gh pr view --json number --jq .number) && gh pr merge "$PR" --squash --auto && python3 .github/scripts/pr_health.py "$PR"

# Fix missing contexts
git commit --allow-empty -m "fix: trigger checks" && git push

# Update branch
gh pr merge "$PR" --update-branch
```

### **Emergency Commands**
```bash
# Abort current PR and start over
git checkout main && git pull && git branch -D feat/my-change

# Force push if needed (use carefully)
git push --force-with-lease
```

---

## 🚀 Implementation Status

### **Deployment Checklist:**
- ✅ **Standard workflow documented** and promoted
- ✅ **Troubleshooting guide** created
- ✅ **Success metrics** defined
- ✅ **Team adoption checklist** prepared
- [ ] **Team training** completed
- [ ] **Metrics tracking** established
- [ ] **Feedback collection** system active

### **Next Steps:**
1. **Train team members** on new workflow
2. **Establish metrics tracking** system
3. **Monitor adoption progress** weekly
4. **Refine workflow** based on feedback

---

*Standard PR Workflow - Team Adoption*  
*Deployed via Stage B Quality Gatekeeper - 2025-11-10*
