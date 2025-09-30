---
project: Career Intelligence Space
type: spec
status: matured
tags: [reference, quick_cards, adoption, workflow]
updated: 2025-11-10
---

# Quick Reference Cards - Promoted Artifacts

**Purpose:** Instant access to key workflows and processes from promoted artifacts for immediate team adoption.

---

## 🚀 PR Workflow (PR_ROUTE.md)

### **6-Step PR Process**
```bash
# 1. Create PR
git checkout -b feat/my-change
git add -A && git commit -m "feat: my change" && git push -u origin feat/my-change
gh pr create --fill

# 2. Enable auto-merge
PR=$(gh pr view --json number --jq .number)
gh pr merge "$PR" --squash --auto

# 3. Check health
python3 .github/scripts/pr_health.py "$PR"

# 4. Fix missing contexts (if needed)
git commit --allow-empty -m "fix: trigger checks"
git push

# 5. Update branch (if needed)
gh pr merge "$PR" --update-branch

# 6. Auto-merge completes when checks pass
```

### **Troubleshooting**
- **"MISSING contexts"** → Push no-op commit
- **"strict block"** → Run update-branch
- **Checks not attaching** → Use recheck workflow

---

## 📋 Frontmatter Compliance (FRONTMATTER_QUICK_REFERENCE.md)

### **Required Frontmatter**
```yaml
---
project: Career Intelligence Space
type: [capsule|memo|assessment|log|decision|spec]
status: [draft|matured|archived]
tags: [tag1, tag2, tag3]  # NON-EMPTY LIST
updated: YYYY-MM-DD
---
```

### **Quick Fixes**
```bash
# Add frontmatter to specific files
python3 .github/scripts/add_frontmatter.py file1.md file2.md

# Add to ALL files missing frontmatter
python3 .github/scripts/add_frontmatter.py --all

# Check compliance before committing
python3 .github/scripts/pre_commit_frontmatter.py

# Check what's wrong
python3 .github/scripts/frontmatter_gate.py
```

### **Common Patterns**
- **Chronicle Files:** `type: log, status: matured, tags: [chronicle, session, date]`
- **Documentation:** `type: spec, status: matured, tags: [docs, topic, category]`
- **Prompts:** `type: spec, status: matured, tags: [prompts, macros, automation]`

---

## 🤖 Cursor Agent Automation (prompts/README.md)

### **Daily PR Macro**
```
Stage all modified files, commit with:
"<type>: <scope> - <summary>",
push to a new branch and open a Pull Request.
Enable auto-merge (squash). If checks are missing or pending, run the recheck workflow or re-run failed jobs.
Finally, post a status summary with PR URL and the states of required checks (gate, links).
```

### **Rebase Fixer**
```
Check rebase state with `git status`. 
If editing a commit, run `git commit --no-edit`.
Then run `GIT_EDITOR=true git rebase --continue`.
If conflicts appear, keep the current file contents as shown in the editor, `git add` them, and repeat the previous step until done.
When finished, push with `git push --force-with-lease` and post a status summary with PR URL and check states.
```

### **New Doc Guard**
```
For any new file under docs/, prepend this exact YAML frontmatter before any content:
---
project: Career Intelligence Space
type: spec
status: draft
tags: [docs]
updated: YYYY-MM-DD
---
Ensure the date is today. If an existing doc is missing or has empty `tags`, populate a sensible non-empty list. Propose a single patch if multiple files change, then stage, commit:
"docs: compliance - add required frontmatter",
push to a new branch, open a PR, enable auto-merge (squash), and post check states.
```

---

## 📚 Reference Documentation (ChatGPT-Pilot-Migration.md)

### **Key Insights**
- **Single Clone Strategy:** Use same repo path for Terminal and Cursor
- **Automation First:** Use Cursor Agent for all Git operations
- **Compliance Automation:** Frontmatter validation prevents gate failures
- **Background Delegation:** Let automation handle routine processes

### **Migration Checklist**
- [ ] Install Cursor IDE and sign in with GitHub
- [ ] Clone repo to standard location
- [ ] Open repo in Cursor and verify Git panel
- [ ] Add repo hygiene files (.editorconfig, .gitattributes, .vscode/settings.json)
- [ ] Enable auto-merge in GitHub settings
- [ ] Test PR workflow with sample change
- [ ] Verify all checks pass and auto-merge works

### **Troubleshooting**
- **Checks not attaching** → Use recheck workflow
- **Auto-merge not working** → Check repo settings and permissions
- **Frontmatter failures** → Use compliance scripts
- **Rebase conflicts** → Use rebase fixer macro

---

## 📊 Adoption Tracking

### **Usage Checklist**
- [ ] **PR Workflow:** Using 6-step process for all PRs
- [ ] **Frontmatter Compliance:** Running compliance scripts before commits
- [ ] **Cursor Automation:** Using Agent macros for routine tasks
- [ ] **Reference Docs:** Consulting migration guide for issues

### **Success Metrics**
- **PR merge time:** Target 50% reduction
- **Gate failures:** Target 90% reduction
- **Task completion:** Target 60% faster
- **Manual work:** Target 70% reduction

---

*Quick Reference Cards - Stage B Adoption*  
*Generated using Strategic Consultant Lenses v1.1.0*
