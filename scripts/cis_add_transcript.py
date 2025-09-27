import sys, re, subprocess, os
from pathlib import Path
from datetime import date

def run(args):
    return subprocess.run(args, check=True, text=True, capture_output=True).stdout.strip()

def main():
    if len(sys.argv) < 2:
        print("usage: cis-add-transcript /path/to/file.md [--tags tag1,tag2]"); sys.exit(2)
    src = Path(sys.argv[1]).expanduser().resolve()
    tags = "transcript,field,chat"
    if len(sys.argv) >= 4 and sys.argv[2] == "--tags": tags = sys.argv[3]

    if not src.exists():
        print(f"missing: {src}"); sys.exit(1)

    today = date.today().isoformat()
    safe = re.sub(r'\.md$', '', src.name, flags=re.I)
    safe = re.sub(r'[^A-Za-z0-9._-]+', '_', safe).strip('_').lower()
    dst = Path("99_LOGS/transcripts")/f"{today}_{safe}.md"
    dst.parent.mkdir(parents=True, exist_ok=True)

    txt = src.read_text(encoding="utf-8", errors="ignore").lstrip()
    fm = f"""---
project: Career Intelligence Space
type: log
status: matured
tags: [{tags}]
updated: {today}
---
"""
    if not txt.startswith("---"):
        if txt and not txt.startswith("\n"): txt = "\n"+txt
        txt = fm + txt
    dst.write_text(txt, encoding="utf-8")
    run(["git","add",str(dst)])

    # branch name
    slug = re.sub(r'[^a-z0-9]+','-', safe).strip('-')
    branch = f"feat/transcript-{today}-{slug}"
    try:
        run(["git","switch","-c",branch])
    except subprocess.CalledProcessError:
        run(["git","switch",branch])

    run(["git","commit","-m","log: add field transcript export"])
    run(["git","push","-u","origin",branch])

    pr_url = run(["gh","pr","create","--fill"])
    pr_num = run(["gh","pr","view","--json","number","--jq",".number"])
    try:
        run(["gh","pr","merge",pr_num,"--squash","--auto"])
    except subprocess.CalledProcessError:
        pass

    # retrigger PR-event checks (tiny no-op)
    Path("README.md").write_text(Path("README.md").read_text(encoding="utf-8") + "\n" if Path("README.md").exists() else "\n", encoding="utf-8")
    run(["git","add","README.md"])
    run(["git","commit","-m",f"chore ci retrigger PR checks PR {pr_num}"])
    run(["git","push"])

    # update-branch (strict protection)
    try:
        run(["gh","api","-X","PUT",f"repos/:owner/:repo/pulls/{pr_num}/update-branch","-H","Accept: application/vnd.github+json"])
    except subprocess.CalledProcessError:
        pass

    # show health
    try:
        out = run(["python3",".github/scripts/pr_health.py",pr_num])
        print(out)
    except Exception:
        pass

    print(f"opened {pr_url}")
    print(f"target file: {dst}")

if __name__ == "__main__":
    main()
