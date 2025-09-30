#!/usr/bin/env python3
"""
Conversation Archive Builder
Automates the creation of structured conversation archives from raw transcripts
"""

import argparse
import os
import re
import yaml
from datetime import datetime
from pathlib import Path

def sanitize_topic(topic):
    """Sanitize topic for safe file paths"""
    # Remove unsafe characters and normalize
    sanitized = re.sub(r'[^\w\s-]', '', topic)
    sanitized = re.sub(r'[-\s]+', '_', sanitized)
    return sanitized.lower()

def validate_inputs(date, topic, participants):
    """Validate input parameters"""
    # Validate date format
    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError(f"Invalid date format: {date}. Use YYYY-MM-DD")
    
    # Validate topic
    if not topic or len(topic.strip()) == 0:
        raise ValueError("Topic cannot be empty")
    
    # Validate participants
    if not participants or len(participants.strip()) == 0:
        raise ValueError("Participants cannot be empty")
    
    return True

def generate_conversation_id(date, topic):
    """Generate a stable conversation ID"""
    safe_topic = sanitize_topic(topic)
    return f"conv_{date}_{safe_topic}"

def create_archive_structure(date, topic, participants, output_dir, conversation_id=None):
    """Create the complete archive structure for a conversation"""
    
    # Validate inputs
    validate_inputs(date, topic, participants)
    
    # Generate conversation ID if not provided
    if not conversation_id:
        conversation_id = generate_conversation_id(date, topic)
    
    # Sanitize topic for paths
    safe_topic = sanitize_topic(topic)
    
    # Create directory structure
    archive_dir = Path(output_dir) / safe_topic
    segments_dir = archive_dir / 'segments'
    
    # Check if archive already exists
    if archive_dir.exists():
        print(f"Warning: Archive directory already exists: {archive_dir}")
        response = input("Continue anyway? (y/N): ")
        if response.lower() != 'y':
            print("Aborted.")
            return
    
    archive_dir.mkdir(parents=True, exist_ok=True)
    segments_dir.mkdir(parents=True, exist_ok=True)
    
    # Create main archive files
    create_readme(archive_dir, date, topic, participants, conversation_id)
    create_full_archive(archive_dir, date, topic, participants, conversation_id)
    create_insights_extraction(archive_dir, date, topic, conversation_id)
    create_implementation_analysis(archive_dir, date, topic, conversation_id)
    
    # Create segment files
    create_segments(segments_dir, date, topic, conversation_id)
    
    print(f"Archive structure created at: {archive_dir}")
    print(f"Conversation ID: {conversation_id}")

def create_readme(archive_dir, date, topic, participants, conversation_id):
    """Create the archive README.md"""
    
    # Parse participants into array
    participants_list = [p.strip() for p in participants.split(',')]
    
    readme_content = f"""---
project: Career Intelligence Space
type: archive_navigation
status: active
tags: [conversation_archive, {topic.lower().replace(' ', '_')}, navigation, reference]
updated: {date}
conversation_id: "{conversation_id}"
archive_date: {date}
timezone: "America/Los_Angeles"
captured_at_utc: "{date}T15:30:00Z"
participants: {participants_list}
topic: "{topic}"
related:
  - "docs/decision-log.md"
  - "08_CHRONICLE/vision/"
---

# {topic} Conversation Archive

## Purpose
This archive preserves the complete context and analysis from the {date} {topic} conversation. The archive serves as a comprehensive reference for future implementation, capturing not just the decisions made but the full strategic thinking and rationale behind them.

## Navigation

### Core Archive Files
- **[Complete Conversation Archive]({date}_full_conversation_archive.md)** - Full transcript with all context
- **[Key Insights Extraction]({date}_key_insights_extraction.md)** - Strategic insights and analysis
- **[Implementation Analysis]({date}_implementation_analysis.md)** - Timing and readiness assessment

### Conversation Segments
- **[01: Introduction](segments/01_introduction.md)** - Initial concept and context
- **[02: Deep Dive](segments/02_deep_dive.md)** - Detailed analysis and exploration
- **[03: Implementation Strategy](segments/03_implementation_strategy.md)** - Implementation approach
- **[04: Timing Assessment](segments/04_timing_assessment.md)** - When to implement
- **[05: Documentation Strategy](segments/05_documentation_strategy.md)** - How to organize
- **[06: Future Framework](segments/06_future_framework.md)** - Implementation readiness

## Key Decisions Made
[To be filled in during conversation analysis]

## Implementation Status
- **Current Status:** Documented for future reference
- **Timing:** To be determined based on analysis
- **Dependencies:** [To be identified]
- **Readiness Criteria:** [To be defined]

## Archive Maintenance
- **Last Updated:** {date}
- **Next Review:** [To be scheduled]
- **Maintenance:** Automated via GitHub Actions
- **Search:** Use repository search with tags: `{topic.lower().replace(' ', '_')}`, `conversation_archive`
"""
    
    readme_path = archive_dir / 'README.md'
    readme_path.write_text(readme_content)

