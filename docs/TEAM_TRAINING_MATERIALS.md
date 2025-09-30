---
project: Career Intelligence Space
type: spec
status: matured
tags: [training, team, adoption, priority_1, workflow]
updated: 2025-11-10
training_status: active
---

# Team Training Materials - Priority 1 Artifacts

**Status:** ✅ **ACTIVE** - Training materials for immediate team adoption  
**Target:** All team members  
**Duration:** 30-45 minutes  
**Adoption Date:** 2025-11-10

---

## 🎯 Training Objectives

By the end of this training, team members will:
1. **Master the standard PR workflow** for all pull requests
2. **Use frontmatter compliance automation** to prevent gate failures
3. **Apply troubleshooting techniques** for common issues
4. **Track personal metrics** for continuous improvement

---

## 📚 Training Agenda

### **Part 1: Standard PR Workflow (20 minutes)**
- Overview of 6-step process
- Hands-on practice with test PR
- Troubleshooting common issues
- Q&A and clarification

### **Part 2: Frontmatter Compliance (15 minutes)**
- Understanding compliance requirements
- Using automation scripts
- Following common patterns
- Preventing gate failures

### **Part 3: Implementation & Metrics (10 minutes)**
- Personal adoption checklist
- Metrics tracking system
- Feedback collection process
- Next steps and support

---

## 🚀 Part 1: Standard PR Workflow

### **Learning Objectives**
- Understand the 6-step PR process
- Practice creating and managing PRs
- Learn troubleshooting techniques
- Apply workflow to real scenarios

### **Training Content**

#### **The 6-Step Process**
```bash
# Step 1: Create PR
git checkout -b feat/my-change
git add -A && git commit -m "feat: my change" && git push -u origin feat/my-change
gh pr create --fill

# Step 2: Enable Auto-Merge
PR=$(gh pr view --json number --jq .number)
gh pr merge "$PR" --squash --auto

# Step 3: Check Health
python3 .github/scripts/pr_health.py "$PR"

# Step 4: Fix Missing Contexts (if needed)
git commit --allow-empty -m "fix: trigger checks"
git push

# Step 5: Update Branch (if needed)
gh pr merge "$PR" --update-branch

# Step 6: Auto-Merge Completes
# When all checks pass, the PR will automatically merge
```

#### **Hands-On Practice**
1. **Create test branch:** `git checkout -b training/test-pr`
2. **Make small change:** Edit a file or add a comment
3. **Follow 6-step process:** Execute each step
4. **Observe auto-merge:** Watch the PR merge automatically
5. **Clean up:** Delete test branch after merge

#### **Common Issues & Solutions**
- **"MISSING contexts"** → Push no-op commit
- **"strict block"** → Update branch from main
- **Checks not attaching** → Use recheck workflow
- **Auto-merge not working** → Check PR settings

### **Practice Exercise**
Create a test PR using the 6-step process and successfully merge it. Document any issues encountered and how you resolved them.

---

## 🤖 Part 2: Frontmatter Compliance

### **Learning Objectives**
- Understand frontmatter requirements
- Use automation scripts effectively
- Follow common patterns for different file types
- Prevent gate failures proactively

### **Training Content**

#### **Required Frontmatter**
```yaml
---
project: Career Intelligence Space
type: [capsule|memo|assessment|log|decision|spec]
status: [draft|matured|archived]
tags: [tag1, tag2, tag3]  # NON-EMPTY LIST
updated: YYYY-MM-DD
---
```

#### **Automation Scripts**
```bash
# Add frontmatter to specific files
python3 .github/scripts/add_frontmatter.py file1.md file2.md

# Add to ALL files missing frontmatter
python3 .github/scripts/add_frontmatter.py --all

# Check compliance before committing
python3 .github/scripts/pre_commit_frontmatter.py

# Check what's wrong with existing files
python3 .github/scripts/frontmatter_gate.py
```

