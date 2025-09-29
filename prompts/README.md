---
project: Career Intelligence Space
type: spec
status: matured
tags: [prompts, macros, automation, strategic_lenses]
updated: 2025-09-29
---

# Prompt Macros Index
A library of reusable Cursor Agent macros and strategic consultant lenses stored in this repo.  
Use these by opening the file, copying the block under the dashed lines, and pasting into **Chat with Repo**.

## Strategic Consultant Lenses
**STATUS: ACTIVE** | *Last Updated: 2025-09-29*

The `strategic_lenses/` folder contains reusable prompt templates that function like **consultant advisors** you can "call in" depending on the situation. Each lens provides a distinct analytical perspective:

> **⚠️ Activation Control:** To deactivate the lens system, set `system_status: inactive` in `strategic_lenses/config.yml` and update this README status.

- **01_strategic_analyst.md** — Broad, S-tier strategic review (weekly reviews, milestone assessments)
- **02_project_manager.md** — Task-level execution and timeline analysis (sprint planning, resource allocation)
- **03_systems_engineer.md** — Technical infrastructure and workflow optimization (bottleneck diagnosis, automation gaps)
- **04_productivity_coach.md** — Momentum, energy management, and sustainable workflow patterns (daily flow, habit formation)
- **05_venture_designer.md** — Market opportunities and strategic positioning (opportunity mapping, competitive analysis)

### When to Use Each Lens
- **Weekly Reviews** → Strategic Analyst + Project Manager
- **Technical Blockages** → Systems Engineer
- **Roadmap Planning** → Venture Designer + Strategic Analyst  
- **Daily Flow Issues** → Productivity Coach
- **Opportunity Assessment** → Venture Designer
- **Infrastructure Problems** → Systems Engineer

Each lens includes ChatGPT and Perplexity-optimized versions for consistent analysis across different AI tools.

---
## Session / Chronicle
- new-session-chronicle.md — Pipeline chat exports from ~/Downloads → 08_CHRONICLE/ with compliant frontmatter, commit, branch, PR, and auto-merge.
## PR Workflow
- git-commit-and-push.md — One-liner commit → branch → PR with auto-merge and recheck.
- pr-open-automerge.md — Open PR, enable squash auto-merge, re-run/recheck if needed.
- pr-stuck-checks-fixer.md — Diagnose failing checks, patch frontmatter/links, update branch, re-run jobs, enable auto-merge.
## Rebase / Conflict
- rebase-fixer.md (planned) — Resolve conflicts, continue rebase, push updated branch.
---
*Maintained by: jwade83*
