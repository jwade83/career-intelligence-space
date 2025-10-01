#!/bin/bash
# Minimal validation plan for Future Silo system
# Run from repo root before merge

set -e

echo "🔍 Future Silo Validation Plan"
echo "================================"
echo ""

# 1) Lint schema + future_spec files
echo "Test 1: Frontmatter Linter"
echo "--------------------------"
python3 scripts/lint_frontmatter.py || {
    echo "❌ Frontmatter linter failed"
    exit 1
}
echo "✅ Frontmatter validation passed"
echo ""

# 2) Dry-run the pinger logic
echo "Test 2: Pinger Logic Dry-Run"
echo "----------------------------"
python3 - << 'PY'
import os, yaml, datetime
base="11_FUTURE"
today=datetime.date.today().isoformat()
hits=[]
for root,_,files in os.walk(base):
  for f in files:
    if f.endswith(".md"):
      p=os.path.join(root,f)
      try:
        t=open(p, encoding='utf-8').read()
        if t.startswith('---'):
          parts = t.split('---', 2)
          if len(parts) >= 2:
            fm=yaml.safe_load(parts[1]) or {}
            if fm.get('type')=='future_spec' and fm.get('review_date','') <= today:
              hits.append(p)
      except:
        pass

if hits:
  print(f"📋 DUE for review: {hits}")
else:
  print("✅ No files due for review (as expected - review_date in future)")
PY
echo ""

# 3) Verify schema exists
echo "Test 3: Schema Validation"
echo "-------------------------"
if [ -f "config/archive_schema.yml" ]; then
    if grep -q "future_spec" config/archive_schema.yml; then
        echo "✅ Schema file exists and contains future_spec type"
    else
        echo "❌ Schema file missing future_spec type"
        exit 1
    fi
else
    echo "❌ Schema file not found: config/archive_schema.yml"
    exit 1
fi
echo ""

# 4) Promotion script dry-run
echo "Test 4: Promotion Script Dry-Run"
echo "---------------------------------"
./scripts/promote_future_silo.sh hardware_assets --dry-run || {
    echo "❌ Promotion script dry-run failed"
    exit 1
}
echo "✅ Promotion script dry-run succeeded"
echo ""

# 5) Verify CODEOWNERS
echo "Test 5: CODEOWNERS Validation"
echo "------------------------------"
if [ -f ".github/CODEOWNERS" ]; then
    if grep -q "/11_FUTURE/\*\* @jwade83" .github/CODEOWNERS; then
        echo "✅ CODEOWNERS configured for /11_FUTURE"
    else
        echo "⚠️  CODEOWNERS might not cover /11_FUTURE correctly"
    fi
else
    echo "❌ CODEOWNERS file not found"
    exit 1
fi
echo ""

# 6) Verify workflows exist
echo "Test 6: Workflow Files"
echo "----------------------"
WORKFLOWS=(
    ".github/workflows/future-review-pinger.yml"
    ".github/workflows/frontmatter-lint.yml"
    ".github/workflows/pr-template-check.yml"
)

for workflow in "${WORKFLOWS[@]}"; do
    if [ -f "$workflow" ]; then
        echo "✅ $workflow exists"
    else
        echo "❌ $workflow missing"
        exit 1
    fi
done
echo ""

# Summary
echo "================================"
echo "🎉 All validation tests passed!"
echo ""
echo "Ready for deployment. Next steps:"
echo "1. Run: ./scripts/ensure_labels.sh (requires gh CLI)"
echo "2. Merge to main"
echo "3. Monitor first cron run (12:00 UTC daily)"
echo "4. Create test PR touching /11_FUTURE to verify CI enforcement"
echo ""

