#!/usr/bin/env python3
"""
Unit tests for frontmatter linter
Run with: pytest -q scripts/tests/test_linter.py
"""

import sys
import os
import tempfile
from pathlib import Path
from datetime import date, timedelta

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))
from lint_frontmatter import validate_future_spec, load_schema

def test_valid_future_spec():
    """Test valid future_spec frontmatter"""
    future_date = (date.today() + timedelta(days=100)).isoformat()
    frontmatter = {
        "type": "future_spec",
        "review_date": future_date,
        "project": "Test",
        "status": "deferred"
    }
    errors = []
    validate_future_spec(frontmatter, "test.md", errors)
    assert len(errors) == 0, f"Expected no errors, got: {errors}"

def test_past_review_date():
    """Test that past review_date is caught"""
    past_date = (date.today() - timedelta(days=10)).isoformat()
    frontmatter = {
        "type": "future_spec",
        "review_date": past_date
    }
    errors = []
    validate_future_spec(frontmatter, "test.md", errors)
    assert len(errors) == 1
    assert "must be in the future" in errors[0][1]
    assert "Fix: sed" in errors[0][1]

def test_too_soon_review_date():
    """Test that review_date < 90 days triggers warning"""
    soon_date = (date.today() + timedelta(days=30)).isoformat()
    frontmatter = {
        "type": "future_spec",
        "review_date": soon_date
    }
    errors = []
    validate_future_spec(frontmatter, "test.md", errors)
    assert len(errors) == 1
    assert "≥ 90 days ahead" in errors[0][1]

def test_yaml_date_object():
    """Test that YAML date objects are converted correctly"""
    future_date_obj = date.today() + timedelta(days=100)
    frontmatter = {
        "type": "future_spec",
        "review_date": future_date_obj  # date object, not string
    }
    errors = []
    validate_future_spec(frontmatter, "test.md", errors)
    assert len(errors) == 0

def test_timestamp_format():
    """Test that timestamps are truncated (as string input)"""
    future_datetime = (date.today() + timedelta(days=100)).isoformat() + "T12:00:00Z"
    frontmatter = {
        "type": "future_spec",
        "review_date": future_datetime
    }
    errors = []
    validate_future_spec(frontmatter, "test.md", errors)
    # Timestamp strings are truncated silently ([:10])
    # No error expected for valid future date
    assert len(errors) == 0

def test_missing_review_date():
    """Test that missing review_date is caught"""
    frontmatter = {
        "type": "future_spec",
        "project": "Test"
    }
    errors = []
    validate_future_spec(frontmatter, "test.md", errors)
    assert len(errors) == 1
    assert "review_date is required" in errors[0][1]

def test_invalid_date_format():
    """Test that invalid date format is caught"""
    frontmatter = {
        "type": "future_spec",
        "review_date": "2025-13-45"  # invalid month/day
    }
    errors = []
    validate_future_spec(frontmatter, "test.md", errors)
    assert len(errors) == 1
    assert "not a valid date" in errors[0][1]

def test_schema_loading():
    """Test that schema loads correctly"""
    schema = load_schema()
    assert "types" in schema
    assert "future_spec" in schema["types"]
    assert "review_date" in schema["types"]["future_spec"]["required"]

if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])

