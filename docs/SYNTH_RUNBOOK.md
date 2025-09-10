# Synthesizer Agent Runbook

## Overview

The Synthesizer Agent is responsible for creating comprehensive career intelligence reports by analyzing and combining data from multiple sources. This runbook provides operational procedures for running synthesis tasks.

## Prerequisites

- Access to research data outputs
- Template configuration files
- Output directory permissions
- Valid API credentials for external services

## Standard Operating Procedures

### 1. Pre-Synthesis Validation

```bash
# Verify data sources
ls -la 99_LOGS/agents/research_runner_log.md
ls -la 03_RESEARCH/

# Check template availability
ls -la 02_TEMPLATES/synthesis/
```

### 2. Running Synthesis Tasks

```bash
# Basic synthesis command
python agents/synthesizer.py --task-id SYNTH-001 --template standard

# With custom parameters
python agents/synthesizer.py --task-id SYNTH-002 --template detailed --output-format pdf
```

### 3. Post-Synthesis Review

- Validate output completeness
- Check formatting compliance
- Verify data accuracy
- Update synthesis log

## Error Handling

### Common Issues

1. **Missing Research Data**: Verify research runner has completed
2. **Template Errors**: Check template syntax and variables
3. **Output Permissions**: Ensure write access to target directories

### Recovery Procedures

```bash
# Clean incomplete synthesis
rm -rf outputs/SYNTH-*/incomplete/

# Restart with recovery mode
python agents/synthesizer.py --recover --task-id SYNTH-XXX
```

## Quality Assurance

### Validation Checklist

- [ ] All source data integrated
- [ ] Template placeholders filled
- [ ] Output format compliance
- [ ] Accuracy verification complete
- [ ] Log entries updated

### Review Process

1. Automated validation checks
2. Manual content review
3. Stakeholder approval
4. Final output delivery

## Monitoring and Logging

- Task execution logs: `99_LOGS/agents/synthesizer_log.md`
- Error tracking: `99_LOGS/errors/synthesis_errors.log`
- Performance metrics: `99_LOGS/metrics/synthesis_performance.json`

## Configuration Management

### Template Updates

```bash
# Update synthesis templates
git pull origin main
cp templates/new_synthesis.yaml 02_TEMPLATES/synthesis/
```

### Agent Configuration

```yaml
synthesis:
  max_concurrent: 3
  timeout_minutes: 30
  retry_attempts: 2
  output_formats: ["md", "pdf", "json"]
```

## Emergency Procedures

### Critical Failure Response

1. Stop all running synthesis tasks
2. Preserve partial outputs
3. Notify stakeholders
4. Initiate recovery procedures
5. Document incident details

### Data Recovery

```bash
# Backup current state
tar -czf synthesis_backup_$(date +%Y%m%d).tar.gz outputs/ 99_LOGS/

# Restore from backup
tar -xzf synthesis_backup_YYYYMMDD.tar.gz
```

# UPGRADE:
