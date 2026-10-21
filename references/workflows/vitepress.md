# Workflow: vitepress

One outcome: A fully compiled, statically hosted VitePress documentation portal with custom luxury typography, surgical RTL flex order, and multi-language routing configured per `memory/vitepress-config.md`.

---

## Steps

1. **Verify Environment & Dependencies:**
   - Run `node --version` (require >= 18).
   - Install VitePress: `npm install -D vitepress` (or verify package.json has `"vitepress": "^1.6.0"`).
   - Inject doc scripts into root `package.json`:
     ```json
     "scripts": {
       "docs:dev": "vitepress dev docs",
       "docs:build": "vitepress build docs",
       "docs:preview": "vitepress preview docs"
     }
     ```

2. **Scaffold Directory Tree & Assets:**
   - Ensure documentation markdown lives in `docs/`.
   - Create `docs/.vitepress/config.mjs` using the master schema in `memory/vitepress-config.md`.
   - Create `docs/.vitepress/theme/index.mjs` registering `custom.css`.
   - Copy brand logo to `docs/public/logo.png`.

3. **Configure Multi-Language Subdirectory Routing:**
   - Enforce dedicated subdirectories for every supported locale to eliminate 404s:
     - Arabic (Native Root): `docs/index.md`
     - English: `docs/en/index.md`
     - Additional growth locales: `docs/es/`, `docs/de/`, `docs/fr/`, `docs/pt/`, `docs/zh/`, `docs/fa/`.

4. **Inject Luxury CSS & RTL Precision:**
   - Write `docs/.vitepress/theme/custom.css` embedding Alexandria, Cairo, and JetBrains Mono fonts.
   - Configure surgical RTL navbar flex order:
     - Title/Logo (`order: 1`), Menu (`order: 2` with `margin-inline-end: auto`), Search (`order: 3`), Translations (`order: 4`), Appearance (`order: 5`), Social (`order: 6`).
   - Align Hero reading hierarchy: Text on the right (`order: 1`), Logo on the left (`order: 2`).
   - Protect Hero Action Buttons (CTAs): single-row layout (`flex-wrap: nowrap !important; white-space: nowrap !important`).
   - Fix 3-Column Feature Cards: explicitly size `.VPFeatures .item` (`width: 33.333333% !important`) and apply `direction: rtl !important; unicode-bidi: plaintext !important` to prevent text or parentheses inversion.

5. **Build & Validate:**
   - Run `npm run docs:build` (must complete with **zero errors and zero broken links**).

6. **Report Deployment Instructions:**
   - Local dev server: `npm run docs:dev` (runs at `http://localhost:5173`).
   - Production bundle: deploy the compiled output directory `docs/.vitepress/dist/`.

---

## Validation Checklist

- [ ] `docs/.vitepress/config.mjs` exists with valid ESM syntax and full locales configuration
- [ ] `docs/.vitepress/theme/custom.css` exists with Alexandria/Cairo fonts, single-row Hero CTAs, and 3-column card widths
- [ ] Hero layout in RTL displays text/CTAs on the right and logo on the left
- [ ] Every active locale index (`docs/index.md`, `docs/en/index.md`, etc.) exists on disk
- [ ] `npm run docs:build` compiles cleanly with **0 errors and 0 dead links**
- [ ] Clean relative links only — no machine workstation paths (`file:///C:/...`) or hardcoded secrets
