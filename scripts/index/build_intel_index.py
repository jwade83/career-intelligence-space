#!/usr/bin/env python3
"""
Intel Index Builder

Builds /intel/INDEX.md from all /intel/*.md files by parsing YAML front-matter.
Extracts metadata like date, title, type, status, tags, last_reviewed, link, promotion_path.
Generates a comprehensive markdown index with exactly one # UPGRADE at the end.
"""

import os
import re
from pathlib import Path
from datetime import datetime
import yaml

def parse_frontmatter(content):
    """Parse YAML front-matter from markdown content."""
    if not content.strip().startswith('---'):
        return {}, content
    
    parts = content.split('---', 2)
    if len(parts) < 3:
        return {}, content
    
    try:
        metadata = yaml.safe_load(parts[1])
        body = parts[2]
        return metadata or {}, body
    except yaml.YAMLError:
        return {}, content

def get_intel_files(intel_dir):
    """Get all .md files in the intel directory."""
    intel_path = Path(intel_dir)
    if not intel_path.exists():
        return []
    
    md_files = []
    for file in intel_path.glob('*.md'):
        if file.name != 'INDEX.md':  # Skip the index file itself
            md_files.append(file)
    
    return sorted(md_files)

def build_index(intel_dir='intel', output_file=None):
    """Build the intel index."""
    if output_file is None:
        output_file = os.path.join(intel_dir, 'INDEX.md')
    
    files = get_intel_files(intel_dir)
    
    if not files:
        print(f"No intel files found in {intel_dir}/")
        return
    
    # Parse all files
    entries = []
    for file_path in files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            metadata, _ = parse_frontmatter(content)
            
            # Build entry with available metadata
            entry = {
                'filename': file_path.name,
                'path': file_path,
                'date': metadata.get('date', 'Unknown'),
                'title': metadata.get('title', file_path.stem),
                'type': metadata.get('type', 'report'),
                'status': metadata.get('status', 'draft'),
                'tags': metadata.get('tags', []),
                'last_reviewed': metadata.get('last_reviewed', ''),
                'link': metadata.get('link', ''),
                'promotion_path': metadata.get('promotion_path', '')
            }
            entries.append(entry)
            
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            continue
    
    # Sort by date (newest first)
    entries.sort(key=lambda x: x.get('date', ''), reverse=True)
    
    # Generate INDEX.md content
    lines = []
    lines.append("# Intel Index")
    lines.append("")
    lines.append("Auto-generated index of all intelligence reports.")
    lines.append("")
    lines.append(f"*Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")
    lines.append("")
    
    if entries:
        lines.append("## Reports")
        lines.append("")
        
        for entry in entries:
            lines.append(f"### [{entry['title']}]({entry['filename']})")
            lines.append("")
            lines.append(f"- **Date:** {entry['date']}")
            lines.append(f"- **Type:** {entry['type']}")
            lines.append(f"- **Status:** {entry['status']}")
            
            if entry['tags']:
                if isinstance(entry['tags'], list):
                    tags_str = ', '.join(entry['tags'])
                else:
                    tags_str = str(entry['tags'])
                lines.append(f"- **Tags:** {tags_str}")
            
            if entry['last_reviewed']:
                lines.append(f"- **Last Reviewed:** {entry['last_reviewed']}")
            
            if entry['link']:
                lines.append(f"- **Link:** {entry['link']}")
            
            if entry['promotion_path']:
                lines.append(f"- **Promotion Path:** {entry['promotion_path']}")
            
            lines.append("")
    
    lines.append("# UPGRADE")
    
    # Write to file
    content = '\n'.join(lines)
    
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Generated {output_file} with {len(entries)} entries")

if __name__ == '__main__':
    build_index()
