---
project: Career Intelligence Space
type: spec
status: matured
tags: [templates, frontmatter, automation]
updated: 2025-09-27
---

# Frontmatter Templates

## Quick Copy-Paste Templates

### Chronicle/Log Files
```yaml
---
project: Career Intelligence Space
type: log
status: matured
tags: [chronicle, session, date]
updated: YYYY-MM-DD
---
```

### Documentation Files
```yaml
---
project: Career Intelligence Space
type: spec
status: matured
tags: [docs, topic, category]
updated: YYYY-MM-DD
---
```

### Assessment Files
```yaml
---
project: Career Intelligence Space
type: assessment
status: draft
tags: [assessment, topic, analysis]
updated: YYYY-MM-DD
---
```

### Capsule Files
```yaml
---
project: Career Intelligence Space
type: capsule
status: draft
tags: [capsule, topic, reflection]
updated: YYYY-MM-DD
---
```

### Exploration Log Files (Sandboxing Phase)
```yaml
---
project: Career Intelligence Space
type: exploration_log
status: active
tags: [exploration, hypothesis, process]
phase: sandboxing
exploration_focus: [systems, implementation, research, design]
hypothesis: [what we're testing]
process_method: [how we're exploring]
context_importance: [why this matters]
updated: YYYY-MM-DD
---
```

### Hypothesis Tracking Files (Sandboxing Phase)
```yaml
---
project: Career Intelligence Space
type: hypothesis_tracking
status: active
tags: [hypothesis, testing, validation]
phase: sandboxing
hypothesis_id: [unique identifier]
hypothesis_status: [untested, testing, validated, invalidated, partial]
updated: YYYY-MM-DD
---
```

### Process Capture Files (Sandboxing Phase)
```yaml
---
project: Career Intelligence Space
type: process_capture
status: active
tags: [process, methodology, exploration]
phase: sandboxing
process_type: [exploration, analysis, design, testing]
process_stage: [planning, executing, reviewing, iterating]
updated: YYYY-MM-DD
---
```

## Allowed Values (from docs/ONTOLOGY.yml)

### Production/Implementation Types (Convergent Thinking)
- `capsule`
- `memo`
- `assessment`
- `log`
- `decision`
- `spec`
- `future_spec`
- `decision_log`
- `harness_addendum`
- `bridge_note`
- `strategic_vision_capsule`
- `alert`
- `implementation_capsule`
- `dashboard`
- `conversation_archive_lite`
- `backlog_log`
- `backfill_log`

### Sandboxing/Exploration Types (Divergent Thinking)
- `exploration_log`
- `hypothesis_tracking`
- `process_capture`
- `context_maintenance`
- `interrelatedness_map`
- `constraint_analysis`
- `timing_exploration`
- `design_experiment`
- `creative_session`
- `sandbox_overview`
- `prerequisite_template`

### Statuses
- `draft`
- `matured`
- `archived`

### Projects
- `Career Intelligence Space`

## Common Tags

### Production/Implementation Tags
- `chronicle`, `session`, `chat`, `migration`
- `docs`, `runbook`, `setup`, `automation`
- `assessment`, `analysis`, `evaluation`
- `capsule`, `reflection`, `insight`
- `pr`, `ci`, `workflow`, `gate`
- `prompts`, `macros`, `templates`

### Sandboxing/Exploration Tags
- `exploration`, `hypothesis`, `process`
- `systems`, `implementation`, `research`, `design`
- `testing`, `validation`, `experiment`
- `methodology`, `creative`, `brainstorming`
- `interrelatedness`, `constraints`, `timing`
- `sandboxing`, `divergent`, `discovery`
