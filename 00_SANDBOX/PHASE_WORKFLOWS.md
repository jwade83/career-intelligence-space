---
project: Career Intelligence Space
type: spec
status: active
tags: [workflows, phases, documentation, thinking_modes]
updated: 2025-10-02
---

# Phase-Specific Documentation Workflows

## Purpose
This document defines how to match documentation practices to project phases, preventing premature summarization during creative exploration.

## Phase Definitions

### 1. Sandboxing Phase (Divergent Thinking)
**Purpose**: Explore, discover, test hypotheses, map interrelatedness
**Thinking Mode**: Creative, exploratory, open-ended
**Documentation Focus**: Process capture, hypothesis tracking, exploration logs

### 2. Design Phase (Convergent Thinking)
**Purpose**: Synthesize, decide, specify, plan implementation
**Thinking Mode**: Analytical, decisive, structured
**Documentation Focus**: Capsules, assessments, decisions, specifications

### 3. Implementation Phase (Production)
**Purpose**: Execute, monitor, maintain, optimize
**Thinking Mode**: Operational, systematic, focused
**Documentation Focus**: Logs, memos, implementation capsules, status updates

## Phase-Appropriate Documentation Types

### Sandboxing Phase (Divergent Thinking)
**Primary Types**:
- `exploration_log` - Full exploration journey
- `hypothesis_tracking` - Testing specific ideas
- `process_capture` - Documenting methodologies
- `interrelatedness_map` - System relationship mapping
- `constraint_analysis` - Technical corner avoidance
- `timing_exploration` - Sequencing and dependencies

**Secondary Types**:
- `creative_session` - Brainstorming and ideation
- `design_experiment` - Testing design approaches
- `context_maintenance` - Preserving important context

**Avoid These Types**:
- `capsule` - Too convergent, premature summarization
- `assessment` - Too evaluative, limits exploration
- `decision` - Too final, constrains creativity
- `spec` - Too prescriptive, limits discovery

### Design Phase (Convergent Thinking)
**Primary Types**:
- `capsule` - Design decisions and rationale
- `assessment` - Evaluation and analysis
- `decision` - Final choices and reasoning
- `spec` - Implementation specifications

**Secondary Types**:
- `process_capture` - For methodology documentation
- `memo` - For status updates and communications

**Avoid These Types**:
- `exploration_log` - Too exploratory, not decisive enough
- `hypothesis_tracking` - Too open-ended, not final enough
- `creative_session` - Too divergent, not focused enough

### Implementation Phase (Production)
**Primary Types**:
- `log` - Execution logs and chronicles
- `memo` - Status updates and communications
- `implementation_capsule` - Deployment and operational notes

**Secondary Types**:
- `process_capture` - For operational procedures
- `assessment` - For performance evaluation

**Avoid These Types**:
- `exploration_log` - Too exploratory, not operational
- `hypothesis_tracking` - Too experimental, not production-ready
- `creative_session` - Too divergent, not systematic

## Workflow Guidelines

### Sandboxing Phase Workflow
1. **Start with Exploration Log** - Capture the full journey
2. **Track Hypotheses** - Test specific ideas systematically
3. **Capture Process** - Document methodologies that work
4. **Map Interrelatedness** - Understand system connections
5. **Analyze Constraints** - Avoid technical corners
6. **Explore Timing** - Understand sequencing requirements

### Design Phase Workflow
1. **Synthesize from Sandboxing** - Use exploration results
2. **Create Capsules** - Document design decisions
3. **Make Assessments** - Evaluate options and trade-offs
4. **Record Decisions** - Finalize choices with rationale
5. **Write Specifications** - Define implementation requirements

### Implementation Phase Workflow
1. **Execute from Specifications** - Follow design decisions
2. **Log Progress** - Track execution and milestones
3. **Send Memos** - Communicate status and issues
4. **Create Implementation Capsules** - Document operational learnings
5. **Monitor Performance** - Assess and optimize

## Phase Transition Guidelines