def create_full_archive(archive_dir, date, topic, participants, conversation_id):
    """Create the full conversation archive template"""
    
    # Parse participants into array
    participants_list = [p.strip() for p in participants.split(',')]
    
    archive_content = f"""---
project: Career Intelligence Space
type: conversation_archive
status: active
tags: [conversation_archive, {topic.lower().replace(' ', '_')}, full_transcript]
updated: {date}
conversation_id: "{conversation_id}"
conversation_date: {date}
timezone: "America/Los_Angeles"
captured_at_utc: "{date}T15:30:00Z"
participants: {participants_list}
topic: "{topic}"
related:
  - "docs/decision-log.md"
  - "08_CHRONICLE/vision/"
---

# {topic}: Complete Conversation Archive
**Date:** {date}  
**Topic:** {topic}  
**Participants:** {participants_list}  
**Context:** [To be filled in]

---

## Conversation Transcript

### [Participant 1]: [Topic Introduction]
[Full text of initial message]

### [Participant 2]: [Response]
[Full text of response]

[Continue for all conversation segments...]

---

## Key Decisions Made
1. **[Decision 1]** - [Rationale and context]
2. **[Decision 2]** - [Rationale and context]
3. **[Decision 3]** - [Rationale and context]

## Next Steps
1. [Action item 1]
2. [Action item 2]
3. [Action item 3]

## Related Documentation
- [Link to related docs]
- [Link to implementation plans]
- [Link to follow-up conversations]

---

**Traceability**
- conversation_id: {conversation_id}
- decision_log: docs/decision-log.md (search for the conversation_id)
- chronicle_path: 08_CHRONICLE/conversations/{safe_topic}/
- schema_version: v1
"""
    
    archive_path = archive_dir / f'{date}_full_conversation_archive.md'
    archive_path.write_text(archive_content)

def create_insights_extraction(archive_dir, date, topic, conversation_id):
    """Create the key insights extraction template"""
    
    insights_content = f"""---
project: Career Intelligence Space
type: insights_extraction
status: active
tags: [insights, {topic.lower().replace(' ', '_')}, key_decisions, strategic_analysis]
updated: {date}
conversation_id: "{conversation_id}"
extraction_date: {date}
timezone: "America/Los_Angeles"
captured_at_utc: "{date}T15:30:00Z"
related:
  - "{date}_full_conversation_archive.md"
  - "{date}_implementation_analysis.md"
---

# Key Insights from {topic} Conversation

## Strategic Insights

### 1. [Key Insight 1]
- [Supporting point 1]
- [Supporting point 2]
- [Supporting point 3]

### 2. [Key Insight 2]
- [Supporting point 1]
- [Supporting point 2]
- [Supporting point 3]

### 3. [Key Insight 3]
- [Supporting point 1]
- [Supporting point 2]
- [Supporting point 3]

## Technical Insights

### 1. [Technical Insight 1]
- [Supporting point 1]
- [Supporting point 2]
- [Supporting point 3]

### 2. [Technical Insight 2]
- [Supporting point 1]
- [Supporting point 2]
- [Supporting point 3]

## Decision Framework

### [Decision Category 1]
1. [Decision criteria 1]
2. [Decision criteria 2]
3. [Decision criteria 3]

### [Decision Category 2]
1. [Decision criteria 1]
2. [Decision criteria 2]
3. [Decision criteria 3]

## Key Takeaways
- [Takeaway 1]
- [Takeaway 2]
- [Takeaway 3]
- [Takeaway 4]
"""
    
    insights_path = archive_dir / f'{date}_key_insights_extraction.md'
    insights_path.write_text(insights_content)

