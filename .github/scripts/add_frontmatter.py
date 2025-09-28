#!/usr/bin/env python3
"""
Frontmatter Helper Script
Adds compliant frontmatter to Markdown files that don't have it.
"""

import os
import sys
import re
from pathlib import Path
from datetime import datetime

# Load allowed values from ONTOLOGY.yml
def load_ontology():
    p = Path("docs/ONTOLOGY.yml")
    if not p.exists():
        return {"types":["capsule","memo","assessment","log","decision","spec"],
                "statuses":["draft","matured","archived"],
                "projects":["Career Intelligence Space"]}
    t = p.read_text(encoding="utf-8", errors="ignore")
    
    def load_list(yaml_text, key):
        m = re.search(rf"(?m)^{key}:\s*\n((?:\s*-\s*[A-Za-z0-9_\-]+\s*\n)+)", yaml_text)
        if not m: return []
        return re.findall(r"-\s*([A-Za-z0-9_\-]+)", m.group(1))
    
    return {"types": load_list(t,"types") or ["capsule","memo","assessment","log","decision","spec"],
            "statuses": load_list(t,"statuses") or ["draft","matured","archived"],
            "projects": load_list(t,"projects") or ["Career Intelligence Space"]}

# Check if file already has frontmatter
def has_frontmatter(content):
    return content.strip().startswith('---\n') and '---\n' in content[4:]

# Generate frontmatter based on file path and content
def generate_frontmatter(file_path, content):
    ontology = load_ontology()
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Determine type based on path
    if "08_CHRONICLE" in str(file_path):
        file_type = "log"
        status = "matured"
        tags = ["chronicle", "session"]
    elif "docs/" in str(file_path):
        file_type = "spec"
        status = "matured"
        tags = ["docs"]
    elif "prompts/" in str(file_path):
        file_type = "spec"
        status = "matured"
        tags = ["prompts", "macros"]
    elif "assessments/" in str(file_path):
        file_type = "assessment"
        status = "draft"
        tags = ["assessment"]
    else:
        file_type = "spec"
        status = "draft"
        tags = ["misc"]
    
    # Add more specific tags based on filename
    filename = Path(file_path).stem.lower()
    if "setup" in filename:
        tags.append("setup")
    elif "runbook" in filename:
        tags.append("runbook")
    elif "template" in filename:
        tags.append("template")
    elif "readme" in filename:
        tags.append("index")
    
    return f"""---
project: Career Intelligence Space
type: {file_type}
status: {status}
tags: {tags}
updated: {today}
---"""

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 add_frontmatter.py <file1> [file2] ...")
        print("       python3 add_frontmatter.py --all  # Process all .md files")
        sys.exit(1)
    
    files_to_process = []
    
    if sys.argv[1] == "--all":
        # Find all .md files that need frontmatter
        for md_file in Path(".").rglob("*.md"):
            if ".git" in str(md_file):
                continue
            try:
                content = md_file.read_text(encoding="utf-8")
                if not has_frontmatter(content):
                    files_to_process.append(md_file)
            except Exception as e:
                print(f"Warning: Could not read {md_file}: {e}")
    else:
        files_to_process = [Path(f) for f in sys.argv[1:]]
    
    if not files_to_process:
        print("No files need frontmatter added.")
        return
    
    for file_path in files_to_process:
        try:
            content = file_path.read_text(encoding="utf-8")
            
            if has_frontmatter(content):
                print(f"✅ {file_path} already has frontmatter")
                continue
            
            frontmatter = generate_frontmatter(file_path, content)
            new_content = frontmatter + "\n\n" + content
            
            # Backup original
            backup_path = file_path.with_suffix(file_path.suffix + ".backup")
            file_path.rename(backup_path)
            
            # Write new content
            file_path.write_text(new_content, encoding="utf-8")
            
            print(f"✅ Added frontmatter to {file_path}")
            print(f"   Backup saved as {backup_path}")
            
        except Exception as e:
            print(f"❌ Error processing {file_path}: {e}")

if __name__ == "__main__":
    main()
