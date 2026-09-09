<!-- last-verified: 2026-09-09 -->
# Memory: changelog-rules

Codified rules and governance standards for maintaining `CHANGELOG.md` as the Single Source of Truth (SSOT) across all software and skill repositories.

## 1. Authoritative Standards

1. **Keep a Changelog v1.1.0**:
   - Humans read changelogs, machines read git logs. Changelogs are curated summaries of user-facing and architectural value, not raw commit dumps.
   - Guiding principles:
     - Group changes by version and release date.
     - Group changes within a release by type.
     - Newest release always appears at the top (reverse chronological).
     - Each version must have a release date formatted as `YYYY-MM-DD`.

2. **Semantic Versioning (SemVer 2.0.0)**:
   - Given a version number `MAJOR.MINOR.PATCH`:
     - **`MAJOR` (x.0.0)**: Incompatible API changes, breaking architectural shifts, or removed features.
     - **`MINOR` (0.x.0)**: Backward-compatible new functionality, new commands, or new workflows.
     - **`PATCH` (0.0.x)**: Backward-compatible bug fixes, link repairs, or documentation corrections.

## 2. Standard Change Sections

Always classify changes into one of these 6 standardized buckets:

| Section | Icon | Purpose |
|---|---|---|
| `Added` | 🚀 | New features, commands, workflows, or platform engines |
| `Changed` | 🔄 | Modifications in existing functionality, refactors, or UI polish |
| `Deprecated` | ⚠️ | Soon-to-be removed features that remain functional for now |
| `Removed` | 🗑️ | Features, endpoints, or deprecated code deleted in this release |
| `Fixed` | 🐛 | Any bug fixes, broken link repairs, or error corrections |
| `Security` | 🔒 | Vulnerability fixes, credential redactions, or auth hardening |

## 3. Conventional Commit Mapping

When parsing `git log`, automatically map commit prefixes to changelog sections:

| Git Commit Prefix | Changelog Section | SemVer Impact |
|---|---|---|
| `feat:` / `feat(*):` | `Added` | MINOR |
| `refactor:` / `style:` / `perf:` | `Changed` | MINOR or PATCH |
| `deprecate:` | `Deprecated` | MINOR |
| `remove:` / `drop:` | `Removed` | MAJOR (if breaking) or MINOR |
| `fix:` / `bug:` / `patch:` | `Fixed` | PATCH |
| `sec:` / `security:` | `Security` | PATCH or MINOR |
| `BREAKING CHANGE:` / `feat!:` | Any (`Added`/`Changed`) with breaking note | MAJOR |
| `docs:` / `chore:` / `test:` | `Changed` or `Fixed` (or omitted if purely internal) | PATCH |

## 4. Invariants & Hygiene

- **Zero Undocumented Drift**: No production code or skill modification may be released without a corresponding dated entry in `CHANGELOG.md`.
- **Atomic Metadata Synchronization**: When updating `CHANGELOG.md`, update all corresponding metadata files synchronously:
  - `package.json` (`"version": "x.y.z"`)
  - `.tidyfactor` (`"version": "x.y.z"`)
  - `brand.yaml` / `brand.json` (`"version": "x.y.z"`)
  - `README.md` / `README.ar.md` (Title banners)
- **Zero Sensitive Data**: Never leak internal server paths, local absolute paths (`file:///C:`), or real API keys in changelogs.
