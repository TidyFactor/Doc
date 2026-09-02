<!-- last-verified: 2026-09-02 -->
# Memory: Site Engines (Docsify vs. MkDocs Material)

Technical evaluation matrix for documentation publishing engines supported by `tidyfactor-doc`.

## Engine Comparison Matrix

| Capability / Factor | ⚡ MkDocs Material (Static Compiler) | 📄 Docsify (Client-Side SPA) |
|---|---|---|
| **Architecture** | Static Site Generator (Python Markdown) | Client-Side SPA (`marked.js` in browser) |
| **Output Type** | Pre-rendered static HTML (`site/`) | Single `index.html` fetching `.md` via AJAX |
| **Build Dependency** | Python 3.10+, `pip install mkdocs-material` | Zero build step, zero compiler required |
| **SEO & Crawlers** | 100/100 Perfect static HTML indexing | Limited (requires JS execution by bots) |
| **Performance & CWV** | Instant initial paint, pre-cached assets | Client-side fetch delay on slow mobile networks |
| **i18n & Localization** | Native parallel builds (`/` and `/ar/`) via `mkdocs-static-i18n` | Single page language or manual separate SPAs |
| **Search Engine** | Lunr.js pre-indexed offline search (bilingual) | In-browser client-side fuzzy search |
| **Styling & Theming** | Material for MkDocs + Neo-Brutalist CSS tokens | Custom CSS over Docsify default theme |
| **Code Highlighting** | Pygments build-time syntax highlighting + line spans | Prism.js client-side syntax highlighting |
| **Target Deployment** | Production doc portals, public SaaS products, multi-language sites | Rapid internal repo docs, single-file lightweight guides |

---

## Decision Logic & Recommendation Rules

1. **Choose MkDocs Material if:**
   - The documentation has more than 10 pages or complex multi-level hierarchy.
   - Public SEO visibility and search engine discoverability are critical.
   - The project is bilingual (Arabic RTL + English LTR) requiring dedicated language switches.
   - The local environment has Python installed (`python --version` returns 3.10+).
   - Production hosting supports static directory routing (`public_html/documentation/`).

2. **Choose Docsify if:**
   - The developer or server environment has **no Python runtime** and requires zero installation.
   - The project needs an instant browsable site by dropping a single `index.html` into `/docs`.
   - The documentation is primarily for internal developers within a repository.
   - The site is hosted on GitHub Pages with zero CI build workflows.

---

## Two-Tier Multi-Language Documentation Pattern

Both engines adhere to the TidyFactor Two-Tier Documentation standard:
- **Canonical Technical SSOT**: Full API specifications, architecture, and code deep-dives maintained in Canonical English (`/docs/en/` or root) with First-Class Arabic (`/docs/ar/`).
- **Localized Adoption Guides**: Quickstarts, tutorials, concepts, and command matrices for Tier 1/2 growth languages (`es`, `pt`, `fa`, `zh`, `de`, `fr`) providing high-conversion onboarding.

---

## Toolchain Verification Command

```bash
# Check if Python is available for MkDocs
python --version 2>&1 || python3 --version 2>&1
```
- If Python is available: recommend **MkDocs Material** as primary production track.
- If Python is not available: recommend **Docsify** as zero-dependency fallback.
