---
project: Career Intelligence Space
type: future_spec
status: deferred
tags: [harness, roadmap, hardware, assets, field_agent, antifragility]
updated: 2025-09-30
review_date: 2026-01-15
schema_version: v1
id: HARNESS_ADDENDUM_HARDWARE_ASSET_ROADMAP
---

# Hardware / Asset Roadmap — Harness Addendum

**Purpose**  
Specify the minimum and recommended non-repo assets (hardware + hosted services) that make the Harness immune system practical under real-world constraints (interrupted devices, limited mobile UIs, stateless LLM sessions). Map each asset to **collapse risks C1–C7**, define phased adoption, security, and acceptance gates.

---

## 1) Collapse Risks ↔ Environment Constraints

| Constraint / Failure Mode | How it manifests | Primary Risks | What an Asset Fix Looks Like |
|---|---|---:|---|
| Laptop sleeps, mobile-only periods | Lost context between sessions; stalled processing | C7, C6 | Always-on node (mini PC/VPS) to run orchestrator, checkpoints, context builds |
| Token limits & stateless LLMs | "Everything prompt," truncation, contradiction | C1, C2 | External vector memory + context-pack generator feeding scoped prompts |
| Unstructured field intake | Notes/photos/voice stuck in phone apps | C6, C7, C4 | Mobile capture channel (Shortcut/PWA/bot) + intake orchestrator + PR creation |
| Vocabulary drift in the wild | Ad-hoc naming from different devices | C3 → C2 → C4 | Ontology linter in CI + pre-commit + sensors running 24/7 |
| No durable provenance | Decisions buried in chats | C6, C5 | Decision Log DB or enforceable repo schema + reconstruction tests |
| Media/transcripts at rest | Audio/images bulky; delayed processing | C1, C6 | Background transcription (Whisper/API), EXIF extraction, links into Lite Archives |
| Link rot / ambiguous refs | "the doc from last week" | C4 → C6 | Stable ID registry + link/anchor checker in CI |

---

## 2) Asset Menu (Good → Better → Best)

> Pick one per row based on cost/ops comfort. All paths keep repo as source of truth.  

