from pathlib import Path
from datetime import date
root=Path("99_LOGS/transcripts"); root.mkdir(parents=True, exist_ok=True)
files=sorted(root.glob("*.txt"), key=lambda p:p.name, reverse=True)
fm=("""---
project: Career Intelligence Space
type: log
status: matured
tags: [transcripts, index]
updated: {today}
---
""".format(today=date.today().isoformat()))
lines=["# Transcripts Index",""]
lines+=["- [{0}](./{0})".format(p.name) for p in files] if files else ["- _No transcripts yet._"]
idx=root/"INDEX.md"; idx.write_text(fm+"\n".join(lines)+"\n", encoding="utf-8"); print("wrote",idx)
