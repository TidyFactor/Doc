<!-- last-verified: 2026-09-09 -->
# Memory: Site Engines (VitePress vs. MkDocs Material vs. Docsify)

Technical evaluation matrix for documentation publishing engines supported by `tidyfactor-doc`.

## Engine Comparison Matrix

| Capability / Factor | ⚡ VitePress (Vue 3 / Vite SSG) | 📦 MkDocs Material (Python Static) | 📄 Docsify (Client SPA) |
|---|---|---|---|
| **Architecture** | Static Site Generator (Vite + Vue 3 SSR) | Static Site Generator (Python Markdown) | Client-Side SPA (`marked.js`) |
| **Output Type** | Pre-rendered static HTML (`dist/`) + Vue hydration | Pre-rendered static HTML (`site/`) | Single `index.html` fetching `.md` |
| **Build Dependency** | Node.js >= 18, `npm i -D vitepress` | Python 3.10+, `pip install mkdocs-material` | Zero build step, zero compiler |
| **SEO & Crawlers** | 100/100 Perfect static HTML indexing | 100/100 Perfect static HTML indexing | Limited (requires bot JS execution) |
| **Performance & CWV** | Instant Vite dev server, sub-second HMR | High compilation speed, pre-cached assets | Client-side fetch delay on slow mobile |
| **i18n & Localization** | Native subdirectory routing (`/`, `/en/`, `/es/`) | Parallel builds via `mkdocs-static-i18n` | Single language or manual SPAs |
| **Search Engine** | Minisearch pre-indexed local search | Lunr.js pre-indexed offline search | In-browser client-side fuzzy search |
| **Styling & Theming** | Custom CSS tokens, Vue components, Luxury RTL | Material theme + Neo-Brutalist tokens | Custom CSS over Docsify default |
| **Code Highlighting** | Shiki build-time syntax highlighting | Pygments build-time syntax highlighting | Prism.js client-side syntax |
| **Target Deployment** | Modern JS/TS repos, SaaS portals, luxury RTL | Python/Backend repos, enterprise wikis | Internal quick prototyping, single guides |

---

## Decision Logic & Recommendation Rules

1. **Choose VitePress if (Recommended for Modern Web / Monorepos):**
   - The project is in the Node.js / TypeScript / Frontend ecosystem.
   - Requires custom interactive Vue components, modern UI aesthetics, or luxury typography (`Alexandria` + `Cairo` + `JetBrains Mono`).
   - Needs seamless multi-language subdirectory routing with zero 404s.
   - Developer desires sub-second Vite HMR during drafting.

2. **Choose MkDocs Material if:**
   - The project is Python-centric or backend-heavy.
   - The team is already using Python toolchains (`pip`, `virtualenv`).
   - The documentation requires MkDocs-specific plugin ecosystems.

3. **Choose Docsify if:**
   - The developer environment has neither Node.js nor Python build workflows.
   - The project needs an instant browsable site by dropping a single `index.html` into `/docs`.
   - The documentation is strictly internal within a small Git repository.

---

## Toolchain Verification Command

```bash
# Check available runtimes
node --version 2>&1
python --version 2>&1 || python3 --version 2>&1
```
- If Node.js is available: recommend **VitePress** as primary luxury web documentation portal.
- If Python is available without Node.js: recommend **MkDocs Material**.
- If no build runtime is available: recommend **Docsify** zero-dependency fallback.
