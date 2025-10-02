#!/usr/bin/env bash
set -euo pipefail

# --- CONFIG ---
OWNER="${OWNER:-jwade83}"
REPO="${REPO:-career-intelligence-space}"
OUTDIR="reports"
TS="$(date -u +%Y-%m-%dT%H-%M-%SZ)"
OUT="$OUTDIR/snapshot_$TS.md"

mkdir -p "$OUTDIR"

have() { command -v "$1" >/dev/null 2>&1; }
section() { printf "\n## %s\n\n" "$1" >> "$OUT"; }

# Header
{
  echo "# Daily Repo Snapshot — $TS (UTC)"
  echo
  echo "- Repo: $OWNER/$REPO"
  echo "- Host: $(uname -a | sed 's/  */ /g')"
  echo "- PWD:  $(pwd)"
  echo
} > "$OUT"

# 1) Git status & remotes
section "Git Status"
{
  echo '```'
  git status -sb || true
  echo
  echo "# Remotes"
  git remote -v || true
  echo '```'
} >> "$OUT"

# 2) Recent commits & changes
section "Recent Commits (last 20)"
{
  echo '```'
  git log --oneline -n 20 || true
  echo '```'
} >> "$OUT"

section "Files Changed in Last 72h"
{
  echo '```'
  git log --since="72 hours ago" --name-only --pretty=format: \
    | sort -u | sed '/^$/d' || true
  echo '```'
} >> "$OUT"

# 3) Untracked & modified files
section "Working Tree Delta"
{
  echo '```'
  echo "# Modified (not staged):"
  git ls-files -m || true
  echo
  echo "# Untracked:"
  git ls-files --others --exclude-standard || true
  echo '```'
} >> "$OUT"

# 4) Large files in tree (top 25)
section "Largest Files (Tree, top 25)"
{
  echo '```'
  du -ah . 2>/dev/null | sort -h | tail -n 25 || true
  echo '```'
} >> "$OUT"

# 5) Large blobs in history (top 15) — optional / best-effort
section "Largest Blobs in Git History (top 15)"
{
  echo '```'
  git rev-list --objects --all \
    | git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' \
    | awk '$1=="blob"{print $3 "\t" $2 "\t" $4}' \
    | sort -nr | head -n 15 || true
  echo
  echo "# Columns: size(bytes)  sha  path"
  echo '```'
} >> "$OUT"

# 6) Workflows (requires gh)
section "GitHub Workflows (gh workflow list)"
if have gh; then
  {
    echo '```'
    gh workflow list || true
    echo '```'
  } >> "$OUT"
else
  echo "_gh not found; skipping workflow sections_" >> "$OUT"
fi

# 7) Last run per workflow (requires gh + jq)
section "Latest Run per Workflow"
if have gh && have jq; then
  {
    echo '| Workflow | Title | Status | Conclusion | URL |'
    echo '|---|---|---|---|---|'
    gh api "repos/$OWNER/$REPO/actions/workflows" \
    | jq -r '.workflows[] | [.name, .id] | @tsv' \
    | while IFS=$'\t' read -r NAME ID; do
        RUN=$(gh api "repos/$OWNER/$REPO/actions/workflows/$ID/runs" -F per_page=1 \
          | jq -r '.workflow_runs[0] | [.name, .display_title, .status, .conclusion, .html_url] | @tsv')
        if [ -n "$RUN" ]; then
          IFS=$'\t' read -r N T S C U <<<"$RUN"
          printf '| %s | %s | %s | %s | %s |\n' "$N" "$T" "$S" "${C:-null}" "$U"
        fi
      done
  } >> "$OUT"
else
  echo "_gh and/or jq not found; skipping last-run table_" >> "$OUT"
fi

# 8) Failing runs (last 15, requires gh + jq)
section "Recent Failing Runs (last 15)"
if have gh && have jq; then
  {
    gh api "repos/$OWNER/$REPO/actions/runs?per_page=50" \
    | jq -r '.workflow_runs[] | select(.conclusion=="failure" or .conclusion=="timed_out" or .conclusion=="cancelled") | [.name, .display_title, .status, .conclusion, .html_url, .run_attempt] | @tsv' \
    | head -n 15 \
    | awk -F'\t' 'BEGIN{print "| Workflow | Title | Status | Conclusion | URL | Attempt |"; print "|---|---|---|---|---|---|"} {printf "| %s | %s | %s | %s | %s | %s |\n", $1,$2,$3,$4,$5,$6}'
  } >> "$OUT"
else
  echo "_gh and/or jq not found; skipping failing runs_" >> "$OUT"
fi

# 9) Open PRs & recently merged (requires gh + jq)
section "Pull Requests (Open, last 20)"
if have gh; then
  {
    echo '```'
    gh pr list --state open --limit 20 || true
    echo '```'
  } >> "$OUT"
fi

section "Pull Requests (Merged last 7 days)"
if have gh && have jq; then
  {
    gh pr list --state merged --limit 100 --search "merged:>=`date -v-7d +%Y-%m-%d`" --json number,title,mergedAt,url \
      | jq -r '.[] | "- PR #\(.number): \(.title) — \(.mergedAt) — \(.url)"'
  } >> "$OUT"
fi

# 10) Issues (Open, last 20) — optional (public repos)
section "Issues (Open, last 20)"
if have gh; then
  {
    echo '```'
    gh issue list --state open --limit 20 || true
    echo '```'
  } >> "$OUT"
fi

# 11) Lint: YAML, Markdown, Frontmatter (best-effort)
section "Lint: YAML / Markdown / Frontmatter (counts only)"
{
  echo '```'
  if have yamllint; then
    echo "# yamllint:"
    yamllint .github/workflows 2>&1 | wc -l | awk '{print "offenses(lines): "$1}'
  else
    echo "yamllint not installed"
  fi

  if have markdownlint; then
    echo "# markdownlint:"
    markdownlint "**/*.md" --ignore "_site/**" 2>&1 | wc -l | awk '{print "offenses(lines): "$1}'
  else
    echo "markdownlint not installed"
  fi

  if have python; then
    if [ -f scripts/lint_frontmatter.py ]; then
      echo "# frontmatter (lint_frontmatter.py):"
      python scripts/lint_frontmatter.py >/tmp/frontmatter_lint.txt 2>&1 || true
      wc -l </tmp/frontmatter_lint.txt | awk '{print "report(lines): "$1}'
    else
      echo "frontmatter linter not found"
    fi
  else
    echo "python not installed"
  fi
  echo '```'
} >> "$OUT"

# 12) Workflow name normalization (filename vs name)
section "Workflow Name Map (filename → displayed name)"
{
  echo '```'
  ls .github/workflows/*.yml .github/workflows/*.yaml 2>/dev/null | while read -r f; do
    # Extract "name:" if present, otherwise print filename
    n=$(grep -E '^[[:space:]]*name:' "$f" | head -n1 | sed 's/^[[:space:]]*name:[[:space:]]*//')
    printf "%-50s -> %s\n" "$(basename "$f")" "${n:-<no name (file name shown in GH)>}"
  done
  echo '```'
} >> "$OUT"

# Footer
{
  echo
  echo "_Generated by scripts/ci/repo_snapshot.sh_"
} >> "$OUT"

echo "Wrote $OUT"
