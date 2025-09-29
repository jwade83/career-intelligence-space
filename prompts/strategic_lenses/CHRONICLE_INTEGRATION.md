---
project: Career Intelligence Space
type: integration_guide
status: active
tags: [cis, strategic_lenses, chronicle, integration, templates]
updated: 2025-09-29
---

# Strategic Lenses Chronicle Integration

## Overview
This document defines how to integrate strategic consultant lens outputs with the CIS chronicle system, ensuring consistent documentation and workflow integration.

## Chronicle Entry Templates

### **Weekly Review with Strategic Lenses**
```markdown
---
project: Career Intelligence Space
type: weekly_review
status: active
tags: [cis, chronicle, weekly_review, strategic_lenses]
updated: YYYY-MM-DD
lenses_used: [strategic_analyst, project_manager, productivity_coach]
---

# Weekly Review - Week of YYYY-MM-DD

## Strategic Analyst Insights
[Insert Strategic Analyst lens output here]

## Project Manager Assessment
[Insert Project Manager lens output here]

## Productivity Coach Analysis
[Insert Productivity Coach lens output here]

## Integrated Insights
[Combine key insights from all lenses into actionable summary]

## Next Week Priorities
[Extract and prioritize action items from lens analyses]

---
*Generated using Strategic Consultant Lenses v1.0.0*
```

### **Crisis Resolution with Systems Engineer**
```markdown
---
project: Career Intelligence Space
type: crisis_resolution
status: active
tags: [cis, chronicle, crisis, systems_engineer, project_manager]
updated: YYYY-MM-DD
lenses_used: [systems_engineer, project_manager, strategic_analyst]
---

# Crisis Resolution - [Issue Description]

## Systems Engineer Analysis
[Insert Systems Engineer lens output here]

## Project Manager Impact Assessment
[Insert Project Manager lens output here]

## Strategic Analyst Implications
[Insert Strategic Analyst lens output here]

## Resolution Plan
[Combined technical and strategic resolution approach]

## Lessons Learned
[Key insights for future prevention]

---
*Generated using Strategic Consultant Lenses v1.0.0*
```

### **Strategic Planning with Venture Designer**
```markdown
---
project: Career Intelligence Space
type: strategic_planning
status: active
tags: [cis, chronicle, strategic_planning, venture_designer, strategic_analyst]
updated: YYYY-MM-DD
lenses_used: [venture_designer, strategic_analyst, project_manager]
---

# Strategic Planning Session - [Planning Period]

## Venture Designer Market Analysis
[Insert Venture Designer lens output here]

## Strategic Analyst Context
[Insert Strategic Analyst lens output here]

## Project Manager Execution Plan
[Insert Project Manager lens output here]

## Strategic Roadmap
[Integrated strategic direction with execution plan]

## Success Metrics
[Measurable outcomes and milestones]

---
*Generated using Strategic Consultant Lenses v1.0.0*
```

## Integration Workflow

### **Step 1: Lens Execution**
1. Select appropriate lens(es) based on situation
2. Execute lens analysis using committed templates
3. Capture output in structured format
4. Review for completeness and quality

### **Step 2: Chronicle Integration**
1. Create new chronicle entry using appropriate template
2. Insert lens outputs into designated sections
3. Add integrated insights and action items
4. Apply proper frontmatter and tagging

### **Step 3: Workflow Integration**
1. Save chronicle entry to `08_CHRONICLE/` directory
2. Update chronicle index if needed
3. Extract action items for task queue
4. Schedule follow-up lens usage if required

### **Step 4: Quality Assurance**
1. Verify all lens outputs are properly integrated
2. Check that insights are actionable and specific
3. Ensure chronicle entry follows CIS standards
4. Confirm integration with existing workflows

## Chronicle Enhancement

### **Lens Metadata Integration**
Add to chronicle frontmatter:
```yaml
lenses_used: [lens1, lens2, lens3]
lens_version: "1.0.0"
analysis_date: "YYYY-MM-DD"
```

### **Cross-Reference System**
- Link lens analyses to specific chronicle entries
- Create index of lens usage across chronicles
- Track lens effectiveness over time
- Maintain lens output archive

### **Automated Integration Points**
- GitHub Actions workflow for lens-based chronicle generation
- Automated frontmatter updates for lens metadata
- Integration with existing chronicle audit system
- Cross-referencing with task queue system

## Quality Standards

### **Lens Output Integration**
- [ ] All lens outputs properly formatted and inserted
- [ ] Integrated insights provide new value beyond individual analyses
- [ ] Action items clearly extracted and prioritized
- [ ] Follow-up actions scheduled and documented

### **Chronicle Standards Compliance**
- [ ] Proper frontmatter with lens metadata
- [ ] CIS tagging conventions followed
- [ ] Chronicle link references included
- [ ] Promotion notice added if applicable

### **Workflow Integration**
- [ ] Chronicle entry saved to correct directory
- [ ] Index updated if needed
- [ ] Task queue updated with action items
- [ ] Follow-up lens usage scheduled

## Success Metrics

### **Integration Effectiveness**
- **Completeness:** All lens outputs properly integrated
- **Quality:** Integrated insights provide actionable value
- **Consistency:** Standardized integration across all chronicle entries
- **Workflow:** Seamless connection to existing CIS processes

### **Chronicle Enhancement**
- **Value:** Chronicle entries provide deeper insights
- **Actionability:** Clear next steps and priorities
- **Traceability:** Lens usage tracked and measured
- **Evolution:** Continuous improvement based on feedback

---

*Updated: 2025-09-29*
