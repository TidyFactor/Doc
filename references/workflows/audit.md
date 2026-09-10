# Workflow: audit

One outcome: a deterministic documentation quality & hygiene audit report verifying zero credential leaks, zero banned machine paths, 100% relative link integrity, and valid CHANGELOG formatting.

## Steps

1. **Determine the target path**:
   - If user specified a file or folder (e.g. `docs/`, `README.md`, `CHANGELOG.md`), audit that target.
   - Otherwise, default to full documentation sweep: `docs/`, `README.md`, `README.ar.md`, `CHANGELOG.md`.

2. **Run deterministic auditor**:
   - Execute the native Python auditing tool:
     ```bash
     python scripts/audit_docs.py docs/
     python scripts/audit_docs.py README.md
     python scripts/audit_docs.py CHANGELOG.md
     ```
   - For machine-readable output or CI pipeline integration:
     ```bash
     python scripts/audit_docs.py docs/ --json
     ```

3. **Analyze findings**:
   - **Critical issues (Score -30 each)**: Plaintext secrets, leaked API keys, database passwords, or private tokens.
   - **High issues (Score -15 each)**: Banned absolute workstation paths (`file:///C:`, `\wamp64\www\`), broken relative markdown links pointing to missing files, missing CHANGELOG headers.
   - **Low issues**: Non-standard changelog version headers or minor formatting irregularities.

4. **Remediate detected issues**:
   - Redact any sensitive tokens into safe RFC placeholders (`EXAMPLE_KEY_1234567890ABCDEFGH`).
   - Fix broken relative links to point to valid paths or update link targets.
   - Convert absolute filesystem URLs to clean relative markdown paths (`./docs/README.md`).

5. **Re-run verification**:
   - Re-execute the auditor until a clean score of **100/100 [PASS]** is achieved.

## Validation checklist

- [ ] All target documentation files scanned by `scripts/audit_docs.py`
- [ ] Overall score is 100/100 (`passed: true`) with 0 critical and 0 high issues
- [ ] Zero sensitive tokens or credentials present across all scanned files
- [ ] All relative links verified to exist on disk (zero broken relative links)
- [ ] CHANGELOG.md conforms to Keep a Changelog v1.1.0 standard headers
