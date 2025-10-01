#!/usr/bin/env bash
# Ensure required GitHub labels exist
# Usage: ./scripts/ensure_labels.sh

set -euo pipefail

echo "🏷️  Ensuring GitHub labels exist..."
echo ""

# Check if gh CLI is installed
if ! command -v gh &> /dev/null; then
    echo "⚠️  GitHub CLI (gh) not installed. Please install it first:"
    echo "   brew install gh"
    exit 1
fi

# Function to create label if it doesn't exist
create_label() {
    local name="$1"
    local color="$2"
    local description="$3"
    
    if gh label list | grep -q "^${name}"; then
        echo "✅ Label exists: ${name}"
    else
        gh label create "$name" --color "$color" --description "$description"
        echo "✅ Created label: ${name}"
    fi
}

# Create required labels for Future Silo system
create_label "future" "d4c5f9" "Future Silo - deferred project"
create_label "review" "fbca04" "Needs review or evaluation"
create_label "harness" "0e8a16" "Harness immune system related"
create_label "promotion" "ff6b6b" "Promoting from Future Silo to active docs"
create_label "automation" "1d76db" "Automation and CI/CD related"

echo ""
echo "🎉 All required labels ready!"

