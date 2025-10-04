---
name: Mobile Technical Analysis
about: Technical field analysis capture using mobile GitHub interface
title: "[TECH] Analysis - [Date]"
labels: ["mobile_copilot", "technical_analysis", "field_capture"]
assignees: ["@jwade83"]
body:
  - type: markdown
    attributes:
      value: |
        ## Technical Context
        Please provide the following technical information:
        
  - type: input
    id: system
    attributes:
      label: System Name
      description: What system is being analyzed?
      placeholder: "e.g., Mobile App, Database, API"
    validations:
      required: true
      
  - type: input
    id: component
    attributes:
      label: Component
      description: Which component of the system?
      placeholder: "e.g., Authentication, Data Layer, UI"
    validations:
      required: true
      
  - type: textarea
    id: issue
    attributes:
      label: Technical Issue
      description: Describe the technical issue or analysis
      placeholder: "Enter the technical issue or analysis details..."
    validations:
      required: true
      
  - type: textarea
    id: analysis
    attributes:
      label: Analysis
      description: Your technical analysis
      placeholder: "Enter your technical analysis here..."
    validations:
      required: true
      
  - type: checkboxes
    id: recommendations
    attributes:
      label: Recommendations
      description: Select applicable recommendations
      options:
        - label: "Recommendation 1"
        - label: "Recommendation 2"
        - label: "Recommendation 3"