def create_implementation_analysis(archive_dir, date, topic, conversation_id):
    """Create the implementation analysis template"""
    
    analysis_content = f"""---
project: Career Intelligence Space
type: implementation_analysis
status: active
tags: [implementation, {topic.lower().replace(' ', '_')}, timing, strategy]
updated: {date}
conversation_id: "{conversation_id}"
analysis_date: {date}
timezone: "America/Los_Angeles"
captured_at_utc: "{date}T15:30:00Z"
related:
  - "{date}_full_conversation_archive.md"
  - "{date}_key_insights_extraction.md"
---

# {topic} Implementation Analysis

## Current System Assessment

### Strengths
- [Strength 1]
- [Strength 2]
- [Strength 3]

### Weaknesses
- [Weakness 1]
- [Weakness 2]
- [Weakness 3]

## Implementation Readiness Assessment

### Current Readiness: [READY/NOT READY]
**Reasoning:**
1. [Reason 1]
2. [Reason 2]
3. [Reason 3]

### Readiness Criteria
- [ ] [Criteria 1]
- [ ] [Criteria 2]
- [ ] [Criteria 3]
- [ ] [Criteria 4]

## Recommended Approach

### Phase 1: [Phase Name]
1. [Action 1]
2. [Action 2]
3. [Action 3]

### Phase 2: [Phase Name]
1. [Action 1]
2. [Action 2]
3. [Action 3]

### Phase 3: [Phase Name]
1. [Action 1]
2. [Action 2]
3. [Action 3]

## Success Metrics

### [Metric Category 1]
- [ ] [Metric 1]
- [ ] [Metric 2]
- [ ] [Metric 3]

### [Metric Category 2]
- [ ] [Metric 1]
- [ ] [Metric 2]
- [ ] [Metric 3]

## Conclusion
[Summary of implementation recommendation and rationale]
"""
    
    analysis_path = archive_dir / f'{date}_implementation_analysis.md'
    analysis_path.write_text(analysis_content)

def create_segments(segments_dir, date, topic, conversation_id):
    """Create the conversation segment templates"""
    
    segments = [
        ("01_introduction.md", "Introduction", "Initial concept and context"),
        ("02_deep_dive.md", "Deep Dive", "Detailed analysis and exploration"),
        ("03_implementation_strategy.md", "Implementation Strategy", "Implementation approach"),
        ("04_timing_assessment.md", "Timing Assessment", "When to implement"),
        ("05_documentation_strategy.md", "Documentation Strategy", "How to organize"),
        ("06_future_framework.md", "Future Framework", "Implementation readiness")
    ]
    
    for filename, title, description in segments:
        segment_content = f"""---
project: Career Intelligence Space
type: conversation_segment
status: active
tags: [conversation_segment, {topic.lower().replace(' ', '_')}, {filename.split('_')[0]}]
updated: {date}
conversation_id: "{conversation_id}"
segment_date: {date}
timezone: "America/Los_Angeles"
captured_at_utc: "{date}T15:30:00Z"
related:
  - "../{date}_full_conversation_archive.md"
  - "../{date}_key_insights_extraction.md"
---

# {title}

## Context
{description}

## Key Points
- [Point 1]
- [Point 2]
- [Point 3]

## Decisions Made
- [Decision 1]
- [Decision 2]

## Next Steps
- [Next step 1]
- [Next step 2]
"""
        
        segment_path = segments_dir / filename
        segment_path.write_text(segment_content)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Build conversation archive structure')
    parser.add_argument('--date', required=True, help='Conversation date (YYYY-MM-DD)')
    parser.add_argument('--topic', required=True, help='Conversation topic')
    parser.add_argument('--participants', required=True, help='Participants (comma-separated)')
    parser.add_argument('--output', required=True, help='Output directory')
    parser.add_argument('--id', help='Conversation ID (optional)')
    
    args = parser.parse_args()
    
    try:
        create_archive_structure(args.date, args.topic, args.participants, args.output, args.id)
    except ValueError as e:
        print(f"Error: {e}")
        exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        exit(1)
