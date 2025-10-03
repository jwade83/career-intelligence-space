#!/bin/bash

# Script to open all barometer review files in Cursor
# Usage: ./scripts/open_review_files.sh

echo "Opening barometer review files in Cursor..."

# Barometer review files
echo "Opening barometer review files..."
cursor 08_CHRONICLE/barometer/2025-10-03_Original_Barometer_Response_Word_for_Word.md
cursor 08_CHRONICLE/barometer/2025-10-03_System_Barometer_Review_scope_concern.md
cursor 08_CHRONICLE/barometer/2025-10-03_ChatGPT_Parallel_Review_Prompt.md

# Core sandboxing files
echo "Opening core sandboxing files..."
cursor 00_SANDBOX/systems/2025-10-03_Autopoietic_System_Evolution.md
cursor 00_SANDBOX/systems/2025-10-03_Emergent_Agentic_Role_Definition.md
cursor 00_SANDBOX/vision/2025-10-03_North_Star_AI_Human_Career_Collaboration_Platform.md
cursor 00_SANDBOX/systems/2025-10-03_Metacognitive_Awareness_System_Implementation.md

# Supporting context files
echo "Opening supporting context files..."
cursor 00_SANDBOX/systems/2025-10-03_Reflexive_Human_AI_Feedback_Loop.md
cursor 00_SANDBOX/design_philosophy/2025-10-03_Reflexive_System_Evolution.md
cursor 00_SANDBOX/meta_insights/2025-10-03_Developmental_Pattern_Recognition.md
cursor 00_SANDBOX/meta_insights/2025-10-03_Downloads_File_Nuance_Analysis.md

echo "All files opened! Check your Cursor tabs."
echo ""
echo "Next steps:"
echo "1. Review the files in the order they opened"
echo "2. Use the ChatGPT prompt (tab 3) for parallel analysis"
echo "3. Compare findings and provide your response"
