---
project: Career Intelligence Space
type: template
status: active
tags: [chatgpt, communication, template, file_access]
updated: 2025-10-02
---

# ChatGPT Communication Template

## Purpose
This template provides a standardized way to communicate with ChatGPT when you need to share files and context for assessment or analysis.

## Template Structure

### **Step 1: File Preparation**
```
I need to share [X] files with ChatGPT for [purpose]. 
Opening files in Cursor for ChatGPT access...
```

### **Step 2: File Opening Commands**
```bash
cursor --reuse-window --goto [file1]:1
cursor --reuse-window --goto [file2]:1
cursor --reuse-window --goto [file3]:1
# ... additional files as needed
```

### **Step 3: ChatGPT Prompt**
```
I've opened [X] key files in Cursor for you to assess [specific purpose]. 
Please review these files and provide a [type of assessment] focusing on:

1. [Specific focus area 1]
2. [Specific focus area 2]
3. [Specific focus area 3]
4. [Specific focus area 4]

The files are:
- [file1] - [description]
- [file2] - [description]
- [file3] - [description]
- [file4] - [description]

Please provide a [detailed/critical/strategic] assessment of [the specific topic].
```

## Usage Examples

### **Example 1: Sandboxing Assessment**
```
I need to share 5 files with ChatGPT for sandboxing system assessment. 
Opening files in Cursor for ChatGPT access...

Files opened:
- 00_SANDBOX/CHATGPT_SANDBOXING_OVERVIEW.md
- 00_SANDBOX/KEY_FILES_SUMMARY.md
- 00_SANDBOX/systems/2025-10-02_harness-stageb-monday-make_interrelatedness.md
- docs/HARNESS/README.md
- 00_SANDBOX/templates/prerequisites/systems/TEMPLATE_systems_prerequisites.md

ChatGPT Prompt:
I've opened 5 key files in Cursor for you to assess our sandboxing system design. 
Please review these files and provide a critical assessment focusing on:

1. System interrelatedness - How well does it capture complex dependencies?
2. Future-proofing - Does it avoid technical "glass ceilings"?
3. LLM optimization - How well does it support information formation through praxis?
4. Critical gaps - What important details might be overlooked?

Please provide a detailed critical assessment of the sandboxing system design.
```

### **Example 2: Technical Review**
```
I need to share 3 files with ChatGPT for technical architecture review.
Opening files in Cursor for ChatGPT access...

Files opened:
- docs/HARNESS/README.md
- .github/workflows/capture-processor.yml
- scripts/capture-processor.py

ChatGPT Prompt:
I've opened 3 key files in Cursor for you to review our technical architecture. 
Please review these files and provide a technical assessment focusing on:

1. Architecture coherence - How well do the components work together?
2. Implementation quality - What are the strengths and weaknesses?
3. Maintenance concerns - What could cause issues over time?
4. Improvement opportunities - What would you recommend?

Please provide a technical assessment of the architecture.
```

## Key Principles

### **File Selection**
- **Choose relevant files** - Only include what's necessary for the assessment
- **Provide context** - Explain why each file is important
- **Keep it focused** - Don't overwhelm with too many files

### **Prompt Design**
- **Be specific** - Ask for exactly what you need
- **Provide context** - Explain the purpose and background
- **Set expectations** - Specify the type of assessment needed
- **Guide focus** - Point to specific areas of concern

### **File Access**
- **Use Cursor CLI** - `cursor --reuse-window --goto filename:line`
- **Verify visibility** - Check that files are actually visible in Cursor
- **Test access** - Confirm ChatGPT can see the files before proceeding

## Common Use Cases

### **Strategic Planning**
- **Purpose:** High-level system design and architecture
- **Files:** Overview documents, system specifications, strategic vision
- **Focus:** Interrelatedness, future-proofing, strategic alignment

### **Technical Review**
- **Purpose:** Implementation quality and architecture
- **Files:** Code files, configuration, technical specifications
- **Focus:** Code quality, architecture coherence, maintenance concerns

### **Process Assessment**
- **Purpose:** Workflow and process evaluation
- **Files:** Workflow definitions, process documentation, templates
- **Focus:** Efficiency, clarity, effectiveness, improvement opportunities

### **Content Analysis**
- **Purpose:** Content quality and consistency
- **Files:** Documentation, templates, examples
- **Focus:** Clarity, completeness, consistency, usability

## Troubleshooting

### **Files Not Visible**
- **Check Cursor tabs** - Verify files are actually open
- **Use different flags** - Try `--new-window` or `--wait`
- **Test manually** - Open files manually to confirm access

### **ChatGPT Can't See Files**
- **Verify file paths** - Ensure files exist and are accessible
- **Check file permissions** - Make sure files are readable
- **Test with simple files** - Start with basic text files

### **Assessment Quality Issues**
- **Provide more context** - Explain the background and purpose
- **Be more specific** - Ask for exactly what you need
- **Guide the focus** - Point to specific areas of concern
- **Set expectations** - Specify the type of assessment needed

---

**This template ensures consistent, effective communication with ChatGPT while maintaining the flexibility needed for different types of assessments and analyses.**

