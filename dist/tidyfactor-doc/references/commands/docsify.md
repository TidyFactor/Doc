# Command: docsify

Runtime entry point for "turn /docs into a doc site" / "set up Docsify (Zero-Build SPA)."

## Dispatch steps

1. Load `../memory/docsify-config.md` — file layout, plugin defaults, sidebar-generation rule, deploy targets.
2. Load `../workflows/docsify.md` — the setup sequence.
3. Confirm `/docs` already has real content (at least one generated doc beyond the scaffold).
4. Run `workflows/docsify.md`.

## Does NOT

- Does not author any new page content — it wires up navigation (`_sidebar.md`), an entry point (`index.html`), and optionally a cover page over whatever already exists in `/docs`.
- Does not load `memory/doc-templates.md` or any `memory/stacks/*.md` file.
