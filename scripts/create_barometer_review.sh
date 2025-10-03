#!/bin/bash

# System Barometer Review Creation Script
# Usage: ./scripts/create_barometer_review.sh [trigger_type] [session_focus]

set -e

# Configuration
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TEMPLATE_DIR="$REPO_ROOT/00_SANDBOX/templates/barometer"
OUTPUT_DIR="$REPO_ROOT/08_CHRONICLE/barometer"
TEMPLATE_FILE="$TEMPLATE_DIR/TEMPLATE_barometer_review.md"

# Input parameters
TRIGGER_TYPE="${1:-manual}"
SESSION_FOCUS="${2:-general_review}"
CURRENT_DATE=$(date +%Y-%m-%d)
CURRENT_PHASE="sandboxing"

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Generate filename
FILENAME="${CURRENT_DATE}_System_Barometer_Review_${TRIGGER_TYPE}.md"
OUTPUT_FILE="$OUTPUT_DIR/$FILENAME"

# Check if template exists
if [[ ! -f "$TEMPLATE_FILE" ]]; then
    echo "Error: Template file not found at $TEMPLATE_FILE"
    exit 1
fi

# Create the barometer review file
echo "Creating barometer review: $FILENAME"

# Copy template and replace placeholders
cp "$TEMPLATE_FILE" "$OUTPUT_FILE"

# Replace placeholders
sed -i.bak "s/\[date\]/$CURRENT_DATE/g" "$OUTPUT_FILE"
sed -i.bak "s/\[current_phase\]/$CURRENT_PHASE/g" "$OUTPUT_FILE"
sed -i.bak "s/\[Manual\/Automatic - specific trigger\]/$TRIGGER_TYPE/g" "$OUTPUT_FILE"
sed -i.bak "s/\[Date range or session focus\]/$SESSION_FOCUS/g" "$OUTPUT_FILE"

# Remove backup file
rm "$OUTPUT_FILE.bak"

echo "Barometer review created: $OUTPUT_FILE"
echo ""
echo "Next steps:"
echo "1. Review and edit the file: $OUTPUT_FILE"
echo "2. Conduct the meta-cognitive analysis"
echo "3. Fill in the key insights and recommendations"
echo "4. Prompt for user response and capture"
echo ""
echo "To open the file:"
echo "code $OUTPUT_FILE"
