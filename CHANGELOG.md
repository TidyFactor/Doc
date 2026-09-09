# CHANGELOG — TidyFactor Doc

All notable changes to `tidyfactor-doc` will be documented in this file.
This project adheres to [Semantic Versioning](https://semver.org/).

## [1.9.0] - 2026-09-09

### 🚀 Added — Architectural Decision Records (ADR), Deep Docblock Scraping, Project Mindmaps & Asset Hygiene
- **Architectural Decision Record Generator (`references/commands/adr.md`, `references/workflows/generate-adr.md`)**:
  - Added dedicated `adr` command with Context-Aware prompts to record technical choices, problem context, decision drivers, and consequences.
  - Standardized on MADR (Markdown Architectural Decision Records) schema with index generation (`docs/adr/README.md`).
- **Deep Code Parsing in Collect Workflow (`references/workflows/collect.md`)**:
  - Enriched Step 1 with automated scraping for PHPDoc (`@param`, `@return`, `@throws`, `@deprecated`) and JSDoc/TSDoc (`@param`, `@returns`, `@typedef`, `@template`) annotations.
  - Mapped AST interface types and class properties directly to documentation templates.
- **Operational Memory Expansion**:
  - Added `references/memory/adr-template.md`: Authoritative MADR record structure and master table of contents.
  - Added `references/memory/project-mindmap.md`: Mermaid AST schemas for architecture layering, component topologies, and execution flows.
  - Added `references/memory/naming-conventions.md`: Uniform naming conventions across PHP (PSR-1/PSR-12), TypeScript, Python, and doc slugs.
  - Added `references/memory/tone-of-voice.md`: Non-negotiable technical writing rules (direct, action-oriented, zero marketing fluff).
  - Added `references/memory/git-doc-sync-hook.md`: Pre-commit hook specification enforcing documentation updates alongside core code changes.
- **Automated Asset Hygiene & Orphan Detection (`scripts/clean_orphaned_assets.py`)**:
  - Added script to scan all `.md` files for image references, identify unreferenced assets in `assets/`, detect duplicate files via SHA-256 hashes, and calculate WebP compression savings.
- **Unified Tooling Manifest (`manifest.json`)**:
  - Registered `clean_orphaned_assets` tool with portable CLI patterns.
  - Registered `adr` command in tool invocation mappings and decision gate options.

---

## [1.8.0] - 2026-09-09

### 🚀 Added — Documentation Hygiene Auditor, Keep a Changelog Architecture & Asset Optimization
- **Documentation Quality & Link Auditor (`references/commands/audit.md`, `references/workflows/audit.md`)**:
  - Added dedicated `audit` command and workflow for sub-second deterministic doc scanning.
  - Added relative markdown link integrity verification in `scripts/audit_docs.py` (`check_relative_links`) to detect broken local file links before release.
  - Added Keep a Changelog structural validator (`check_changelog_format`) verifying SemVer release headers and standard change categories.
- **Changelog Workflow & SSOT Architecture (`references/workflows/generate-changelog.md`)**:
  - Codified automated `generate-changelog` workflow strictly adhering to Keep a Changelog v1.1.0 and SemVer 2.0.0.
  - Conventional Commits parser mapping git commits to standard sections (`Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`, `Security`).
  - Integrated changelog generation routing into `references/commands/generate.md`.
- **Operational Memory & Governance Templates (`references/memory/changelog-rules.md`, `references/memory/doc-templates.md`)**:
  - Added `references/memory/changelog-rules.md` establishing release standards, SemVer bump formulas, and conventional commit mappings.
  - Added standard `CHANGELOG.md` template to `references/memory/doc-templates.md`.
  - Refreshed all memory verification timestamps (`<!-- last-verified: 2026-09-09 -->`).
- **Asset Deduplication & Hygiene (`assets/`)**:
  - Removed duplicate 242KB asset (`assets/og-default.png`), saving 50% of the asset footprint without breaking references.
- **Unified Tooling & Decision Manifest (`manifest.json`)**:
  - Expanded `audit_docs` tool contract with link integrity and changelog validation scopes.
  - Registered `audit` and `vitepress` commands in tool invocation mappings and decision gate options.

---

## [1.7.0] - 2026-09-09

### 🚀 Added — Triple-Engine Publishing Platform (VitePress Integration) & Luxury RTL Design System
- **VitePress Publishing Engine (references/commands/vitepress.md)**: Added full VitePress SSG engine support alongside MkDocs Material and Docsify.
- **Ordered Workflow & Automation (references/workflows/vitepress.md)**: 6-step workflow covering scaffolding, multi-language subdirectory routing, luxury CSS injection, and zero-dead-link validation (npm run docs:build).
- **Master Configuration & Luxury Tokens (references/memory/vitepress-config.md)**: Codified complete ESM config.mjs schema, Alexandria + Cairo + JetBrains Mono typography, surgical RTL navbar flex order, and Quick-Navigation grid templates.
- **Luxury Hero & Actions Architecture**: Codified single-row CTA button flex safeguards (white-space: nowrap) and stable natural RTL Hero direction (Text/CTAs on right, Logo on left).
- **3-Column Feature Cards & Column Collapse Fix**: Codified explicit width assignment on .VPFeatures .item and BiDi text safeguards.
- **3-Way Engine Evaluation Matrix (references/memory/site-engines.md)**: Expanded to comprehensive 3-way evaluation across VitePress, MkDocs Material, and Docsify.

---

## [1.6.0] - 2026-09-08

### 🧠 Added — Dual-Mode Decision Architect (DM-DA) & Debate Mode Engine (CDL v2.0)
- **Interactive Interview & Debate Command (`brief`)**: Added `references/commands/brief.md` supporting trigger phrases `brief`, `interview`, `debate`, "استجوبني", and "ناقشني في معمارية التوثيق".
- **Dual Operational Modes (`references/workflows/brief.md`)**:
  - **[MODE A] Smart 3-Round Protocol**: Fast-track structured alignment in 3 deterministic rounds (Purpose & Target Persona ➔ Architecture & Engine ➔ Hygiene & Safe Defaults) terminating with an explicit escalation gate prompt.
  - **[MODE B] Relentless Debate & Interview (Debate Mode)**: Deep multi-turn architectural counter-questioning, challenging assumptions on static vs. SPA, bilingual overhead, and automated secret scrubbing. Strictly terminates only on `"END DEBATE"` / `"اعتماد"`, emitting a formal `docs/architectural_debate_synthesis.md` artifact.
- **Architectural Decision Matrix (`references/memory/decision-points.md`)**: Codified 5 core documentation dimensions (D1: Purpose & Scope, D2: Platform Engine, D3: Target Persona & Register, D4: Hygiene & Leak Policy, D5: Extraction Depth) with Boolean Skip Conditions for zero-overhead execution.
- **Declarative Gate Expansion (`manifest.json`)**: Expanded manifest schema v1.1.0 with formal `brief` decision gates for D1–D5 with local YAML persistence (`.tidyfactor/doc-brief.snapshot.yaml`).

---

## [1.5.1] - 2026-09-08

### 🏛️ Fixed & Synchronized — Governance Compliance (TidyFactor Skill Architect)
- **Memory Freshness (Rule 11)**: Added `<!-- last-verified: 2026-09-08 -->` stamps to all stack memory files (`js-ts.md`, `php.md`, `react-vue-next.md`).
- **Two-Tier Multi-Language Documentation (Rule 13)**:
  - Integrated universal 8-language switcher bar into `README.md` and `README.ar.md`.
  - Synchronized title banner versioning (`v1.5.1`) across all 8 market localizations (`README.md`, `README.ar.md`, `README.de.md`, `README.es.md`, `README.fa.md`, `README.fr.md`, `README.pt.md`, `README.zh.md`).
- **Contextual Decision Layer CDL v2.0 (Rule 14)**:
  - Integrated Step 0 Context Delta Resolution into `references/workflows/init-docs.md` with auto-sensing for `doc_engine`, `target_scope`, and `audience_persona`.
- **Token Efficiency & YAML Primacy (Rule 15)**:
  - Created canonical `brand.yaml` SSOT at skill root alongside `brand.json`.
  - Updated `manifest.json` to persist decision snapshots to `.tidyfactor/doc-brief.snapshot.yaml` and discover from `brand.yaml`.

---

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
