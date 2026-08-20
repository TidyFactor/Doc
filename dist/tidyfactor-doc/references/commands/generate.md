# Command: generate

Runtime entry point for "write API docs" / "generate a README" / "add inline comments" / "write a guide." A router within a router: figure out which doc type is wanted, then load exactly one workflow for it.

## Dispatch steps

1. **Identify the doc type.** If not obvious from the request, ask:
   > "Which one — API reference, README, inline code comments, or a technical guide (setup/architecture/workflow)?"
2. **Identify the stack** (PHP / JS / TS / React / Vue / Next). If not obvious from the project, ask or detect from file extensions / config files (`composer.json`, `package.json` + `tsconfig.json`, framework config files).
3. Load the matching workflow — exactly one:
   - API reference → `../workflows/generate-api.md`
   - README → `../workflows/generate-readme.md`
   - Inline comments → `../workflows/generate-inline.md`
   - Guide → `../workflows/generate-guide.md`
4. Load `../memory/doc-templates.md`.
5. Load the matching stack file under `../memory/stacks/` — `php.md`, `js-ts.md`, or `react-vue-next.md`. Never load more than the stacks actually present in the target.
6. Confirm `collect` has already run for this target (check for `docs/.collected/<target>.md`). If it hasn't, and the user hasn't supplied equivalent detail inline, stop and say so — do not generate from assumption. See constraint 2 in `SKILL.md`.
7. Run the loaded workflow.

## Does NOT

- Does not load more than one `workflows/generate-*.md` file per invocation. Multiple doc types requested at once → run this dispatch sequence once per type, sequentially.
- Does not load `memory/collection-sources.md` or `memory/docsify-config.md` — not this command's concern.
