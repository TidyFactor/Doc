# CHANGELOG — TidyFactor Doc

All notable changes to `tidyfactor-doc` will be documented in this file.
This project adheres to [Semantic Versioning](https://semver.org/).

---

## [1.1.0] - 2026-08-20

### Added
- **Security Sanitization Constraint (Zero Sensitive Data Leakage)**:
  - Enforced strict automated redaction of sensitive credentials across all workflows and memory files.
  - Prohibited real API keys, passwords, database credentials, secret auth tokens, and private server IP addresses from leaking into `/docs`.
  - Added safe placeholder standard replacements table in `references/memory/collection-sources.md` (RFC 5737 doc IP ranges, dummy token formats).
- **Clean Relative Links Constraint (Clean Relative Links Only)**:
  - Prohibited local machine URLs (`file:///C:/...`, `file:c:`, and absolute workstation paths) in all generated documentation.
  - Mandated clean relative markdown links (`./docs/README.md`, `../api/project.md`) and standard public URLs.
- **Workflow & Memory Hardening**:
  - Updated `collect.md`, `generate-api.md`, `generate-guide.md`, `generate-readme.md`, `generate-inline.md`, and `docsify.md` with explicit validation checkboxes for zero credential leaks and clean link paths.
  - Updated `doc-templates.md` to showcase secure dummy placeholders in environment variable tables and relative link cross-references.
  - Added automated build pipeline script (`tools/build-skill.js`) for packaging and multi-target synchronization.

---

## [1.0.0] - 2026-08-19

### Added
- Initial canonical release of `tidyfactor-doc` under the TidyFactor Skills-LAB ecosystem.
- Standard 4-command router architecture in `SKILL.md`:
  - `init`: Scaffolds standard `/docs` folder structure and manifest.
  - `collect`: Non-destructive codebase analysis for PHP, TS/JS, and React/Next stacks.
  - `generate`: Produces API references, developer setup guides, inline docblocks, and READMEs.
  - `docsify`: Generates responsive Docsify documentation websites with persistent subfolder sidebar routing.
- Stack-specific memory rules for PHP 8, TypeScript, JavaScript, and React/Vue/Next component docs.
- Full cross-agent compatibility across Google Antigravity, Claude Code, Cursor, Codex, and Windsurf.
- Packaging as `@alwkala/tidyfactor-doc` under Apache License 2.0.
