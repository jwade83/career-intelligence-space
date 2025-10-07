---
project: Career Intelligence Space
type: meta_documentation
status: active
version: v0.3
created: 2025-10-07
updated: 2025-10-07
tags: [guidelines, commits, learning, documentation]
---

# Learning Commit Guidelines

## Philosophy

This repository treats every commit as a "learning commit" that documents not just what changed, but how the system and its creator evolved through the process. This approach transforms a technical repository into a learning portfolio that demonstrates:

- **Systematic Thinking**: How problems are identified and solved
- **Process Literacy**: Understanding how ideas become repeatable systems
- **Reflexive Practice**: Building self-awareness about learning and development
- **Transparency Engineering**: Maintaining auditability in complex processes

---

## Commit Message Structure

### Basic Format
```
type(scope): brief description

Learning Context:
- What was attempted
- What failed and why (if applicable)
- What was learned
- How the system evolved

Technical Details:
- Specific changes made
- Files affected
- Dependencies or requirements
```

### Extended Format (for complex changes)
```
type(scope): brief description

Learning Context:
- What was attempted
- What failed and why (if applicable)
- What was learned
- How the system evolved

Technical Details:
- Specific changes made
- Files affected
- Dependencies or requirements

Meta-Insights:
- How this fits into larger learning goals
- What patterns this reveals
- How this informs future development
```

---

## Commit Types

### Learning-Focused Types
- `learn:` - Documenting new understanding or insights
- `experiment:` - Testing new approaches or techniques
- `iterate:` - Refining existing approaches based on learning
- `discover:` - Finding new patterns or solutions
- `reflect:` - Meta-analysis of process or outcomes

### Traditional Types (with learning context)
- `feat:` - New functionality (explain why it was needed)
- `fix:` - Bug fixes (explain what was learned from the failure)
- `docs:` - Documentation (explain what understanding was gained)
- `refactor:` - Code improvement (explain what patterns were discovered)
- `test:` - Testing (explain what was validated)

---

## Examples

### Successful Learning Commit
```
learn(meta): document prototype positioning strategy

Learning Context:
- Attempted to present repo as finished product
- Failed because it's clearly in development phase
- Learned that "unfinished" can be reframed as "learning in progress"
- System evolved to include meta-documentation layer

Technical Details:
- Created docs/meta/README_State_of_Prototype.md
- Updated main README with prototype context
- Established versioned meta-layer tracking system
- Added learning commit guidelines

Meta-Insights:
- This reveals the value of transparent development processes
- Shows how AI collaboration can be documented and taught
- Establishes foundation for research publication on human-AI collaboration
```

### Failure Learning Commit
```
fix(templates): resolve ontology mismatch in v3.3 field capture

Learning Context:
- Attempted to add complex frontmatter with new fields
- Failed due to type mismatch with CIS ontology (field_case vs mobile_copilot_field_capture)
- Learned that schema compliance is critical for automation
- System evolved to include validation checkpoints

Technical Details:
- Changed type from 'field_case' to 'mobile_copilot_field_capture'
- Removed undefined fields (template_id, template_ver, slug)
- Simplified pr: block structure
- Updated all related documentation

Meta-Insights:
- This reveals the importance of incremental validation
- Shows how AI-generated code needs human oversight for compliance
- Demonstrates the value of documenting failures for future learning
```

### Experiment Learning Commit
```
experiment(mobile): test simplified frontmatter for field capture

Learning Context:
- Attempting to reduce validation failures in mobile workflow
- Testing hypothesis that simpler frontmatter is more reliable
- Learning about the relationship between complexity and failure rates
- System evolving toward more robust template system

Technical Details:
- Created minimal frontmatter template
- Tested with mobile copilot field capture
- Documented validation results
- Updated template documentation

Meta-Insights:
- This tests the principle of "simplicity over complexity"
- Reveals patterns in AI tool reliability
- Informs future template design decisions
```

---

## Learning Context Guidelines

### What to Include
- **Attempted Goal**: What you were trying to achieve
- **Failure Analysis**: What went wrong and why (if applicable)
- **Learning Outcome**: What new understanding was gained
- **System Evolution**: How this changes the overall approach

