# Repository Style Guide and Conventions

## Commit Message Format

All commit messages MUST adhere to the Conventional Commit Specification with Career Intelligence Space enhancements.

### **Required Format**
```
type(scope): description

[Optional body with more details]

Source-Provenance: [source_details]
Mobile-Context: [mobile_specific_info] (if applicable)
```

### **Type Prefixes**
- `feat`: New features or capabilities
- `fix`: Bug fixes and corrections
- `docs`: Documentation updates
- `refactor`: Code restructuring without behavior changes
- `perf`: Performance improvements
- `test`: Test additions or modifications
- `chore`: Maintenance tasks, dependencies
- `mobile`: Mobile-specific improvements
- `template`: Template or prompt updates
- `workflow`: Process or workflow changes

### **Scope Guidelines**
- Use lowercase with hyphens: `mobile-ui`, `templates`, `docs`
- Be specific: `mobile-copilot`, `field-capture`, `compliance`
- Keep under 20 characters

### **Description Rules**
- Start with lowercase verb
- Keep under 50 characters
- Be descriptive but concise
- Use present tense: "add", "update", "fix"

### **Source-Provenance Requirements**
- **Local IDE**: `Source-Provenance: VS Code Copilot`
- **Web Editor**: `Source-Provenance: GitHub Web Editor`
- **Mobile**: `Source-Provenance: Mobile GitHub Copilot`
- **Conversation**: `Source-Provenance: Conversation with Copilot Chat`
- **Manual**: `Source-Provenance: Manual Entry`

### **Mobile-Specific Context**
When capturing mobile field data, include:
```
Mobile-Context: device=[device_type], method=[capture_method], template=[template_used]
```

## Examples

### **Mobile Field Capture**
```
feat(mobile-copilot): add compliance checklist to mobile guide

- Add comprehensive mobile compliance checklist
- Include frontmatter validation steps
- Add mobile-specific requirements
- Create quality assurance guidelines

Source-Provenance: Mobile GitHub Copilot
Mobile-Context: device=iPhone, method=mobile_copilot_chat, template=basic_field_capture
```

### **Template Updates**
```
template(mobile): enhance field capture template with default values

- Add mobile default values guidance
- Include device-specific configurations
- Add mobile-specific metadata fields
- Enhance mobile optimization features

Source-Provenance: VS Code Copilot
```

### **Documentation Updates**
```
docs(mobile-ui): create comprehensive mobile workflow guide

- Document end-to-end mobile capture process
- Add troubleshooting for common issues
- Include success metrics and quality assurance
- Add best practices for mobile users

Source-Provenance: Conversation with Copilot Chat
```

## Mobile-Specific Commit Guidelines

### **Mobile Field Capture Commits**
- Always include `Mobile-Context` field
- Use `mobile` or `mobile-copilot` scope
- Include device type and capture method
- Reference template used if applicable

### **Mobile Template Commits**
- Use `template` type with `mobile` scope
- Include template name in description
- Add mobile optimization details
- Reference compliance requirements

### **Mobile Workflow Commits**
- Use `workflow` type with `mobile-ui` scope
- Include process improvements
- Add user experience enhancements
- Reference mobile-specific considerations

## Quality Standards

### **Commit Message Quality**
- **Clarity**: Clear, descriptive messages
- **Consistency**: Follow format exactly
- **Completeness**: Include all required fields
- **Context**: Provide sufficient detail

### **Mobile Optimization**
- **Device Awareness**: Include device context
- **Method Tracking**: Specify capture method
- **Template Reference**: Link to templates used
- **Compliance**: Ensure mobile-specific requirements

### **Provenance Tracking**
- **Source Identification**: Always specify source
- **Method Documentation**: Include capture method
- **Context Preservation**: Maintain mobile context
- **Audit Trail**: Enable complete traceability

## Repository-Specific Conventions

### **Career Intelligence Space Context**
- **Project**: Always reference "Career Intelligence Space"
- **Type**: Use mobile_copilot_field_capture for mobile captures
- **Tags**: Include mobile_copilot tag
- **Source**: Specify mobile_github_copilot for mobile captures

### **Mobile Field Capture Standards**
- **Frontmatter**: Follow CIS ontology requirements
- **Compliance**: Use mobile compliance checklist
- **Quality**: Ensure mobile-optimized content
- **Integration**: Follow mobile workflow process

### **Template Usage**
- **Consistency**: Use exact template format
- **Customization**: Follow placeholder guidelines
- **Validation**: Use compliance checklists
- **Quality**: Ensure mobile optimization

---

**These instructions ensure consistent, high-quality commit messages across all environments while maintaining mobile field capture standards and provenance tracking.**
