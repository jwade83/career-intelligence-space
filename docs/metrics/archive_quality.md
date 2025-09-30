---
project: Career Intelligence Space
type: metrics
status: active
tags: [metrics, archive_quality, harness, monitoring]
updated: 2025-11-10
timezone: "America/Los_Angeles"
---

# Archive Quality Metrics

This document tracks key metrics for the Harness archive system to ensure it's working effectively and providing value.

## Current Metrics (2025-11-10)

### Lint Pass Rate
- **Target:** ≥95%
- **Current:** 100% (2/2 archives pass)
- **Status:** ✅ **EXCELLENT**

### Average Time to Fix Failing Archive
- **Target:** <10 minutes
- **Current:** N/A (no failures yet)
- **Status:** ✅ **NO DATA** (good problem to have)

### PII False-Positive Rate
- **Target:** Falling over time
- **Current:** 0% (no false positives detected)
- **Status:** ✅ **EXCELLENT**

### Decision Log Linkage Rate
- **Target:** 100%
- **Current:** 100% (2/2 archives linked)
- **Status:** ✅ **EXCELLENT**

### Discoverability Check
- **Target:** 100% for full archives
- **Current:** 100% (2/2 full archives listed in index)
- **Status:** ✅ **EXCELLENT**

## Archive Inventory

### Full Archives (2)
1. **harness_architecture_and_implementation_strategy** - 2025-11-10
2. **harness_archive_qa_smoke** - 2025-11-10

### Lite Archives (0)
- None yet

### Total Archives: 2
- **Full:** 2
- **Lite:** 0

## Schema Compliance

### Schema Version: 1
- **Last Updated:** 2025-11-10
- **Compliance Rate:** 100%
- **Breaking Changes:** 0

## Quality Trends

### Week of 2025-11-10
- **New Archives:** 2
- **Lint Failures:** 0
- **PII Issues:** 0
- **Schema Violations:** 0
- **Decision Log Updates:** 2

## Action Items

### Immediate (This Week)
- [ ] Test schema versioning with a breaking change
- [ ] Validate allowlist effectiveness with synthetic data
- [ ] Create first lite archive as proof of concept

### Ongoing (Monthly)
- [ ] Review and tune PII allowlist
- [ ] Audit archive discoverability
- [ ] Update metrics baseline
- [ ] Review schema evolution needs

## Success Criteria

### System Health Indicators
- ✅ **Lint pass rate** ≥95%
- ✅ **PII protection** active and effective
- ✅ **Schema compliance** 100%
- ✅ **Decision log linkage** 100%
- ✅ **Discoverability** 100%

### Quality Gates
- ✅ **New archives** must pass linting
- ✅ **PII scanning** must pass before commit
- ✅ **Decision log** must be updated for new archives
- ✅ **Archive index** must be updated for full archives

## Notes

- **System Status:** Production-ready and fully operational
- **Risk Level:** Low (all metrics green)
- **Next Review:** 2025-12-10 (monthly)
- **Maintenance:** Automated via CI/CD and pre-commit hooks
