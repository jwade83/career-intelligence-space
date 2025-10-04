---
project: Career Intelligence Space
type: career_coaching_spec
status: active
tags: [career_coaching, mcp_tools, constitutional_compliance, career_intelligence]
updated: 2025-01-10
schema_version: v1
---

# Career Coaching Branch: MCP Tool Pack

## 🎯 Purpose

The Career Coaching Branch is a controlled set of MCP tools that enable career intelligence capabilities while maintaining constitutional compliance. It operates within constitutional constraints, providing career guidance without compromising system integrity.

## 🏛️ Constitutional Framework

### **Doctrine Compliance**
Every career coaching tool must:
- **Respect ontology constraints** - Use exact vocabulary from ontology.yml
- **Log decision provenance** - All recommendations must be auditable
- **Require human approval** - External actions need human confirmation
- **Support checkpoint recovery** - Career decisions must be recoverable

### **Risk Management**
Career coaching tools are categorized by risk level:

| Risk Level | Tool Type | Human Gate | External Write | Examples |
|------------|-----------|------------|----------------|----------|
| **Low** | Read-Only | No | No | `linkedin.search_jobs()`, `catalog.search_courses()` |
| **Medium** | Draft-Only | No | No | `outreach.compose_message()`, `resume.tailor()` |
| **High** | Human-Gated | Yes | Yes | `outreach.send_message()`, `application.submit()` |
| **Forbidden** | Never Allowed | N/A | N/A | `system.shell()`, `file.delete()` |

## 🔧 MCP Tool Specifications

### **LinkedIn Integration (Read-Only)**

#### **Job Search Tools**
```yaml
linkedin_search:
  search_jobs:
    description: "Search LinkedIn job postings with filters"
    constitutional_compliance:
      - c3_vocabulary_enforcement: true
      - c6_provenance_logging: true
      - c4_reference_stability: true
    mcp_schema:
      query: string
      filters:
        location: string
        experience_level: string
        company_size: string
        remote: boolean
      returns:
        jobs: array
        metadata:
          source: "linkedin"
          retrieved_at: timestamp
          query_hash: string
    rate_limits:
      requests_per_minute: 10
      requests_per_hour: 100
    data_retention: 30_days
```

#### **Profile Analysis Tools**
```yaml
linkedin_profile:
  get_profile:
    description: "Retrieve public LinkedIn profile information"
    constitutional_compliance:
      - c3_vocabulary_enforcement: true
      - c6_provenance_logging: true
    mcp_schema:
      profile_url: string
      returns:
        profile_data: object
        metadata:
          source: "linkedin"
          retrieved_at: timestamp
          profile_id: string
    privacy_compliance:
      public_data_only: true
      no_contact_info: true
      no_private_data: true
```

### **Outreach Integration (Draft-Only)**

#### **Message Composition Tools**
```yaml
outreach_compose:
  compose_message:
    description: "Draft outreach message using templates"
    constitutional_compliance:
      - c3_vocabulary_enforcement: true
      - c6_provenance_logging: true
      - c5_human_approval: true
    mcp_schema:
      template_id: string
      recipient_info: object
      personalization: object
      returns:
        draft_message: string
        metadata:
          template_used: string
          personalization_applied: array
          draft_created_at: timestamp
    external_write: false
    human_gate: true
    approval_required: true
```

#### **Template Management Tools**
```yaml
outreach_templates:
  get_template:
    description: "Retrieve outreach template"
    constitutional_compliance:
      - c3_vocabulary_enforcement: true
      - c6_provenance_logging: true
    mcp_schema:
      template_id: string
      returns:
        template_content: string
        metadata:
          template_version: string
          last_updated: timestamp
          usage_count: number
    external_write: false
```

### **Learning Integration (Evidence Ledger)**

#### **Course Search Tools**
```yaml
learning_catalog:
  search_courses:
    description: "Search for learning courses and certifications"
    constitutional_compliance:
      - c3_vocabulary_enforcement: true
      - c6_provenance_logging: true
      - c7_checkpoint_support: true
    mcp_schema:
      skill_tag: string
      duration_filter: string
      cost_filter: string
      returns:
        courses: array
        metadata:
          source: "catalog"
          retrieved_at: timestamp
          skill_alignment: object
    evidence_ledger: true
    checkpoint_support: true
```

