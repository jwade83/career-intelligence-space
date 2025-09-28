#!/usr/bin/env python3
"""
Pre-commit hook to check frontmatter compliance
Run this before committing to catch issues early.
"""

import os
import sys
import subprocess
from pathlib import Path

def run_frontmatter_gate():
    """Run the frontmatter gate script and return success/failure"""
    try:
        result = subprocess.run([
            sys.executable, 
            ".github/scripts/frontmatter_gate.py"
        ], capture_output=True, text=True, cwd=Path.cwd())
        
        if result.returncode == 0:
            print("✅ Frontmatter gate passed!")
            return True
        else:
            print("❌ Frontmatter gate failed:")
            print(result.stdout)
            print(result.stderr)
            return False
    except Exception as e:
        print(f"❌ Error running frontmatter gate: {e}")
        return False

def main():
    print("🔍 Running frontmatter compliance check...")
    
    if run_frontmatter_gate():
        print("✅ All files have compliant frontmatter!")
        sys.exit(0)
    else:
        print("\n💡 To fix frontmatter issues:")
        print("   python3 .github/scripts/add_frontmatter.py --all")
        print("   # or for specific files:")
        print("   python3 .github/scripts/add_frontmatter.py <file1> <file2> ...")
        sys.exit(1)

if __name__ == "__main__":
    main()
