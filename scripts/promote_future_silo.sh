#!/bin/bash
# Idempotent promotion script for Future Silo → Active Docs
# Usage: ./scripts/promote_future_silo.sh <silo_name>

set -e

SILO_NAME="${1:-hardware_assets}"
SOURCE_DIR="11_FUTURE/${SILO_NAME}"
TARGET_DIR="docs/architecture/harness/${SILO_NAME}"
DECISION_LOG="docs/DECISION_LOG.md"
DATE=$(date +%Y-%m-%d)
TIMESTAMP=$(date +%Y%m%d-%H%M%S)

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}🚀 Future Silo Promotion Script${NC}"
echo "=================================="
echo ""

# Validate source exists
if [ ! -d "$SOURCE_DIR" ]; then
    echo -e "${RED}❌ Error: Source directory not found: $SOURCE_DIR${NC}"
    exit 1
fi

echo -e "${YELLOW}📦 Promoting: ${SOURCE_DIR} → ${TARGET_DIR}${NC}"
echo ""

# Step 1: Create target directory
echo "Step 1: Creating target directory..."
mkdir -p "$TARGET_DIR"
echo -e "${GREEN}✅ Target directory ready${NC}"
echo ""

# Step 2: Copy files (idempotent - will overwrite)
echo "Step 2: Copying files..."
cp -r "$SOURCE_DIR"/* "$TARGET_DIR/"
echo -e "${GREEN}✅ Files copied${NC}"
echo ""

# Step 3: Update frontmatter status from 'deferred' to 'active'
echo "Step 3: Updating frontmatter status..."
find "$TARGET_DIR" -name "*.md" -type f -exec sed -i '' 's/^status: deferred$/status: active/' {} \;
echo -e "${GREEN}✅ Frontmatter updated${NC}"
echo ""

# Step 4: Create Decision Log entry
echo "Step 4: Adding Decision Log entry..."
DECISION_ENTRY="
### ${DATE} — Activate ${SILO_NAME}

- **Decision:** Promote \`/${SOURCE_DIR}/\` → \`${TARGET_DIR}/\`
- **Rationale:** Activation triggers met (see TODOs.md for criteria)
- **Alternatives:** Maintain as deferred (rejected: triggers indicate readiness)
- **Reversibility:** High — rollback via checkpoint tag \`checkpoint/${SILO_NAME}-activation-${TIMESTAMP}\`
- **Success Criteria:** Implementation of MVI-1 antibodies; weekly stress tests operational
- **Related:** FUTURE_HARDWARE_ASSETS_HOME, HARNESS_ADDENDUM_HARDWARE_ASSET_ROADMAP

---
"

# Check if entry already exists (idempotent)
if grep -q "Activate ${SILO_NAME}" "$DECISION_LOG" 2>/dev/null; then
    echo -e "${YELLOW}⚠️  Decision Log entry already exists (skipping)${NC}"
else
    # Insert before the template section
    if [ -f "$DECISION_LOG" ]; then
        # Find the line number of "## Template for Future Activation Decision"
        LINE_NUM=$(grep -n "## Template for Future Activation Decision" "$DECISION_LOG" | cut -d: -f1)
        if [ -n "$LINE_NUM" ]; then
            # Insert before the template
            sed -i '' "${LINE_NUM}i\\
$DECISION_ENTRY
" "$DECISION_LOG"
        else
            # Append to end
            echo "$DECISION_ENTRY" >> "$DECISION_LOG"
        fi
        echo -e "${GREEN}✅ Decision Log updated${NC}"
    else
        echo -e "${YELLOW}⚠️  Decision Log not found (skipping)${NC}"
    fi
fi
echo ""

# Step 5: Create checkpoint tag
echo "Step 5: Creating checkpoint tag..."
TAG_NAME="checkpoint/${SILO_NAME}-activation-${TIMESTAMP}"
git add -A
git commit -m "feat: Promote ${SILO_NAME} from Future Silo to active docs

- Copied from ${SOURCE_DIR} → ${TARGET_DIR}
- Updated frontmatter status: deferred → active
- Added Decision Log entry
- Checkpoint tag: ${TAG_NAME}

Activation triggered by: [specify trigger from TODOs.md]" || echo -e "${YELLOW}⚠️  No changes to commit${NC}"

git tag -a "$TAG_NAME" -m "Checkpoint: ${SILO_NAME} activation at ${TIMESTAMP}" || echo -e "${YELLOW}⚠️  Tag already exists${NC}"
echo -e "${GREEN}✅ Checkpoint tag created: ${TAG_NAME}${NC}"
echo ""

# Step 6: Create promotion PR
echo "Step 6: Creating promotion branch and PR..."
BRANCH_NAME="feat/promote-${SILO_NAME}-${TIMESTAMP}"
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)

# Only create new branch if not already on it
if [ "$CURRENT_BRANCH" != "$BRANCH_NAME" ]; then
    git checkout -b "$BRANCH_NAME" 2>/dev/null || git checkout "$BRANCH_NAME"
    echo -e "${GREEN}✅ Branch created: ${BRANCH_NAME}${NC}"
else
    echo -e "${YELLOW}⚠️  Already on promotion branch${NC}"
fi

echo ""
echo -e "${GREEN}🎉 Promotion Complete!${NC}"
echo ""
echo "Next steps:"
echo "1. Review changes: git diff main"
echo "2. Push branch: git push origin ${BRANCH_NAME}"
echo "3. Open PR with label 'promotion'"
echo "4. Update Chronicle with activation note"
echo ""
echo "Rollback command (if needed):"
echo "  git checkout ${TAG_NAME}"
echo ""

