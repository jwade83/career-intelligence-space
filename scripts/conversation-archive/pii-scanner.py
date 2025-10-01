#!/usr/bin/env python3
"""
PII Scanner for Conversation Archives
Scans markdown files for potential PII and masks sensitive information
"""

import os
import re
import argparse
from pathlib import Path
from typing import List, Dict, Tuple

# Common PII patterns
PII_PATTERNS = {
    'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
    'phone': r'\b(?:\+?1[-.\s]?)?\(?([0-9]{3})\)?[-.\s]?([0-9]{3})[-.\s]?([0-9]{4})\b',
    'ssn': r'\b\d{3}-?\d{2}-?\d{4}\b',
    'credit_card': r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b',
    'ip_address': r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b',
    'mac_address': r'\b(?:[0-9A-Fa-f]{2}[:-]){5}(?:[0-9A-Fa-f]{2})\b',
}

def mask_pii(text: str, pattern: str, mask_char: str = '*') -> Tuple[str, int]:
    """Mask PII in text and return masked text and count of matches"""
    matches = re.findall(pattern, text)
    if not matches:
        return text, 0
    
    # Create mask based on pattern type
    if 'email' in pattern:
        masked_text = re.sub(pattern, lambda m: mask_email(m.group()), text)
    elif 'phone' in pattern:
        masked_text = re.sub(pattern, lambda m: mask_phone(m.group()), text)
    else:
        # Generic masking - keep first and last character, mask the rest
        masked_text = re.sub(pattern, lambda m: mask_generic(m.group(), mask_char), text)
    
    return masked_text, len(matches)

def mask_email(email: str) -> str:
    """Mask email address while preserving domain"""
    local, domain = email.split('@', 1)
    if len(local) <= 2:
        return f"{local[0]}*@{domain}"
    return f"{local[0]}{'*' * (len(local) - 2)}{local[-1]}@{domain}"

def mask_phone(phone: str) -> str:
    """Mask phone number"""
    digits = re.sub(r'[^\d]', '', phone)
    if len(digits) == 10:
        return f"({digits[:3]}) ***-{digits[-4:]}"
    return f"{digits[:3]}-***-{digits[-4:]}" if len(digits) >= 7 else "***-***-****"

def mask_generic(text: str, mask_char: str = '*') -> str:
    """Generic masking for other PII types"""
    if len(text) <= 2:
        return mask_char * len(text)
    return f"{text[0]}{mask_char * (len(text) - 2)}{text[-1]}"

def scan_file(file_path: Path, mask: bool = False) -> Dict[str, any]:
    """Scan a single file for PII"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return {"error": f"Failed to read {file_path}: {e}"}
    
    results = {
        "file": str(file_path),
        "pii_found": False,
        "total_matches": 0,
        "patterns_found": {},
        "masked_content": content if mask else None
    }
    
    current_content = content
    
    for pii_type, pattern in PII_PATTERNS.items():
        masked_text, count = mask_pii(current_content, pattern)
        if count > 0:
            results["pii_found"] = True
            results["total_matches"] += count
            results["patterns_found"][pii_type] = count
            current_content = masked_text
    
    if mask and results["pii_found"]:
        results["masked_content"] = current_content
    
    return results

def scan_directory(directory: Path, mask: bool = False) -> List[Dict[str, any]]:
    """Scan all markdown files in a directory for PII"""
    results = []
    
    if not directory.exists():
        print(f"Directory not found: {directory}")
        return results
    
    for file_path in directory.glob("*.md"):
        if file_path.name.startswith("TEMPLATE_") or file_path.name == "README.md":
            continue
        
        result = scan_file(file_path, mask)
        results.append(result)
    
    return results

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description="Scan conversation archives for PII")
    parser.add_argument("--path", required=True, help="Path to scan for PII")
    parser.add_argument("--mask", action="store_true", help="Mask PII in output files")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    
    args = parser.parse_args()
    
    directory = Path(args.path)
    results = scan_directory(directory, args.mask)
    
    total_files = len(results)
    files_with_pii = sum(1 for r in results if r.get("pii_found", False))
    total_matches = sum(r.get("total_matches", 0) for r in results)
    
    print(f"🔍 PII Scan Results")
    print(f"📁 Directory: {directory}")
    print(f"📄 Files scanned: {total_files}")
    print(f"⚠️  Files with PII: {files_with_pii}")
    print(f"🔢 Total PII matches: {total_matches}")
    
    if files_with_pii > 0:
        print(f"\n⚠️  PII Found in {files_with_pii} files:")
        for result in results:
            if result.get("pii_found", False):
                print(f"  📄 {result['file']}")
                for pii_type, count in result.get("patterns_found", {}).items():
                    print(f"    - {pii_type}: {count} matches")
        
        if args.mask:
            print(f"\n🔒 PII has been masked in files")
        else:
            print(f"\n💡 Use --mask flag to automatically mask PII")
            return 1  # Exit with error code if PII found and not masked
    else:
        print(f"\n✅ No PII detected")
    
    return 0

if __name__ == "__main__":
    exit(main())
