#!/usr/bin/env python3
"""
Ontology Linter: C3 Vocabulary Drift Prevention
Blocks commits that violate vocabulary constraints from ontology.yml
"""

import yaml
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple

class OntologyLinter:
    def __init__(self, ontology_file: str = "docs/ONTOLOGY.yml"):
        self.ontology_file = Path(ontology_file)
        self.violations = []
        self.load_ontology()
    
    def load_ontology(self):
        """Load vocabulary constraints from ontology.yml"""
        try:
            with open(self.ontology_file, 'r') as f:
                self.ontology = yaml.safe_load(f)
        except FileNotFoundError:
            print(f"ERROR: Ontology file not found: {self.ontology_file}")
            sys.exit(1)
        except yaml.YAMLError as e:
            print(f"ERROR: Invalid YAML in ontology file: {e}")
            sys.exit(1)
    
    def get_forbidden_terms(self) -> Dict[str, str]:
        """Extract forbidden terms and their required replacements"""
        forbidden = {}
        
        # Extract from core vocabulary tables
        if 'core_vocabulary' in self.ontology:
            for category in self.ontology['core_vocabulary'].values():
                if isinstance(category, dict):
                    for term_data in category.values():
                        if isinstance(term_data, dict) and 'forbidden_synonyms' in term_data:
                            for forbidden_term, required_term in term_data['forbidden_synonyms'].items():
                                forbidden[forbidden_term] = required_term
        
        # Extract from technical terms
        if 'technical_terms' in self.ontology:
            for category in self.ontology['technical_terms'].values():
                if isinstance(category, dict):
                    for term_data in category.values():
                        if isinstance(term_data, dict) and 'forbidden_terms' in term_data:
                            for forbidden_term, required_term in term_data['forbidden_terms'].items():
                                forbidden[forbidden_term] = required_term
        
        return forbidden
    
    def check_file(self, file_path: Path) -> List[Tuple[str, str, str]]:
        """Check a single file for vocabulary violations"""
        violations = []
        
        try:
            content = file_path.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            # Skip binary files
            return violations
        
        forbidden_terms = self.get_forbidden_terms()
        
        for forbidden_term, required_term in forbidden_terms.items():
            # Case-insensitive search for forbidden terms
            pattern = re.compile(re.escape(forbidden_term), re.IGNORECASE)
            matches = pattern.findall(content)
            
            if matches:
                for match in matches:
                    violations.append((
                        str(file_path),
                        forbidden_term,
                        required_term
                    ))
        
        return violations
    
    def check_repository(self) -> bool:
        """Check entire repository for vocabulary violations"""
        print("🔍 Checking repository for vocabulary drift...")
        
        # Get all markdown files
        md_files = list(Path('.').rglob('*.md'))
        
        # Also check YAML files
        yaml_files = list(Path('.').rglob('*.yml')) + list(Path('.').rglob('*.yaml'))
        
        all_files = md_files + yaml_files
        
        total_violations = 0
        
        for file_path in all_files:
            # Skip certain directories
            if any(skip_dir in str(file_path) for skip_dir in ['.git', 'node_modules', '__pycache__']):
                continue
            
            violations = self.check_file(file_path)
            total_violations += len(violations)
            
            for file_path_str, forbidden_term, required_term in violations:
                self.violations.append((file_path_str, forbidden_term, required_term))
        
        if total_violations > 0:
            self.report_violations()
            return False
        
        print("✅ No vocabulary drift detected")
        return True
    
    def report_violations(self):
        """Report all vocabulary violations"""
        print(f"\n🚨 C3 VIOLATION: Vocabulary drift detected ({len(self.violations)} violations)")
        print("=" * 80)
        
        for file_path, forbidden_term, required_term in self.violations:
            print(f"\n📁 File: {file_path}")
            print(f"❌ Forbidden: '{forbidden_term}'")
            print(f"✅ Required: '{required_term}'")
            print(f"💡 Fix: Replace '{forbidden_term}' with '{required_term}'")
        
        print("\n" + "=" * 80)
        print("🛡️  C3 Vocabulary Drift Prevention")
        print("📚 Reference: docs/GOVERNANCE/ontology.yml")
        print("🔧 Fix: Use exact vocabulary from ontology")
        print("=" * 80)

def main():
    """Main entry point for ontology linter"""
    linter = OntologyLinter()
    
    if not linter.check_repository():
        print("\n❌ C3 Vocabulary drift detected - blocking commit")
        sys.exit(1)
    
    print("✅ C3 Vocabulary enforcement passed")
    sys.exit(0)

if __name__ == "__main__":
    main()
