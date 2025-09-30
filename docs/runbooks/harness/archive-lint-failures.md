---
project: Career Intelligence Space
type: runbook
status: active
tags: [runbook, harness, archive, linting, troubleshooting]
updated: 2025-11-10
timezone: "America/Los_Angeles"
---

# Archive Lint Failures - Quick Fix Guide

This runbook provides quick solutions for common frontmatter linting failures in conversation archives.

## Common Errors & Solutions

### "Missing keys" Error
**Error:** `[ERR] file.md: missing keys ['conversation_id', 'participants']. (C4)`

**Solution:** Copy this template and fill in the blanks:
```yaml
---
project: Career Intelligence Space
type: conversation_archive
status: active
tags: [conversation_archive, your_topic]
updated: 2025-11-10
conversation_date: 2025-11-10
participants: ["user", "assistant"]
conversation_id: conv_2025_11_10_your_topic
timezone: "America/Los_Angeles"
related: []
---
```

### "Participants not array" Error
**Error:** `[ERR] file.md: 'participants' must be a non-empty list. (C4)`

**Solution:** Wrap participants in array format:
```yaml
# Wrong
participants: "user, assistant"

# Correct
participants: ["user", "assistant"]
```

### "Date format" Error
**Error:** `[ERR] file.md: 'updated' must be YYYY-MM-DD. (C4)`

**Solution:** Use ISO date format only:
```yaml
# Wrong
updated: "Nov 10, 2025"
updated: "2025/11/10"

# Correct
updated: "2025-11-10"
```

### "Term not in ontology" Warning
**Warning:** `[WARN] file.md: term 'HARNESS' not in ontology. (C3)`

**Solutions:**
1. **Add to ontology** (if legitimate term):
   ```yaml
   # In ontology/ontology.yml
   terms:
     harness:
       definition: "Scaffolding system for long-term LLM memory"
       synonyms: ["HARNESS", "harness"]
   ```

2. **Downgrade to lowercase** (if false positive):
   ```markdown
   # Change "HARNESS" to "harness" in content
   ```

### "Missing frontmatter block" Error
**Error:** `[ERR] file.md: missing frontmatter block '---' at top. (C4)`

**Solution:** Add YAML frontmatter at the very top of the file:
```markdown
---
project: Career Intelligence Space
type: conversation_archive
status: active
tags: [conversation_archive, your_topic]
updated: 2025-11-10
conversation_date: 2025-11-10
participants: ["user", "assistant"]
conversation_id: conv_2025_11_10_your_topic
---

# Your Content Here
```

## Quick Templates

### Full Archive Template
```yaml
---
project: Career Intelligence Space
type: conversation_archive
status: active
tags: [conversation_archive, topic_name]
updated: YYYY-MM-DD
conversation_date: YYYY-MM-DD
participants: ["user", "assistant"]
conversation_id: conv_YYYY_MM_DD_topic_name
timezone: "America/Los_Angeles"
related: []
---
```

### Lite Archive Template
```yaml
---
project: Career Intelligence Space
type: conversation_archive_lite
status: active
tags: [conversation_archive, lite, topic_name]
updated: YYYY-MM-DD
conversation_date: YYYY-MM-DD
participants: ["user", "assistant"]
conversation_id: conv_YYYY_MM_DD_topic_name
timezone: "America/Los_Angeles"
related: []
---
```

## Prevention Tips

1. **Use the archive builder script** for new archives
2. **Copy from existing archives** rather than creating from scratch
3. **Run linter locally** before committing: `python scripts/lint_frontmatter.py`
4. **Install pre-commit hooks** for automatic validation

## Getting Help

- **Schema reference:** `config/archive_schema.yml`
- **Linter source:** `scripts/lint_frontmatter.py`
- **Decision log:** `docs/decision-log.md`
- **Archive index:** `docs/archives/harness-archives.md`
