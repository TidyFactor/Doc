# Workflow: generate-inline

One outcome: source files in the target with inline documentation comments added or brought up to date, per the matching stack file's conventions. This workflow edits source directly — it does not write anything under `/docs`.

## Steps

1. **Load the findings** from `docs/.collected/<target>.md`, specifically the code-parsing section (what's already documented) and the error-patterns section (what exceptions/failure modes need noting).
2. **Load the comment convention** from the matching stack file — PHPDoc block format for PHP, JSDoc for JS, TSDoc for TS, component-comment conventions for React/Vue/Next.
3. **For each undocumented (or stale-documented) public function/method/class/component in the target**, add or correct a doc comment: purpose, parameters, return value, thrown/handled errors. Leave already-correct existing comments untouched — this is additive/corrective, not a rewrite of the file.
4. **Do not touch private/internal implementation details** that don't need a doc comment per the stack convention — inline documentation targets the public surface, not every line.
5. **Update `docs/.doc-manifest.json`**'s `generated` section, listing the files touched (not a `/docs` file, but still tracked for audit purposes).

## Validation

- [ ] Every added/updated comment follows the target stack's exact convention (tag names, block format)
- [ ] No comment content is invented — parameters, return types, and error conditions match the actual code and the findings
- [ ] Already-correct existing comments were left untouched
- [ ] Only public surface area was documented, not every internal line
- [ ] `docs/.doc-manifest.json`'s `generated` section lists the touched files
