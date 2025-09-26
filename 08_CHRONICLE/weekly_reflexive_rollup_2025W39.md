# Reflexive Rollup — 2025W39

## Stress Signals (last 7 days)
- capsules_added: 5
- capsule_growth_rate: 5.0
- index_missing_entries: 0
- broken_internal_links: 34
- tag_entropy: 0.0
- top5_tag_coverage_pct: 0.0
- oov_tag_rate_pct: 0.0
- collapse_events_count: 0
- override_count: 0
- frustration_events: 0
- context_reprime_events: 0
- days_since_last_checkpoint: 0

## Notes
- Budget-capped & offline; advanced metrics skipped if runtime exceeds budget.
- brownout: false

## Next Actions
- If 2+ signals trend up for 2 weeks, consult `harness/docs/OPS_PROMOTION.yml` to consider promotion.
- If index_missing_entries > 0, verify auto-index or update `08_CHRONICLE/INDEX.md`.
- If oov_tag_rate_pct is high, update `docs/TAGS_REGISTRY.yml` and/or `docs/ONTOLOGY.yml`.
- If days_since_last_checkpoint is high with heavy change, tag a new checkpoint.