# Workflow: collect

One outcome: a structured findings file — `docs/.collected/<target>.md` — that `generate` can turn into any doc type without re-deriving facts from the codebase itself. `<target>` is the module, package, API surface, or component named by the request (or the whole project if none was named).

## Steps

Run all five collection dimensions from `memory/collection-sources.md` against the target. Skip a dimension only if it genuinely doesn't apply (e.g., no Git history available for an uploaded snapshot) — note the skip and why, don't silently omit it.

1. **Code parsing.** Extract existing docblocks/comments, function/method/class signatures, exported types, and public surface area directly from source. Flag anything already documented inline so `generate` doesn't duplicate it.
2. **Commit history.** Read `git log` and any available PR descriptions for the target's files. Pull out *why* behind non-obvious code — rationale, past bugs fixed, deliberate tradeoffs — not just *what* changed.
3. **Runtime & environment.** Enumerate required environment variables, config files, software dependencies (with version constraints), and any stated hardware/resource limits. **MANDATORY**: Scrub and redact any actual secrets, production server IPs, database passwords, or private API tokens found in `.env` or config files—record only variable names, expected formats, and generic placeholder values.
4. **User persona tracing.** Identify who actually reads docs for this target — API consumers, internal maintainers, end-users — and note which facts matter to which persona (an internal maintainer needs the "why"; an API consumer needs the contract).
5. **Error patterns.** Collect how the code fails: thrown exceptions, error codes, logged failure messages, and how each is meant to be handled or surfaced. Scrub any sensitive runtime credentials or local workstation paths that appear inside logged messages.

6. **Write the findings** to `docs/.collected/<target>.md` as plain structured notes under five headings matching the dimensions above — this is source material for `generate`, not a finished doc, so skip prose polish.
7. **Update `docs/.doc-manifest.json`**: add `<target>` to the `collected` section with a timestamp.

## Validation

- [ ] `docs/.collected/<target>.md` exists and has content (or an explicit "not applicable" note) under all five dimension headings
- [ ] Every fact traces to something actually found in the code, history, config, or logs — nothing inferred or assumed
- [ ] Zero sensitive data leaked: all real API keys, passwords, private IPs, and secrets are replaced with safe generic placeholders
- [ ] No local workstation drive paths (`C:\...`, `file:///...`) exist in findings; all paths are normalized to project-relative paths
- [ ] `docs/.doc-manifest.json`'s `collected` section includes `<target>`
- [ ] Findings are organized by dimension, not pre-formatted as any particular doc type
