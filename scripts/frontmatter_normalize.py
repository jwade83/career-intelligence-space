#!/usr/bin/env python3
"""
Frontmatter Normalizer

Purpose: Auto-fix common frontmatter issues on changed markdown files in a PR.

Behavior:
- Limits scope to changed .md files against base ref
- Ensures required keys exist: project, type, status, tags, updated
- Normalizes values per docs/ONTOLOGY.yml and docs/TAGS_REGISTRY.yml when possible
- Adds missing 'updated' as today's date
- Converts known type aliases (e.g., quick_reference -> quick-reference)

This is a pragmatic normalizer; it never scans the entire repo.
"""
import os
import re
import sys
import subprocess
import datetime
from pathlib import Path

FM_RE = re.compile(r"^\ufeff?\s*---\s*\n(.*?)\n---\s*\n?", re.DOTALL)

def load_list(yaml_text: str, key: str):
    m = re.search(rf"(?m)^{key}:\s*\n((?:[^\n]*\n)*?)(?=\n[A-Za-z_]+:|$)", yaml_text)
    if not m:
        return []
    lines = m.group(1).split('\n')
    items = []
    for line in lines:
        if re.match(r"^\s*-\s+", line):
            mm = re.search(r"^\s*-\s+(.+)", line)
            if mm:
                items.append(mm.group(1).strip().strip("\"'"))
    return items

def load_ontology():
    p = Path("docs/ONTOLOGY.yml")
    if not p.exists():
        return {
            "types": ["capsule","memo","assessment","log","decision","spec"],
            "statuses": ["draft","matured","archived","active"],
            "projects": ["Career Intelligence Space"],
        }
    txt = p.read_text(encoding="utf-8", errors="ignore")
    return {
        "types": load_list(txt, "types") or ["capsule","memo","assessment","log","decision","spec"],
        "statuses": load_list(txt, "statuses") or ["draft","matured","archived","active"],
        "projects": load_list(txt, "projects") or ["Career Intelligence Space"],
    }

def load_allowed_tags():
    p = Path("docs/TAGS_REGISTRY.yml")
    if not p.exists():
        return set()
    txt = p.read_text(encoding="utf-8", errors="ignore")
    return set(re.findall(r"(?m)^-\s*([A-Za-z0-9_\-]+)\s*$", txt))

def changed_md_files():
    try:
        event = os.getenv("GITHUB_EVENT_NAME", "")
        base  = os.getenv("GITHUB_BASE_REF", "")
        if event == "pull_request" and base:
            subprocess.run(["git","fetch","origin", base, "--depth","1"], check=False)
            out = subprocess.check_output(["git","diff","--name-only", f"origin/{base}...HEAD"], text=True, stderr=subprocess.DEVNULL)
            files = [f for f in out.splitlines() if f.endswith(".md")]
        else:
            # Fallback to last commit diff in non-PR contexts
            out = subprocess.check_output(["git","diff","--name-only","HEAD~1..HEAD"], text=True, stderr=subprocess.DEVNULL)
            files = [f for f in out.splitlines() if f.endswith(".md")]
    except Exception:
        files = []
    return sorted(set(files))

def parse_frontmatter(text: str):
    m = FM_RE.match(text)
    if not m:
        return None, {}
    head = m.group(1)
    data = {}
    def grab(key, pat):
        mm = re.search(pat, head, re.M)
        return mm.group(1).strip().strip("\"'") if mm else None
    data["project"] = grab("project", r"^\s*project:\s*(.+)$")
    data["type"]    = grab("type",    r"^\s*type:\s*([A-Za-z0-9_\-]+)")
    data["status"]  = grab("status",  r"^\s*status:\s*([A-Za-z0-9_\-]+)")
    data["updated"] = grab("updated", r"^\s*updated:\s*['\"]?([0-9]{4}-[0-9]{2}-[0-9]{2})['\"]?")
    # tags list
    tags = []
    m_inline = re.search(r"^\s*tags:\s*\[(.*?)\]", head, re.M)
    if m_inline:
        for x in re.split(r"[,\s]+", m_inline.group(1)):
            x = x.strip().strip("\"'")
            if x:
                tags.append(x)
    else:
        if re.search(r"^\s*tags:\s*$", head, re.M):
            lines = head.splitlines()
            idx = None
            for i, l in enumerate(lines):
                if re.match(r"^\s*tags:\s*$", l):
                    idx = i; break
            if idx is not None:
                j = idx + 1
                while j < len(lines) and re.match(r"^\s", lines[j]):
                    m2 = re.match(r"^\s*-\s*(.+)$", lines[j])
                    if m2:
                        x = m2.group(1).strip().strip("\"'")
                        if x:
                            tags.append(x)
                    j += 1
    data["tags"] = tags
    return head, data

def render_frontmatter(data: dict) -> str:
    lines = ["---"]
    for key in ["project","type","status","tags","updated"]:
        if key == "tags":
            tags = data.get("tags") or []
            if tags and all("," not in t for t in tags):
                lines.append(f"tags: [{', '.join(tags)}]")
            else:
                lines.append("tags:")
                for t in tags:
                    lines.append(f"  - {t}")
        else:
            val = data.get(key)
            if key == "updated" and val:
                lines.append(f"updated: '{val}'")
            elif val is not None:
                lines.append(f"{key}: {val}")
    lines.append("---\n")
    return "\n".join(lines)

def normalize_file(path: Path, onto: dict, allowed_tags: set) -> bool:
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return False
    m = FM_RE.match(text)
    today = datetime.date.today().isoformat()
    changed = False
    head, data = (None, {}) if not m else parse_frontmatter(text)

    # If no frontmatter, do not synthesize from scratch; leave to author
    if not m:
        return False

    # Defaults
    if not data.get("project"):
        data["project"] = "Career Intelligence Space"; changed = True
    if not data.get("status"):
        data["status"] = "active"; changed = True
    if not data.get("updated"):
        data["updated"] = today; changed = True
    # Normalize type alias
    alias_map = {
        "quick_reference": "quick-reference",
        "quickreference": "quick-reference",
    }
    t = data.get("type")
    if t in alias_map:
        data["type"] = alias_map[t]; changed = True
    # Coerce to allowed values if close
    if data.get("type") and onto["types"] and data["type"] not in onto["types"]:
        # keep as-is; let gate fail rather than guess wrong
        pass
    # Tags: ensure list
    if data.get("tags") is None:
        data["tags"] = []
    # Write back
    if changed:
        new_fm = render_frontmatter(data)
        rest = text[m.end():] if m else text
        path.write_text(new_fm + rest, encoding="utf-8")
    return changed

def main():
    onto = load_ontology()
    allowed_tags = load_allowed_tags()
    files = changed_md_files()
    if not files:
        print("No changed markdown files to normalize. Skipping.")
        return 0
    any_changed = False
    for f in files:
        p = Path(f)
        if not p.exists():
            continue
        if normalize_file(p, onto, allowed_tags):
            print(f"Normalized frontmatter: {f}")
            any_changed = True
    if any_changed:
        # stage changes so caller can commit
        try:
            subprocess.run(["git","add"] + files, check=False)
        except Exception:
            pass
    print("Normalization complete.")
    return 0

if __name__ == "__main__":
    sys.exit(main())


