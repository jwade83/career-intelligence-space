# COMMANDS

## Agent Commands

This document outlines all available commands for interacting with agents in the Career Intelligence Space platform.

### Research Runner Agent

#### Basic Commands
```bash
# Start a new research task
run-research --topic "<research_topic>" --depth <shallow|deep>

# View active tasks
list-tasks --status active

# View task history
list-tasks --status completed --limit 10

# Stop a running task
stop-task --id <task_id>
```

#### Research Configuration
```bash
# Set research parameters
configure-research --max-sources 25 --timeout 3600 --output-format markdown

# View current configuration
show-config research

# Reset to defaults
reset-config research
```

#### Data Export
```bash
# Export research results
export-results --task-id <task_id> --format <json|markdown|pdf>

# Export all results for a topic
export-topic --topic "<topic_name>" --format markdown
```

### Task Management

#### Task Operations
```bash
# Create task from template
create-task --template research --config task.yml

# Monitor task progress
watch-task --id <task_id>

# Schedule recurring tasks
schedule-task --cron "0 9 * * 1" --template research
```

#### Status Queries
```bash
# System status
status --all

# Agent health check
health-check --agent research

# Resource usage
stats --resource memory,cpu,disk
```

### Integration Commands

#### GitHub Integration
```bash
# Create issue from research
create-issue --task-id <task_id> --repo <repository>

# Update PR with findings
update-pr --number <pr_number> --research-id <task_id>
```

#### Logging
```bash
# View logs
show-logs --agent research --level info --tail 100

# Export logs
export-logs --date-range 2025-09-01:2025-09-09 --format json
```

### Advanced Operations

#### Batch Processing
```bash
# Run multiple research tasks
batch-research --input topics.yml --parallel 3

# Bulk export
bulk-export --tasks completed --format json
```

#### Development
```bash
# Test configuration
test-config --file agents/research.yml

# Validate templates
validate-template --file tasks/templates/TEMPLATE_research_task.yml

# Debug mode
debug-agent --agent research --level verbose
```

### Configuration Files

#### Agent Configuration
- `agents/research.yml` - Research Runner agent settings
- `tasks/templates/TEMPLATE_research_task.yml` - Research task template

#### System Configuration
- `.github/workflows/agent-ci.yml` - CI/CD pipeline
- `00_GOVERNANCE/changelog.md` - Change tracking

### Environment Variables

```bash
# Core settings
CIS_AGENT_TIMEOUT=3600
CIS_MAX_CONCURRENT_TASKS=5
CIS_LOG_LEVEL=info

# Research specific
CIS_RESEARCH_MAX_SOURCES=25
CIS_RESEARCH_OUTPUT_DIR=./99_LOGS/agents/

# GitHub integration
GITHUB_TOKEN=<your_token>
GITHUB_REPO=jwade83/career-intelligence-space
```

### Error Handling

#### Common Issues
- Task timeout: Increase `CIS_AGENT_TIMEOUT`
- Memory issues: Reduce parallel tasks
- API limits: Implement rate limiting

#### Troubleshooting
```bash
# Check system health
health-check --comprehensive

# Validate configuration
validate-system --fix-issues

# Reset agent state
reset-agent --agent research --confirm
```

# UPGRADE
