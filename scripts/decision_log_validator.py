#!/usr/bin/env python3
"""
Decision Log Validator: C6 Evidence Entropy Prevention
Blocks commits without proper decision logging and provenance
"""

import yaml
import re
import sys
from pathlib import Path
from typing import List, Dict, Any

class DecisionLogValidator:
    def __init__(self):
        self.violations = []
        self.required_fields = [
            'decision_id', 'rationale', 'evidence_sources', 
            'human_approval', 'timestamp', 'provenance'
        ]
    
    def _load_frontmatter(self, file_path: Path) -> Dict[str, Any]:
        try:
            content = file_path.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            return {}
        if '---' not in content:
            return {}
        parts = content.split('---', 2)
        if len(parts) < 3:
            return {}
        try:
            return yaml.safe_load(parts[1]) or {}
        except yaml.YAMLError:
            return {}

    def _is_decision_log(self, file_path: Path) -> bool:
        """Only validate files explicitly marked as decision logs.
        Criteria: frontmatter type == 'decision_log' OR tags includes 'decision_log'.
        """
        fm = self._load_frontmatter(file_path)
        if not fm:
            return False
        if str(fm.get('type', '')).strip() == 'decision_log':
            return True
        tags = fm.get('tags') or []
        try:
            return 'decision_log' in tags
        except Exception:
            return False
    
    def validate_decision_log_file(self, file_path: Path) -> bool:
        """Validate a single decision log file"""
        try:
            content = file_path.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            return True  # Skip binary files
        
        if '---' not in content:
            return True  # Not a YAML frontmatter file
        
        # Extract frontmatter
        frontmatter = content.split('---')[1]
        
        try:
            data = yaml.safe_load(frontmatter)
        except yaml.YAMLError:
            self.violations.append(f"{file_path}: Invalid YAML frontmatter")
            return False
        
        # Check required fields
        for field in self.required_fields:
            if field not in data:
                self.violations.append(f"{file_path}: Missing required field '{field}'")
                return False
        
        # Validate decision_id format
        if not re.match(r'^DEC_\d{4}-\d{2}-\d{2}_\d{3}$', data['decision_id']):
            self.violations.append(f"{file_path}: Invalid decision_id format")
            return False
        
        # Validate rationale length
        if len(data['rationale']) < 10:
            self.violations.append(f"{file_path}: Rationale too short (minimum 10 characters)")
            return False
        
        # Validate evidence_sources
        if not isinstance(data['evidence_sources'], list) or len(data['evidence_sources']) == 0:
            self.violations.append(f"{file_path}: Evidence sources must be non-empty array")
            return False
        
        # Validate human_approval
        if not isinstance(data['human_approval'], bool):
            self.violations.append(f"{file_path}: Human approval must be boolean")
            return False
        
        # Validate provenance
        if not isinstance(data['provenance'], dict):
            self.violations.append(f"{file_path}: Provenance must be object")
            return False
        
        if 'source' not in data['provenance'] or 'reviewer' not in data['provenance']:
            self.violations.append(f"{file_path}: Provenance missing required fields")
            return False
        
        return True
    
    def validate_repository(self) -> bool:
        """Validate all decision log files in repository (explicitly typed)."""
        print("🔍 Checking repository for decision log completeness...")
        md_files = list(Path('.').rglob('*.md'))
        decision_files = [p for p in md_files if self._is_decision_log(p)]
        if not decision_files:
            print("ℹ️  No decision log files found")
            return True
        total_violations = 0
        for file_path in decision_files:
            if not self.validate_decision_log_file(file_path):
                total_violations += 1
        
        if total_violations > 0:
            self.report_violations()
            return False
        
        print("✅ All decision logs have complete provenance")
        return True
    
    def report_violations(self):
        """Report all decision log violations"""
        print(f"\n🚨 C6 VIOLATION: Evidence entropy detected ({len(self.violations)} violations)")
        print("=" * 80)
        
        for violation in self.violations:
            print(f"❌ {violation}")
        
        print("\n" + "=" * 80)
        print("🛡️  C6 Evidence Entropy Prevention")
        print("📚 Reference: docs/GOVERNANCE/decision_log_schema.yml")
        print("🔧 Fix: Add complete decision log with provenance")
        print("=" * 80)

def main():
    """Main entry point for decision log validator"""
    validator = DecisionLogValidator()
    
    if not validator.validate_repository():
        print("\n❌ C6 Evidence entropy detected - blocking commit")
        sys.exit(1)
    
    print("✅ C6 Evidence entropy prevention passed")
    sys.exit(0)

if __name__ == "__main__":
    main()
