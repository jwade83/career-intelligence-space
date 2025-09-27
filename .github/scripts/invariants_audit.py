import os, re, sys, json, subprocess
from pathlib import Path

def warn(msg):
    print(f"::warning::{msg}")

def fm_missing(paths):
    FM = re.compile(r"^\ufeff?\s*---\s*\n(.*?)\n---\s*\n?", re.DOTALL)
    bad=[]
    for p in paths:
        if not p.endswith(".md"): continue
        if p.startswith(".github/"): continue
        try:
            t = Path(p).read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        if not FM.match(t):
            bad.append(p)
    return bad

def docs_antipattern(paths):
    bad=[]
    for p in paths:
        if not p.startswith("docs/"): continue
        if not p.endswith(".md"): continue
        try:
            t = Path(p).read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        if re.search(r"\]\(docs/", t):
            bad.append(p)
    return bad

def list_md():
    return [str(p) for p in Path(".").rglob("*.md")]

def main():
    files = list_md()
    bad_fm = fm_missing(files)
    if bad_fm:
        warn("Files missing front-matter: " + ", ".join(sorted(bad_fm)[:50]))
    anti = docs_antipattern(files)
    if anti:
        warn("docs/ link anti-pattern (use ](./...)): " + ", ".join(sorted(anti)[:50]))
    print("✅ invariants audit completed (warn-only)")
    sys.exit(0)

if __name__ == "__main__":
    main()
