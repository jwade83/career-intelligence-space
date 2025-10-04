---
name: Mobile Meta Insight
about: Strategic insight capture using mobile GitHub interface
title: "[INSIGHT] Meta Insight - [Date]"
labels: ["mobile_copilot", "meta_insight", "strategic"]
assignees: ["@jwade83"]
body:
  - type: markdown
    attributes:
      value: |
        ## Insight Context
        Please provide the following strategic information:
        
  - type: input
    id: pattern
    attributes:
      label: Pattern Identified
      description: What pattern or trend have you identified?
      placeholder: "e.g., Market shift, User behavior change, Process improvement"
    validations:
      required: true
      
  - type: textarea
    id: evidence
    attributes:
      label: Supporting Evidence
      description: What evidence supports this insight?
      placeholder: "Enter supporting evidence, data, or observations..."
    validations:
      required: true
      
  - type: textarea
    id: implications
    attributes:
      label: Strategic Implications
      description: What are the strategic implications?
      placeholder: "Enter the strategic implications of this insight..."
    validations:
      required: true
      
  - type: textarea
    id: analysis
    attributes:
      label: Meta Analysis
      description: Your meta-level analysis
      placeholder: "Enter your meta analysis here..."
    validations:
      required: true
      
  - type: checkboxes
    id: actions
    attributes:
      label: Strategic Recommendations
      description: Select applicable strategic actions
      options:
        - label: "Action 1"
        - label: "Action 2"
        - label: "Action 3"
