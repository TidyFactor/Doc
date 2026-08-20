# Command: collect

Runtime entry point for "document this codebase" / "gather what's needed to document X."

## Dispatch steps

1. Load `../memory/collection-sources.md` — the five collection dimensions and what to extract from each.
2. Load `../workflows/collect.md` — the ordered interview/extraction sequence.
3. Run the workflow against the target codebase (or the specific slice of it the user named — a single module, endpoint, or component).

## Does NOT

- Does not write any files under `/docs`. `collect`'s output is structured source material (findings written to `docs/.collected/<target>.md`, per `collect.md`'s own step) — not a finished doc.
- Does not load `memory/doc-templates.md` or any `memory/stacks/*.md` file — formatting the findings into a stack-correct doc is `generate`'s job, not this one.
- Does not require `init` to have run first, but if `docs/.doc-manifest.json` doesn't exist yet, say so and offer to run `init` first rather than silently creating an ad hoc structure.
