# Workflow: docsify

One outcome: `/docs` is browsable as a Docsify site — an `index.html` entry point and an auto-generated `_sidebar.md`, wired per `memory/docsify-config.md`.

## Steps

1. **Write `docs/index.html`** using the template in `memory/docsify-config.md` — project name, theme, and the plugin list from that file. Do not hand-roll a different Docsify setup.
2. **Generate `docs/_sidebar.md`** by walking the current `/docs` tree per `doc-tree.md`'s structure and listing every existing generated file (skip `.doc-manifest.json` and the `.collected/` folder — those aren't site content). Group by section (API, Guides, root docs) matching the folder structure.
3. **Optionally write `docs/_coverpage.md`** if the user wants a landing/cover page — only if asked, per `docsify-config.md`'s note that the coverpage is opt-in, not default.
4. **Report how to preview it** (local static server command from `docsify-config.md`) and note the deploy targets listed there (GitHub Pages / Netlify / Cloudflare Pages / cPanel static hosting) without picking one — that's the user's call.

## Validation

- [ ] `docs/index.html` exists and matches the template/plugin list in `memory/docsify-config.md`
- [ ] `docs/_sidebar.md` lists every current doc under `/docs`, correctly grouped, and excludes `.doc-manifest.json`/`.collected/`
- [ ] All sidebar links use root-relative leading slashes (`/guides/...`, `/api/...`) and never point outside `/docs` (no `../` or `file:///` links)
- [ ] No real secrets or sensitive server configurations are hardcoded into `docs/index.html` or navigation files
- [ ] No new documentation *content* was authored by this workflow — only navigation/entry-point files
- [ ] Preview instructions and deploy target options were reported, with no deploy target chosen unilaterally
