# Command: docsify

Runtime entry point for "turn /docs into a doc site" / "set up Docsify."

## Dispatch steps

1. Load `../memory/docsify-config.md` — file layout, plugin defaults, sidebar-generation rule, deploy targets.
2. Load `../workflows/docsify.md` — the setup sequence.
3. Confirm `/docs` already has real content (at least one generated doc beyond the scaffold). If `/docs` is still empty or placeholder-only, say so and suggest running `collect` + `generate` first rather than standing up a site with nothing in it.
4. Run the workflow.

## Does NOT

- Does not author any new page content — it wires up navigation (`_sidebar.md`), an entry point (`index.html`), and optionally a cover page over whatever already exists in `/docs`.
- Does not load `memory/doc-templates.md` or any `memory/stacks/*.md` file — content formatting isn't this command's concern.