### What to Avoid
- **Blame**: Focus on process, not personal failure
- **Vague Language**: Be specific about what was learned
- **Technical Jargon**: Explain in terms others can understand
- **Assumptions**: Document what you assumed and whether it was correct

---

## Meta-Insights Guidelines

### When to Include Meta-Insights
- **Pattern Recognition**: When you notice recurring themes
- **Strategic Implications**: When changes affect overall direction
- **Teaching Value**: When insights could help others learn
- **Research Potential**: When findings could contribute to broader knowledge

### Meta-Insight Categories
- **Process Patterns**: How workflows evolve over time
- **AI Collaboration**: What works and what doesn't with AI tools
- **System Design**: How architecture decisions impact outcomes
- **Learning Methodology**: How the learning process itself can be improved

---

## Quality Standards

### Good Learning Commits
- ✅ **Clear Learning Context**: Explains what was attempted and learned
- ✅ **Specific Technical Details**: Documents exact changes made
- ✅ **Honest Failure Analysis**: Acknowledges what didn't work and why
- ✅ **Future Implications**: Explains how this informs next steps

### Poor Learning Commits
- ❌ **No Learning Context**: Just technical changes without explanation
- ❌ **Vague Descriptions**: "Fixed stuff" or "Updated things"
- ❌ **Blame-Focused**: "This was broken" without analysis
- ❌ **No Future Connection**: Doesn't explain how this helps going forward

---

## Integration with Project Goals

### Learning Portfolio Development
Each commit contributes to building evidence of:
- **Applied Curiosity**: Systematic exploration of new domains
- **Process Literacy**: Understanding how ideas become systems
- **AI Collaboration Skills**: Effective human-AI partnership
- **Transparency Engineering**: Maintaining auditability in complex processes

### Research Value
Commits create qualitative data for studying:
- **Human-AI Collaboration Patterns**: What works and what doesn't
- **Iterative Learning Processes**: How understanding evolves over time
- **Systems Design Evolution**: How architecture decisions impact outcomes
- **Meta-Learning**: How the learning process itself can be improved

### Teaching Potential
Commits provide material for:
- **Case Studies**: Real examples of AI-assisted development
- **Process Documentation**: How to structure learning projects
- **Failure Analysis**: How to learn from mistakes
- **Meta-Reflection**: How to build self-awareness about learning

---

## Governance Framework Integration

### C3 Vocabulary Drift Prevention
All commits must use canonical terms from the governance framework:
- **Use**: "Career Intelligence Space (CIS)", "Master Portfolio (MP)", "Career Sprint"
- **Avoid**: "career repo", "portfolio", "learning sprint"
- **Reference**: `docs/GOVERNANCE/ontology.yml` for complete vocabulary

### Ontology Compliance
All documents must use valid types from the ontology:
- **Mobile Types**: `mobile_copilot_field_capture`, `mobile_copilot_technical_analysis`, `mobile_copilot_meta_insight`
- **Meta Types**: `meta_documentation`, `governance_spec`, `decision_log`
- **Reference**: `docs/ONTOLOGY.yml` for complete type list

### Decision Logging Integration
Significant learning commits should be logged in the decision framework:
- **Decision Log**: `docs/DECISION_LOG.md` for major architectural decisions
- **Provenance**: Always include source and rationale
- **Human Approval**: Required for changes affecting external systems

---

## Tools and Automation

### Commit Message Templates
Create templates for common commit types:
- `learn:` - New understanding or insights
- `experiment:` - Testing new approaches
- `fix:` - Bug fixes with learning context
- `docs:` - Documentation with understanding gained

### Validation Checklist
Before committing, ask:
- [ ] Is the learning context clear?
- [ ] Are technical details specific?
- [ ] Is failure analysis honest and constructive?
- [ ] Does this contribute to the learning portfolio?
- [ ] Will this help future contributors understand the process?
- [ ] Are all terms canonical (C3 vocabulary drift prevention)?
- [ ] Is the type field ontology-compliant?
- [ ] Are required frontmatter fields present?
- [ ] Does this align with governance framework requirements?

---

*These guidelines transform every commit into a learning opportunity, building not just a technical repository, but a comprehensive learning portfolio that demonstrates systematic thinking, process literacy, and reflexive practice.*
