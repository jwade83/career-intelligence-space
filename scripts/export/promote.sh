#!/usr/bin/env bash
set -euo pipefail
usage(){ echo "Usage: $0 <source_path> --to published|candidates|outreach|local|master_portfolio [--note 'reason']"; exit 1; }
[ $# -ge 3 ] || usage
SRC="$1"; shift
DEST=""; NOTE=""
while [ $# -gt 0 ]; do
  case "$1" in
    --to) DEST="$2"; shift 2;;
    --note) NOTE="$2"; shift 2;;
    *) usage;;
  esac
done
root="$(git rev-parse --show-toplevel)"
cfg="$root/export/export_config.yml"
path="$(yq '.targets.'"$DEST"'.path // ""' "$cfg")"
enabled="$(yq '.targets.'"$DEST"'.enabled // false' "$cfg")"
[ "$enabled" = "true" ] || { echo "Target '$DEST' disabled"; exit 2; }
[ -n "$path" ] || { echo "No path configured for '$DEST'"; exit 2; }
mkdir -p "$root/$path"
base="$(basename "$SRC")"
dest_file="$root/$path/$base"
# Ensure provenance header exists
if ! head -n1 "$SRC" | grep -qi 'Provenance:'; then
  {
    echo "_Provenance: Promoted from $SRC on $(date -u +%F)Z_"
    cat "$SRC"
  } > "$dest_file"
else
  cp "$SRC" "$dest_file"
fi
# Enforce single '# UPGRADE' footer
grep -qx '# UPGRADE' "$dest_file" || echo '# UPGRADE' >> "$dest_file"
git add "$dest_file"
msg="export($DEST): promote $(basename "$SRC")"
[ -n "$NOTE" ] && msg="$msg — $NOTE"
git commit -m "$msg"
git push
# Append Captain's Log
today="99_LOGS/journal/$(date +%Y%m%d)_journal.md"
if [ -f "$today" ]; then
  printf "\n- Promoted %s to %s (%s)\n" "$SRC" "$path" "$(date -u +%F)" >> "$today"
  grep -qx '# UPGRADE' "$today" || echo '# UPGRADE' >> "$today"
  git add "$today" && git commit -m "journal: note promotion of $base to $DEST" && git push
fi
echo "Promoted to: $dest_file"
# UPGRADE
