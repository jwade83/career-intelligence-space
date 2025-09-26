import re, glob, sys
from pathlib import Path

root = Path('.').resolve()
link_re = re.compile(r'!?\[[^\]]+\]\((?!https?://|mailto:|#)([^)]+)\)')

broken = []
case_mismatch = []

for p in glob.glob("**/*.md", recursive=True):
    src = Path(p)
    try:
        txt = src.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        continue
    for raw in link_re.findall(txt):
        t = raw.split("#")[0].strip()
        if not t:
            continue
        base = root if t.startswith("/") else src.parent
        rel  = t.lstrip("/") if t.startswith("/") else t
        target = (base / rel)
        if target.exists():
            continue
        # case-insensitive probe
        probe = base
        ok_ci = True
        for comp in Path(rel).parts:
            try:
                names = list(probe.iterdir())
            except Exception:
                ok_ci = False; break
            exact = [n for n in names if n.name == comp]
            if exact:
                probe = exact[0]; continue
            low = [n for n in names if n.name.lower() == comp.lower()]
            if low:
                probe = low[0]
                case_mismatch.append(f"{src} -> {t}")
            else:
                ok_ci = False; break
        if not ok_ci:
            broken.append(f"{src} -> {t}")

if case_mismatch:
    print("⚠️ Case-mismatch links (fix casing in filename or link):")
    print("\n".join(f"- {x}" for x in sorted(set(case_mismatch))))

if broken:
    print("❌ Broken internal links:")
    print("\n".join(f"- {x}" for x in sorted(set(broken))))
    sys.exit(1)

print("✅ Internal links OK")
