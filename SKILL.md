---
name: tidyfactor-doc
description: "Code documentation builder, ADR generator, llms.txt standard generator, and triple-engine publishing platform (VitePress, MkDocs Material, and Docsify). Generates API references, READMEs, changelogs, ADRs, llms.txt, inline docblocks, and guides. Trigger on commands 'brief', 'init', 'collect', 'generate', 'adr', 'site', 'vitepress', 'mkdocs', 'docsify', 'audit', 'llms', or requests like 'document this codebase', 'generate ADR', 'create changelog', 'audit docs', 'generate llms.txt', or 'set up VitePress'."
---
# TidyFactor Doc

A command dispatcher. This file does not do the work itself — it routes to the right command, which routes to the right workflow, which injects the right memory.

## Commands

| User intent | Command | What it loads |
|---|---|---|
| "Establish documentation context / interview / debate codebase architecture" / "brief" / "debate" | `references/commands/brief.md` | `workflows/brief.md` + `memory/decision-points.md` |
| "Set up docs for this project" / "scaffold /docs" | `references/commands/init.md` | `workflows/init-docs.md` + `memory/doc-tree.md` |
| "Document this codebase" / "gather what's needed to document X" | `references/commands/collect.md` | `workflows/collect.md` + `memory/collection-sources.md` |
| "Record architectural decision / generate ADR" / "adr" | `references/commands/adr.md` | `workflows/generate-adr.md` + `memory/adr-template.md` + `memory/tone-of-voice.md` |
| "Write API docs" / "generate a README" / "create CHANGELOG" / "add inline comments" / "write a guide" | `references/commands/generate.md` | `workflows/generate-api.md` (or `generate-readme.md` / `generate-changelog.md` / `generate-inline.md` / `generate-guide.md`) + `memory/doc-templates.md` + `memory/changelog-rules.md` + matching `memory/stacks/*.md` |
| "Publish documentation portal" / "turn /docs into a doc site" (Interactive) | `references/commands/site.md` | `memory/site-engines.md` + interactive selection (`workflows/vitepress.md`, `workflows/mkdocs.md`, or `workflows/docsify.md`) |
| "Set up VitePress" / "build modern Vue-powered doc portal" | `references/commands/vitepress.md` | `workflows/vitepress.md` + `memory/vitepress-config.md` |
| "Set up MkDocs Material" / "compile static documentation" | `references/commands/mkdocs.md` | `workflows/mkdocs.md` + `memory/mkdocs-config.md` |
| "Set up Docsify" / "build lightweight zero-build doc SPA" | `references/commands/docsify.md` | `workflows/docsify.md` + `memory/docsify-config.md` |
| "Audit docs quality / scan credential leaks / verify links & changelog" / "audit" | `references/commands/audit.md` | `workflows/audit.md` + `scripts/audit_docs.py` |
| "Generate llms.txt & llms-full.txt / AI agent documentation index" / "llms" | `references/commands/llms.md` | `workflows/generate-llmstxt.md` + `memory/llmstxt-spec.md` |

Read only the command file that matches the request. Do not read all commands simultaneously.

## Non-negotiable constraints on every command

1. **All generated documentation lives under `/docs`.** Never write API references, guides, or generated READMEs to another location. (`README.md` itself stays at the project root, per convention — everything else generated goes in `/docs`.)
2. **`generate` never invents content.** It only writes docs from what `collect` gathered (or equivalent detail the user supplies directly in the conversation) — never from assumed signatures, assumed env vars, or assumed behavior. If required detail is missing, `generate` says what's missing and asks or falls back to running `collect` first.
3. **Stack rules are looked up, never guessed.** Before writing any code-level doc (API reference, inline comments), load the matching file under `memory/stacks/` for the language/framework actually in use. Do not mix PHPDoc conventions into a TypeScript file or vice versa.
4. **`site`, `vitepress`, `mkdocs`, and `docsify` only organize and publish what's already in `/docs`.** They never author new documentation content — that's `generate`'s job.
   - For **VitePress**: Generate ESM `config.mjs`, inject luxury typography (`Alexandria` + `Cairo` + `JetBrains Mono`), enforce surgical RTL navbar order, single-row Hero action CTAs (`white-space: nowrap`), and explicit 3-column card widths (`width: 33.333333% !important`) with BiDi protection (`unicode-bidi: plaintext`). Build cleanly with `npx vitepress build docs`.
   - For **MkDocs Material**: Generate standard `mkdocs.yml`, configure Neo-Brutalist CSS tokens (`extra.css`), configure Arabic/English i18n (`*.ar.md` suffix), and build cleanly with `mkdocs build --strict`.
   - For **Docsify**: Include `alias: { '/.*/_sidebar.md': '/_sidebar.md' }` and root-relative leading slashes `/` in `_sidebar.md` to guarantee persistent sidebar navigation across all subfolder routes.
5. **Standalone.** This skill does not read or depend on any other `tidyfactor-*` skill's conventions, even when the project happens to be built on one of those tracks.
6. **Zero Sensitive Data Leakage.** Under absolutely no circumstances should any real sensitive data (e.g., real API tokens, WHM/cPanel passwords, production server IPs, real DB credentials, secret keys, private auth tokens, or local absolute drive paths) be written into documentation. ALWAYS redact and replace these with safe generic placeholders.
7. **Clean Relative Links Only.** Never include local machine filesystem URLs (such as `file:///C:/...`, `file:c:`, or absolute workstation paths) in documentation links or markdown cross-references. All document cross-links must use clean relative markdown paths or standard public web URLs (`https://...`).

## Anti-Triggers

- Do NOT use for writing marketing campaigns or sales copywriting (use `tidyfactor-marketing`).
- Do NOT use for platform infrastructure management or deployment tasks (use `tidyfactor-github` or ops skills).

## Tooling Scope (Rule 10)

- **Execution Tools**:
  - `audit_docs` (`scripts/audit_docs.py`): Sub-second AST scanner for documentation under `/docs`, root `README.md`, and `CHANGELOG.md`. Audits credential leaks, machine-specific paths, broken relative links, and Keep a Changelog formatting.
  - `clean_orphaned_assets` (`scripts/clean_orphaned_assets.py`): Scans markdown documents for image references, detects unreferenced orphan assets in `assets/`, detects duplicate assets via SHA-256 hashing, and reports WebP compression opportunities.
- **Contract & Schema**: Portably declared in `manifest.json` with `"skill_root_anchor": "self"`.
- **Invocability**: Executable via direct CLI or through `tidyfactor-brain` MCP `run_skill_tool`.

## Skill vs MCP Boundary (Rule 12)

- **Inside Skill**: Static documentation templates, stack-specific docblock schemas, and local hygiene auditing scripts.
- **MCP Layer**: Sovereign Brain persistence (`search_knowledge_base`, `extract_knowledge_item`) operating under the strict Fail-Open protocol (`references/memory/20-brain-baas-integration.md`).

## Sequencing

`brief` (optional, architectural alignment & debate) → `init` → `collect` → `adr` (record technical decisions) → `generate` (repeatable, once per doc target) → `site` / `vitepress` / `mkdocs` / `docsify` → `llms` (AI agent indexing) → `audit` (quality, links & orphan verification before release).
