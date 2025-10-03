#!/usr/bin/env python3
"""
Meta-Insight Detection Script
Automatically detects phase mismatches, premature convergence, and collapse risks
"""

import os
import re
import yaml
from pathlib import Path
from typing import Dict, List, Tuple

class MetaInsightDetector:
    def __init__(self, repo_path: str = "."):
        self.repo_path = Path(repo_path)
        self.phase_indicators = {
            'sandboxing': ['exploration', 'hypothesis', 'testing', 'discovering', 'exploring'],
            'design': ['decision', 'choice', 'select', 'specify', 'define'],
            'implementation': ['execute', 'deploy', 'run', 'operate', 'monitor']
        }
        
        self.convergent_types = ['capsule', 'decision', 'assessment', 'spec']
        self.divergent_types = ['exploration_log', 'hypothesis_tracking', 'process_capture']
        
        self.collapse_indicators = [
            'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7',
            'context saturation', 'instruction dilution', 'vocabulary drift',
            'reference ambiguity', 'goal creep', 'evidence entropy', 'thread fragmentation'
        ]
        
        self.context_indicators = [
            'why now', 'what triggered', 'context', 'background', 'reasoning',
            'emotional', 'feeling', 'energy', 'momentum'
        ]

    def detect_phase_mismatch(self, file_path: Path) -> List[str]:
        """Detect if documentation type matches the thinking phase"""
        issues = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Extract frontmatter
            frontmatter_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
            if not frontmatter_match:
                return ["No frontmatter found"]
                
            frontmatter = yaml.safe_load(frontmatter_match.group(1))
            doc_type = frontmatter.get('type', '')
            phase = frontmatter.get('phase', '')
            
            # Analyze content for phase indicators
            content_lower = content.lower()
            phase_scores = {}
            for phase_name, indicators in self.phase_indicators.items():
                score = sum(1 for indicator in indicators if indicator in content_lower)
                phase_scores[phase_name] = score
            
            detected_phase = max(phase_scores, key=phase_scores.get) if phase_scores else 'unknown'
            
            # Check for phase mismatch
            if phase and phase != detected_phase:
                issues.append(f"Phase mismatch: frontmatter says '{phase}' but content suggests '{detected_phase}'")
            
            # Check for type-phase mismatch
            if phase == 'sandboxing' and doc_type in self.convergent_types:
                issues.append(f"Using convergent type '{doc_type}' during sandboxing phase - consider exploration_log or hypothesis_tracking")
            
            if phase == 'design' and doc_type in self.divergent_types:
                issues.append(f"Using divergent type '{doc_type}' during design phase - consider capsule or decision")
                
        except Exception as e:
            issues.append(f"Error analyzing file: {e}")
            
        return issues

    def detect_premature_convergence(self, file_path: Path) -> List[str]:
        """Detect premature summarization or convergence"""
        issues = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Check for summary patterns without process
            summary_indicators = ['conclusion', 'summary', 'final', 'decided', 'chose']
            process_indicators = ['explored', 'tested', 'discovered', 'learned', 'hypothesis']
            
            summary_count = sum(1 for indicator in summary_indicators if indicator in content.lower())
            process_count = sum(1 for indicator in process_indicators if indicator in content.lower())
            
            if summary_count > process_count and 'exploration' in content.lower():
                issues.append("Potential premature convergence: more summary language than process language")
            
            # Check for missing exploration context
            if 'exploration' in content.lower() and not any(indicator in content.lower() for indicator in process_indicators):
                issues.append("Exploration mentioned but no process captured - consider exploration_log template")
                
        except Exception as e:
            issues.append(f"Error analyzing convergence: {e}")
            
        return issues

    def detect_context_loss(self, file_path: Path) -> List[str]:
        """Detect missing context or fragile insights"""
        issues = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Check for missing context indicators
            context_found = any(indicator in content.lower() for indicator in self.context_indicators)
            if not context_found and 'decision' in content.lower():
                issues.append("Decision made but no context provided - consider adding 'why now' context")
            
            # Check for fragile insights section
            if 'fragile insights' not in content.lower() and 'exploration' in content.lower():
                issues.append("Exploration documented but no fragile insights captured - consider adding fragile insights section")
                
        except Exception as e:
            issues.append(f"Error analyzing context: {e}")
            
        return issues

    def detect_collapse_risks(self, file_path: Path) -> List[str]:
        """Detect potential collapse risks"""
        issues = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Check for collapse indicators without prevention
            collapse_mentioned = any(indicator in content.lower() for indicator in self.collapse_indicators)
            prevention_mentioned = any(word in content.lower() for word in ['prevent', 'avoid', 'mitigate', 'address'])
            
            if collapse_mentioned and not prevention_mentioned:
                issues.append("Collapse risks identified but no prevention strategy mentioned")
            
            # Check for interrelatedness without mapping
            if 'interrelated' in content.lower() and 'map' not in content.lower():
                issues.append("Interrelatedness mentioned but no mapping provided - consider interrelatedness_map template")
                
        except Exception as e:
            issues.append(f"Error analyzing collapse risks: {e}")
            
        return issues

    def analyze_file(self, file_path: Path) -> Dict[str, List[str]]:
        """Comprehensive analysis of a single file"""
        results = {
            'phase_mismatch': self.detect_phase_mismatch(file_path),
            'premature_convergence': self.detect_premature_convergence(file_path),
            'context_loss': self.detect_context_loss(file_path),
            'collapse_risks': self.detect_collapse_risks(file_path)
        }
        return results

    def analyze_recent_files(self, days: int = 7) -> Dict[str, Dict[str, List[str]]]:
        """Analyze recently modified files"""
        results = {}
        
        for file_path in self.repo_path.rglob("*.md"):
            if file_path.is_file():
                # Check if file was modified recently
                import time
                file_age = time.time() - file_path.stat().st_mtime
                if file_age < days * 24 * 3600:  # Within specified days
                    analysis = self.analyze_file(file_path)
                    if any(analysis.values()):  # Only include files with issues
                        results[str(file_path)] = analysis
                        
        return results

    def generate_report(self, analysis_results: Dict[str, Dict[str, List[str]]]) -> str:
        """Generate a human-readable report"""
        report = ["# Meta-Insight Detection Report\n"]
        
        if not analysis_results:
            report.append("✅ No issues detected in recent files")
            return "\n".join(report)
        
        for file_path, issues in analysis_results.items():
            report.append(f"## {file_path}\n")
            
            for category, issue_list in issues.items():
                if issue_list:
                    report.append(f"### {category.replace('_', ' ').title()}")
                    for issue in issue_list:
                        report.append(f"- ⚠️ {issue}")
                    report.append("")
            
            report.append("---\n")
        
        return "\n".join(report)

def main():
    """Main execution function"""
    detector = MetaInsightDetector()
    
    # Analyze recent files
    analysis_results = detector.analyze_recent_files(days=7)
    
    # Generate report
    report = detector.generate_report(analysis_results)
    
    # Output report
    print(report)
    
    # Save report to file
    report_path = Path("00_SANDBOX/reports/meta_insight_report.md")
    report_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"\nReport saved to: {report_path}")

if __name__ == "__main__":
    main()
