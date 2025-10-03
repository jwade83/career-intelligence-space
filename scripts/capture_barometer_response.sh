#!/bin/bash

# Barometer Response Capture Script
# Usage: ./scripts/capture_barometer_response.sh [barometer_file] [user_response]

set -e

# Configuration
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BAROMETER_FILE="$1"
USER_RESPONSE="$2"
CURRENT_DATE=$(date +%Y-%m-%d)

# Check if barometer file exists
if [[ ! -f "$BAROMETER_FILE" ]]; then
    echo "Error: Barometer file not found at $BAROMETER_FILE"
    exit 1
fi

# Check if user response is provided
if [[ -z "$USER_RESPONSE" ]]; then
    echo "Error: User response is required"
    echo "Usage: ./scripts/capture_barometer_response.sh [barometer_file] [user_response]"
    exit 1
fi

# Create temporary file for response processing
TEMP_FILE=$(mktemp)

# Add user response to barometer file
echo "**User Response**: $USER_RESPONSE" >> "$TEMP_FILE"
echo "**Response Date**: $CURRENT_DATE" >> "$TEMP_FILE"
echo "" >> "$TEMP_FILE"

# Add action items section
echo "**Action Items**: [To be filled based on user response]" >> "$TEMP_FILE"

# Append to barometer file
cat "$TEMP_FILE" >> "$BAROMETER_FILE"

# Clean up
rm "$TEMP_FILE"

echo "User response captured in: $BAROMETER_FILE"
echo ""
echo "Next steps:"
echo "1. Review the user response"
echo "2. Generate specific action items based on the response"
echo "3. Update the action items section"
echo "4. Commit the changes"
