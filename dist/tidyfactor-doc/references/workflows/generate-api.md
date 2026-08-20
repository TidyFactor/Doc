# Workflow: generate-api

One outcome: an API reference file under `docs/api/` for one target, built from `docs/.collected/<target>.md` and formatted per the matching `memory/stacks/*.md` file.

## Steps

1. **Load the findings** from `docs/.collected/<target>.md`. If it doesn't exist, stop — see constraint 2 in `SKILL.md`.
2. **Pull the doc-type shape** from `memory/doc-templates.md` (API reference section) and the **comment/tag conventions** from the matching stack file — PHPDoc tags for PHP, JSDoc for JS, TSDoc for TS, or component prop-table conventions for React/Vue/Next.
3. **Write `docs/api/<target>.md`**: for every public function/method/endpoint/component found in the findings, document signature, parameters (with types), return value, thrown errors (from the "error patterns" findings), and a short usage example. Prioritize facts an **API consumer** needs (per the persona-tracing findings) over internal rationale. Ensure code examples use dummy/placeholder tokens and endpoints, never real secrets.
4. **Cross-link**: if the target has related targets already documented, add clean relative "See also" links between them (e.g. `[Other API](./other.md)`). Never use `file:///` or local drive paths.
5. **Update `docs/.doc-manifest.json`**'s `generated` section with the new file and timestamp.

## Validation

- [ ] `docs/api/<target>.md` exists and follows the API-reference shape in `memory/doc-templates.md`
- [ ] Every documented signature matches what `collect` actually found — no invented parameters or return types
- [ ] Comment/tag style matches the target's stack file exactly (no PHPDoc tags in a TS doc, etc.)
- [ ] Zero sensitive data leaked (all auth tokens, secrets, private IPs replaced with generic placeholders)
- [ ] All cross-references use clean relative markdown paths or web URLs; zero `file:///` or local absolute drive paths
- [ ] Thrown/returned error conditions from the findings are represented
- [ ] `docs/.doc-manifest.json` updated
