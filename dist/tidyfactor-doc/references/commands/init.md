# Command: init

Runtime entry point for "set up docs for this project" / "scaffold /docs."

## Dispatch steps

1. Load `../memory/doc-tree.md` — the canonical `/docs` folder shape and the doc-manifest schema.
2. Load `../workflows/init-docs.md` — the scaffolding sequence.
3. Run the workflow.

## Does NOT

- Does not write any actual documentation content (no API entries, no guide prose). That's `generate`.
- Does not run `collect`. If the user wants both, run `init` first, then hand off to `collect`.
- Does not load any `memory/stacks/*.md` file — stack detection here only decides which manifest fields to pre-fill, not how to document anything yet.