### Sandboxing → Design Transition
**Triggers**:
- Exploration phase complete
- Key hypotheses validated
- Interrelatedness mapped
- Constraints understood

**Actions**:
- Synthesize exploration results
- Create design capsules
- Make key decisions
- Write specifications

### Design → Implementation Transition
**Triggers**:
- Design decisions finalized
- Specifications complete
- Implementation plan ready
- Resources allocated

**Actions**:
- Begin execution
- Set up monitoring
- Create operational procedures
- Establish feedback loops

## Quality Gates by Phase

### Sandboxing Phase Quality Gates
- **Exploration Completeness**: All key areas explored
- **Hypothesis Testing**: Major hypotheses tested
- **Interrelatedness Mapped**: System connections understood
- **Constraints Identified**: Technical corners avoided
- **Process Documented**: Methodologies captured

### Design Phase Quality Gates
- **Decisions Made**: Key choices finalized
- **Specifications Complete**: Implementation requirements defined
- **Trade-offs Evaluated**: Options analyzed
- **Rationale Documented**: Reasoning captured
- **Implementation Ready**: Plan complete

### Implementation Phase Quality Gates
- **Execution Started**: Implementation begun
- **Progress Tracked**: Milestones monitored
- **Issues Identified**: Problems surfaced
- **Solutions Implemented**: Issues resolved
- **Performance Monitored**: Results assessed

## Common Mistakes to Avoid

### Sandboxing Phase Mistakes
- **Premature Summarization**: Using capsule/assessment types too early
- **Over-Structuring**: Applying too much structure during exploration
- **Skipping Process Capture**: Not documenting how you explored
- **Ignoring Interrelatedness**: Not mapping system connections
- **Rushing to Decisions**: Moving to design phase too quickly

### Design Phase Mistakes
- **Insufficient Synthesis**: Not using sandboxing results effectively
- **Vague Specifications**: Not being specific enough about requirements
- **Missing Trade-offs**: Not evaluating alternatives
- **Poor Rationale**: Not documenting why decisions were made
- **Implementation Gaps**: Not considering operational requirements

### Implementation Phase Mistakes
- **Process Overhead**: Too much documentation, not enough execution
- **Missing Monitoring**: Not tracking progress and issues
- **Poor Communication**: Not keeping stakeholders informed
- **No Learning Capture**: Not documenting operational insights
- **Rigid Execution**: Not adapting to changing conditions

## Template Selection Guide

| Phase | Primary Template | Use When | Focus |
|-------|------------------|----------|-------|
| Sandboxing | Exploration Log | Exploring new systems | Full journey capture |
| Sandboxing | Hypothesis Tracking | Testing specific ideas | Systematic validation |
| Sandboxing | Process Capture | Developing methods | Methodology documentation |
| Design | Capsule | Making design decisions | Decision rationale |
| Design | Assessment | Evaluating options | Analysis and evaluation |
| Design | Decision | Finalizing choices | Final choice documentation |
| Design | Spec | Defining requirements | Implementation specifications |
| Implementation | Log | Tracking execution | Progress and milestones |
| Implementation | Memo | Communicating status | Updates and communications |
| Implementation | Implementation Capsule | Documenting operations | Operational learnings |

## Integration with Existing Systems

### Frontmatter Integration
- Use phase-appropriate metadata
- Include phase-specific tags
- Add phase indicators to frontmatter

### CI/CD Integration
- Phase-specific quality gates
- Different validation rules per phase
- Phase-appropriate automation

### LLM Integration
- Phase-specific context optimization
- Different prompt strategies per phase
- Phase-appropriate output formatting

## Future Enhancements

### Planned Features
- **Phase Detection**: Automatic phase identification
- **Template Suggestions**: AI-powered template recommendations
- **Quality Gate Automation**: Automated phase transition checks
- **Cross-Phase Linking**: Better integration between phases

### Integration Opportunities
- **Project Management**: Phase tracking in project tools
- **Team Collaboration**: Phase-appropriate collaboration patterns
- **Knowledge Management**: Phase-specific knowledge organization
- **Performance Metrics**: Phase-appropriate success measures
