---
project: Career Intelligence Space
type: spec
status: draft
tags: ['misc']
updated: 2025-10-02
---

# Orchestrator Log Schema

## Purpose
Structured logging format for Agent 0 (Orchestrator) operations.

## Schema Definition

### Log Entry Structure
```json
{
  "timestamp": "ISO 8601 timestamp",
  "agent_id": "orchestrator",
  "task_id": "unique task identifier",
  "event_type": "task_received|task_routed|task_completed|error",
  "source_agent": "originating agent identifier",
  "target_agent": "destination agent identifier",
  "payload": {
    "task_description": "string",
    "priority": "high|medium|low",
    "metadata": {}
  },
  "status": "pending|in_progress|completed|failed",
  "duration_ms": "processing time in milliseconds",
  "error_details": "error information if applicable"
}
```

### Event Types

#### task_received
- New task intake
- Validation results
- Initial routing decisions

#### task_routed
- Agent assignment
- Routing rationale
- Load balancing decisions

#### task_completed
- Completion notifications
- Quality check results
- Performance metrics

#### error
- System errors
- Validation failures
- Routing conflicts

### Required Fields
- timestamp
- agent_id
- task_id
- event_type
- status

### Optional Fields
- source_agent
- target_agent
- payload
- duration_ms
- error_details

### Example Log Entries

```json
{
  "timestamp": "2025-09-09T22:34:00Z",
  "agent_id": "orchestrator",
  "task_id": "task-001",
  "event_type": "task_received",
  "status": "pending",
  "payload": {
    "task_description": "Research market trends",
    "priority": "high"
  }
}
```

```json
{
  "timestamp": "2025-09-09T22:34:01Z",
  "agent_id": "orchestrator",
  "task_id": "task-001",
  "event_type": "task_routed",
  "target_agent": "research_agent",
  "status": "in_progress",
  "duration_ms": 150
}
```

# UPGRADE:
