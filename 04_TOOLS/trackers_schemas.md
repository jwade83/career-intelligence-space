---
project: Career Intelligence Space
type: spec
status: draft
tags: ['misc']
updated: 2025-10-02
---

# Trackers and Data Schemas

## Overview
This document defines the data tracking schemas and structures for the career intelligence system.

## Core Tracking Schemas

### User Profile Schema

#### Personal Information
```json
{
  "user_id": "string (UUID)",
  "personal_info": {
    "first_name": "string",
    "last_name": "string",
    "email": "string",
    "location": {
      "city": "string",
      "country": "string",
      "timezone": "string"
    },
    "created_at": "timestamp",
    "last_updated": "timestamp"
  }
}
```

#### Career Information
```json
{
  "career_profile": {
    "current_role": "string",
    "current_company": "string",
    "industry": "string",
    "experience_level": "enum [entry, mid, senior, executive]",
    "years_experience": "integer",
    "salary_range": {
      "min": "integer",
      "max": "integer",
      "currency": "string"
    },
    "career_goals": ["string"]
  }
}
```

### Skills Tracking Schema

#### Skills Inventory
```json
{
  "skills": [
    {
      "skill_id": "string (UUID)",
      "skill_name": "string",
      "category": "enum [technical, soft, domain]",
      "proficiency_level": "enum [beginner, intermediate, advanced, expert]",
      "verified": "boolean",
      "verification_source": "string",
      "acquired_date": "timestamp",
      "last_assessed": "timestamp"
    }
  ]
}
```

#### Skills Gap Analysis
```json
{
  "gap_analysis": {
    "target_role": "string",
    "required_skills": ["string"],
    "current_skills": ["string"],
    "skill_gaps": [
      {
        "skill_name": "string",
        "importance": "enum [critical, high, medium, low]",
        "estimated_learning_time": "integer (hours)",
        "recommended_resources": ["string"]
      }
    ],
    "analysis_date": "timestamp"
  }
}
```

### Learning Progress Schema

#### Course Tracking
```json
{
  "learning_activities": [
    {
      "activity_id": "string (UUID)",
      "activity_type": "enum [course, certification, project, mentoring]",
      "title": "string",
      "provider": "string",
      "start_date": "timestamp",
      "end_date": "timestamp",
      "completion_percentage": "integer",
      "status": "enum [not_started, in_progress, completed, paused]",
      "skills_targeted": ["string"],
      "time_invested": "integer (hours)",
      "cost": "decimal",
      "rating": "integer (1-5)"
    }
  ]
}
```

#### Progress Metrics
```json
{
  "progress_metrics": {
    "total_learning_hours": "integer",
    "courses_completed": "integer",
    "certifications_earned": "integer",
    "skills_acquired": "integer",
    "learning_streak": "integer (days)",
    "monthly_progress": {
      "month": "string (YYYY-MM)",
      "hours_logged": "integer",
      "courses_completed": "integer",
      "assessments_passed": "integer"
    }
  }
}
```

### Career Progression Schema

#### Job History
```json
{
  "job_history": [
    {
      "position_id": "string (UUID)",
      "job_title": "string",
      "company": "string",
      "industry": "string",
      "start_date": "timestamp",
      "end_date": "timestamp",
      "employment_type": "enum [full-time, part-time, contract, freelance]",
      "salary": "decimal",
      "responsibilities": ["string"],
      "achievements": ["string"],
      "skills_used": ["string"],
      "skills_developed": ["string"]
    }
  ]
}
```

#### Career Milestones
```json
{
  "milestones": [
    {
      "milestone_id": "string (UUID)",
      "milestone_type": "enum [promotion, role_change, certification, project_completion]",
      "title": "string",
      "description": "string",
      "achievement_date": "timestamp",
      "impact_metrics": {
        "salary_increase": "decimal",
        "responsibility_level": "integer",
        "team_size": "integer"
      }
    }
  ]
}
```

### Market Intelligence Schema

#### Job Market Data
```json
{
  "market_data": {
    "role_demand": {
      "role_title": "string",
      "demand_level": "enum [very_high, high, medium, low]",
      "job_postings_count": "integer",
      "growth_rate": "decimal",
      "location_data": [
        {
          "location": "string",
          "openings": "integer",
          "avg_salary": "decimal"
        }
      ]
    },
    "skills_demand": [
      {
        "skill_name": "string",
        "demand_score": "integer (1-100)",
        "trend": "enum [increasing, stable, decreasing]",
        "salary_premium": "decimal"
      }
    ]
  }
}
```

### Analytics and Reporting Schema

#### Dashboard Data
```json
{
  "dashboard_metrics": {
    "career_health_score": "integer (1-100)",
    "learning_velocity": "decimal",
    "skill_gap_ratio": "decimal",
    "market_alignment": "integer (1-100)",
    "roi_projections": {
      "6_months": "decimal",
      "1_year": "decimal",
      "3_years": "decimal"
    },
    "last_calculated": "timestamp"
  }
}
```

## Data Validation Rules

### Required Fields
- All user_id fields must be valid UUIDs
- Timestamps must be in ISO 8601 format
- Email addresses must pass RFC 5322 validation
- Salary ranges must have min <= max

### Data Quality Standards
- Proficiency levels must progress logically
- Completion percentages must be 0-100
- Rating scores must be 1-5
- Currency codes must be ISO 4217 compliant

### Privacy and Security
- All PII fields must be encrypted at rest
- Data retention policies apply after user deletion
- Access logging required for all data modifications
- GDPR compliance for EU users

## Integration Specifications

### API Endpoints
- GET /api/user/{user_id}/profile
- PUT /api/user/{user_id}/skills
- POST /api/learning/progress
- GET /api/analytics/dashboard

### Database Indexing
- Primary indexes on all ID fields
- Composite indexes on user_id + timestamp
- Text search indexes on skills and job titles
- Performance monitoring on query execution

## Maintenance and Updates

### Schema Evolution
- Version control for schema changes
- Backward compatibility requirements
- Migration procedures for data updates
- Testing protocols for schema modifications
