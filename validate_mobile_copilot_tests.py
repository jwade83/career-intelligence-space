
#!/usr/bin/env python3
"""
Mobile Copilot Field Capture Validation Script

This script validates the results of mobile copilot field capture tests.
"""

import os
import yaml
from pathlib import Path

def validate_frontmatter(file_path):
    """Validate that a file has proper CIS-compliant frontmatter."""
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        
        if not content.startswith('---'):
            return False, "Missing frontmatter start"
        
        parts = content.split('---', 2)
        if len(parts) < 3:
            return False, "Incomplete frontmatter"
        
        frontmatter = yaml.safe_load(parts[1])
        required_keys = ['project', 'type', 'status', 'tags', 'source']
        
        for key in required_keys:
            if key not in frontmatter:
                return False, f"Missing required key: {key}"
        
        return True, "Frontmatter valid"
    except Exception as e:
        return False, f"Error parsing frontmatter: {e}"

def validate_cis_ontology(file_path):
    """Validate that frontmatter complies with CIS ontology."""
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        
        parts = content.split('---', 2)
        frontmatter = yaml.safe_load(parts[1])
        
        # Check project
        if frontmatter.get('project') != 'Career Intelligence Space':
            return False, "Invalid project name"
        
        # Check type (should be in allowed types)
        allowed_types = ['field_capture', 'field_capture_test', 'meta_insight_tracking', 'systems']
        if frontmatter.get('type') not in allowed_types:
            return False, f"Invalid type: {frontmatter.get('type')}"
        
        # Check status
        allowed_statuses = ['active', 'draft', 'matured', 'archived']
        if frontmatter.get('status') not in allowed_statuses:
            return False, f"Invalid status: {frontmatter.get('status')}"
        
        return True, "CIS ontology compliant"
    except Exception as e:
        return False, f"Error validating ontology: {e}"

def run_validation():
    """Run validation on all test files."""
    test_files = [
        '00_SANDBOX/agent_inbox/mobile_copilot_test_basic.md',
        '00_SANDBOX/systems/mobile_copilot_architecture_analysis.md',
        '00_SANDBOX/meta_insights/mobile_copilot_meta_analysis.md',
        'mobile_copilot_main_branch_test.md',
        '00_SANDBOX/agent_inbox/mobile_copilot_test_001.md',
        '00_SANDBOX/agent_inbox/mobile_copilot_test_002.md',
        '00_SANDBOX/agent_inbox/mobile_copilot_test_003.md'
    ]
    
    results = {}
    
    for file_path in test_files:
        if os.path.exists(file_path):
            frontmatter_valid, frontmatter_msg = validate_frontmatter(file_path)
            ontology_valid, ontology_msg = validate_cis_ontology(file_path)
            
            results[file_path] = {
                'exists': True,
                'frontmatter_valid': frontmatter_valid,
                'frontmatter_message': frontmatter_msg,
                'ontology_valid': ontology_valid,
                'ontology_message': ontology_msg
            }
        else:
            results[file_path] = {
                'exists': False,
                'frontmatter_valid': False,
                'frontmatter_message': 'File not found',
                'ontology_valid': False,
                'ontology_message': 'File not found'
            }
    
    return results

if __name__ == "__main__":
    results = run_validation()
    
    print("Mobile Copilot Field Capture Validation Results")
    print("=" * 50)
    
    for file_path, result in results.items():
        print(f"\nFile: {file_path}")
        print(f"  Exists: {result['exists']}")
        if result['exists']:
            print(f"  Frontmatter: {result['frontmatter_valid']} - {result['frontmatter_message']}")
            print(f"  CIS Ontology: {result['ontology_valid']} - {result['ontology_message']}")
        else:
            print(f"  Status: {result['frontmatter_message']}")
