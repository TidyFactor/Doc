# Command: site

Runtime entry point for "turn /docs into a doc site" / "publish documentation portal" / "set up documentation site".

## Dispatch steps

1. Load `../memory/site-engines.md` — comparison between VitePress, MkDocs Material, and Docsify.
2. Confirm `/docs` has real content (at least one generated doc beyond the scaffold).
3. **Interactive Engine Selection:**
   - Detect available runtimes: `node --version 2>&1` and `python --version 2>&1`.
   - If the user explicitly requested a specific engine (e.g., "use vitepress", "use mkdocs", or "use docsify"), route directly:
     - "vitepress" → Dispatch `references/commands/vitepress.md`.
     - "mkdocs" → Dispatch `references/commands/mkdocs.md`.
     - "docsify" → Dispatch `references/commands/docsify.md`.
   - If no engine was specified:
     - Present the options to the user with the summary from `memory/site-engines.md`:
       - **Option 1: VitePress (Recommended for Modern Web, Monorepos & Luxury RTL)**: Vue 3 / Vite SSG, sub-second HMR, native multi-locale subdirectory routing (`/`, `/en/`, `/es/`), and bespoke luxury typography (`Alexandria` + `Cairo` + `JetBrains Mono`). Requires Node.js.
       - **Option 2: MkDocs Material (Recommended for Python & Backend Services)**: Pre-compiled static HTML, 100/100 Core Web Vitals, parallel builds, offline search indexing, and Neo-Brutalist styling. Requires Python.
       - **Option 3: Docsify (Zero-Build Lightweight SPA)**: Client-side SPA, zero build step, single `index.html` + `_sidebar.md` over CDN. Recommended when neither Node nor Python build workflows are available.
     - Prompt the user to pick their preference or proceed with the recommended engine based on detected toolchain.
4. Execute the chosen workflow (`workflows/vitepress.md`, `workflows/mkdocs.md`, or `workflows/docsify.md`).

## Does NOT

- Does not author any new markdown content — it structures, configures, and publishes what's already in `/docs`.
