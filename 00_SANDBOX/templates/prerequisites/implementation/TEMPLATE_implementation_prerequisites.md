---
project: Career Intelligence Space
type: template
status: active
tags: [sandbox, template, prerequisites, implementation]
updated: 2025-10-02
---

# Implementation Prerequisites Template

## Purpose
Guide thinking about deployment and operational work without constraining exploration.

## Prerequisite Questions (Answer as you explore)

### 1. Implementation Sequencing
- **What gets built first?** (Starting point and rationale)
- **What are the dependencies?** (What must be ready before each step)
- **What are the rollback points?** (Where can we safely stop or reverse)
- **What are the critical path items?** (What blocks everything else)

### 2. Data Flow Architecture
- **How does data move between systems?** (Data flow paths)
- **What are the data formats?** (Input/output formats and transformations)
- **What happens when data flow breaks?** (Error handling and recovery)
- **How do we validate data integrity?** (Data quality checks)

### 3. Failure Mode Analysis
- **What happens when [System A] is down?** (Single system failures)
- **What happens when [System B] rate limits hit?** (Resource constraint failures)
- **What happens when [System C] API fails?** (External dependency failures)
- **What are the recovery procedures?** (How to restore function)

### 4. Cost and Resource Modeling
- **What are the setup costs?** (Initial investment required)
- **What are the ongoing costs?** (Monthly/operational expenses)
- **What are the scaling costs?** (Cost growth with usage)
- **What are the time investments?** (Setup, maintenance, learning curve)

### 5. User Experience Design
- **How do users interact with this?** (User workflows and interfaces)
- **What's the learning curve?** (Training and adoption requirements)
- **How does this change daily work?** (Workflow impact)
- **What are the pain points?** (Potential user friction)

### 6. Security and Privacy
- **What sensitive data flows through this?** (Data classification)
- **How is PII handled?** (Privacy protection measures)
- **What are the compliance requirements?** (Regulatory considerations)
- **What are the security risks?** (Threats and vulnerabilities)

### 7. Performance and Scalability
- **How many operations per minute?** (Throughput requirements)
- **What's the latency for key operations?** (Response time requirements)
- **How does performance degrade under load?** (Scaling characteristics)
- **What are the bottlenecks?** (Performance limitations)

### 8. Testing Strategy
- **How do we test the entire system?** (Integration testing approach)
- **What are the test scenarios?** (Specific test cases)
- **How do we simulate failures?** (Failure testing approach)
- **What are the success criteria?** (How we know it works)

### 9. Monitoring and Observability
- **How do we know if it's working?** (Health indicators)
- **What metrics indicate system health?** (Key performance indicators)
- **How do we debug when things go wrong?** (Troubleshooting approach)
- **What alerts do we need?** (Early warning systems)

### 10. Change Management
- **How do we evolve this over time?** (Evolution strategy)
- **How do we handle breaking changes?** (API change management)
- **How do we migrate data between systems?** (Data migration strategy)
- **How do we maintain backward compatibility?** (Compatibility requirements)

## Validation Checklist
- [ ] Implementation sequence defined
- [ ] Data flow architecture mapped
- [ ] Failure modes analyzed
- [ ] Costs and resources modeled
- [ ] User experience considered
- [ ] Security and privacy addressed
- [ ] Performance characteristics understood
- [ ] Testing strategy defined
- [ ] Monitoring approach planned
- [ ] Change management strategy outlined

## Notes
- **Start with what you know** - Don't force answers to everything
- **Document assumptions** - Note what you're assuming
- **Identify unknowns** - Mark what needs research
- **Iterate and refine** - Come back as understanding grows
- **Focus on critical path** - Prioritize the most important items
