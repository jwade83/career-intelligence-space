#!/usr/bin/env python3
"""
Cross-link Guard for Decision Log Integration
Checks if a conversation ID is referenced in the Decision Log
"""

import sys
import re
import json
from pathlib import Path

def main():
    if len(sys.argv) < 2:
        print("usage: check_decision_links.py <conversation_id>")
        sys.exit(1)
    
    cid = sys.argv[1]
    log_path = Path("docs/decision-log.md")
    
    if not log_path.exists():
        print("WARN: decision-log missing")
        sys.exit(0)
    
    try:
        text = log_path.read_text()
        ok = re.search(re.escape(cid), text) is not None
        
        result = {
            "conversation_id": cid,
            "linked": ok,
            "decision_log_path": str(log_path)
        }
        
        print(json.dumps(result))
        sys.exit(0 if ok else 2)
        
    except Exception as e:
        print(f"Error reading decision log: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