#### **Common Patterns**
- **Chronicle Files:** `type: log, status: matured, tags: [chronicle, session, date]`
- **Documentation:** `type: spec, status: matured, tags: [docs, topic, category]`
- **Prompts:** `type: spec, status: matured, tags: [prompts, macros, automation]`

### **Practice Exercise**
1. **Create a new file** without frontmatter
2. **Run compliance check** and observe failure
3. **Use automation script** to add frontmatter
4. **Verify compliance** passes
5. **Commit the file** successfully

---

## 📊 Part 3: Implementation & Metrics

### **Learning Objectives**
- Understand personal adoption checklist
- Learn metrics tracking system
- Know feedback collection process
- Plan next steps and support

### **Training Content**

#### **Personal Adoption Checklist**
- [ ] **Learn the 6-step PR process** (memorize or bookmark)
- [ ] **Practice with test PR** (create and merge)
- [ ] **Use troubleshooting guide** when issues arise
- [ ] **Run compliance scripts** before every commit
- [ ] **Follow common patterns** for different file types
- [ ] **Track personal metrics** (merge time, failures)
- [ ] **Report any problems** to team lead

#### **Metrics Tracking**
- **PR merge time:** Track time from creation to merge
- **PR failure rate:** Count failed PRs vs. successful ones
- **Compliance rate:** Track gate failures vs. successes
- **Automation usage:** Monitor script usage frequency

#### **Feedback Collection**
- **Weekly check-ins:** Report progress and issues
- **Monthly reviews:** Assess adoption success
- **Continuous improvement:** Suggest workflow refinements
- **Support requests:** Ask for help when needed

### **Implementation Plan**
1. **Week 1:** Practice with test PRs and compliance scripts
2. **Week 2:** Use new workflows for all real work
3. **Week 3:** Track metrics and report progress
4. **Week 4:** Provide feedback and suggest improvements

---

## 🎯 Training Assessment

### **Knowledge Check**
1. **What are the 6 steps** in the standard PR workflow?
2. **What frontmatter is required** for all .md files?
3. **How do you fix** a "MISSING contexts" error?
4. **What automation scripts** are available for compliance?
5. **How do you track** personal adoption metrics?

### **Practical Assessment**
1. **Create a test PR** using the 6-step process
2. **Add frontmatter** to a new file using automation
3. **Resolve a common issue** using troubleshooting guide
4. **Track metrics** for your test activities
5. **Provide feedback** on the training experience

---

## 🚀 Post-Training Support

### **Resources Available**
- **Quick Reference Cards:** `docs/QUICK_REFERENCE_CARDS.md`
- **Standard PR Workflow:** `docs/STANDARD_PR_WORKFLOW.md`
- **Compliance System:** `docs/FRONTMATTER_COMPLIANCE_SYSTEM.md`
- **Team Adoption Plan:** `docs/runbooks/TEAM_ADOPTION_PLAN.md`

### **Support Channels**
- **Team Lead:** For workflow questions and issues
- **Documentation:** Self-service reference materials
- **Weekly Check-ins:** Progress monitoring and support
- **Feedback System:** Continuous improvement input

### **Success Criteria**
- **Week 1:** 50% of team using new workflows
- **Week 2:** 100% of team using new workflows
- **Week 3:** Measurable productivity improvements
- **Week 4:** Positive feedback and refinements

---

## 📝 Training Completion

### **Completion Checklist**
- [ ] **Attended training session** (30-45 minutes)
- [ ] **Completed practice exercises** (test PR + compliance)
- [ ] **Passed knowledge check** (5 questions)
- [ ] **Passed practical assessment** (5 tasks)
- [ ] **Understood support resources** and channels
- [ ] **Committed to adoption timeline** and metrics

### **Next Steps**
1. **Begin using new workflows** immediately
2. **Track personal metrics** from day one
3. **Report progress weekly** to team lead
4. **Provide feedback** for continuous improvement
5. **Support other team members** in adoption

---

*Team Training Materials - Priority 1 Artifacts*  
*Deployed via Stage B Quality Gatekeeper - 2025-11-10*