| Capability | Good (zero/low cost) | Better (managed OSS/self-host light) | Best (hosted, SLA'd) |
|---|---|---|---|
| **Always-on execution** | Spare mini PC (NUC/mini) at home on UPS | $5–10/mo VPS (Lightsail/Droplet) | Serverless (Cloud Run / Fly.io) w/ autosleep wake |
| **Orchestrator** | GitHub Actions-only (batch) | **n8n** self-host on node/VPS | n8n cloud / Make (Integromat) |
| **Vector memory** | **Chroma** server mode on node | **Weaviate** OSS on VPS | Pinecone / Weaviate Cloud |
| **Transcription** | **whisper.cpp** on node (tiny/base) | FasterGPU whisper on node | OpenAI Whisper / AssemblyAI |
| **Decision Log storage** | Markdown in repo (enforced schema) | SQLite/Postgres (lite API) | Airtable/Notion DB (if permitted) |
| **Mobile capture** | GitHub Mobile + iOS Shortcut / Android HTTP Shortcut | Minimal PWA (static host, GitHub PAT) | Telegram/Signal bot + n8n webhook |
| **Secrets** | GitHub Actions secrets | GitHub OIDC → cloud KMS (no static keys) | Cloud Secret Manager w/ Terraform |
| **Observability** | JSONL artifacts in repo | Loki/Promtail or simple S3 logs | Managed log store + dashboards |

---

## 3) Minimal Viable Hardware Setups (MVI tiers)

### **MVI-0 (Now, no spend)**
- **GitHub Actions only** (batch processing every 6h)
- **Shortcuts → repo** (single-file or inbox)
- **Local laptop** as dev only  
**What you get:** Field Agent inbox works; Lite Archives via batch; lints/PII in CI.  
**Limits:** No near-real-time, no background indexing, latency higher.

### **MVI-1 (Low-lift, low-cost)**
- **$5–10/mo VPS** (1 vCPU / 1–2 GB RAM)
- **n8n** + **Chroma (server mode)** on the VPS
- **whisper.cpp** for short clips; fall back to API when too long
- GitHub OIDC to fetch/write artifacts  
**What you get:** Near-real-time capture→PR, background embeddings, context packs.  
**Limits:** Single-node SPOF; set up simple backups/snapshots.

### **MVI-2 (Comfortable growth path)**
- Same as MVI-1 plus:  
  - **Weaviate OSS** (or Weaviate Cloud starter)  
  - **OpenAI/AssemblyAI** for faster transcription  
  - **Telegram bot** → n8n webhook  
  - **S3-compatible bucket** for media  
**What you get:** Snappier UX, cleaner APIs, durable artifacts, scalable vector store.

---

## 4) Reference Architecture (Phase 2 → 3)

```
[Phone: Shortcut/Telegram/Email]
│  HTTPS / IMAP
▼
[Orchestrator: n8n]  ──►  [Transcribe: whisper.cpp | API]
│               └─►  [Classifier: rules | LLM-lite]
│
├─► [Vector DB: Chroma/Weaviate/Pinecone]
├─► [Media store: repo assets | S3]
├─► [Decision Log: repo | SQLite/Airtable]
└─► [GitHub PR: Lite Archive + links]
    └─► [CI: Linter, PII, Link/Anchor, Sensors, Context Packs]
```

---

## 5) Secrets, Identity, & Access

- **Prefer OIDC** from GitHub Actions → cloud roles for any hosted asset (no static keys).  
- **n8n** hosted: store per-integration secrets in its vault; rotate quarterly.  
- **Least-privilege**: use a dedicated "Capture Bot" GitHub fine-scoped PAT for mobile Shortcuts when needed (contents:write to one repo).  
- **PII posture**: redact emails/phones before LLM calls; store raw-only in restricted paths; log hashes, not raw strings.

---

## 6) Mapping Assets to C1–C7 Neutralization

| Asset | C1 | C2 | C3 | C4 | C5 | C6 | C7 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Orchestrator (n8n/VPS) |  |  |  |  |  | ✓ | ✓ |
| Vector DB (Chroma/Weaviate/Pinecone) | ✓ | ✓ |  |  |  |  |  |
| Transcription (whisper/API) |  |  |  | ✓ |  | ✓ | ✓ |
| Decision Log DB / enforced schema |  |  |  | ✓ | ✓ | ✓ | ✓ |
| Mobile capture (Shortcut/PWA/bot) |  |  |  |  |  | ✓ | ✓ |
| Link/Anchor checker + ID registry |  |  |  | ✓ |  | ✓ |  |
| Context-pack generator | ✓ | ✓ | ✓ |  |  |  |  |
| Checkpoint tags + rollback tests |  |  |  |  |  | ✓ | ✓ |

---

## 7) Phased Plan (Assets + Workstreams)

### **Phase 1 (Week 1): Keystone immunity on current stack**
- **Repo-only**: Ontology.yml + blocking linter (CI + pre-commit)
- **Decision Log**: schema + PR template check
- **Charter.yml**: non-negotiables + CODEOWNERS required
- **Link/Anchor checker** + **Stable ID registry** (YAML)  
**Acceptance:** CI fails on synonym drift, missing decision ID, or unresolved links.

### **Phase 2 (Week 2): Low-cost always-on + near-real-time**
- Provision **$5–10 VPS**; install **n8n** + **Chroma (server)** + **whisper.cpp**
- Deploy **capture webhooks** (Shortcut/Telegram → n8n)
- n8n creates **PRs** with Lite Archives, runs **rules classifier**, stores media  
**Acceptance:** "Dictate on phone → PR within ≤60s" for text; ≤3–5m for short audio.

### **Phase 3 (Week 3): Antifragility + scale paths**
- Add **cascade sensors** (C3→C2, C4→C6, C2→C5) in CI
- Add **stress tests** (synonym injection, vague ref, orphan decision)
- Upgrade vector (Weaviate Cloud/Pinecone) or transcription (API) if latency/cost warrants
- Add **weekly metrics** artifact (JSONL→Markdown dashboard)  
**Acceptance:** Sensors catch deliberate injections; weekly report published automatically.

---

## 8) Security & Privacy Baselines

- **Geo privacy**: `PRIVACY_REDACT_GEO=1` by default; EXIF stripped unless opted in.
- **Media**: use Git LFS or bucket; store only redacted derivatives in public paths.
- **Backups**: weekly snapshot of VPS disk; scheduled dump of vector DB metadata and n8n config.
- **Incident playbook**: revoke bot token, rotate secrets, quarantine PR, run rollback tag.

---

## 9) Cost Envelope (typical)

- **MVI-1 VPS**: $5–10/mo  
- **n8n cloud** (optional): $20–50/mo  
- **Vector DB**:  
  - Chroma self-host: $0 + VPS  
  - Weaviate Cloud starter: ~$25–50/mo  
  - Pinecone starter: ~$0–$20+ depending on usage  
- **Transcription**:  
  - whisper.cpp: $0 + CPU time  
  - API: ~$0.006–0.015/min (rough; adjust to provider)  
- **Storage**: S3-compatible bucket: $0.02–0.025/GB/mo

---

## 10) Observability & SLOs

- **SLOs**  
  - Text capture → PR: **P95 ≤ 60s** (near-real-time path)  
  - ≤ 2MB audio → PR: **P95 ≤ 5m** (local whisper) or **≤ 60–90s** (API)  
  - CI gate latency (lint+PII+links): **≤ 3m**  
- **Telemetry**  
  - Emit **JSONL** per step (source, cid, duration, status, warnings)  
  - Weekly dashboard: drift attempts, unresolved links, PII hits, stress-test pass/fail, rehydration time trend

---

## 11) Testing & Stress (antifragility)

- **Weekly stress job** (CI):  
  - Inject synonym for a locked term → expect linter block  
  - Replace a versioned ref with vague text → expect link checker fail  
  - Remove rationale from a decision → expect reconstruction test fail  
- **Rollback drill** (monthly):  
  - Tag checkpoint, simulate bad merge, perform rollback dry-run; verify continuity.

---

## 12) Migration & Failure Modes

- **If orchestrator down**: Shortcuts still commit to `capture_inbox/`; GitHub Actions batch will process on next push/cron.  
- **If vector down**: fallback to repo-only context packs (reduced recall) with an alert.  
- **If transcription fails**: attach audio and create a "needs transcript" task.

---

## 13) Governance

- **CODEOWNERS**: Charter, Ontology, Decision Log schemas require Architect + Librarian review.  
- **Exceptions**: "override" label requires a Decision Log entry explaining the breach and a time-bounded expiry.  
- **Term proposals**: issue template; tier-2 experimental terms behind a feature flag until ratified.

---

## 14) Immediate TODOs (copy-ready)

- [ ] Provision **MVI-1 VPS**, install **n8n** + **Chroma** + **whisper.cpp**  
- [ ] Create **Telegram bot** or finalize **iOS/Android Shortcut** → n8n webhook  
- [ ] Add **GitHub OIDC** role for VPS pulls/pushes (no static PAT on server)  
- [ ] Wire **PR creation** from n8n with labels: `type:capture`, `source:mobile`, `status:triage`  
- [ ] Add **link/anchor checker** and **ID registry** to CI (Phase 1.5)  
- [ ] Schedule **weekly stress job** + **metrics report** to `docs/metrics/`

---

## 15) Acceptance Gates (Roadmap-level)

- **Gate A (MVI-1 live)**:  
  - Phone → PR ≤ 60s (text)  
  - CI gates pass by default; red flags render visible labels

- **Gate B (Vector memory live)**:  
  - Context packs built from vector search; scoped ≤ target tokens; zero duplicates

- **Gate C (Antifragility live)**:  
  - All three sensors and stress tests run weekly; report generated; at least one deliberate injection caught each cycle

---

## 16) Asset-to-Doctrine Justification

- **Assets are not features**; they exist to enforce doctrine under hardware limits.  
- Always-on node + orchestrator ensure **externalization** is continuous (C6/C7).  
- Vector memory + packs ensure **bounded context** (C1/C2).  
- Transcription + link/ID checks protect **reference and provenance** (C4/C6).  
- Decision Log storage + checkpoints create **reconstruction and recovery** (C5/C6/C7).

---

**Bottom Line**  
Adopt **MVI-1** first (VPS + n8n + Chroma + whisper.cpp): that single move gives you near-real-time capture→PR, background memory, and the scheduling backbone for sensors/stress tests. Then level up selectively (vector SaaS, API transcription) as usage and latency demand.

