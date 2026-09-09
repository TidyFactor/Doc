# Workflow: generate-changelog

One outcome: a project-root `CHANGELOG.md` created or updated strictly conforming to **Keep a Changelog v1.1.0** and **SemVer 2.0.0**. Along with `README.md`, this is the authoritative Single Source of Truth (SSOT) for version releases, changes, and migration notes.

## Steps

1. **Locate or initialize `CHANGELOG.md`**:
   - Check if `CHANGELOG.md` exists at the project root.
   - If missing, load the Keep a Changelog template from `../memory/doc-templates.md` and initialize with standard header, description, and link definitions.

2. **Extract change history & commit deltas**:
   - Inspect git commit history:
     ```bash
     git log --oneline --no-merges -n 50
     # Or between tags:
     git log <last-tag>..HEAD --oneline
     ```
   - Parse Conventional Commits (`feat:`, `fix:`, `refactor:`, `docs:`, `perf:`, `chore:`, `sec:`).
   - If non-git or manual changes are provided, align them with the verified codebase changes.

3. **Categorize entries into Keep a Changelog standard sections**:
   - `### 🚀 Added`: For new features, commands, or capabilities.
   - `### 🔄 Changed`: For changes in existing functionality, refactors, or UX enhancements.
   - `### ⚠️ Deprecated`: For once-stable features slated for removal in upcoming releases.
   - `### 🗑️ Removed`: For features, deprecated APIs, or obsolete assets removed in this release.
   - `### 🐛 Fixed`: For any bug fixes, link repairs, or error resolutions.
   - `### 🔒 Security`: In case of vulnerability patches or credential hardening.

4. **Determine SemVer version bump**:
   - Load `../memory/changelog-rules.md`.
   - `MAJOR` (X.0.0): Any breaking change or incompatible API/workflow modification.
   - `MINOR` (0.X.0): Backward-compatible new features, commands, or workflows.
   - `PATCH` (0.0.X): Backward-compatible bug fixes, link corrections, or documentation polish.

5. **Format the version entry**:
   - Structure: `## [X.Y.Z] - YYYY-MM-DD` (e.g. `## [1.8.0] - 2026-09-09`).
   - If drafting work-in-progress, record changes under `## [Unreleased]`.
   - Maintain strict reverse-chronological order (newest release at the top).

6. **Validate & update metadata**:
   - Run `python scripts/audit_docs.py CHANGELOG.md` to guarantee zero absolute machine URLs or credential leaks.
   - Ensure atomic synchronization with `package.json`, `.tidyfactor`, `brand.yaml`, `brand.json`, and `README.md`.

## Validation checklist

- [ ] `CHANGELOG.md` exists at project root and follows Keep a Changelog v1.1.0 format
- [ ] Version header strictly matches `## [X.Y.Z] - YYYY-MM-DD` or `## [Unreleased]`
- [ ] All entries classified under valid sections (`Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`, `Security`)
- [ ] Entries are organized in reverse chronological order
- [ ] SemVer bump is fully justified by the logged changes (Breaking → Major, Feat → Minor, Fix → Patch)
- [ ] Zero sensitive data, API tokens, passwords, or absolute workstation paths (`file:///`) present
- [ ] Audited with `python scripts/audit_docs.py CHANGELOG.md` and passed cleanly
