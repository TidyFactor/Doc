---
name: tidyfactor-doc
description: TidyFactor Doc — code documentation builder and dual-engine publishing platform (MkDocs Material & Docsify). Interviews codebases (source comments, Git history, env requirements, error patterns) to generate accurate, maintainable docs under /docs — API references, READMEs, inline comments, and technical guides. Supports interactive doc portal generation with static compilation (MkDocs Material with native Arabic RTL i18n & Neo-Brutalist themes) or zero-build lightweight SPAs (Docsify). Trigger on commands "init", "collect", "generate", "site", "mkdocs", "docsify", or requests like "document this repo", "write API docs", "generate a README", "add JSDoc/PHPDoc", "publish doc portal", "set up MkDocs", "set up Docsify". Has stack-specific rules for PHP, JavaScript, TypeScript, React/Vue/Next.
---

# TidyFactor Doc

A command dispatcher. This file does not do the work itself — it routes to the right command, which routes to the right workflow, which injects the right memory.

## Commands

| User intent | Command | What it loads |
|---|---|---|
| "Set up docs for this project" / "scaffold /docs" | `references/commands/init.md` | `workflows/init-docs.md` + `memory/doc-tree.md` |
| "Document this codebase" / "gather what's needed to document X" | `references/commands/collect.md` | `workflows/collect.md` + `memory/collection-sources.md` |
| "Write API docs" / "generate a README" / "add inline comments" / "write a guide" | `references/commands/generate.md` | `workflows/generate-api.md` (or `generate-readme.md` / `generate-inline.md` / `generate-guide.md`) + `memory/doc-templates.md` + matching `memory/stacks/*.md` |
| "Publish documentation portal" / "turn /docs into a doc site" (Interactive) | `references/commands/site.md` | `memory/site-engines.md` + interactive selection (`workflows/mkdocs.md` or `workflows/docsify.md`) |
| "Set up MkDocs Material" / "compile static documentation" | `references/commands/mkdocs.md` | `workflows/mkdocs.md` + `memory/mkdocs-config.md` |
| "Set up Docsify" / "build lightweight zero-build doc SPA" | `references/commands/docsify.md` | `workflows/docsify.md` + `memory/docsify-config.md` |

Read only the command file that matches the request. Do not read all commands simultaneously.

## Non-negotiable constraints on every command

1. **All generated documentation lives under `/docs`.** Never write API references, guides, or generated READMEs to another location. (`README.md` itself stays at the project root, per convention — everything else generated goes in `/docs`.)
2. **`generate` never invents content.** It only writes docs from what `collect` gathered (or equivalent detail the user supplies directly in the conversation) — never from assumed signatures, assumed env vars, or assumed behavior. If required detail is missing, `generate` says what's missing and asks or falls back to running `collect` first.
3. **Stack rules are looked up, never guessed.** Before writing any code-level doc (API reference, inline comments), load the matching file under `memory/stacks/` for the language/framework actually in use. Do not mix PHPDoc conventions into a TypeScript file or vice versa.
4. **`site`, `mkdocs`, and `docsify` only organize and publish what's already in `/docs`.** They never author new documentation content — that's `generate`'s job.
   - For **MkDocs Material**: Generate standard `mkdocs.yml`, configure Neo-Brutalist CSS tokens (`extra.css`), configure Arabic/English i18n (`*.ar.md` suffix), and build cleanly with `mkdocs build --strict`.
   - For **Docsify**: Include `alias: { '/.*/_sidebar.md': '/_sidebar.md' }` and root-relative leading slashes `/` in `_sidebar.md` to guarantee persistent sidebar navigation across all subfolder routes.
5. **Standalone.** This skill does not read or depend on any other `tidyfactor-*` skill's conventions, even when the project happens to be built on one of those tracks.
6. **Zero Sensitive Data Leakage.** Under absolutely no circumstances should any real sensitive data (e.g., real API tokens, WHM/cPanel passwords, production server IPs, real DB credentials, secret keys, private auth tokens, or local absolute drive paths) be written into documentation. ALWAYS redact and replace these with safe generic placeholders.
7. **Clean Relative Links Only.** Never include local machine filesystem URLs (such as `file:///C:/...`, `file:c:`, or absolute workstation paths) in documentation links or markdown cross-references. All document cross-links must use clean relative markdown paths or standard public web URLs (`https://...`).

## Sequencing

`init` → `collect` → `generate` (repeatable, once per doc target) → `site` / `mkdocs` / `docsify` (optional, once /docs has real content).
