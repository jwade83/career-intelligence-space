---
project: Career Intelligence Space
type: spec
status: matured
tags: [compliance, frontmatter, automation, team, adoption]
updated: 2025-11-10
adoption_status: active
---

# Frontmatter Compliance System - Team Adoption

**Status:** ✅ **ACTIVE** - This is the official compliance system for all team members  
**Source:** Promoted from `docs/FRONTMATTER_QUICK_REFERENCE.md` via Stage B Quality Gatekeeper  
**Adoption Date:** 2025-11-10

---

## 🎯 Compliance Requirements

### **Required Frontmatter for ALL .md Files**
```yaml
---
project: Career Intelligence Space
type: [capsule|memo|assessment|log|decision|spec]
status: [draft|matured|archived]
tags: [tag1, tag2, tag3]  # NON-EMPTY LIST
updated: YYYY-MM-DD
---
```

### **Type Enums (from docs/ONTOLOGY.yml)**
- **capsule:** Time-capsule documents, vision checkpoints
- **memo:** Process guides, quick references
- **assessment:** Analysis documents, evaluations
- **log:** Chronicle entries, session logs
- **decision:** Decision records, architectural choices
- **spec:** Specifications, runbooks, documentation

### **Status Enums**
- **draft:** Work in progress, initial creation
- **matured:** Quality-assured, ready for use
- **archived:** Deprecated, historical reference

---

## 🤖 Automation Scripts

### **Add Frontmatter to Files**
```bash
# Add to specific files
python3 .github/scripts/add_frontmatter.py file1.md file2.md

# Add to ALL files missing frontmatter
python3 .github/scripts/add_frontmatter.py --all
```

### **Check Compliance Before Committing**
```bash
# Pre-commit compliance check
python3 .github/scripts/pre_commit_frontmatter.py

# Check what's wrong with existing files
python3 .github/scripts/frontmatter_gate.py
```

### **Automated Compliance Workflow**
```bash
# Complete compliance workflow
python3 .github/scripts/add_frontmatter.py --all && python3 .github/scripts/pre_commit_frontmatter.py
```

---

## 📋 Common Patterns

### **Chronicle Files (08_CHRONICLE/)**
```yaml
---
project: Career Intelligence Space
type: log
status: matured
tags: [chronicle, session, date]
updated: YYYY-MM-DD
---
```

### **Documentation (docs/)**
```yaml
---
project: Career Intelligence Space
type: spec
status: matured
tags: [docs, topic, category]
updated: YYYY-MM-DD
---
```

### **Prompts (prompts/)**
```yaml
---
project: Career Intelligence Space
type: spec
status: matured
tags: [prompts, macros, automation]
updated: YYYY-MM-DD
---
```

### **Assessments (assessments/)**
```yaml
---
project: Career Intelligence Space
type: assessment
status: draft
tags: [assessment, topic, analysis]
updated: YYYY-MM-DD
---
```

---

## ⚠️ Common Mistakes & Fixes

### **1. Missing Frontmatter Entirely**
- **Problem:** File has no frontmatter
- **Solution:** Use `add_frontmatter.py`
- **Command:** `python3 .github/scripts/add_frontmatter.py filename.md`

### **2. Empty Tags Array**
- **Problem:** `tags: []` (empty array)
- **Solution:** Add at least one tag
- **Fix:** `tags: [docs, topic]`

### **3. Wrong Date Format**
- **Problem:** `updated: MM/DD/YYYY` or `updated: YYYY-MM-DD HH:MM:SS`
- **Solution:** Use ISO date format
- **Fix:** `updated: YYYY-MM-DD`

### **4. Code Fences Around Frontmatter**
- **Problem:** ```yaml around frontmatter
- **Solution:** Use triple dashes only
- **Fix:** `---` not ```yaml

### **5. Invalid Type/Status**
- **Problem:** Type or status not in allowed enums
- **Solution:** Check `docs/ONTOLOGY.yml`
- **Fix:** Use valid enum values

---

## 🎯 Team Adoption Workflow

### **Before Creating Files**
1. **Check templates** in `.github/templates/frontmatter_templates.md`
2. **Use appropriate type** from enum list
3. **Set status to draft** initially
4. **Add relevant tags** (non-empty list)

### **After Creating Files**
1. **Run compliance check:** `python3 .github/scripts/pre_commit_frontmatter.py`
2. **Fix any issues** using troubleshooting guide
3. **Verify compliance** before committing

### **Before Committing**
1. **Run pre-commit check:** `python3 .github/scripts/pre_commit_frontmatter.py`
2. **Fix any failures** immediately
3. **Never commit** non-compliant files

### **If Gate Fails**
1. **Check error message** for specific issue
2. **Use troubleshooting guide** to fix
3. **Re-run compliance check** to verify
4. **Commit fixed version**

---

## 📊 Success Metrics

### **Target Improvements**
- **Gate failure reduction:** 90% fewer failures
- **Compliance automation rate:** 100% automated
- **Manual intervention reduction:** 80% less manual work

### **Current Status**
- **Compliance Rate:** TBD (baseline)
- **Gate Failure Rate:** TBD
- **Automation Usage:** TBD

---

## 🎯 Team Adoption Checklist

### **For Each Team Member:**
- [ ] **Learn frontmatter requirements** (memorize or bookmark)
- [ ] **Use compliance scripts** before every commit
- [ ] **Follow common patterns** for different file types
- [ ] **Fix issues immediately** when gate fails
- [ ] **Report persistent problems** to team lead

### **For Team Lead:**
- [ ] **Train all team members** on compliance system
- [ ] **Monitor compliance metrics** weekly
- [ ] **Address compliance barriers** promptly
- [ ] **Refine automation** based on feedback
- [ ] **Celebrate compliance improvements**

---

## 🚀 Implementation Status

### **Deployment Checklist:**
- ✅ **Compliance system documented** and promoted
- ✅ **Automation scripts** available and tested
- ✅ **Common patterns** documented
- ✅ **Troubleshooting guide** created
- ✅ **Success metrics** defined
- ✅ **Team adoption checklist** prepared
- [ ] **Team training** completed
- [ ] **Metrics tracking** established
- [ ] **Feedback collection** system active

### **Next Steps:**
1. **Train team members** on compliance system
2. **Establish metrics tracking** system
3. **Monitor compliance progress** weekly
4. **Refine automation** based on feedback

---

*Frontmatter Compliance System - Team Adoption*  
*Deployed via Stage B Quality Gatekeeper - 2025-11-10*
