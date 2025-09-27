#!/usr/bin/env python3
import json, subprocess, sys

def jrun(args):
    r = subprocess.run(["gh"]+args, capture_output=True, text=True)
    if r.returncode != 0: return None
    try: return json.loads(r.stdout)
    except: return None

def api(path, jq=None):
    args=["api", path]
    if jq: args += ["--jq", jq]
    r = subprocess.run(["gh"]+args, capture_output=True, text=True)
    if r.returncode != 0: return None
    return r.stdout.strip()

def main():
    pr = sys.argv[1] if len(sys.argv) > 1 else None
    if not pr:
        cur = jrun(["pr","view","--json","number"])
        if not cur:
            print("ERR: not on a PR branch; pass PR number", file=sys.stderr)
            sys.exit(2)
        pr = str(cur["number"])

    repo = api("repos/{owner}/{repo}", ".full_name")
    if not repo:
        print("ERR: gh repo lookup failed", file=sys.stderr); sys.exit(2)

    prot = jrun(["api", f"repos/{repo}/branches/main/protection"])
    if not prot:
        print("ERR: branch protection read failed", file=sys.stderr); sys.exit(2)

    strict = bool(prot.get("required_status_checks",{}).get("strict", False))
    req = prot.get("required_status_checks",{}).get("contexts",[]) or []

    pv = jrun(["pr","view",pr,"--json","headRefOid,mergeStateStatus,state,headRefName,baseRefName"])
    if not pv:
        print("ERR: PR view failed", file=sys.stderr); sys.exit(2)

    sha = pv["headRefOid"]
    st = jrun(["api", f"repos/{repo}/commits/{sha}/status"])
    contexts = []
    if st and isinstance(st.get("statuses"), list):
        for s in st["statuses"]:
            c = s.get("context")
            if c: contexts.append(c)
    missing = [c for c in req if c not in set(contexts)]
    state = st.get("state") if st else "unknown"
    merge_state = pv.get("mergeStateStatus","?")

    print(f"PR #{pr} on {repo}")
    print(f"required: {req} strict={strict}")
    print(f"head: {sha[:7]} status: {state} mergeState: {merge_state}")
    if missing:
        print("MISSING contexts:", ", ".join(missing))

    cmds = []
    if missing:
        cmds.append("printf '\n' >> README.md && git add README.md && git commit -m \"chore(ci): retrigger PR checks\" && git push")
    if strict and merge_state in ("BLOCKED","DIRTY"):
        cmds.append(f"gh api -X PUT repos/{repo}/pulls/{pr}/update-branch -H \"Accept: application/vnd.github+json\"")
    cmds.append(f"gh pr merge {pr} --squash --auto")

    print("next:")
    for c in cmds:
        print("  ", c)

    if missing or state == "pending" or merge_state in ("BLOCKED","DIRTY"):
        sys.exit(1)
    sys.exit(0)

if __name__ == "__main__":
    main()