#### **Activity Recording Tools**
```yaml
learning_evidence:
  record_activity:
    description: "Record learning activity in evidence ledger"
    constitutional_compliance:
      - c6_evidence_entropy_prevention: true
      - c7_checkpoint_support: true
      - c3_vocabulary_enforcement: true
    mcp_schema:
      activity_type: string
      skill_focus: string
      duration: number
      evidence_refs: array
      returns:
        activity_id: string
        ledger_entry: object
        metadata:
          recorded_at: timestamp
          checkpoint_id: string
          provenance: object
    evidence_ledger: true
    immutable_logging: true
    checkpoint_support: true
```

### **Calendar Integration (Read-Only)**

#### **Availability Tools**
```yaml
calendar_availability:
  list_slots:
    description: "List available time slots for scheduling"
    constitutional_compliance:
      - c3_vocabulary_enforcement: true
      - c6_provenance_logging: true
    mcp_schema:
      date_range: object
      duration: number
      returns:
        available_slots: array
        metadata:
          source: "calendar"
          retrieved_at: timestamp
          timezone: string
    privacy_compliance:
      no_event_details: true
      availability_only: true
      no_private_info: true
```

## 🛡️ Constitutional Enforcement

### **C3 Vocabulary Drift Prevention**
```yaml
vocabulary_enforcement:
  required_terms:
    - "Career Intelligence Space (CIS)"
    - "Master Portfolio (MP)"
    - "Career Sprint"
    - "Evidence Ledger"
    - "Opportunity Log"
  forbidden_synonyms:
    - "career repo" → "Career Intelligence Space (CIS)"
    - "portfolio" → "Master Portfolio (MP)"
    - "learning sprint" → "Career Sprint"
    - "activity log" → "Evidence Ledger"
  blocking_linter: true
```

### **C6 Evidence Entropy Prevention**
```yaml
decision_logging:
  mandatory_fields:
    - decision_id: string
    - rationale: string
    - evidence_sources: array
    - human_approval: boolean
    - timestamp: string
    - provenance: object
  immutable_storage: true
  rollback_support: true
  human_rationale_required: true
```

### **C5 Goal Creep Prevention**
```yaml
human_gates:
  external_actions:
    - outreach.send_message
    - application.submit
    - connection.request
  approval_required: true
  decision_log_entry: true
  rationale_required: true
  rollback_plan: true
```

## 📋 Implementation Phases

### **Phase 1: Read-Only Tools (Safe-by-Default)**
- LinkedIn job search
- Course catalog search
- Calendar availability
- Profile analysis
- **Risk Level**: Low
- **Human Gate**: No
- **External Write**: No

### **Phase 2: Draft-Only Tools (Templated Assist)**
- Message composition
- Resume tailoring
- Cover letter generation
- Interview preparation
- **Risk Level**: Medium
- **Human Gate**: No
- **External Write**: No

### **Phase 3: Human-Gated Tools (Narrow Writes)**
- Message sending
- Application submission
- Connection requests
- Public posting
- **Risk Level**: High
- **Human Gate**: Yes
- **External Write**: Yes

## 🎯 Success Criteria

**Career Coaching Branch is successful when:**
- All tools respect constitutional requirements
- Vocabulary drift is impossible
- Decision provenance is complete
- Human oversight is maintained
- External actions are auditable
- Career decisions are recoverable
- System integrity is preserved

## 📊 Monitoring and Compliance

### **Constitutional Compliance Metrics**
- Vocabulary drift attempts blocked
- Decision log completeness
- Human approval rates
- External action audit trails
- Checkpoint recovery success

### **Career Intelligence Metrics**
- Job search effectiveness
- Outreach response rates
- Learning progress tracking
- Skill gap identification
- Career sprint completion

---

**Career coaching tools must serve career intelligence while preserving system integrity.** 🎯
