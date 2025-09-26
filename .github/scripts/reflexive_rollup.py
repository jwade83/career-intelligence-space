import os, re, json, time, math, glob, datetime
from pathlib import Path

BUDGET = 5*60
start = time.time()

repo = Path(".").resolve()
chron = repo/"08_CHRONICLE"
logs_collapse = repo/"99_LOGS"/"collapse"
logs_anom = repo/"99_LOGS"/"anomalies"
tags_reg = repo/"docs"/"TAGS_REGISTRY.yml"
checkpoints = repo/"03_CHECKPOINTS"
index_md = chron/"INDEX.md"

chron.mkdir(parents=True, exist_ok=True)
logs_anom.mkdir(parents=True, exist_ok=True)

FM_RE = re.compile(r"^\ufeff?\s*---\s*\n(.*?)\n---", re.DOTALL)  # BOM/leading-space tolerant

def fm_tags(text: str):
    m = FM_RE.search(text)
    if not m: return []
    head = m.group(1).splitlines()
    tags=[]; i=0
    while i<len(head):
        line=head[i]
        if line.strip().startswith('tags:'):
            val=line.split(':',1)[1].strip()
            if val and not val.startswith('|'):
                val2=val.strip('[]')
                if val2:
                    for x in re.split(r'[,\s]+', val2):
                        x=x.strip().strip('"').strip("'")
                        if x: tags.append(x)
            j=i+1
            while j<len(head) and (head[j].startswith(' ') or head[j].startswith('\t')):
                m2=re.match(r"\s*-\s*(.+)$", head[j])
                if m2:
                    x=m2.group(1).strip().strip('"').strip("'")
                    if x: tags.append(x)
                j+=1
            i=j-1
        i+=1
    return tags

def H(counts: dict) -> float:
    tot=sum(counts.values()) or 1
    h=0.0
    for c in counts.values():
        p=c/tot
        h -= p*math.log(p,2)
    return round(h,3)

now = datetime.datetime.utcnow()
w1 = now - datetime.timedelta(days=7)
w2 = now - datetime.timedelta(days=14)

def mdt(p: Path):
    try: return datetime.datetime.utcfromtimestamp(p.stat().st_mtime)
    except Exception: return w2 - datetime.timedelta(days=365)

all_md=[Path(p) for p in glob.glob("**/*.md", recursive=True)]
chron_md=[p for p in all_md if str(p).startswith("08_CHRONICLE/") and p.name!="INDEX.md"]

caps_last7=[p for p in chron_md if mdt(p)>=w1]
caps_prev =[p for p in chron_md if w2<=mdt(p)<w1]
capsules_added=len(caps_last7)
growth=round(capsules_added/max(1,len(caps_prev)),3)

idx_txt=index_md.read_text(encoding="utf-8", errors="ignore") if index_md.exists() else ""
index_missing=sum(1 for p in chron_md if p.name not in idx_txt)

# Broken internal links (treat "/..." as repo-root). Track case-mismatch separately.
link_re=re.compile(r"\[[^\]]+\]\((?!https?://)([^)]+)\)")
broken=0
case_mismatch=0
for p in all_md:
    try: txt=p.read_text(encoding="utf-8", errors="ignore")
    except Exception: continue
    for tgt in link_re.findall(txt):
        tgt=tgt.split("#")[0].strip()
        if not tgt or tgt.startswith("mailto:"): continue
        target_path = (repo / tgt.lstrip("/")) if tgt.startswith("/") else (p.parent / tgt)
        if target_path.exists():
            continue
        # case-insensitive fallback: if any file matches path ignoring case, count as case_mismatch
        parts = target_path.parts
        probe = repo if target_path.is_absolute() else p.parent
        ok=True
        for comp in parts[-(len(target_path.relative_to(probe) .parts) if str(probe) in str(target_path) else len(parts)):]:
            # iterative descent; listdir for available names at this level
            try:
                names = {n.name for n in probe.iterdir()}
                if comp in names:
                    probe = probe / comp
                else:
                    # try case-insensitive hit
                    low = comp.lower()
                    match = next((n for n in names if n.lower()==low), None)
                    if match:
                        probe = probe / match
                        case_mismatch += 1
                        ok=True
                    else:
                        ok=False
                        break
            except Exception:
                ok=False; break
        if not ok:
            broken += 1

