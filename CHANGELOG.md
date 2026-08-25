# CHANGELOG — TidyFactor Doc

All notable changes to `tidyfactor-doc` will be documented in this file.
This project adheres to [Semantic Versioning](https://semver.org/).

## [1.2.1] - 2026-08-25

### Fixed
- **CLI Executable & NPX Packaging**: Added standard `"add-skill": "bin/add-skill.js"` mapping in `package.json` to ensure unified `npx @alwkala/tidyfactor-doc add-skill` execution.
- **Workflow Compliance**: Standardized `## Validation checklist` headers across all 8 workflows.

---

## [1.2.0] - 2026-08-25

### Added
- **MkDocs Material Publishing Engine**:
  - Full static HTML compilation track for high-performance production doc portals.
  - Native bilingual parallel build support (`/` and `/ar/`) via `mkdocs-static-i18n`.
  - Built-in Lunr.js offline search indexing (English + Arabic tokenization).
  - Neo-Brutalist luxury styling tokens (`tidyfactor-light` & `tidyfactor-dark`) via `stylesheets/extra.css`.
  - macOS-style terminal dots on highlighted code blocks with line spans.
  - GitHub-style alert callout transformer (`[!IMPORTANT]`, `[!NOTE]`, `[!WARNING]`, `[!TIP]`) via `javascripts/extra.js`.
  - Local Apache subfolder transparent routing via `.htaccess`.
- **Interactive Engine Selector Command (`site`)**:
  - Interactive evaluation matrix in `references/commands/site.md` and `references/memory/site-engines.md`.
  - Auto-detection of local Python/pip environment vs. zero-build CDN requirements.
  - Clear user choice and recommendation guidance between MkDocs Material and Docsify.
- **Dedicated Direct Commands**:
  - `mkdocs`: Direct entry point for MkDocs Material static portal compilation.
  - `docsify`: Direct entry point for Docsify zero-build lightweight SPA.
- **New Workflows & Memory Specs**:
  - `references/workflows/mkdocs.md`: End-to-end scaffolding, building, and validation checklist.
  - `references/memory/mkdocs-config.md`: Master `mkdocs.yml` schema, theme configuration, and i18n rules.
  - `references/memory/site-engines.md`: Technical comparison between Docsify and MkDocs Material.

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
