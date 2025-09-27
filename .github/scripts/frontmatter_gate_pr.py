from pathlib import Path
import sys, re

REQ = ['project','type','status','tags','updated']
files = [f for f in sys.argv[1:] if f.lower().endswith('.md')]
if not files:
    print("gate(pr-scope): no changed markdown files; ok")
    raise SystemExit(0)

errors = []
for f in files:
    p = Path(f)
    if not p.exists():
        continue
    txt = p.read_text(encoding='utf-8', errors='ignore')
    m = re.match(r'^\s*---\n(.*?)\n---\s*\n', txt, re.S)
    if not m:
        errors.append(f"{f}: no front-matter block at top"); continue
    fm = m.group(1)
    present = {k: False for k in REQ}
    for line in fm.splitlines():
        if ':' in line:
            k = line.split(':',1)[0].strip()
            if k in present: present[k] = True
    missing = [k for k,v in present.items() if not v]
    if missing:
        errors.append(f"{f}: missing keys {missing}")
if errors:
    print("❌ Front-matter violations (changed files only)")
    for e in errors: print("-", e)
    raise SystemExit(1)
print("✅ Front-matter gate (changed files) OK")
