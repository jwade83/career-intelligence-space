# Career Intelligence Space - Quality Assurance Targets

.PHONY: qa qa-lite help

# Full QA check - runs all validations
qa:
	@echo "🔍 Running full Harness archive QA..."
	python3 scripts/lint_frontmatter.py
	python3 scripts/conversation-archive/pii-scanner.py --path 08_CHRONICLE --mask --exit-nonzero-on-detect
	@echo "✅ Harness archive QA passed."

# Lite QA check - runs validations but doesn't fail on issues
qa-lite:
	@echo "🔍 Running lite Harness archive QA..."
	python3 scripts/lint_frontmatter.py || true
	python3 scripts/conversation-archive/pii-scanner.py --path 08_CHRONICLE --mask || true
	@echo "✅ Lite QA completed (non-blocking)."

# Help target
help:
	@echo "Available targets:"
	@echo "  qa       - Run full QA check (fails on issues)"
	@echo "  qa-lite  - Run lite QA check (non-blocking)"
	@echo "  help     - Show this help message"
