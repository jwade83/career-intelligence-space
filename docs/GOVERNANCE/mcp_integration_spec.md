---
project: Career Intelligence Space
type: integration_spec
status: active
tags: [mcp, integration, mechanical_layer, constitutional_compliance]
updated: 2025-01-10
schema_version: v1
---

# MCP Integration Specification

## 🎯 Purpose

This document defines how Model Context Protocol (MCP) tools integrate with the Career Intelligence Space while maintaining constitutional compliance. MCP serves as the **mechanical enforcement layer** that implements the **constitutional requirements** defined in the governance framework.

## 🏛️ Constitutional Compliance Framework

### **MCP as Mechanical Layer**
MCP provides the technical implementation of constitutional requirements:

| Constitutional Requirement | MCP Implementation | Enforcement Method |
|---------------------------|-------------------|-------------------|
| **C3 Vocabulary Drift Prevention** | Schema validation | MCP enforces exact field names and types |
| **C6 Evidence Entropy Prevention** | Audit logging | MCP logs all tool calls with provenance |
| **C5 Goal Creep Prevention** | ACL enforcement | MCP blocks unauthorized actions |
| **C1 Context Saturation Prevention** | Scoped tool access | MCP limits available tools per context |
| **C4 Reference Ambiguity Prevention** | Stable tool IDs | MCP uses canonical tool names |

### **Constitutional Supremacy**
- **No MCP tool can override constitutional requirements**
- **All MCP tools must prove collapse prevention value**
- **Human approval required for external actions**
- **Provenance tracking mandatory for all decisions**

## 🔧 MCP Tool Architecture

### **Tool Categories by Risk Level**

#### **Read-Only Tools (Low Risk)**
```yaml
linkedin:
  search_jobs:
    description: "Search LinkedIn job postings"
    risk_level: low
    human_gate: false
    provenance_required: true
    schema:
      query: string
      filters: object
      returns: array
```

#### **Draft-Only Tools (Medium Risk)**
```yaml
outreach:
  compose_message:
    description: "Draft outreach message"
    risk_level: medium
    human_gate: false
    provenance_required: true
    external_write: false
    schema:
      template_id: string
      variables: object
      returns: string
```

#### **Human-Gated Tools (High Risk)**
```yaml
outreach:
  send_message:
    description: "Send outreach message"
    risk_level: high
    human_gate: true
    provenance_required: true
    external_write: true
    approval_required: true
    schema:
      recipient: string
      message: string
      returns: boolean
```

#### **Forbidden Tools (Never Allowed)**
```yaml
system:
  shell: FORBIDDEN
  delete_file: FORBIDDEN
  execute_command: FORBIDDEN
  access_secrets: FORBIDDEN
```

## 🛡️ Constitutional Enforcement

### **C3 Vocabulary Drift Prevention**
```yaml
# MCP enforces exact vocabulary from ontology.yml
tool_schemas:
  must_use_canonical_terms: true
  forbidden_synonyms: true
  vocabulary_validation: true
  blocking_on_drift: true
```

### **C6 Evidence Entropy Prevention**
```yaml
# MCP logs all decisions with provenance
decision_logging:
  mandatory: true
  provenance_required: true
  immutable: true
  rollback_support: true
  human_rationale: true
```

### **C5 Goal Creep Prevention**
```yaml
# MCP enforces human approval for external actions
human_gates:
  external_writes: true
  public_actions: true
  high_risk_operations: true
  approval_rationale: true
  decision_log_entry: true
```

## 📋 Career Coaching Branch Implementation

### **LinkedIn Integration (Read-Only)**
```yaml
linkedin_tools:
  search_jobs:
    constitutional_compliance:
      - c3_vocabulary_enforcement: true
      - c6_provenance_logging: true
      - c4_reference_stability: true
    mcp_implementation:
      schema_validation: strict
      audit_logging: mandatory
      rate_limiting: conservative
      data_retention: 30_days
```

### **Outreach Integration (Draft-Only)**
```yaml
outreach_tools:
  compose_message:
    constitutional_compliance:
      - c3_vocabulary_enforcement: true
      - c6_provenance_logging: true
      - c5_human_approval: true
    mcp_implementation:
      external_write: false
      draft_only: true
      human_gate: true
      approval_required: true
```

### **Learning Integration (Evidence Ledger)**
```yaml
learning_tools:
  record_activity:
    constitutional_compliance:
      - c6_evidence_entropy_prevention: true
      - c7_checkpoint_support: true
      - c3_vocabulary_enforcement: true
    mcp_implementation:
      evidence_ledger: true
      checkpoint_support: true
      immutable_logging: true
```

## 🚨 Enforcement Rules

### **Constitutional Compliance Checklist**
Every MCP tool must pass:

- [ ] **C3 Check**: Uses exact vocabulary from ontology.yml
- [ ] **C6 Check**: Logs decisions with full provenance
- [ ] **C7 Check**: Supports checkpoint recovery
- [ ] **C5 Check**: Requires human approval for external actions
- [ ] **Constitutional Check**: Strengthens rather than weakens doctrine

### **MCP Server Requirements**
```yaml
mcp_server:
  constitutional_compliance:
    ontology_enforcement: true
    decision_logging: true
    human_gates: true
    checkpoint_support: true
  technical_requirements:
    schema_validation: strict
    audit_logging: mandatory
    rate_limiting: conservative
    error_handling: graceful
```

## 📊 Integration Phases

### **Phase 1: Constitutional Foundation**
- Deploy ontology.yml + blocking linter
- Implement decision log schema
- Add checkpoint support
- Create human gate policies

### **Phase 2: MCP Tool Integration**
- Add read-only tools (LinkedIn, calendar, courses)
- Implement draft-only tools (outreach, resume)
- Add evidence ledger tools
- Deploy MCP server with constitutional compliance

### **Phase 3: Human-Gated Tools**
- Add high-risk tools with human approval
- Implement approval workflows
- Add rollback capabilities
- Deploy full career coaching branch

## 🎯 Success Criteria

**MCP Integration is successful when:**
- All tools respect constitutional requirements
- Vocabulary drift is impossible
- Decision provenance is complete
- Human oversight is maintained
- External actions are auditable
- System recovery is guaranteed

---

**MCP is the mechanical layer that implements constitutional requirements.** 🔧
