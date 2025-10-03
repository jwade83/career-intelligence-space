#!/usr/bin/env python3
"""
Meta-Insight Detection Script
Automatically detects phase mismatches, premature convergence, and collapse risks
Based on analysis from cursor_failed_field_capture_workflows_d.md
"""

import os
import re
import yaml
from pathlib import Path
from typing import Dict, List, Tuple
from datetime import datetime

class MetaInsightDetector:
    def __init__(self, repo_path: str = "."):
        self.repo_path = Path(repo_path)
        self.phase_indicators = {
            'sandboxing': ['exploration', 'hypothesis', 'testing', 'discovering', 'exploring', 'experimenting', 'iterating'],
            'design': ['decision', 'choice', 'select', 'specify', 'define', 'architecture', 'structure'],
            'implementation': ['execute', 'deploy', 'run', 'operate', 'monitor', 'production', 'live']
        }
        
        self.convergent_types = ['capsule', 'decision', 'assessment', 'spec', 'memo', 'log']
        self.divergent_types = ['exploration_log', 'hypothesis_tracking', 'process_capture', 'design_experiment', 'creative_session']
        
        self.collapse_indicators = [
            'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7',
            'context saturation', 'instruction dilution', 'vocabulary drift',
            'reference ambiguity', 'goal creep', 'evidence entropy', 'thread fragmentation'
        ]
        
        self.context_indicators = [
            'why now', 'what triggered', 'context', 'background', 'reasoning',
            'emotional', 'feeling', 'energy', 'momentum', 'fragile insights'
        ]

    def detect_phase_mismatch(self, file_path: Path) -> List[str]:
        """Detect phase mismatches in documentation files"""
        issues = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract frontmatter
            frontmatter_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL | re.MULTILINE)
            if not frontmatter_match:
                issues.append("No frontmatter found")
                return issues
            
            frontmatter_text = frontmatter_match.group(1)
            frontmatter = yaml.safe_load(frontmatter_text) if frontmatter_text else {}
            
            phase = frontmatter.get('phase', 'unknown')
            doc_type = frontmatter.get('type', 'unknown')
            
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

    def detect_collapse_risks(self, file_path: Path) -> List[str]:
        """Detect potential collapse risks in documentation"""
        issues = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            content_lower = content.lower()
            
            # Check for collapse indicators
            for indicator in self.collapse_indicators:
                if indicator.lower() in content_lower:
                    issues.append(f"Potential collapse risk detected: {indicator}")
            
            # Check for missing context
            context_found = any(indicator in content_lower for indicator in self.context_indicators)
            if not context_found and len(content) > 500:  # Only check longer documents
                issues.append("Missing context indicators - consider adding 'why now', 'what triggered', or emotional context")
                
        except Exception as e:
            issues.append(f"Error analyzing file: {e}")
            
        return issues

    def generate_metacognitive_prompts(self, file_path: Path) -> List[str]:
        """Generate meta-cognitive review prompts for a file"""
        prompts = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            frontmatter_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL | re.MULTILINE)
            if frontmatter_match:
                frontmatter_text = frontmatter_match.group(1)
                frontmatter = yaml.safe_load(frontmatter_text) if frontmatter_text else {}
                
                phase = frontmatter.get('phase', 'unknown')
                doc_type = frontmatter.get('type', 'unknown')
                
                # Phase-specific prompts
                if phase == 'sandboxing':
                    prompts.extend([
                        "Are you preserving ambiguity and multiple possibilities?",
                        "Are you capturing the exploration process, not just outcomes?",
                        "Are you using divergent thinking tools (exploration_log, hypothesis_tracking)?"
                    ])
                elif phase == 'design':
                    prompts.extend([
                        "Are you making clear decisions and choices?",
                        "Are you using convergent thinking tools (capsule, decision, spec)?",
                        "Are you synthesizing rather than exploring?"
                    ])
                elif phase == 'implementation':
                    prompts.extend([
                        "Are you focused on execution and operation?",
                        "Are you monitoring and maintaining rather than exploring?",
                        "Are you using implementation-focused tools?"
                    ])
                
                # General meta-cognitive prompts
                prompts.extend([
                    "Review your last response for phase mismatches and thinking mode alignment",
                    "Am I using the right documentation type for my current phase?",
                    "Am I capturing process, not just outcomes?",
                    "Am I preserving context and fragile insights?"
                ])
                
        except Exception as e:
            prompts.append(f"Error generating prompts: {e}")
            
        return prompts

    def analyze_repository(self) -> Dict[str, List[str]]:
        """Analyze entire repository for phase mismatches and collapse risks"""
        results = {
            'phase_mismatches': [],
            'collapse_risks': [],
            'metacognitive_prompts': [],
            'summary': {}
        }
        
        # Find all markdown files
        md_files = list(self.repo_path.rglob("*.md"))
        
        total_files = len(md_files)
        issues_found = 0
        
        for file_path in md_files:
            # Skip if file is too large or binary
            if file_path.stat().st_size > 1024 * 1024:  # 1MB limit
                continue
                
            phase_issues = self.detect_phase_mismatch(file_path)
            collapse_issues = self.detect_collapse_risks(file_path)
            prompts = self.generate_metacognitive_prompts(file_path)
            
            if phase_issues or collapse_issues:
                issues_found += 1
                relative_path = file_path.relative_to(self.repo_path)
                
                if phase_issues:
                    results['phase_mismatches'].append({
                        'file': str(relative_path),
                        'issues': phase_issues
                    })
                
                if collapse_issues:
                    results['collapse_risks'].append({
                        'file': str(relative_path),
                        'issues': collapse_issues
                    })
                
                if prompts:
                    results['metacognitive_prompts'].append({
                        'file': str(relative_path),
                        'prompts': prompts
                    })
        
        # Generate summary
        results['summary'] = {
            'total_files_analyzed': total_files,
            'files_with_issues': issues_found,
            'phase_mismatch_count': len(results['phase_mismatches']),
            'collapse_risk_count': len(results['collapse_risks']),
            'analysis_timestamp': datetime.now().isoformat()
        }
        
        return results

    def print_report(self, results: Dict[str, List[str]]):
        """Print a formatted report of the analysis"""
        print("🔍 Meta-Insight Detection Report")
        print("=" * 50)
        
        summary = results['summary']
        print(f"📊 Analysis Summary:")
        print(f"   Total files analyzed: {summary['total_files_analyzed']}")
        print(f"   Files with issues: {summary['files_with_issues']}")
        print(f"   Phase mismatches: {summary['phase_mismatch_count']}")
        print(f"   Collapse risks: {summary['collapse_risk_count']}")
        print(f"   Analysis time: {summary['analysis_timestamp']}")
        print()
        
        if results['phase_mismatches']:
            print("⚠️  Phase Mismatches Found:")
            for item in results['phase_mismatches']:
                print(f"   📄 {item['file']}")
                for issue in item['issues']:
                    print(f"      • {issue}")
            print()
        
        if results['collapse_risks']:
            print("🚨 Collapse Risks Detected:")
            for item in results['collapse_risks']:
                print(f"   📄 {item['file']}")
                for issue in item['issues']:
                    print(f"      • {issue}")
            print()
        
        if results['metacognitive_prompts']:
            print("💭 Meta-Cognitive Review Prompts:")
            for item in results['metacognitive_prompts']:
                print(f"   📄 {item['file']}")
                for prompt in item['prompts'][:3]:  # Show first 3 prompts
                    print(f"      • {prompt}")
                if len(item['prompts']) > 3:
                    print(f"      • ... and {len(item['prompts']) - 3} more prompts")
            print()

def main():
    """Main function to run the meta-insight detector"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Meta-Insight Detection Script')
    parser.add_argument('--repo-path', default='.', help='Path to repository root')
    parser.add_argument('--output', help='Output file for results (JSON format)')
    parser.add_argument('--quiet', action='store_true', help='Suppress output')
    
    args = parser.parse_args()
    
    detector = MetaInsightDetector(args.repo_path)
    results = detector.analyze_repository()
    
    if not args.quiet:
        detector.print_report(results)
    
    if args.output:
        import json
        with open(args.output, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"Results saved to {args.output}")

if __name__ == "__main__":
    main()
