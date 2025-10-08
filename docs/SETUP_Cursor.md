---
project: Career Intelligence Space
type: spec
status: matured
tags: [cursor, ide, setup, workflow, ci, prerequisites, bootstrap, repository]
updated: 2025-09-27
---

# Project Setup & Cursor IDE Configuration

## Prerequisites
- **Git**: Version control system
- **Cursor IDE**: AI-powered code editor
- **GitHub Account**: For repository access and PR management
- **Terminal Access**: For git operations and CI/CD workflows

## Repository Layout
The Career Intelligence Space follows a structured directory organization:
- `00_SANDBOX/` - Experimental work and design iterations
- `01_GUIDELINES/` - Project guidelines and frameworks
- `02_TEMPLATES/` - Reusable templates and formats
- `03_CHECKPOINTS/` - Project milestones and assessments
- `03_RESEARCH/` - Research findings and company intelligence
- `04_TOOLS/` - Decision matrices and tracking tools
- `05_ASSETS/` - Portfolio materials and case studies
- `05_EXPORTS/` - Published content and deliverables
- `06_CASES/` - Case studies and examples
- `08_CHRONICLE/` - Project chronicles and documentation
- `10_LLM_STREAMS/` - AI interaction logs and prompts
- `11_FUTURE/` - Future planning and hardware assets
- `99_LOGS/` - System logs and operational records

## Repo Path (Single-Clone, Dual-Interface)
Local clone used by both **Cursor** and **Terminal**:
```
/Users/johnwade/Desktop/career-intelligence-space
```
> Cursor and Terminal operate on the **same** working copy. All commits and PRs originate here.

## First-Time Use in Cursor
1. **Open repo**: `File → Open...` → select the path above.
2. **Verify Git**: Open the Git panel (left sidebar) → you should see your branch and changes.
3. **Safety check** (optional): In Terminal, run `git status` in this folder to confirm sync.

## Daily Flow (Cursor)
- **Edit** files (use Chat with Repo for patch-style diffs).
- **Stage** changes in Git panel.
- **Commit** with a Conventional Commit message.
- **Push**.
- **Open PR** and **Enable Auto-merge** (GitHub UI).

## When Checks Don't Attach
- On the PR page → **Run workflow** → select **recheck** → **Run**.
- Auto-merge will proceed once required checks pass.

## CI/OK + Recheck Workflow
- **Required Contexts**: `links` and `gate` must pass
- **Recheck Process**: 
  1. Go to PR page on GitHub
  2. Click "Re-run all checks" or "Re-run failed jobs"
  3. Wait for status checks to complete
  4. Auto-merge will trigger once all required contexts pass
- **Manual Override**: Use `ci/ok` comment to bypass checks (admin only)

## Repo Hygiene
- **Branch Protection**: Strict enforcement on main branch
- **Required Reviews**: At least one approval before merge
- **Status Checks**: All CI workflows must pass
- **Clean History**: Use squash merge for feature branches
- **Documentation**: Keep docs/ updated with any workflow changes

## Conventional Commits (Format)
```
<type>: <scope> - <summary>
```
Example:
```
docs: setup - add Cursor IDE setup notes
```

---
*Updated: 2025-09-27*
