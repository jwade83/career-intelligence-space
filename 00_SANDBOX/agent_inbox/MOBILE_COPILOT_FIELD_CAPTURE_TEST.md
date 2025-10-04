---
project: Career Intelligence Space
type: field_capture_test
status: active
tags: [mobile_copilot, field_capture, test_protocol, api_validation]
source: mobile_github_copilot
captured_at: '2025-10-03'
test_id: mobile_copilot_field_capture_001
test_phase: validation
---

# Mobile Copilot Field Capture Test Protocol

## Test Objective
Validate and extend mobile GitHub Copilot's field capture capabilities for the Career Intelligence Space repository.

## Critical Questions to Test

### 1. API Permission Validation
- **Question**: What specific permissions enable mobile copilot file writes?
- **Test**: Try creating files in different repo sections
- **Expected**: Identify minimum permission requirements

### 2. Branch Strategy
- **Question**: Does mobile copilot always create new branches or can it write to existing ones?
- **Test**: Attempt writes to main branch vs. feature branches
- **Expected**: Understand branch creation patterns

### 3. Frontmatter Compliance
- **Question**: Can mobile copilot generate CIS-compliant frontmatter?
- **Test**: Request specific frontmatter schemas
- **Expected**: Validate metadata generation accuracy

### 4. File Path Patterns
- **Question**: What file paths can mobile copilot access?
- **Test**: Try different directory structures
- **Expected**: Map accessible vs. restricted paths

### 5. Content Generation Quality
- **Question**: How sophisticated is mobile copilot's content generation?
- **Test**: Request complex technical content
- **Expected**: Assess content quality and structure

## Test Scenarios

### Scenario A: Basic File Creation
```
Prompt: "Create a new file in 00_SANDBOX/agent_inbox/ called test_basic.md with frontmatter and basic content"
Expected: File created with proper metadata
```

### Scenario B: Complex Technical Content
```
Prompt: "Create a technical analysis file about the repository's architecture in 00_SANDBOX/systems/"
Expected: Sophisticated technical content with proper structure
```

### Scenario C: Template Compliance
```
Prompt: "Create a file using the CIS template for meta_insight_tracking type"
Expected: Perfect frontmatter compliance with CIS ontology
```

### Scenario D: Branch Management
```
Prompt: "Create a file in the main branch instead of a new branch"
Expected: Understanding of branch write permissions
```

## Success Criteria

### Minimum Viable Field Capture
- ✅ Can create files with proper frontmatter
- ✅ Can access multiple repo directories
- ✅ Can generate structured content
- ✅ Can create appropriate branches

### Advanced Field Capture
- ✅ Perfect CIS ontology compliance
- ✅ Complex technical content generation
- ✅ Automated branch management
- ✅ Integration with existing workflows

## Next Steps After Validation

### 1. Standardize Field Capture Schema
```yaml
---
project: Career Intelligence Space
type: field_capture
status: active
tags: [mobile_copilot, field_capture, source_system]
source: mobile_github_copilot
captured_at: 'YYYY-MM-DD'
field_agent_id: mobile_copilot_001
capture_context: [conversation_topic]
branch_strategy: auto_create
review_required: true
---
```

### 2. Automation Pipeline
```
Mobile Copilot → Field Capture → Auto PR → CI Validation → Human Review → Merge
```

### 3. Multi-Agent Integration
```
Mobile Copilot (Field Agent) → Cursor (Review Agent) → GitHub Actions (CI Agent) → Human (Decision Agent)
```

## Test Execution Plan

1. **Phase 1**: Basic capability validation
2. **Phase 2**: Advanced feature testing
3. **Phase 3**: Integration testing
4. **Phase 4**: Production workflow design

## Expected Outcomes

- **Immediate**: Validate mobile copilot field capture capabilities
- **Short-term**: Design standardized field capture workflow
- **Long-term**: Implement distributed capture architecture

---

**This test protocol will validate whether mobile GitHub Copilot can serve as a reliable field capture interface for the Career Intelligence Space repository.**
