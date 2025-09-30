#!/usr/bin/env python3
"""
Update QUICK_INPUT.md with current date
Run this to refresh the date before mobile use
"""

from datetime import datetime
from pathlib import Path

def update_quick_input():
    """Update QUICK_INPUT.md with current date"""
    
    quick_input_path = Path("08_CHRONICLE/capture_inbox/QUICK_INPUT.md")
    
    if not quick_input_path.exists():
        print("❌ QUICK_INPUT.md not found")
        return False
    
    # Read current content
    content = quick_input_path.read_text()
    
    # Update date
    today = datetime.now().strftime("%Y-%m-%d")
    updated_content = content.replace(
        "captured_at: 2025-11-10",
        f"captured_at: {today}"
    )
    
    # Write updated content
    quick_input_path.write_text(updated_content)
    print(f"✅ Updated QUICK_INPUT.md with date: {today}")
    return True

if __name__ == "__main__":
    update_quick_input()
