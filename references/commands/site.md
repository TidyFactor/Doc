# Command: site

Runtime entry point for "turn /docs into a doc site" / "publish documentation portal" / "set up documentation site".

## Dispatch steps

1. Load `../memory/site-engines.md` — comparison between MkDocs Material and Docsify.
2. Confirm `/docs` has real content (at least one generated doc beyond the scaffold).
3. **Interactive Engine Selection:**
   - Detect if Python is available via `python --version 2>&1`.
   - If the user explicitly requested a specific engine (e.g., "use mkdocs" or "use docsify"), route directly:
     - "mkdocs" → Dispatch `references/commands/mkdocs.md`.
     - "docsify" → Dispatch `references/commands/docsify.md`.
   - If no engine was specified:
     - Present the two options to the user with the summary from `memory/site-engines.md`:
       - **Option 1: MkDocs Material (Recommended for Production)**: Pre-compiled static HTML, 100/100 Core Web Vitals, bilingual (Arabic RTL + English LTR) parallel builds, offline search indexing, and Neo-Brutalist styling. Requires Python locally for building.
       - **Option 2: Docsify (Zero-Build Lightweight SPA)**: Client-side SPA, zero build step, single `index.html` + `_sidebar.md` over CDN. Recommended when Python is not available or for internal repo prototyping.
     - Prompt the user to pick their preference or proceed with the recommended engine based on detected toolchain.
4. Execute the chosen workflow (`workflows/mkdocs.md` or `workflows/docsify.md`).

## Does NOT

- Does not author any new markdown content — it structures, configures, and publishes what's already in `/docs`.
