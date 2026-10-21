<!-- last-verified: 2026-09-09 -->
# Memory: git-doc-sync-hook

Specification and configuration guide for pre-commit documentation synchronization hooks.

## 1. Objective

Prevent drift between code changes and documentation by verifying that when core functions, endpoints, or public APIs are modified in staged git commits, their corresponding documentation files in `/docs` or root `README.md` / `CHANGELOG.md` are also staged.

## 2. Husky / Git Hook Implementation (`.husky/pre-commit` or `.git/hooks/pre-commit`)

```bash
#!/usr/bin/env bash
# TidyFactor Doc Pre-Commit Guard
set -e

# 1. Check staged files
STAGED_CODE=$(git diff --cached --name-only --diff-filter=ACM | grep -E '\.(php|ts|js|py|go|rs)$' || true)
STAGED_DOCS=$(git diff --cached --name-only --diff-filter=ACM | grep -E '(^docs/|README\.md|CHANGELOG\.md)' || true)

# 2. If core code changed, verify documentation activity or bypass flag
if [ -n "$STAGED_CODE" ]; then
    # Check if core services / interfaces were modified
    CORE_CHANGES=$(echo "$STAGED_CODE" | grep -E '(Core/|Services/|Controllers/|api/|interfaces/)' || true)
    
    if [ -n "$CORE_CHANGES" ] && [ -z "$STAGED_DOCS" ]; then
        if [ "$DOC_OVERRIDE" != "1" ]; then
            echo ""
            echo "❌ [TidyFactor Doc Guard] Core code modified without documentation update!"
            echo "Staged core files:"
            echo "$CORE_CHANGES"
            echo ""
            echo "Please update corresponding files under /docs or CHANGELOG.md."
            echo "To bypass intentionally for hotfixes, run: DOC_OVERRIDE=1 git commit -m '...'"
            echo ""
            exit 1
        fi
    fi
fi

# 3. Run audit_docs on staged docs
if [ -n "$STAGED_DOCS" ]; then
    echo "🔍 [TidyFactor Doc Guard] Auditing staged documentation quality..."
    python scripts/audit_docs.py docs/
fi

exit 0
```

## 3. Benefits

- Enforces the Single Source of Truth rule.
- Eliminates stale documentation where APIs evolve but docs remain outdated.
- Runs sub-second link and secret checks before commit creation.
