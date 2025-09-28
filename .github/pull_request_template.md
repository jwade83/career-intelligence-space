### Frontmatter Compliance
- [ ] All new `.md` files have frontmatter at the very top (no code fences)
- [ ] Required keys: `project`, `type`, `status`, `tags`, `updated`
- [ ] `type`/`status` values match `docs/ONTOLOGY.yml` enums
- [ ] `tags` is a non-empty list (e.g., `[tag1, tag2, tag3]`)
- [ ] `updated` is in YYYY-MM-DD format
- [ ] **Quick fix**: `python3 .github/scripts/add_frontmatter.py <file1> <file2> ...`

### Link Compliance  
- [ ] `docs/` links are relative (./path), no `](docs/...)` inside docs/
- [ ] All internal links exist and are case-sensitive

### Pre-commit Checks
- [ ] Ran `python3 .github/scripts/pre_commit_frontmatter.py` locally
- [ ] Ran `python3 .github/scripts/pr_health.py <PR#>` and addressed any issues

### Templates Available
- **Chronicle files**: See `.github/templates/frontmatter_templates.md`
- **Documentation**: Use `type: spec`, `status: matured`
- **Assessments**: Use `type: assessment`, `status: draft`
