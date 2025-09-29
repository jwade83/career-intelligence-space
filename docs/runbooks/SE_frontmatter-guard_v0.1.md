# SE Runbook — Frontmatter Guard
**Context:** Pre-commit hook validates YAML frontmatter on chronicle files to prevent metadata consistency issues.

**Trigger:** Any commit attempt that includes files matching `08_CHRONICLE/.*\.md$` pattern.

**Steps:**
1. Check if any staged files match chronicle pattern
2. For each chronicle file:
   - Verify first line is `---`
   - Count `---` lines in first 10 lines
   - Ensure exactly 2 `---` lines (opening and closing)
3. Block commit if validation fails
4. Allow commit if all files pass validation

**Verification:** 
```bash
# Test with invalid file (should block)
echo "# No frontmatter" > test.md
git add test.md
git commit -m "test"  # Should fail

# Test with valid file (should pass)
echo -e "---\nproject: test\n---\n# Content" > test.md
git add test.md
git commit -m "test"  # Should succeed
```

**Rollback:** 
```bash
# Remove the hook
rm .git/hooks/pre-commit
# Or disable temporarily
mv .git/hooks/pre-commit .git/hooks/pre-commit.disabled
```

**Last updated:** 2025-10-13
