#!/usr/bin/env python3
"""
Quick Capture Generator for Field Agent
Creates mobile capture files with minimal user input.
Usage: python3 scripts/quick-capture.py "Your content here"
"""

import sys
import os
from datetime import datetime
from pathlib import Path

def create_quick_capture(content, capture_type="quick_note"):
    """Create a quick capture file with auto-filled metadata"""
    
    # Generate timestamp
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M")
    
    # Create filename
    filename = f"raw_{timestamp}.md"
    capture_path = Path("08_CHRONICLE/capture_inbox") / filename
    
    # Auto-fill frontmatter
    frontmatter = f"""---
project: Career Intelligence Space
type: mobile_capture
status: raw
tags: [mobile_capture, field_agent, {capture_type}]
captured_at: {now.strftime("%Y-%m-%d")}
capture_type: {capture_type}
source: github_mobile
timestamp: {now.isoformat()}
---

# {capture_type.replace('_', ' ').title()}

## Content
{content}

---
**Field Agent Quick Capture - {timestamp}**"""

    # Write file
    capture_path.write_text(frontmatter)
    print(f"✅ Created capture: {capture_path}")
    return capture_path

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/quick-capture.py \"Your content here\"")
        print("Example: python3 scripts/quick-capture.py \"Had a great conversation with John about the project\"")
        sys.exit(1)
    
    content = sys.argv[1]
    capture_type = sys.argv[2] if len(sys.argv) > 2 else "quick_note"
    
    create_quick_capture(content, capture_type)

if __name__ == "__main__":
    main()
