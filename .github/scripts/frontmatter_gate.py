import os, re, sys, subprocess, datetime
from pathlib import Path

REQ_KEYS = ["project","type","status","tags","updated"]
SKIP_PATTERNS = [re.compile(r"^README\.md$"), re.compile(r"^LICENSE"), re.compile(r"^\.github/")]

def load_list(yaml_text, key):
    # Look for the key and capture everything until the next top-level key
    m = re.search(rf"(?m)^{key}:\s*\n((?:[^\n]*\n)*?)(?=\n[A-Za-z_]+:|$)", yaml_text)
    if not m: return []
    # Extract all lines that start with '  - ' (two spaces and dash)
    lines = m.group(1).split('\n')
    items = []
    for line in lines:
        if re.match(r'^\s*-\s+', line):
            # Extract everything after '  - ' (allowing spaces in values)
            match = re.search(r'^\s*-\s+(.+)', line)
            if match:
                items.append(match.group(1).strip())
    return items

def load_ontology():
    p = Path("docs/ONTOLOGY.yml")
    if not p.exists():
        return {"types":["capsule","memo","assessment","log","decision","spec"],
                "statuses":["draft","matured","archived"],
                "projects":["Career Intelligence Space"]}
    t = p.read_text(encoding="utf-8", errors="ignore")
    return {"types": load_list(t,"types") or ["capsule","memo","assessment","log","decision","spec"],
            "statuses": load_list(t,"statuses") or ["draft","matured","archived"],
            "projects": load_list(t,"projects") or ["Career Intelligence Space"]}

def load_allowed_tags():
    p = Path("docs/TAGS_REGISTRY.yml")
    if not p.exists(): return set()
    txt = p.read_text(encoding="utf-8", errors="ignore")
    return set(re.findall(r"(?m)^-\s*([A-Za-z0-9_\-]+)\s*$", txt))

FM_RE = re.compile(r"^\ufeff?\s*---\s*\n(.*?)\n---\s*\n?", re.DOTALL)

def parse_fm_block(text):
    m = FM_RE.match(text)
    if not m: return None, {}
    head = m.group(1)
    data = {}
    def grab(key, pat):
        mm = re.search(pat, head, re.M)
        return mm.group(1).strip().strip("\"'") if mm else None
    data["project"] = grab("project", r"^\s*project:\s*(.+)$")
    data["type"]    = grab("type",    r"^\s*type:\s*([A-Za-z0-9_\-]+)")
    data["status"]  = grab("status",  r"^\s*status:\s*([A-Za-z0-9_\-]+)")
    data["updated"] = grab("updated", r"^\s*updated:\s*['\"]?([0-9]{4}-[0-9]{2}-[0-9]{2})['\"]?")
    tags=[]
    m_inline = re.search(r"^\s*tags:\s*\[(.*?)\]", head, re.M)
    if m_inline:
        for x in re.split(r"[,\s]+", m_inline.group(1)):
            x = x.strip().strip("\"'"); 
            if x: tags.append(x)
    else:
        m_tagline = re.search(r"^\s*tags:\s*$", head, re.M)
        if m_tagline:
            lines=head.splitlines()
            idx=None
            for i,l in enumerate(lines):
                if re.match(r"^\s*tags:\s*$", l): idx=i; break
            if idx is not None:
                j=idx+1
                while j<len(lines) and re.match(r"^\s", lines[j]):
                    m2=re.match(r"^\s*-\s*(.+)$", lines[j])
                    if m2:
                        x=m2.group(1).strip().strip("\"'")
                        if x: tags.append(x)
                    j+=1
    data["tags"]=tags
    return head, data

def changed_md_files():
    try:
        event = os.getenv("GITHUB_EVENT_NAME","")
        base  = os.getenv("GITHUB_BASE_REF","")
        if event=="pull_request" and base:
            subprocess.run(["git","fetch","origin",base,"--depth","1"], check=False)
            out = subprocess.check_output(["git","diff","--name-only",f"origin/{base}...HEAD"], text=True, stderr=subprocess.DEVNULL)
            files = [f for f in out.splitlines() if f.endswith(".md")]
        else:
            out = subprocess.check_output(["git","diff","--name-only","HEAD~1..HEAD"], text=True, stderr=subprocess.DEVNULL)
            files = [f for f in out.splitlines() if f.endswith(".md")]
    except Exception:
        files=[]
    # Do not fallback to repo-wide scan; keep scope limited to diffs
    keep=[]
    for f in files:
        skip=False
        for pat in SKIP_PATTERNS:
            if pat.search(f): skip=True; break
        if not skip: keep.append(f)
    return sorted(set(keep))

def prior_updated(path, base_ref):
    try:
        if not base_ref: return None
        txt = subprocess.check_output(["git","show",f"origin/{base_ref}:{path}"], text=True, stderr=subprocess.DEVNULL)
        m = FM_RE.match(txt or "")
        if not m: return None
        mm = re.search(r"^\s*updated:\s*([0-9]{4}-[0-9]{2}-[0-9]{2})", m.group(1), re.M)
        return mm.group(1) if mm else None
    except Exception:
        return None

def main():
    onto = load_ontology()
    allowed_tags = load_allowed_tags()
    base = os.getenv("GITHUB_BASE_REF","")
    strict_tags = os.getenv("FRONTMATTER_STRICT_TAGS","0")=="1"
    files = changed_md_files()
    errs=[]; warns=[]
    for f in files:
        p = Path(f)
        try:
            text = p.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        m = FM_RE.match(text)
        if not m:
            errs.append(f"{f}: no front-matter block at top")
            continue
        _, data = parse_fm_block(text)
        miss=[k for k in REQ_KEYS if not data.get(k)]
        if miss:
            errs.append(f"{f}: missing keys {miss}")
        if data.get("project") and data["project"] not in onto["projects"]:
            errs.append(f"{f}: project '{data['project']}' not in {onto['projects']}")
        if data.get("type") and data["type"] not in onto["types"]:
            errs.append(f"{f}: type '{data['type']}' not in {onto['types']}")
        if data.get("status") and data["status"] not in onto["statuses"]:
            errs.append(f"{f}: status '{data['status']}' not in {onto['statuses']}")
        if data.get("updated"):
            try:
                new_dt = datetime.date.fromisoformat(data["updated"])
            except Exception:
                errs.append(f"{f}: updated not ISO YYYY-MM-DD")
            else:
                old = prior_updated(f, base)
                if old:
                    try:
                        old_dt = datetime.date.fromisoformat(old)
                        if new_dt < old_dt:
                            errs.append(f"{f}: updated {data['updated']} older than base {old}")
                    except Exception:
                        pass
        tlist = data.get("tags") or []
        if not tlist:
            errs.append(f"{f}: tags empty")
        elif allowed_tags:
            oov=[t for t in tlist if t not in allowed_tags]
            if oov and strict_tags:
                errs.append(f"{f}: tags not in registry {oov}")
            elif oov:
                warns.append(f"OOV tags in {f}: {', '.join(oov)}")
    if warns:
        for w in warns:
            print(f"::warning::{w}")
    if errs:
        print(f"❌ Front-matter violations ({len(errs)} files)")
        for e in errs:
            print(f"- {e}")
        sys.exit(1)
    print("✅ Front-matter OK")
if __name__=="__main__":
    main()
