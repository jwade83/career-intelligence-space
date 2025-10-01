#!/usr/bin/env python3
"""
Frontmatter Linter for Career Intelligence Space
Validates frontmatter across the repository, with special rules for future_spec types
"""

import os
import sys
import yaml
from pathlib import Path
from datetime import date, timedelta

def load_schema():
    """Load archive schema configuration"""
    schema_file = Path("config/archive_schema.yml")
    if not schema_file.exists():
        print(f"❌ FATAL: Schema file not found: {schema_file}")
        print("   The frontmatter linter requires config/archive_schema.yml to function.")
        sys.exit(1)
    
    try:
        with open(schema_file, 'r', encoding='utf-8') as f:
            schema = yaml.safe_load(f) or {}
            if not schema:
                print(f"❌ FATAL: Schema file is empty: {schema_file}")
                sys.exit(1)
            return schema
    except Exception as e:
        print(f"❌ FATAL: Could not load schema: {e}")
        sys.exit(1)

def validate_future_spec(frontmatter, path, errors):
    """Validate future_spec type frontmatter"""
    if frontmatter.get("type") != "future_spec":
        return
    
    # Check review_date exists
    rd = frontmatter.get("review_date")
    if not rd:
        errors.append((path, "future_spec.review_date is required"))
        return
    
    # YAML can parse dates as date objects - convert to string
    if hasattr(rd, 'isoformat'):
        rd_str = rd.isoformat()
        # Tolerate timestamps, truncate to date with warning
        if 'T' in rd_str:
            rd = rd_str[:10]
            errors.append((path, f"future_spec.review_date should be date only (YYYY-MM-DD), not timestamp. Truncating {rd_str} to {rd}"))
        else:
            rd = rd_str
    
    # Check ISO format YYYY-MM-DD
    if not isinstance(rd, str) or len(rd) < 10 or rd[4] != '-' or rd[7] != '-':
        errors.append((path, f"future_spec.review_date must be ISO YYYY-MM-DD format (got: {type(rd).__name__})"))
        return
    
    # Truncate if longer than 10 (in case of accidental timestamp string)
    if len(rd) > 10:
        rd = rd[:10]
    
    # Check date is in the future (at least 90 days)
    try:
        review_date = date.fromisoformat(rd)
        today = date.today()
        min_future_date = today + timedelta(days=90)
        
        if review_date < today:
            errors.append((path, f"future_spec.review_date ({rd}) must be in the future. Set review_date ≥ {min_future_date.isoformat()} (today + 90 days)\n   Fix: sed -i 's/review_date: {rd}/review_date: {min_future_date.isoformat()}/' {path}"))
        elif review_date < min_future_date:
            errors.append((path, f"future_spec.review_date ({rd}) should be ≥ 90 days ahead. Recommended: {min_future_date.isoformat()} or later\n   Fix: sed -i 's/review_date: {rd}/review_date: {min_future_date.isoformat()}/' {path}"))
    except ValueError:
        min_future_date = date.today() + timedelta(days=90)
        errors.append((path, f"future_spec.review_date ({rd}) is not a valid date. Use ISO format YYYY-MM-DD (e.g., {min_future_date.isoformat()})"))

def validate_frontmatter(file_path, schema):
    """Validate frontmatter in a single file"""
    errors = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        errors.append((file_path, f"Could not read file: {e}"))
        return errors
    
    # Check if file starts with frontmatter
    if not content.startswith('---'):
        # Skip template files and READMEs in design/review directories
        filename = os.path.basename(file_path)
        skip_patterns = ['TEMPLATE', 'INDEX', 'README.md', 'portfolio_to_ci_index']
        
        # Only require frontmatter for specific directories, excluding templates
        if any(d in str(file_path) for d in ['08_CHRONICLE', '11_FUTURE']):
            if not any(pattern in filename for pattern in skip_patterns):
                errors.append((file_path, "Missing frontmatter"))
        return errors
    
    # Extract frontmatter
    parts = content.split('---', 2)
    if len(parts) < 3:
        errors.append((file_path, "Malformed frontmatter"))
        return errors
    
    try:
        frontmatter = yaml.safe_load(parts[1]) or {}
    except Exception as e:
        errors.append((file_path, f"Invalid YAML frontmatter: {e}"))
        return errors
    
    # Validate against schema if type is defined
    doc_type = frontmatter.get('type')
    if doc_type and schema.get('types', {}).get(doc_type):
        type_schema = schema['types'][doc_type]
        
        # Check required fields
        for field in type_schema.get('required', []):
            if field not in frontmatter:
                errors.append((file_path, f"Missing required field for type '{doc_type}': {field}"))
    
    # Special validation for future_spec
    validate_future_spec(frontmatter, file_path, errors)
    
    return errors

def main():
    """Main linter function"""
    print("🔍 Linting frontmatter...")
    
    schema = load_schema()
    all_errors = []
    
    # Directories to check
    check_dirs = ['08_CHRONICLE', '11_FUTURE', 'docs']
    
    for check_dir in check_dirs:
        if not os.path.exists(check_dir):
            continue
        
        for root, _, files in os.walk(check_dir):
            for file in files:
                if not file.endswith('.md'):
                    continue
                
                file_path = os.path.join(root, file)
                errors = validate_frontmatter(file_path, schema)
                all_errors.extend(errors)
    
    # Report errors
    if all_errors:
        print(f"\n❌ Found {len(all_errors)} frontmatter error(s):\n")
        for path, error in all_errors:
            print(f"  {path}")
            print(f"    → {error}\n")
        sys.exit(1)
    else:
        print("✅ All frontmatter valid")
        sys.exit(0)

if __name__ == "__main__":
    main()

