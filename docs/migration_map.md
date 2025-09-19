# Migration Map

## 📑 Index

- **Automated Migration Map**  
  - [`docs/migration_map.md`](./migration_map.md) — auto-updated on each commit with file adds/renames.
- **Backfill Transcript(s)**  
  - [`99_LOGS/migration_backfill_20250917.md`](../99_LOGS/migration_backfill_20250917.md) — one-time historical log of portfolio/asset migrations pre-automation.
- **Captain's Logs (Daily Journals)**  
  - [`99_LOGS/journal/`](../99_LOGS/journal/) — daily narrative logs of repo activities, automation events, and sync operations.

---

## Automated Migration Map (Live)

# Migration Index

This section links to both the **one-time backfill** (historical baseline) and the **ongoing migration map** (automation-driven).

- **Backfill (pre-automation snapshot):**  
  [99_LOGS/migration_backfill_20250917.md](../99_LOGS/migration_backfill_20250917.md)
- **Current Migration Map (auto-updated):**  
  [docs/migration_map.md](migration_map.md)
- **Captain's Logs (daily journals):**  
  [99_LOGS/journal/](../99_LOGS/journal/)
- **Design Lane Index →** [docs/design/INDEX.md](design/INDEX.md)

---

*This index ensures migration lineage is always visible — from past archives to present automation and narrative logs.*

# Migration Map

## Overview

This document outlines the migration strategy and mapping for Career Intelligence Space platform components.

## Data Migration Strategy

### Phase 1: Legacy System Analysis

- [ ] Identify existing data sources
- [ ] Map current data structures
- [ ] Assess data quality and completeness
- [ ] Document dependencies

### Phase 2: Target Architecture Design

- [ ] Define new data models
- [ ] Design API interfaces
- [ ] Plan database schema changes
- [ ] Establish data validation rules

### Phase 3: Migration Execution

- [ ] Set up staging environment
- [ ] Execute data transformation
- [ ] Validate migrated data
- [ ] Perform testing and rollback procedures

## Component Mapping

### Job Intelligence

- **Source**: Legacy job tracking system
- **Target**: `03_RESEARCH/job_intelligence/`
- **Format**: Structured JSON with metadata
- **Dependencies**: Company profiles, salary data

### Career Profiles

- **Source**: Individual profile data
- **Target**: `05_ASSETS/profiles/`
- **Format**: Markdown with YAML frontmatter
- **Dependencies**: Skills taxonomy, experience validation

### Application Tracking

- **Source**: Spreadsheet-based tracking
- **Target**: `99_LOGS/applications/`
- **Format**: Structured logs with timestamps
- **Dependencies**: Job postings, outcome tracking

## Migration Scripts

Location: `src/migration/`

- `migrate_jobs.py` - Job posting and intelligence migration
- `migrate_profiles.py` - Career profile data migration
- `migrate_applications.py` - Application tracking migration
- `validate_migration.py` - Data validation and integrity checks

## Rollback Strategy

1. **Database Snapshots**: Automated before each migration phase
2. **Version Control**: All configuration changes tracked
3. **Rollback Scripts**: Automated reversion procedures
4. **Testing Protocol**: Comprehensive validation before production

## Timeline

- Week 1-2: Legacy analysis and documentation
- Week 3-4: Target architecture design
- Week 5-6: Migration script development
- Week 7: Testing and validation
- Week 8: Production migration

## Success Metrics

- [ ] 100% data integrity maintained
- [ ] Zero data loss during migration
- [ ] Performance benchmarks met
- [ ] All dependencies mapped and validated
- [ ] Rollback procedures tested and verified

## Notes

- All migration activities logged in `99_LOGS/migration/`
- Regular checkpoints established for validation
- Stakeholder communication plan in place
- Emergency contacts and procedures documented

**Last Updated**: September 2025  
**Document Version**: 1.0  
**Responsible Team**: Platform Engineering
