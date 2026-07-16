---
project: Career Intelligence Space
type: spec
status: draft
tags: [meta, agents]
updated: 2026-07-16
---

# AGENTS.md

## Cursor Cloud specific instructions

This repository is a documentation / knowledge-management system ("Career
Intelligence Space"), **not** a long-running web or backend service. The
"application" is a set of Python CLI tools + shell scripts (in `scripts/` and
`.github/scripts/`) that lint, validate, and build indexes over the Markdown
content. There is no dev server to start.

Environment facts (the startup update script already runs `pip install pyyaml
pytest requests`):
- Python 3 is used. Only third-party deps are `pyyaml`, `requests`, and
  `pytest` (test-only). `pyyaml`/`requests` ship with the base image.
- `yq` (mikefarah) is available at `/usr/bin/yq`; the `Agent CI` workflow uses
  it to validate `agents/*.yml` and `tasks/*.yml`.

How to test / lint / run (see `.github/workflows/` for the authoritative CI):
- Tests: `python3 -m pytest -q scripts/tests/test_linter.py` (also
  `scripts/test_mobile_copilot_capture.py`, `scripts/test_rich_interactions.py`).
- Frontmatter lint: `python3 scripts/lint_frontmatter.py`. NOTE: this exits
  non-zero when it finds **stale content** (e.g. `future_spec` docs whose
  `review_date` is now in the past). That is a content signal, not a broken
  environment — do not "fix" it as part of setup.
- Internal link check: `python3 .github/scripts/linkcheck.py` (internal links
  only, no network needed).
- Invariants audit: `python3 .github/scripts/invariants_audit.py` (warn-only,
  always exits 0).
- Index builders (representative "app" action) write `INDEX.md` files, e.g.
  `python3 scripts/index/build_intel_index.py` regenerates `intel/INDEX.md`.

Gotchas:
- Running pytest/scripts creates `__pycache__/` and `.pytest_cache/` which are
  **not** in `.gitignore`. Do not commit them.
- The `harness/` submodule (`cis-harness`) is empty/uninitialized here; the
  tooling above does not require it.
