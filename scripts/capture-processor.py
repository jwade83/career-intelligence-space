#!/usr/bin/env python3
"""
Capture Processor for Field Agent Inbox
Processes raw captures from capture_inbox/ and promotes them to lite archives
"""

import os
import re
import yaml
import json
from pathlib import Path
from datetime import datetime
import hashlib

# Configuration
CAPTURE_INBOX = Path("08_CHRONICLE/capture_inbox")
LITE_ARCHIVES = Path("08_CHRONICLE/conversations/lite")
SCHEMA_FILE = Path("config/archive_schema.yml")

def load_schema():
    """Load archive schema configuration"""
    if not SCHEMA_FILE.exists():
        return {
            "version": 1,
            "required_conversation_archive_lite": ["conversation_date", "participants", "conversation_id"]
        }
    
    try:
        with open(SCHEMA_FILE, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f) or {}
    except Exception:
        return {
            "version": 1,
            "required_conversation_archive_lite": ["conversation_date", "participants", "conversation_id"]
        }

def detect_capture_type(file_path, content):
    """Detect capture type from file name and content"""
    filename = file_path.name.lower()
    
    if "photo" in filename or "image" in filename:
        return "photo_capture"
    elif "voice" in filename or "audio" in filename:
        return "voice_memo"
    elif "meeting" in filename:
        return "meeting_notes"
    else:
        return "mobile_note"

def generate_conversation_id(capture_id):
    """Generate conversation ID from capture ID"""
    # Convert raw_20251110_2215 to conv_2025_11_10_mobile_note_001
    match = re.match(r'raw_(\d{8})_(\d{4})', capture_id)
    if match:
        date_str = match.group(1)
        time_str = match.group(2)
        # Format: YYYY-MM-DD
        formatted_date = f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:8]}"
        return f"conv_{formatted_date.replace('-', '_')}_capture_{time_str}"
    return f"conv_{capture_id}"

def process_capture_file(file_path):
    """Process a single capture file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None
    
    # Extract frontmatter
    if not content.startswith("---"):
        print(f"Warning: {file_path} missing frontmatter")
        return None
    
    parts = content.split("\n---", 1)
    if len(parts) < 2:
        print(f"Warning: {file_path} malformed frontmatter")
        return None
    
    try:
        frontmatter = yaml.safe_load(parts[0].lstrip("-\n")) or {}
    except Exception as e:
        print(f"Error parsing frontmatter in {file_path}: {e}")
        return None
    
    body = parts[1].lstrip("-\n")
    
    # Detect capture type
    capture_type = detect_capture_type(file_path, body)
    
    # Generate conversation ID
    capture_id = frontmatter.get("capture_id", file_path.stem)
    conversation_id = generate_conversation_id(capture_id)
    
    # Create lite archive frontmatter
    lite_frontmatter = {
        "project": "Career Intelligence Space",
        "type": "conversation_archive_lite",
        "status": "active",
        "tags": ["conversation_archive", "lite", "field_agent", capture_type],
        "updated": frontmatter.get("capture_date", datetime.now().strftime("%Y-%m-%d")),
        "conversation_date": frontmatter.get("capture_date", datetime.now().strftime("%Y-%m-%d")),
        "participants": ["user", "field_agent"],
        "conversation_id": conversation_id,
        "timezone": "America/Los_Angeles",
        "related": [],
        "capture_metadata": {
            "original_capture_id": capture_id,
            "capture_type": capture_type,
            "processed_at": datetime.now().isoformat(),
            "source_file": str(file_path)
        }
    }
    
    # Create lite archive content
    lite_content = f"""---
{yaml.dump(lite_frontmatter, default_flow_style=False, sort_keys=False)}---

# {capture_type.replace('_', ' ').title()} — Lite Archive

## Summary
- **Captured:** {frontmatter.get('capture_date', 'Unknown date')}
- **Type:** {capture_type.replace('_', ' ').title()}
- **Source:** Field Agent Mobile Capture

## Content
{body}

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
- original_capture_id: {capture_id}
"""
    
    return lite_content, conversation_id

def process_capture_inbox():
    """Process all files in capture inbox"""
    if not CAPTURE_INBOX.exists():
        print(f"Capture inbox directory not found: {CAPTURE_INBOX}")
        return
    
    # Ensure lite archives directory exists
    LITE_ARCHIVES.mkdir(parents=True, exist_ok=True)
    
    processed_files = []
    
    # Process all markdown files in capture inbox
    for file_path in CAPTURE_INBOX.glob("*.md"):
        if file_path.name.startswith("TEMPLATE_") or file_path.name == "README.md":
            continue
        
        print(f"Processing {file_path.name}...")
        result = process_capture_file(file_path)
        
        if result:
            lite_content, conversation_id = result
            
            # Create lite archive file
            lite_filename = f"{conversation_id}.md"
            lite_path = LITE_ARCHIVES / lite_filename
            
            try:
                with open(lite_path, 'w', encoding='utf-8') as f:
                    f.write(lite_content)
                print(f"Created lite archive: {lite_path}")
                processed_files.append((file_path, lite_path))
            except Exception as e:
                print(f"Error writing lite archive {lite_path}: {e}")
        else:
            print(f"Failed to process {file_path.name}")
    
    return processed_files

def main():
    """Main processing function"""
    print("🔄 Processing Field Agent Capture Inbox...")
    
    processed_files = process_capture_inbox()
    
    if processed_files:
        print(f"✅ Processed {len(processed_files)} capture files")
        print("📋 Processed files:")
        for original, lite in processed_files:
            print(f"  {original.name} → {lite.name}")
        
        print("\n📝 Next steps:")
        print("1. Review generated lite archives")
        print("2. Run QA gates: make qa")
        print("3. Commit and push changes")
        print("4. Update Decision Log if strategic")
    else:
        print("ℹ️  No capture files to process")

if __name__ == "__main__":
    main()
