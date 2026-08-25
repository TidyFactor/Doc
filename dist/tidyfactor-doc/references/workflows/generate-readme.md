# Workflow: generate-readme

One outcome: a project-root `README.md`, built from `docs/.collected/<target>.md` (target = whole project) and the README shape in `memory/doc-templates.md`. This is the one exception to "everything generated lives under /docs" — README stays at the project root, per convention.

## Steps

1. **Load the findings** from `docs/.collected/<target>.md`. If it doesn't exist for the whole project, stop — see constraint 2 in `SKILL.md`.
2. **Pull the README shape** from `memory/doc-templates.md`.
3. **Write `README.md`** at the project root: project name/one-line description, install/setup steps (from the runtime & environment findings), usage example, required env vars (with safe placeholders, never real secrets), and a clean relative link to `./docs/README.md` or `docs/` for the full reference. Keep it scannable — this is an entry point, not the full documentation.
4. **If a `README.md` already exists**, show a diff-style summary of what would change rather than overwriting silently, and confirm before replacing it.
5. **Update `docs/.doc-manifest.json`**'s `generated` section.

## Validation checklist

- [ ] `README.md` exists at project root and follows the shape in `memory/doc-templates.md`
- [ ] Every setup/env-var claim traces to the runtime & environment findings — nothing assumed
- [ ] Zero real secrets, API keys, or passwords in environment variable tables or examples
- [ ] Existing `README.md` content was never silently overwritten without confirmation
- [ ] Links to `docs/` are clean relative links (`./docs/README.md`), never local absolute drive paths or `file:///` URLs
- [ ] `docs/.doc-manifest.json` updated
