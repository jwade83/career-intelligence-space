# RESEARCH RUNBOOK

## Research Runner Agent Operations Manual

This comprehensive runbook provides detailed operational procedures for the Research Runner Agent in the Career Intelligence Space platform.

### Quick Reference

#### Emergency Contacts
- **System Administrator**: admin@career-intel.space
- **On-Call Engineer**: oncall@career-intel.space
- **GitHub Repository**: jwade83/career-intelligence-space

#### Key Files
- **Agent Config**: `agents/research.yml`
- **Task Template**: `tasks/templates/TEMPLATE_research_task.yml`
- **Log Directory**: `99_LOGS/agents/`
- **Runbook**: `docs/RESEARCH_RUNBOOK.md`

### Pre-Operations Checklist

#### System Prerequisites
```bash
# Verify system status
health-check --comprehensive
status --all-services

# Check resource availability
df -h  # Disk space
free -h  # Memory
top  # CPU usage

# Validate configuration
validate-config --file agents/research.yml
test-connectivity --all-endpoints
```

#### Environment Setup
```bash
# Set required environment variables
export CIS_AGENT_TIMEOUT=3600
export CIS_RESEARCH_MAX_SOURCES=25
export CIS_LOG_LEVEL=info
export GITHUB_TOKEN="${GITHUB_TOKEN}"

# Verify environment
env | grep CIS_
echo "GitHub token: ${GITHUB_TOKEN:0:8}..."
```

### Standard Operations

#### 1. Starting a Research Task

##### Manual Task Creation
```bash
# Basic research task
run-research \
  --topic "AI in Career Development" \
  --depth deep \
  --sources 25 \
  --format markdown

# With custom parameters
run-research \
  --topic "Remote Work Trends 2025" \
  --depth shallow \
  --sources 15 \
  --timeout 1800 \
  --output-dir "./custom-output" \
  --tags "remote,trends,2025"
```

##### Template-Based Task Creation
```bash
# Create from template
create-task \
  --template research \
  --config "topic=Machine Learning Careers" \
  --config "priority=high"

# Batch task creation
batch-create-tasks --input research-topics.yml
```

##### GitHub Issue Integration
```bash
# Create task from GitHub issue
create-task-from-issue \
  --issue-number 42 \
  --repo jwade83/career-intelligence-space

# Auto-create issue after task completion
run-research \
  --topic "Data Science Salaries" \
  --create-issue \
  --assignee "jwade83"
```

#### 2. Monitoring Task Execution

##### Real-Time Monitoring
```bash
# Watch active tasks
watch-tasks --status active --refresh 30

# Monitor specific task
watch-task --id task_20250909_001 --verbose

# Stream logs
tail -f 99_LOGS/agents/research_runner_log.md
```

##### Progress Tracking
```bash
# Check task progress
get-task-status --id task_20250909_001

# List all tasks with status
list-tasks --format table --show-progress

# Export progress report
export-task-report --date-range "2025-09-01:2025-09-09" --format json
```

#### 3. Task Management

##### Pause/Resume Operations
```bash
# Pause running task
pause-task --id task_20250909_001

# Resume paused task
resume-task --id task_20250909_001

# Pause all tasks (maintenance mode)
pause-all-tasks --reason "System maintenance"
```

##### Task Cancellation
```bash
# Cancel specific task
cancel-task --id task_20250909_001 --reason "Obsolete requirement"

# Cancel all pending tasks
cancel-tasks --status pending --confirm

# Emergency stop all tasks
emergency-stop --confirm --reason "Critical system issue"
```

### Performance Optimization

#### Resource Tuning
```bash
# Adjust concurrent task limit
set-config --key max_concurrent_tasks --value 3

# Optimize memory usage
set-config --key memory_limit --value "4GB"

# Configure cache settings
set-config --key cache_ttl --value 3600
set-config --key cache_size --value "1GB"
```

#### Load Balancing
```bash
# Scale agent instances
scale-agent --name research --instances 3

# Check load distribution
get-load-stats --agent research

# Rebalance tasks
rebalance-tasks --strategy round-robin
```

### Troubleshooting Procedures

#### Common Issues and Solutions

##### 1. Task Timeouts
**Symptoms**: Tasks hanging, no progress updates
**Diagnosis**:
```bash
# Check task status
get-task-status --id <task_id> --verbose

# Review resource usage
get-resource-usage --task-id <task_id>

# Check for network issues
test-connectivity --endpoints all
```

**Resolution**:
```bash
# Increase timeout
set-config --key agent_timeout --value 7200

# Restart task with extended timeout
restart-task --id <task_id> --timeout 7200

# Kill and recreate if necessary
kill-task --id <task_id>
recreate-task --from-id <task_id>
```

##### 2. Memory Issues
**Symptoms**: High memory usage, OOM errors
**Diagnosis**:
```bash
# Monitor memory usage
watch -n 1 'free -h && ps aux | grep research | head -10'

# Check for memory leaks
get-memory-profile --agent research

# Review large datasets
list-tasks --sort-by memory_usage --desc
```

**Resolution**:
```bash
# Restart agent to clear memory
restart-agent --name research

# Reduce concurrent tasks
set-config --key max_concurrent_tasks --value 1

# Enable memory cleanup
set-config --key memory_cleanup_interval --value 300
```

