---
project: Career Intelligence Space
type: spec
status: matured
tags: [docs, frontmatter, reference, compliance]
updated: 2025-09-27
---

# Frontmatter Quick Reference

## 🚨 **REQUIRED FOR ALL .md FILES**

```yaml
---
project: Career Intelligence Space
type: [capsule|memo|assessment|log|decision|spec]
status: [draft|matured|archived]
tags: [tag1, tag2, tag3]  # NON-EMPTY LIST
updated: YYYY-MM-DD
---
```

## 🛠️ **QUICK FIXES**

### Add Frontmatter to Files
```bash
# Add to specific files
python3 .github/scripts/add_frontmatter.py file1.md file2.md

# Add to ALL files missing frontmatter
python3 .github/scripts/add_frontmatter.py --all
```

### Check Compliance Before Committing
```bash
python3 .github/scripts/pre_commit_frontmatter.py
```

### Check What's Wrong
```bash
python3 .github/scripts/frontmatter_gate.py
```

## 📋 **COMMON PATTERNS**

### Chronicle Files (08_CHRONICLE/)
```yaml
type: log
status: matured
tags: [chronicle, session, date]
```

### Documentation (docs/)
```yaml
type: spec
status: matured
tags: [docs, topic, category]
```

### Prompts (prompts/)
```yaml
type: spec
status: matured
tags: [prompts, macros, automation]
```

### Assessments (assessments/)
```yaml
type: assessment
status: draft
tags: [assessment, topic, analysis]
```

## ⚠️ **COMMON MISTAKES**

1. **Missing frontmatter entirely** → Use `add_frontmatter.py`
2. **Empty tags** → Must be `[tag1, tag2]` not `[]`
3. **Wrong date format** → Use `YYYY-MM-DD` not `MM/DD/YYYY`
4. **Code fences around frontmatter** → Use `---` not ```yaml
5. **Invalid type/status** → Check `docs/ONTOLOGY.yml`

## 🎯 **WORKFLOW**

1. **Before creating files**: Check templates in `.github/templates/frontmatter_templates.md`
2. **After creating files**: Run `add_frontmatter.py` if needed
3. **Before committing**: Run `pre_commit_frontmatter.py`
4. **If gate fails**: Check this reference and fix issues
