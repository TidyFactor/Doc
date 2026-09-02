# CHANGELOG — TidyFactor Doc

All notable changes to `tidyfactor-doc` will be documented in this file.
This project adheres to [Semantic Versioning](https://semver.org/).

## [1.5.0] - 2026-09-02

### 🧠 Added — Contextual Decision Layer (CDL v1.1.0) & Declarative Decision Gates
- **Declarative Decision Gates (`manifest.json`)**: Added formal `decision_gates[]` declaration for the `init` command conforming to manifest schema v1.1.0, defining `doc_engine`, `target_scope`, and `audience_persona` with `track_staleness: true`.
- **Context Delta Resolution Engine (`references/workflows/collect.md`)**: Upgraded collect workflow to evaluate the mechanical Delta formula:
  $$\text{Unknowns} = \text{Required Decisions} - (\text{Discovered Facts} \cup \text{Brain KIs})$$
- **Interactive Disclosure & User Agency First**: Surfacing all genuine Unknowns interactively with structured options and recommendations.
- **Anti-Dual-Write Architecture**: Enforcing local markdown files under `docs/` as sole SSOT, with one-way outbound cloud sync via `--sync-brain`.

---

## [1.4.0] - 2026-09-02

### 🧠 Added — Sovereign Brain MCP Integration, Hygiene Auditor & Fail-Open Protocol
- **Brain Integration Contract (`references/memory/20-brain-baas-integration.md`)**: Sovereign self-hosted architecture and Documentation Knowledge Item (KI) payload schemas.
- **Fail-Open Active Discovery (`references/workflows/collect.md`)**: Local workspace auto-sensing first, optional Brain MCP context acceleration (`search_knowledge_base`) when active, and instant 0ms silent fallback.
- **Runtime Tooling Manifest (`manifest.json`)**: Declared portable `audit_docs` tool conforming to `skill-manifest.tools.schema.json` with `"skill_root_anchor": "self"`.
- **Documentation Quality & Hygiene Auditor (`scripts/audit_docs.py`)**: Sub-second AST and pattern scanner detecting sensitive credentials leaks, passwords, private tokens, and banned absolute workstation URLs.
- **Tooling Scope & Anti-Triggers**: Enriched `SKILL.md` with explicit Rule 10 Tooling Scope and anti-triggers.

---

## [1.3.0] - 2026-08-29

### Added - Global Multi-Tier & Multi-Language Documentation Architecture
- **Rule 13 Implementation**: Two-tier documentation separation between Canonical Technical Documentation (`README.md` SSOT) and First-Class Market Localizations.
- **Universal Multi-Language Switcher**: Standardized 8-language switcher navigation bar across all documentation files (`EN`, `AR`, `FA`, `ES`, `PT`, `ZH`, `DE`, `FR`).
- **First-Class Localized Developer Adoption Guides**: `README.es.md`, `README.pt.md`, `README.fa.md`, `README.zh.md`, `README.de.md`, `README.fr.md`.
- **Automated Validation & Packaging**: Updated `tools/build-skill.js` and `tools/validate_skill.py`.

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
- Packaging as `@tidyfactor/doc` under Apache License 2.0.