# Tags (inline + block; tolerant frontmatter)
tags={}
for p in all_md:
    try: t=p.read_text(encoding="utf-8", errors="ignore")
    except Exception: continue
    for tag in fm_tags(t):
        tags[tag]=tags.get(tag,0)+1
tag_entropy=H(tags)
top5=sorted(tags.items(), key=lambda x:x[1], reverse=True)[:5]
top5_cov=round(100*(sum(v for _,v in top5)/(sum(tags.values()) or 1)),1)

oov_rate=None
if tags_reg.exists():
    try:
        allowed=set(re.findall(r"-\s*([A-Za-z0-9_\-]+)", tags_reg.read_text(encoding="utf-8",errors="ignore")))
        used=set(tags.keys())
        oov=[t for t in used if t not in allowed]
        oov_rate=round(100*len(oov)/max(1,len(used)),1) if used else 0.0
    except Exception:
        oov_rate=None

events=[]
if logs_collapse.exists():
    for p in logs_collapse.glob("*.json"):
        try:
            data=json.loads(p.read_text(encoding="utf-8",errors="ignore"))
            ts=data.get("ts"); dt=w2
            if ts:
                try: dt=datetime.datetime.fromisoformat(ts.replace("Z",""))
                except Exception: dt=w2
            data["_dt"]=dt; events.append(data)
        except Exception: pass
ev7=[e for e in events if e["_dt"]>=w1]
override=sum(1 for e in ev7 if "override" in (e.get("action_taken") or []))
frustr  =sum(1 for e in ev7 if "frustration" in (e.get("signal") or []))
reprime =sum(1 for e in ev7 if "reprime" in (e.get("action_taken") or []))

cps=list(checkpoints.glob("cp_*.md")) if checkpoints.exists() else []
last_cp=max([mdt(p) for p in cps], default=None)
days_since_cp=(now-last_cp).days if last_cp else None

wk=f"{now.isocalendar().year}W{now.isocalendar().week:02d}"
out=chron/f"weekly_reflexive_rollup_{wk}.md"
lines=[
f"# Reflexive Rollup — {wk}","",
"## Stress Signals (last 7 days)",
f"- capsules_added: {capsules_added}",
f"- capsule_growth_rate: {growth}",
f"- index_missing_entries: {index_missing}",
f"- broken_internal_links: {broken}",
f"- case_mismatch_links: {case_mismatch}",
f"- tag_entropy: {tag_entropy}",
f"- top5_tag_coverage_pct: {top5_cov}",
f"- oov_tag_rate_pct: {oov_rate if oov_rate is not None else 'n/a'}",
f"- collapse_events_count: {len(ev7)}",
f"- override_count: {override}",
f"- frustration_events: {frustr}",
f"- context_reprime_events: {reprime}",
f"- days_since_last_checkpoint: {days_since_cp if days_since_cp is not None else 'n/a'}","",
"## Notes",
"- Budget-capped & offline; advanced metrics skipped if runtime exceeds budget.",
f"- brownout: {str((time.time()-start)>BUDGET).lower()}","",
"## Next Actions",
"- If 2+ signals trend up for 2 weeks, consult `harness/docs/OPS_PROMOTION.yml` to consider promotion.",
"- If index_missing_entries > 0, verify auto-index or update `08_CHRONICLE/INDEX.md`.",
"- If oov_tag_rate_pct is high, update `docs/TAGS_REGISTRY.yml` and/or `docs/ONTOLOGY.yml`.",
"- If days_since_last_checkpoint is high with heavy change, tag a new checkpoint."
]
out.write_text("\n".join(lines), encoding="utf-8")
print(f"Wrote {out}")
