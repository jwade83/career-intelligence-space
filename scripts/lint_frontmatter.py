#!/usr/bin/env python3
"""
Frontmatter linter for CIS Harness archives.
- Enforces required keys per type
- Normalizes participants to list
- Validates ISO dates, timezone, tags
- (Optional) Checks terms against ontology.yml if present
Exit nonzero on any error.
"""
import sys, re, json, yaml
from pathlib import Path

ROOT = Path(".")
ARCHIVE_DIRS = [Path("08_CHRONICLE/conversations")]
ISO_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

def load_schema():
    """Load archive schema configuration"""
    schema_file = ROOT / "config" / "archive_schema.yml"
    if not schema_file.exists():
        # Fallback to hardcoded values
        return {
            "version": 1,
            "required_common": ["project", "type", "status", "tags", "updated"],
            "required_conversation_archive": ["conversation_date", "participants", "conversation_id"],
            "required_conversation_archive_lite": ["conversation_date", "participants", "conversation_id"],
            "recommended": ["timezone", "related"]
        }
    
    try:
        import yaml
        with open(schema_file, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f) or {}
    except Exception:
        # Fallback to hardcoded values
        return {
            "version": 1,
            "required_common": ["project", "type", "status", "tags", "updated"],
            "required_conversation_archive": ["conversation_date", "participants", "conversation_id"],
            "required_conversation_archive_lite": ["conversation_date", "participants", "conversation_id"],
            "recommended": ["timezone", "related"]
        }

def read_frontmatter(p: Path):
    txt = p.read_text(encoding="utf-8", errors="ignore")
    if not txt.startswith("---"):
        return None, txt
    parts = txt.split("\n---", 1)
    if len(parts) < 2: return None, txt
    fm_raw = parts[0].lstrip("-\n")
    try:
        fm = yaml.safe_load(fm_raw) or {}
    except Exception as e:
        raise SystemExit(f"[LINT] YAML parse error in {p}: {e}")
    body = parts[1].lstrip("-\n")
    return fm, body

def to_list(x):
    if isinstance(x, list): return x
    if isinstance(x, str):
        s = x.strip()
        # try JSON array first
        if s.startswith("[") and s.endswith("]"):
            try: return json.loads(s)
            except: pass
        # comma separated
        return [i.strip() for i in s.split(",") if i.strip()]
    return [x]

def load_ontology_terms():
    onto_file = ROOT / "ontology" / "ontology.yml"
    if not onto_file.exists(): return set()
    try:
        data = yaml.safe_load(onto_file.read_text()) or {}
        terms = set()
        for k, v in (data.get("terms", {}) or {}).items():
            terms.add(str(k).strip().lower())
            for syn in (v.get("synonyms",[]) or []):
                terms.add(str(syn).strip().lower())
        return terms
    except Exception:
        return set()

def check_terms(body: str, terms:set, path:Path):
    # Optional semantic nudge: flag unknown ALL-CAPS tokens that look like project terms
    if not terms: return []
    suspects = set(re.findall(r"\b[A-Z][A-Z0-9_-]{2,}\b", body))
    warnings=[]
    for tok in sorted(suspects):
        if tok.lower() not in terms:
            warnings.append(f"[WARN] {path}: term '{tok}' not in ontology. (C3)")
    return warnings

def lint_file(p: Path, terms:set, schema:dict):
    fm, body = read_frontmatter(p)
    errs, warns = [], []
    if fm is None:
        errs.append(f"[ERR] {p}: missing frontmatter block '---' at top. (C4)")
        return errs, warns
    
    # Check common required fields
    req_common = set(schema.get("required_common", []))
    missing = (req_common - set(fm.keys()))
    if missing:
        errs.append(f"[ERR] {p}: missing keys {sorted(missing)}. (C4)")
    
    # Check tags
    if "tags" in fm and not fm["tags"]:
        errs.append(f"[ERR] {p}: 'tags' must be non-empty list. (C4)")
    
    # Check date format
    if "updated" in fm and not ISO_DATE.match(str(fm["updated"])):
        errs.append(f"[ERR] {p}: 'updated' must be YYYY-MM-DD. (C4)")
    
    # Type-specific checks
    file_type = fm.get("type")
    if file_type == "conversation_archive":
        req_convo = set(schema.get("required_conversation_archive", []))
        missing2 = (req_convo - set(fm.keys()))
        if missing2:
            errs.append(f"[ERR] {p}: missing convo keys {sorted(missing2)}. (C4)")
    elif file_type == "conversation_archive_lite":
        req_lite = set(schema.get("required_conversation_archive_lite", []))
        missing2 = (req_lite - set(fm.keys()))
        if missing2:
            errs.append(f"[ERR] {p}: missing lite convo keys {sorted(missing2)}. (C4)")
    
    # Conversation-specific validations
    if file_type in {"conversation_archive", "conversation_archive_lite"}:
        # participants -> list
        if "participants" in fm:
            fm["participants"] = to_list(fm["participants"])
            if not isinstance(fm["participants"], list) or not fm["participants"]:
                errs.append(f"[ERR] {p}: 'participants' must be a non-empty list. (C4)")
        if "conversation_date" in fm and not ISO_DATE.match(str(fm["conversation_date"])):
            errs.append(f"[ERR] {p}: 'conversation_date' must be YYYY-MM-DD. (C4)")
        if "conversation_id" in fm and not str(fm["conversation_id"]).strip():
            errs.append(f"[ERR] {p}: 'conversation_id' must be non-empty. (C4)")
    
    # Check recommended fields
    recommended = schema.get("recommended", [])
    for rec_field in recommended:
        if rec_field not in fm:
            if rec_field == "timezone":
                warns.append(f"[WARN] {p}: add 'timezone: America/Los_Angeles' for temporal clarity. (C4)")
            else:
                warns.append(f"[WARN] {p}: consider adding '{rec_field}' field. (C4)")
    
    # Light vocabulary drift nudge
    warns += check_terms(body, terms, p)
    return errs, warns

def main():
    schema = load_schema()
    terms = load_ontology_terms()
    targets=[]
    for base in ARCHIVE_DIRS:
        if base.exists():
            targets += list(base.rglob("*.md"))
    if not targets:
        print("[LINT] No markdown files found under archives.")
        sys.exit(0)
    
    print(f"[LINT] Using Archive Schema v{schema.get('version', 'unknown')}")
    total_errs, total_warns = 0, 0
    for p in sorted(targets):
        errs, warns = lint_file(p, terms, schema)
        for e in errs: print(e)
        for w in warns: print(w)
        total_errs += len(errs); total_warns += len(warns)
    print(f"[LINT] Completed. errs={total_errs} warns={total_warns}")
    sys.exit(1 if total_errs else 0)

if __name__ == "__main__":
    main()
