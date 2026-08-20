# Workflow: init-docs

One outcome: a working `/docs` scaffold plus a doc manifest, ready for `collect` and `generate` to populate.

## Steps

1. **Detect the stack(s) present** in the project root — PHP (`composer.json`), JS/TS (`package.json`, `tsconfig.json`), and any of React/Vue/Next (framework deps or config files). Note more than one if the project is mixed (e.g., a PHP API with a React front end).
2. **Create the folder tree** exactly per `memory/doc-tree.md` — no extra top-level folders, no missing ones. Do not create a folder for a doc type the project doesn't have yet (e.g., skip `docs/api/` for a project with no API surface) — see the "No Empty Structures" note in `doc-tree.md`.
3. **Write `docs/.doc-manifest.json`** using the schema in `memory/doc-tree.md`, pre-filled with: detected stack(s), project name (from `composer.json`/`package.json`), and empty `collected` / `generated` tracking sections.
4. **Write a placeholder `docs/README.md` index** (one paragraph: what this `/docs` folder contains, and a note that it's generated/maintained by TidyFactor Doc) — this is the doc-site landing page, distinct from the project-root `README.md`.
5. **Report** what was created and what stack(s) were detected, and suggest `collect` as the next step.

## Validation

- [ ] `/docs` exists with only the subfolders `doc-tree.md` calls for given the detected stack(s) — nothing extra, nothing missing
- [ ] `docs/.doc-manifest.json` exists, is valid JSON, and matches the schema in `memory/doc-tree.md`
- [ ] `docs/README.md` (doc-site index) exists and is distinct in content from any project-root `README.md`
- [ ] No API/inline/guide content was written — this workflow scaffolds only
