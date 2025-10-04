#!/usr/bin/env python3
"""
Checkpoint Validator: C7 Thread Fragmentation Prevention
Blocks commits without checkpoint support and rollback capabilities
"""

import re
import sys
from pathlib import Path
from typing import List, Tuple

class CheckpointValidator:
    def __init__(self):
        self.violations = []
        self.checkpoint_pattern = r'checkpoint_id:\s*[a-zA-Z0-9_-]+'
        self.rollback_pattern = r'rollback_plan:\s*.+'
        self.recovery_pattern = r'recovery_metadata:\s*.+'
    
    def validate_checkpoint_file(self, file_path: Path) -> bool:
        """Validate a single checkpoint file"""
        try:
            content = file_path.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            return True  # Skip binary files
        
        violations = []
        
        # Check for checkpoint_id
        if not re.search(self.checkpoint_pattern, content):
            violations.append(f"{file_path}: Missing checkpoint_id")
        
        # Check for rollback_plan
        if not re.search(self.rollback_pattern, content):
            violations.append(f"{file_path}: Missing rollback_plan")
        
        # Check for recovery_metadata
        if not re.search(self.recovery_pattern, content):
            violations.append(f"{file_path}: Missing recovery_metadata")
        
        if violations:
            self.violations.extend(violations)
            return False
        
        return True
    
    def validate_repository(self) -> bool:
        """Validate all checkpoint files in repository"""
        print("🔍 Checking repository for checkpoint support...")
        
        # Find all checkpoint files
        checkpoint_files = []
        for pattern in ['*checkpoint*.md', '*CP_*.md', '*checkpoint*.yml']:
            checkpoint_files.extend(Path('.').rglob(pattern))
        
        if not checkpoint_files:
            print("ℹ️  No checkpoint files found")
            return True
        
        total_violations = 0
        
        for file_path in checkpoint_files:
            if not self.validate_checkpoint_file(file_path):
                total_violations += 1
        
        if total_violations > 0:
            self.report_violations()
            return False
        
        print("✅ All checkpoints have rollback support")
        return True
    
    def report_violations(self):
        """Report all checkpoint violations"""
        print(f"\n🚨 C7 VIOLATION: Thread fragmentation detected ({len(self.violations)} violations)")
        print("=" * 80)
        
        for violation in self.violations:
            print(f"❌ {violation}")
        
        print("\n" + "=" * 80)
        print("🛡️  C7 Thread Fragmentation Prevention")
        print("📚 Reference: docs/GOVERNANCE/checkpoint_schema.yml")
        print("🔧 Fix: Add checkpoint support with rollback capabilities")
        print("=" * 80)

def main():
    """Main entry point for checkpoint validator"""
    validator = CheckpointValidator()
    
    if not validator.validate_repository():
        print("\n❌ C7 Thread fragmentation detected - blocking commit")
        sys.exit(1)
    
    print("✅ C7 Thread fragmentation prevention passed")
    sys.exit(0)

if __name__ == "__main__":
    main()
