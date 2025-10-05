#!/usr/bin/env python3
"""
Human Gate Validator: C5 Goal Creep Prevention
Blocks commits with unauthorized external actions without human approval
"""

import re
import sys
from pathlib import Path
from typing import List, Tuple

class HumanGateValidator:
    def __init__(self):
        self.violations = []
        self.external_actions = [
            'send_message', 'submit_application', 'request_connection',
            'post_publicly', 'apply_job', 'connect_linkedin',
            'send_email', 'publish_content', 'share_externally'
        ]
        self.human_approval_pattern = r'human_approval:\s*true'
        self.decision_log_pattern = r'decision_id:\s*DEC_\d{4}-\d{2}-\d{2}_\d{3}'
        
        # Governance documents define rules, don't execute them
        self.governance_exclusions = [
            'docs/GOVERNANCE/',
            'docs/HARNESS/',
            'docs/ARCHITECTURE/',
            'scripts/',  # Validation scripts themselves
            'docs/decision_log_schema.yml',
            'docs/ontology.yml',
            'docs/enforcement_rules.yml'
        ]
    
    def is_governance_document(self, file_path: Path) -> bool:
        """Governance documents define rules, don't execute them"""
        return any(exclusion in str(file_path) for exclusion in self.governance_exclusions)
    
    def validate_file(self, file_path: Path) -> bool:
        """Validate a single file for human gate compliance"""
        # Skip governance documents - they define rules, don't execute them
        if self.is_governance_document(file_path):
            return True
            
        try:
            content = file_path.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            return True  # Skip binary files
        
        violations = []
        
        # Check for external actions
        for action in self.external_actions:
            if action in content:
                # Check if human approval is present
                if not re.search(self.human_approval_pattern, content):
                    violations.append(f"{file_path}: External action '{action}' without human approval")
                
                # Check if decision log is present
                if not re.search(self.decision_log_pattern, content):
                    violations.append(f"{file_path}: External action '{action}' without decision log")
        
        if violations:
            self.violations.extend(violations)
            return False
        
        return True
    
    def validate_repository(self) -> bool:
        """Validate entire repository for human gate compliance"""
        print("🔍 Checking repository for human approval gates...")
        
        # Get all markdown and YAML files
        files_to_check = []
        for pattern in ['*.md', '*.yml', '*.yaml']:
            files_to_check.extend(Path('.').rglob(pattern))
        
        # Skip certain directories
        skip_dirs = ['.git', 'node_modules', '__pycache__', '.github']
        
        total_violations = 0
        
        for file_path in files_to_check:
            # Skip certain directories
            if any(skip_dir in str(file_path) for skip_dir in skip_dirs):
                continue
            
            if not self.validate_file(file_path):
                total_violations += 1
        
        if total_violations > 0:
            self.report_violations()
            return False
        
        print("✅ All external actions have human approval")
        return True
    
    def report_violations(self):
        """Report all human gate violations"""
        print(f"\n🚨 C5 VIOLATION: Goal creep detected ({len(self.violations)} violations)")
        print("=" * 80)
        
        for violation in self.violations:
            print(f"❌ {violation}")
        
        print("\n" + "=" * 80)
        print("🛡️  C5 Goal Creep Prevention")
        print("📚 Reference: docs/GOVERNANCE/human_gates_policy.yml")
        print("🔧 Fix: Add human approval and decision log for external actions")
        print("=" * 80)

def main():
    """Main entry point for human gate validator"""
    validator = HumanGateValidator()
    
    if not validator.validate_repository():
        print("\n❌ C5 Goal creep detected - blocking commit")
        sys.exit(1)
    
    print("✅ C5 Goal creep prevention passed")
    sys.exit(0)

if __name__ == "__main__":
    main()