##### 3. API Rate Limiting
**Symptoms**: HTTP 429 errors, slow data collection
**Diagnosis**:
```bash
# Check API usage
get-api-usage --service all --time-range 1h

# Review rate limit headers
check-rate-limits --endpoints all

# Monitor request patterns
tail -f 99_LOGS/agents/research_runner_log.md | grep "rate_limit"
```

**Resolution**:
```bash
# Enable rate limiting
set-config --key enable_rate_limiting --value true

# Adjust request intervals
set-config --key request_interval --value 2000

# Implement exponential backoff
set-config --key backoff_strategy --value exponential
```

##### 4. Configuration Errors
**Symptoms**: Agent startup failures, invalid settings
**Diagnosis**:
```bash
# Validate configuration
validate-config --file agents/research.yml --strict

# Check syntax
yamllint agents/research.yml

# Compare with template
diff agents/research.yml agents/research.yml.template
```

**Resolution**:
```bash
# Reset to defaults
reset-config --agent research --confirm

# Restore from backup
restore-config --from-backup --date "2025-09-08"

# Manual fix and validate
vim agents/research.yml
validate-config --file agents/research.yml
```

### Maintenance Procedures

#### Routine Maintenance

##### Daily Tasks
```bash
# Check system health
health-check --comprehensive | tee daily-health-$(date +%Y%m%d).log

# Review error logs
grep -i error 99_LOGS/agents/research_runner_log.md | tail -20

# Clean temporary files
cleanup-temp-files --age 24h

# Backup configuration
backup-config --destination s3://cis-backups/configs/$(date +%Y%m%d)
```

##### Weekly Tasks
```bash
# Performance analysis
generate-performance-report --week-ending $(date +%Y-%m-%d)

# Update dependencies
update-dependencies --dry-run
update-dependencies --confirm

# Security scan
security-scan --agent research --full

# Rotate logs
rotate-logs --keep 30
```

##### Monthly Tasks
```bash
# Capacity planning
generate-capacity-report --month $(date +%Y-%m)

# Configuration review
audit-configuration --agent research

# Update documentation
update-runbook --auto-generate

# Disaster recovery test
test-disaster-recovery --dry-run
```

### Emergency Procedures

#### Critical System Failure
```bash
# Immediate response
emergency-stop --all-agents
notify-oncall --priority critical --message "Research agent failure"

# Assessment
diagnose-system --comprehensive
collect-debug-info --output emergency-debug-$(date +%Y%m%d-%H%M).tar.gz

# Recovery
restore-from-backup --latest
restart-all-services
run-health-checks
```

#### Data Corruption
```bash
# Stop all operations
emergency-stop --reason "Data corruption detected"

# Assess damage
check-data-integrity --all-stores
identify-corrupted-tasks

# Recovery
restore-data --from-backup --verify-integrity
rerun-corrupted-tasks
validate-results
```

### Monitoring and Alerting

#### Key Metrics
```yaml
metrics:
  performance:
    - task_completion_rate
    - average_task_duration
    - resource_utilization
    - error_rate
  
  health:
    - agent_uptime
    - memory_usage
    - cpu_usage
    - disk_usage
  
  business:
    - research_quality_score
    - source_diversity
    - citation_accuracy
    - user_satisfaction
```

#### Alert Thresholds
```yaml
alerts:
  critical:
    - agent_down: 0 tolerance
    - error_rate: >10%
    - memory_usage: >90%
  
  warning:
    - task_duration: >2x average
    - cpu_usage: >80%
    - disk_usage: >85%
  
  info:
    - new_task_created
    - task_completed
    - configuration_changed
```

### Performance Benchmarks

#### Expected Performance
```yaml
benchmarks:
  task_completion:
    shallow_research: "5-15 minutes"
    deep_research: "30-60 minutes"
    batch_processing: "2-4 hours per 10 tasks"
  
  resource_usage:
    memory: "<2GB per task"
    cpu: "<70% sustained"
    disk: "<100MB per task output"
  
  quality_metrics:
    source_accuracy: ">95%"
    citation_completeness: ">90%"
    content_relevance: ">85%"
```

### Security Procedures

#### Access Control
```bash
# Review access permissions
audit-permissions --agent research

# Rotate API keys
rotate-api-keys --confirm

# Update certificates
update-certificates --auto-renew

# Review security logs
analyze-security-logs --time-range 24h
```

#### Data Protection
```bash
# Encrypt sensitive data
encrypt-data --agent-data research

# Verify backups
test-backup-integrity --latest

# Clean PII data
sanitize-logs --remove-pii

# Update privacy settings
update-privacy-config --gdpr-compliant
```

### Integration Points

#### GitHub Workflow
```bash
# Sync with repository
git-sync --repo jwade83/career-intelligence-space

# Update workflows
update-github-actions --auto-deploy

# Create release
create-release --version $(get-next-version)

# Deploy to production
deploy --environment production --confirm
```

#### External Services
```bash
# Test API connections
test-external-apis --all

# Update service credentials
update-service-credentials --rotate

# Monitor service health
monitor-external-services --alert-on-failure

# Update rate limits
sync-rate-limits --from-providers
```

### Documentation Updates

#### Runbook Maintenance
```bash
# Auto-generate sections
update-runbook --auto-generate --sections metrics,procedures

# Validate procedures
test-runbook-procedures --dry-run

# Update screenshots
update-documentation-images --auto-capture

# Publish updates
publish-runbook --version $(date +%Y.%m.%d)
```

# UPGRADE
