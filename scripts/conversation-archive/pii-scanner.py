#!/usr/bin/env python3
"""
PII Scanner for Conversation Archives
Scans for potential personally identifiable information in conversation transcripts
"""

import re
import argparse
import json
import hashlib
from pathlib import Path

# PII patterns to detect
PII_PATTERNS = {
    'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
    'phone': r'\b(?:\+?1[-.\s]?)?\(?([0-9]{3})\)?[-.\s]?([0-9]{3})[-.\s]?([0-9]{4})\b',
    'ssn': r'\b\d{3}-?\d{2}-?\d{4}\b',
    'credit_card': r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b',
    'ip_address': r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b',
    'url': r'https?://[^\s<>"{}|\\^`\[\]]+',
    'api_key': r'\b[A-Za-z0-9]{20,}\b',  # Generic long alphanumeric strings
}

def hash_snippet(s: str) -> str:
    """Create a short hash of a snippet for deduplication"""
    return hashlib.sha1(s.encode("utf-8", "ignore")).hexdigest()[:10]

def emit_finding(path, kind, snippet, line):
    """Emit a structured finding as JSON"""
    print(json.dumps({
        "path": str(path),
        "type": kind,
        "line": line,
        "hash": hash_snippet(snippet),
        "preview": snippet[:60]
    }))

def load_allowlist():
    """Load PII allowlist patterns"""
    allowlist_file = Path(__file__).parent / "pii-allowlist.txt"
    if not allowlist_file.exists():
        return set()
    
    try:
        with open(allowlist_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        allowlist = set()
        for line in lines:
            line = line.strip()
            if line and not line.startswith('#'):
                allowlist.add(line.lower())
        
        return allowlist
    except Exception:
        return set()

def scan_file_for_pii(file_path, emit_json=False):
    """Scan a file for potential PII"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return {'error': f"Could not read file {file_path}: {e}"}
    
    allowlist = load_allowlist()
    findings = {}
    findings_count = 0
    
    # Split content into lines for line number reporting
    lines = content.split('\n')
    
    for pii_type, pattern in PII_PATTERNS.items():
        matches = re.findall(pattern, content, re.IGNORECASE)
        if matches:
            # Filter out allowlisted patterns
            filtered_matches = []
            for match in matches:
                # Handle tuple matches (from regex groups)
                if isinstance(match, tuple):
                    match_str = ''.join(match).lower()
                else:
                    match_str = str(match).lower()
                
                is_allowlisted = any(allow_pattern in match_str for allow_pattern in allowlist)
                if not is_allowlisted:
                    filtered_matches.append(match)
            
            if filtered_matches:
                findings[pii_type] = {
                    'count': len(filtered_matches),
                    'matches': filtered_matches[:5],  # Show first 5 matches
                    'pattern': pattern
                }
                findings_count += len(filtered_matches)
                
                # Emit JSON findings if requested
                if emit_json:
                    for match in filtered_matches:
                        # Find line number for the match
                        match_str = ''.join(match) if isinstance(match, tuple) else str(match)
                        line_num = 1
                        for i, line in enumerate(lines):
                            if match_str in line:
                                line_num = i + 1
                                break
                        emit_finding(file_path, pii_type, match_str, line_num)
    
    return findings, findings_count

def scan_directory_for_pii(directory_path):
    """Scan a directory for PII in markdown files"""
    directory = Path(directory_path)
    
    if not directory.exists():
        return {'error': f"Directory {directory_path} does not exist"}
    
    results = {}
    
    # Scan all markdown files
    for md_file in directory.rglob('*.md'):
        relative_path = md_file.relative_to(directory)
        findings = scan_file_for_pii(md_file)
        
        if findings and 'error' not in findings:
            results[str(relative_path)] = findings
    
    return results

def generate_report(results):
    """Generate a PII scan report"""
    if not results:
        return "✅ No PII detected in scanned files."
    
    report = ["🚨 PII DETECTED - Manual Review Required", ""]
    
    for file_path, findings in results.items():
        if 'error' in findings:
            report.append(f"❌ Error scanning {file_path}: {findings['error']}")
            continue
            
        report.append(f"📄 {file_path}")
        
        for pii_type, data in findings.items():
            report.append(f"  🔍 {pii_type.upper()}: {data['count']} matches")
            for match in data['matches']:
                # Handle tuple matches (from regex groups)
                if isinstance(match, tuple):
                    match_str = ''.join(match)
                else:
                    match_str = str(match)
                
                # Mask sensitive data for display
                if pii_type == 'email':
                    masked = re.sub(r'([^@]+)@', '***@', match_str)
                elif pii_type == 'phone':
                    masked = re.sub(r'\d', '*', match_str)
                elif pii_type == 'ssn':
                    masked = re.sub(r'\d', '*', match_str)
                elif pii_type == 'credit_card':
                    masked = re.sub(r'\d', '*', match_str)
                else:
                    masked = match_str[:10] + "..." if len(match_str) > 10 else match_str
                
                report.append(f"    - {masked}")
        
        report.append("")
    
    report.append("📋 Next Steps:")
    report.append("1. Review each flagged item manually")
    report.append("2. Redact or remove sensitive information")
    report.append("3. Re-run scan to verify cleanup")
    report.append("4. Commit only after PII is removed")
    
    return "\n".join(report)

def main():
    parser = argparse.ArgumentParser(description='Scan conversation archives for PII')
    parser.add_argument('files', nargs='*', help='Files to scan')
    parser.add_argument('--path', help='Directory to scan')
    parser.add_argument('--report', action='store_true', help='Generate detailed report')
    parser.add_argument('--fail-on-pii', action='store_true', help='Exit with error code if PII found')
    parser.add_argument('--mask', action='store_true', help='Emit JSON findings for CI processing')
    parser.add_argument('--exit-nonzero-on-detect', action='store_true', help='Exit with error code if PII found')
    
    args = parser.parse_args()
    
    total_findings = 0
    
    if args.path:
        directory = Path(args.path)
        if not directory.exists():
            print(f"Error: Directory {args.path} does not exist")
            return 1
        
        markdown_files = list(directory.rglob("*.md"))
        if not markdown_files:
            print(f"No markdown files found in {args.path}")
            return 0
        
        for file_path in markdown_files:
            result = scan_file_for_pii(file_path, emit_json=args.mask)
            if isinstance(result, tuple):
                findings, count = result
                total_findings += count
            else:
                if 'error' in result:
                    print(f"Error: {result['error']}")
                    return 1
    elif args.files:
        for file_path in args.files:
            result = scan_file_for_pii(file_path, emit_json=args.mask)
            if isinstance(result, tuple):
                findings, count = result
                total_findings += count
            else:
                if 'error' in result:
                    print(f"Error: {result['error']}")
                    return 1
    else:
        print("Error: Please specify files to scan or use --path")
        return 1
    
    # Print summary
    if args.mask:
        print(f"SUMMARY: findings={total_findings}")
    else:
        if total_findings > 0:
            print("🚨 PII detected in the following files:")
            print(f"  Total findings: {total_findings}")
        else:
            print("✅ No PII detected")
    
    # Exit with error code if PII found and fail-on-pii is set
    exit_code = 1 if total_findings > 0 and (args.fail_on_pii or args.exit_nonzero_on_detect) else 0
    return exit_code

if __name__ == "__main__":
    exit(main())
