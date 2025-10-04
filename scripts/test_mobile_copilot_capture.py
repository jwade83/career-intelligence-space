#!/usr/bin/env python3
"""
Mobile Copilot Field Capture Test Script

This script validates mobile GitHub Copilot's field capture capabilities
and provides test prompts for systematic validation.
"""

import json
import datetime
from pathlib import Path

def generate_test_prompts():
    """Generate test prompts for mobile copilot field capture validation."""
    
    test_prompts = {
        "basic_file_creation": {
            "prompt": "Create a new file in 00_SANDBOX/agent_inbox/ called mobile_copilot_test_basic.md with the following content:\n\n---\nproject: Career Intelligence Space\ntype: field_capture_test\nstatus: active\ntags: [mobile_copilot, test, basic]\nsource: mobile_github_copilot\ncaptured_at: '2025-10-03'\n---\n\n# Mobile Copilot Basic Test\n\nThis is a test file created by mobile GitHub Copilot to validate field capture capabilities.\n\n## Test Results\n- [ ] File created successfully\n- [ ] Frontmatter compliant\n- [ ] Content properly formatted\n\n## Next Steps\n- Validate file creation\n- Check frontmatter compliance\n- Test content quality",
            "expected_outcome": "File created with proper frontmatter and content",
            "validation_criteria": [
                "File exists in 00_SANDBOX/agent_inbox/",
                "Frontmatter matches CIS ontology",
                "Content is properly formatted",
                "Branch created appropriately"
            ]
        },
        
        "complex_technical_content": {
            "prompt": "Create a technical analysis file in 00_SANDBOX/systems/ called mobile_copilot_architecture_analysis.md with a comprehensive analysis of the Career Intelligence Space repository architecture, including:\n\n1. System components and their relationships\n2. Data flow patterns\n3. Integration points\n4. Scalability considerations\n5. Security implications\n\nUse proper CIS frontmatter and structure the content professionally.",
            "expected_outcome": "Sophisticated technical analysis with proper structure",
            "validation_criteria": [
                "Technical content quality",
                "Proper system analysis",
                "CIS frontmatter compliance",
                "Professional structure"
            ]
        },
        
        "template_compliance_test": {
            "prompt": "Create a file in 00_SANDBOX/meta_insights/ called mobile_copilot_meta_analysis.md using the exact CIS template for meta_insight_tracking type. Include analysis of the repository's evolution patterns and provide insights about the mobile copilot integration.",
            "expected_outcome": "Perfect CIS template compliance",
            "validation_criteria": [
                "Exact frontmatter match with CIS ontology",
                "Proper meta_insight_tracking type",
                "Content matches template structure",
                "Insights are valuable and relevant"
            ]
        },
        
        "branch_strategy_test": {
            "prompt": "Create a file in the main branch (not a new branch) called mobile_copilot_main_branch_test.md with content about testing direct main branch writes. Use proper frontmatter and explain the implications of writing directly to main.",
            "expected_outcome": "Understanding of branch write permissions",
            "validation_criteria": [
                "File created in main branch",
                "Proper frontmatter",
                "Content explains branch strategy",
                "No new branch created"
            ]
        },
        
        "multi_file_creation": {
            "prompt": "Create three related files in 00_SANDBOX/agent_inbox/:\n1. mobile_copilot_test_001.md - Basic test file\n2. mobile_copilot_test_002.md - Intermediate test file\n3. mobile_copilot_test_003.md - Advanced test file\n\nEach should have proper frontmatter and reference the others. This tests batch file creation capabilities.",
            "expected_outcome": "Multiple files created with proper cross-references",
            "validation_criteria": [
                "All three files created",
                "Proper frontmatter in each",
                "Cross-references between files",
                "Consistent naming pattern"
            ]
        }
    }
    
    return test_prompts

def generate_validation_script():
    """Generate a validation script to check test results."""
    
    validation_script = """
#!/usr/bin/env python3
\"\"\"
Mobile Copilot Field Capture Validation Script

This script validates the results of mobile copilot field capture tests.
\"\"\"

import os
import yaml
from pathlib import Path

def validate_frontmatter(file_path):
    \"\"\"Validate that a file has proper CIS-compliant frontmatter.\"\"\"
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
    \"\"\"Validate that frontmatter complies with CIS ontology.\"\"\"
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
    \"\"\"Run validation on all test files.\"\"\"
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
        print(f"\\nFile: {file_path}")
        print(f"  Exists: {result['exists']}")
        if result['exists']:
            print(f"  Frontmatter: {result['frontmatter_valid']} - {result['frontmatter_message']}")
            print(f"  CIS Ontology: {result['ontology_valid']} - {result['ontology_message']}")
        else:
            print(f"  Status: {result['frontmatter_message']}")
"""
    
    return validation_script

def main():
    """Generate test prompts and validation script."""
    
    print("Mobile Copilot Field Capture Test Generator")
    print("=" * 50)
    
    # Generate test prompts
    test_prompts = generate_test_prompts()
    
    # Save test prompts to JSON
    with open('mobile_copilot_test_prompts.json', 'w') as f:
        json.dump(test_prompts, f, indent=2)
    
    print(f"Generated {len(test_prompts)} test prompts")
    print("Saved to: mobile_copilot_test_prompts.json")
    
    # Generate validation script
    validation_script = generate_validation_script()
    
    with open('validate_mobile_copilot_tests.py', 'w') as f:
        f.write(validation_script)
    
    print("Generated validation script: validate_mobile_copilot_tests.py")
    
    # Print test prompts for immediate use
    print("\n" + "=" * 50)
    print("IMMEDIATE TEST PROMPTS FOR MOBILE COPILOT")
    print("=" * 50)
    
    for test_name, test_data in test_prompts.items():
        print(f"\n--- {test_name.upper().replace('_', ' ')} ---")
        print(f"Prompt: {test_data['prompt']}")
        print(f"Expected: {test_data['expected_outcome']}")

if __name__ == "__main__":
    main()
