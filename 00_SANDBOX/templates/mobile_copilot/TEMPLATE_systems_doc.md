---
project: Career Intelligence Space
type: template
status: active
tags: [mobile_copilot, template, systems_documentation, prompt]
updated: '2025-10-03'
---

# Mobile Copilot Systems Documentation Template

## 🎯 Purpose

This template provides a standardized prompt for systems documentation using mobile GitHub Copilot Chat Assistant. It ensures consistent frontmatter compliance and comprehensive systems documentation structure.

## 📋 Template

```
Create a new file in 00_SANDBOX/systems/ called [filename].md with the following structure:

---
project: Career Intelligence Space
type: mobile_copilot_systems_doc
status: active
tags: [mobile_copilot, systems_doc, [specific_tags]]
source: mobile_github_copilot
captured_at: '2025-10-03'
initiated_by: mobile_user
mobile_device: [device_type]
doc_type: [documentation_type]
system_scope: [scope_level]
---

# [Systems Documentation Title]

## System Overview
[Brief description of the system and its purpose]

## System Architecture
### Core Components
- **Component 1**: [Description and purpose]
- **Component 2**: [Description and purpose]
- **Component 3**: [Description and purpose]

### System Interactions
- **Interaction 1**: [How components interact]
- **Interaction 2**: [How components interact]
- **Data Flow**: [How data flows through the system]

## Technical Specifications
### System Requirements
- **Hardware**: [Hardware requirements]
- **Software**: [Software dependencies]
- **Network**: [Network requirements]
- **Storage**: [Storage requirements]

### Performance Characteristics
- **Throughput**: [System throughput capabilities]
- **Latency**: [Response time characteristics]
- **Scalability**: [Scaling capabilities and limits]
- **Reliability**: [System reliability metrics]

## System Behavior
### Normal Operations
- **Startup Sequence**: [How the system starts]
- **Operational Flow**: [Normal system operations]
- **Shutdown Sequence**: [How the system shuts down]

### Error Handling
- **Error Types**: [Types of errors the system handles]
- **Recovery Procedures**: [How the system recovers from errors]
- **Monitoring**: [How system health is monitored]

## Integration Points
### External Dependencies
- **Dependency 1**: [External system dependency]
- **Dependency 2**: [External system dependency]
- **API Interfaces**: [External API integrations]

### Internal Connections
- **Internal System 1**: [How it connects to other internal systems]
- **Internal System 2**: [How it connects to other internal systems]
- **Data Exchange**: [How data is exchanged internally]

## Configuration & Maintenance
### Configuration Management
- **Configuration Files**: [Key configuration files]
- **Environment Variables**: [Important environment settings]
- **Runtime Parameters**: [Configurable runtime parameters]

### Maintenance Procedures
- **Regular Maintenance**: [Routine maintenance tasks]
- **Update Procedures**: [How to update the system]
- **Backup & Recovery**: [Backup and recovery procedures]

## Troubleshooting Guide
### Common Issues
- **Issue 1**: [Common problem and solution]
- **Issue 2**: [Common problem and solution]
- **Issue 3**: [Common problem and solution]

### Diagnostic Procedures
- **Health Checks**: [How to check system health]
- **Log Analysis**: [How to analyze system logs]
- **Performance Monitoring**: [How to monitor system performance]

## Future Considerations
### Planned Improvements
- **Enhancement 1**: [Planned system improvements]
- **Enhancement 2**: [Planned system improvements]
- **Enhancement 3**: [Planned system improvements]

### Scalability Planning
- **Growth Projections**: [Expected system growth]
- **Resource Planning**: [Resource requirements for growth]
- **Architecture Evolution**: [How the architecture will evolve]

## Documentation References
- **Related Docs**: [Links to related documentation]
- **API Documentation**: [API reference links]
- **Configuration Guides**: [Configuration documentation links]
- **Troubleshooting Resources**: [Additional troubleshooting resources]
```

## 🔧 Usage Instructions

### **Step 1: Customize Placeholders**
- Replace `[filename]` with descriptive systems filename
- Replace `[Systems Documentation Title]` with specific system title
- Replace `[specific_tags]` with relevant system tags
- Update `captured_at` date
- Set `[device_type]` (iPhone, Android, iPad)
- Set `[documentation_type]` (architecture, operations, maintenance)
- Set `[scope_level]` (component, system, enterprise)

### **Step 2: Add Systems Content**
- Fill in System Overview with purpose and scope
- Add System Architecture with components and interactions
- Include Technical Specifications and requirements
- Describe System Behavior and operations
- List Integration Points and dependencies
- Add Configuration & Maintenance procedures
- Include Troubleshooting Guide
- Plan Future Considerations

### **Step 3: Submit**
- Copy the complete prompt
- Paste into mobile GitHub Copilot Chat
- Review generated systems documentation
- Submit for processing

## 📱 Mobile Default Values Guide

### **Systems Documentation Defaults**
```yaml
# Mobile Systems Documentation Defaults
initiated_by: mobile_user
mobile_device: [device_type]  # e.g., "iPhone", "Android", "iPad"
doc_type: architecture  # architecture, operations, maintenance, troubleshooting
system_scope: system  # component, system, enterprise
capture_method: mobile_copilot_chat
documentation_level: [level]  # e.g., "overview", "detailed", "comprehensive"
```

### **Systems-Specific Tags**
```yaml
# Common systems documentation tags
tags: [mobile_copilot, systems_doc, [domain], [type], [complexity]]
# Examples:
# [mobile_copilot, systems_doc, architecture, high_complexity, comprehensive]
# [mobile_copilot, systems_doc, operations, medium_complexity, standard]
```

## 📊 Quality Checklist

### **Frontmatter Validation**
- [ ] `project: Career Intelligence Space`
- [ ] `type: mobile_copilot_systems_doc`
- [ ] `status: active`
- [ ] `tags: [mobile_copilot, systems_doc, [specific_tags]]`
- [ ] `source: mobile_github_copilot`
- [ ] `captured_at: 'YYYY-MM-DD'`
- [ ] `initiated_by: mobile_user`
- [ ] `mobile_device: [device_type]`
- [ ] `doc_type: [documentation_type]`
- [ ] `system_scope: [scope_level]`

### **Content Validation**
- [ ] Clear systems title
- [ ] Comprehensive system overview
- [ ] Well-structured architecture description
- [ ] Complete technical specifications
- [ ] Detailed system behavior
- [ ] Integration points documented
- [ ] Maintenance procedures included
- [ ] Troubleshooting guide provided

## 🎯 Best Practices

### **Systems Documentation Guidelines**
- **Architecture Focus**: Emphasize system structure and relationships
- **Technical Detail**: Include specific technical specifications
- **Operational Focus**: Cover how the system actually works
- **Maintenance Ready**: Provide practical maintenance guidance
- **Troubleshooting**: Include common issues and solutions

### **Mobile Optimization**
- **Structured Content**: Use consistent formatting for technical content
- **Visual Hierarchy**: Use headers and bullet points effectively
- **Technical Clarity**: Ensure technical content is clear and accessible
- **Mobile Readability**: Ensure content is readable on mobile screens

---

**This template ensures consistent, high-quality systems documentation using mobile GitHub Copilot Chat Assistant.**
