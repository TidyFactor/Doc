# Workflow: mkdocs

One outcome: A fully compiled, statically hosted MkDocs Material documentation portal configured per `memory/mkdocs-config.md`.

---

## Steps

1. **Verify Environment & Dependencies:**
   - Run `python --version` and ensure Python is accessible.
   - Write `requirements.txt` containing `mkdocs-material>=9.5` and `mkdocs-static-i18n>=1.2`.
   - Install dependencies via `pip install -r requirements.txt` if not already installed.

2. **Structure `/docs` Source Tree:**
   - Ensure documentation markdown files live in `docs/` (e.g. `docs/index.md`, `docs/guides/`, `docs/api/`).
   - If bilingual, ensure Arabic files use the `.ar.md` suffix (e.g., `docs/guides/topic.ar.md`).
   - Strip any raw `<div align="center">` wrappers around Markdown headers so Python-Markdown parses them cleanly.

3. **Generate Configuration (`mkdocs.yml`):**
   - Write `mkdocs.yml` at the documentation root using the schema in `memory/mkdocs-config.md`.
   - Configure site name, palette themes (`tidyfactor-light` and `tidyfactor-dark`), PyMdown extensions, and the `nav:` tree mirroring `/docs`.

4. **Inject Luxury Styling & JS Enhancers:**
   - Create `docs/stylesheets/extra.css` with Neo-Brutalist tokens, macOS terminal dots for code blocks, and Arabic font pairings (`El Messiri` + `Tajawal`).
   - Create `docs/javascripts/extra.js` with the GitHub alert transformer and badge bar formatter.

5. **Build & Validate:**
   - Run `mkdocs build --strict` to ensure 0 warnings and 0 broken links.
   - If hosting locally on Apache, inject `.htaccess` with transparent rewrite rules pointing to `site/`.

6. **Report Deployment Instructions:**
   - Report local preview command: `mkdocs serve` (runs at `http://127.0.0.1:8000`).
   - Report production deploy rule: upload the generated contents of `site/` directly into the public server directory.

---

## Validation Checklist

- [ ] `mkdocs.yml` exists with valid YAML syntax and complete `nav:` mapping
- [ ] `docs/index.md` exists and contains no unparsed raw HTML header wrappers
- [ ] `docs/stylesheets/extra.css` and `docs/javascripts/extra.js` are present
- [ ] `mkdocs build` completes with **zero errors and zero broken links**
- [ ] Language switcher functions properly between English and Arabic (if bilingual)
- [ ] Clean relative links only — no workstation paths (`file:///C:/...`) or hardcoded secrets
