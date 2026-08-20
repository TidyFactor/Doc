---
name: tidyfactor-doc
description: TidyFactor Doc — a code documentation builder that interviews a codebase (source comments, Git log/PR history, env/runtime requirements, error patterns) and turns it into accurate, maintainable docs saved under /docs — API references, README files, inline comments, and technical guides. Use whenever the user asks to document a codebase or API, write or update a README, add or audit inline comments, write a developer/setup guide, or publish project docs as a browsable site. Trigger on the named commands "init", "collect", "generate", "docsify", or requests like "document this repo", "write API docs for this", "generate a README", "add JSDoc/PHPDoc comments", "write a getting-started guide", "turn /docs into a doc site". Has stack-specific rules for PHP, JavaScript, TypeScript, and React/Vue/Next component docs. Standalone — does not depend on any other TidyFactor track skill.
---

# TidyFactor Doc

A command dispatcher. This file does not do the work itself — it routes to the right command, which routes to the right workflow, which injects the right memory.

## Commands

| User intent | Command | What it loads |
|---|---|---|
| "Set up docs for this project" / "scaffold /docs" | `references/commands/init.md` | `workflows/init-docs.md` + `memory/doc-tree.md` |
| "Document this codebase" / "gather what's needed to document X" | `references/commands/collect.md` | `workflows/collect.md` + `memory/collection-sources.md` |
| "Write API docs" / "generate a README" / "add inline comments" / "write a guide" | `references/commands/generate.md` | one of `workflows/generate-*.md` + `memory/doc-templates.md` + the matching `memory/stacks/*.md` |
| "Turn /docs into a doc site" / "set up Docsify" | `references/commands/docsify.md` | `workflows/docsify.md` + `memory/docsify-config.md` |

Read only the command file that matches the request. Do not read all four.

## Non-negotiable constraints on every command

1. **All generated documentation lives under `/docs`.** Never write API references, guides, or generated READMEs to another location. (`README.md` itself stays at the project root, per convention — everything else generated goes in `/docs`.)
2. **`generate` never invents content.** It only writes docs from what `collect` gathered (or equivalent detail the user supplies directly in the conversation) — never from assumed signatures, assumed env vars, or assumed behavior. If required detail is missing, `generate` says what's missing and asks or falls back to running `collect` first.
3. **Stack rules are looked up, never guessed.** Before writing any code-level doc (API reference, inline comments), load the matching file under `memory/stacks/` for the language/framework actually in use. Do not mix PHPDoc conventions into a TypeScript file or vice versa.
4. **`docsify` only organizes and publishes what's already in `/docs`.** It never authors new documentation content — that's `generate`'s job. Always include `alias: { '/.*/_sidebar.md': '/_sidebar.md' }` and root-relative leading slashes `/` in `_sidebar.md` to guarantee persistent sidebar navigation across all subfolder routes. Never link to relative `../` files outside `/docs` to prevent 404 errors.
5. **Standalone.** This skill does not read or depend on any other `tidyfactor-*` skill's conventions, even when the project happens to be built on one of those tracks.
6. **Zero Sensitive Data Leakage.** Under absolutely no circumstances should any real sensitive data (e.g., real API tokens, WHM/cPanel passwords, production server IPs, real DB credentials, secret keys, private auth tokens, or local absolute drive paths) be written into documentation. ALWAYS redact and replace these with safe generic placeholders (e.g., `EXAMPLE_TOKEN_1234567890ABCDEFGH`, `203.0.113.50`, `your_secret_password`, `/path/to/project`).
7. **Clean Relative Links Only.** Never include local machine filesystem URLs (such as `file:///C:/...`, `file:c:`, or absolute workstation paths) in documentation links or markdown cross-references. All document cross-links must use clean relative markdown paths (e.g., `./guides/architecture.md`, `../api/auth.md`, `/api/auth.md`) or standard public web URLs (`https://...`).

## Sequencing

`init` → `collect` → `generate` (repeatable, once per doc target) → `docsify` (optional, once /docs has real content). Running `generate` before `collect` (or before the user has supplied equivalent detail inline) violates constraint 2 above.
