import sys,re,subprocess,os
from pathlib import Path
from datetime import date
def run(a): return subprocess.run(a,check=True,text=True,capture_output=True).stdout.strip()
def main():
    if len(sys.argv)<2: print("usage: cis-add-transcript /path/to/export.(md|txt) [--tags tag1,tag2]"); exit(2)
    src=Path(sys.argv[1]).expanduser().resolve()
    if not src.exists(): print(f"missing: {src}"); exit(1)
    today=date.today().isoformat()
    safe=re.sub(r'\.(md|txt)$','',src.name,flags=re.I); safe=re.sub(r'[^A-Za-z0-9._-]+','_',safe).strip('_').lower()
    dst=Path("99_LOGS/transcripts")/f"{today}_{safe}.txt"; dst.parent.mkdir(parents=True,exist_ok=True)
    dst.write_text(src.read_text(encoding="utf-8",errors="ignore"),encoding="utf-8")
    slug=re.sub(r'[^a-z0-9]+','-',safe).strip('-'); br=f"feat/transcript-{today}-{slug}"
    try: run(["git","switch","-c",br])
    except subprocess.CalledProcessError: run(["git","switch",br])
    run(["git","add",str(dst)]); run(["git","commit","-m","log add transcript (txt)"]); run(["git","push","-u","origin",br])
    url=run(["gh","pr","create","--fill"]); num=run(["gh","pr","view","--json","number","--jq",".number"])
    try: run(["gh","pr","merge",num,"--squash","--auto"])
    except subprocess.CalledProcessError: pass
    rd=Path("README.md"); rd.write_text((rd.read_text(encoding="utf-8") if rd.exists() else "")+"\n",encoding="utf-8")
    run(["git","add","README.md"]); run(["git","commit","-m",f"chore(ci): retrigger PR checks PR {num}"]); run(["git","push"])
    print(f"opened {url}\ntarget file: {dst}")
if __name__=="__main__": main()
