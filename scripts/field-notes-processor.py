#!/usr/bin/env python3
"""
Field Notes Processor - Phase 1 MVP
Processes FIELD_NOTES.md nightly and creates timestamped captures with full Harness compliance.
"""

import os
import re
import yaml
from datetime import datetime, timezone
from pathlib import Path

# Configuration
FIELD_NOTES_PATH = Path("08_CHRONICLE/field/FIELD_NOTES.md")
PROCESSED_DIR = Path("08_CHRONICLE/field/processed")
LITE_ARCHIVES_DIR = Path("08_CHRONICLE/conversations/lite")

def load_field_notes():
    """Load and parse FIELD_NOTES.md"""
    if not FIELD_NOTES_PATH.exists():
        print("❌ FIELD_NOTES.md not found")
        return None, None
    
    content = FIELD_NOTES_PATH.read_text()
    
    # Extract frontmatter
    frontmatter_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if not frontmatter_match:
        print("❌ No frontmatter found in FIELD_NOTES.md")
        return None, None
    
    frontmatter = yaml.safe_load(frontmatter_match.group(1))
    
    # Extract today's notes
    today_section = re.search(r'## Today\'s Notes\n(.*?)\n---', content, re.DOTALL)
    if not today_section:
        print("❌ No 'Today's Notes' section found")
        return None, None
    
    today_notes = today_section.group(1).strip()
    
    # Check if there's actual content (not just placeholder)
    if "[Use voice-to-text here" in today_notes:
        print("ℹ️ No new content to process")
        return None, None
    
    return frontmatter, today_notes

def create_timestamped_capture(content, timestamp):
    """Create timestamped capture file"""
    capture_filename = f"raw_{timestamp}.md"
    capture_path = PROCESSED_DIR / capture_filename
    
    # Create capture file
    capture_content = f"""---
project: Career Intelligence Space
type: mobile_capture
status: raw
tags: [mobile_capture, field_agent, field_notes]
captured_at: {datetime.now().strftime('%Y-%m-%d')}
capture_type: field_notes
source: github_mobile
timestamp: {datetime.now(timezone.utc).isoformat()}
---

# Field Notes Capture

## Content
{content}

---
**Field Agent Field Notes - {timestamp}**"""

    capture_path.write_text(capture_content)
    print(f"✅ Created capture: {capture_filename}")
    return capture_path

def create_lite_archive(capture_path, timestamp):
    """Create Harness-compliant lite archive"""
    conversation_id = f"conv_{timestamp.replace('_', '_')}"
    archive_filename = f"{conversation_id}.md"
    archive_path = LITE_ARCHIVES_DIR / archive_filename
    
    # Read capture content
    capture_content = capture_path.read_text()
    
    # Extract content section
    content_match = re.search(r'## Content\n(.*?)\n---', capture_content, re.DOTALL)
    if not content_match:
        print("❌ Could not extract content from capture")
        return None
    
    content = content_match.group(1).strip()
    
    # Create lite archive
    archive_content = f"""---
project: Career Intelligence Space
type: conversation_archive_lite
status: active
tags:
- conversation_archive
- lite
- field_agent
- field_notes
updated: {datetime.now().strftime('%Y-%m-%d')}
conversation_date: {datetime.now().strftime('%Y-%m-%d')}
participants:
- user
- field_agent
conversation_id: {conversation_id}
timezone: America/Los_Angeles
related: []
capture_metadata:
  original_capture_id: raw_{timestamp}
  capture_type: field_notes
  processed_at: {datetime.now(timezone.utc).isoformat()}
  source_file: {capture_path}
---

# Field Notes — Lite Archive

## Summary
- **Captured:** {datetime.now().strftime('%Y-%m-%d')}
- **Type:** Field Notes
- **Source:** Field Agent Mobile Capture

## Content
{content}

## Next Steps
- [ ] Review and refine content
- [ ] Add to Decision Log if strategic
- [ ] Link to related archives
- [ ] Archive or promote to full conversation

---

**Traceability**
- conversation_id: {conversation_id}
- decision_log: docs/decision-log.md (search for the conversation_id)
- chronicle_path: 08_CHRONICLE/conversations/lite/
- schema_version: v1
- original_capture_id: raw_{timestamp}"""

    archive_path.write_text(archive_content)
    print(f"✅ Created lite archive: {archive_filename}")
    return archive_path

def reset_field_notes(frontmatter, today_notes):
    """Reset FIELD_NOTES.md with new content in history"""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M')
    
    # Create new content
    new_content = f"""---
project: Career Intelligence Space
type: field_notes
status: active
tags: [field_notes, mobile_capture, persistent]
updated: {datetime.now().strftime('%Y-%m-%d')}
---

# Field Notes - Daily Capture

## Today's Notes
[Use voice-to-text here - speak your thoughts and they'll appear here]

---

## Previous Days
### {timestamp}
{today_notes}

---
**Field Agent Daily Capture - Always Ready for Voice Input**"""

    FIELD_NOTES_PATH.write_text(new_content)
    print("✅ Reset FIELD_NOTES.md for next day")

def main():
    """Main processing function"""
    print("🔄 Starting Field Notes Processor...")
    
    # Ensure directories exist
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    LITE_ARCHIVES_DIR.mkdir(parents=True, exist_ok=True)
    
    # Load field notes
    frontmatter, today_notes = load_field_notes()
    if not frontmatter or not today_notes:
        return
    
    # Create timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M')
    
    # Create timestamped capture
    capture_path = create_timestamped_capture(today_notes, timestamp)
    if not capture_path:
        return
    
    # Create lite archive
    archive_path = create_lite_archive(capture_path, timestamp)
    if not archive_path:
        return
    
    # Reset field notes
    reset_field_notes(frontmatter, today_notes)
    
    print("✅ Field Notes processing complete!")

if __name__ == "__main__":
    main()
