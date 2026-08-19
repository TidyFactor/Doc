# Memory: collection-sources

The five dimensions `collect` runs against a target, and exactly what to pull from each. Operational — no rationale.

## 1. Code parsing

- Extract existing docblocks/comments verbatim (don't paraphrase yet — that's `generate`'s job).
- List every public function, method, class, exported type, and (for components) prop/slot/event definition.
- Note which of these already have adequate comments vs. none vs. stale (comment doesn't match current signature).

## 2. Commit history

- `git log --follow -- <path>` for the target's files: pull commit messages that explain *why*, not routine messages ("fix typo").
- Any available PR/MR descriptions touching the target: design decisions, rejected alternatives, known limitations mentioned by the author.
- Flag any TODO/FIXME/HACK comments found alongside — they're often undocumented known issues.

## 3. Runtime & environment

- Every environment variable the target reads (grep for `getenv`/`process.env`/`$_ENV`/config-loader calls), with whether it's required or optional and any default.
- Software dependencies and version constraints from the manifest (`composer.json`, `package.json`) that the target actually uses — not the whole project's dependency list.
- Any stated hardware/resource limits (memory limits, timeout values, rate limits) found in config or comments.

## 4. User persona tracing

- Classify the target's readership: **API consumer** (calls it from outside), **internal maintainer** (edits this code), **end-user** (uses a UI built on it), or a mix.
- For each persona present, note which facts from the other four dimensions matter to them — this list is what `generate` uses to prioritize content per doc type.

## 5. Error patterns

- Every thrown exception / returned error code / rejected promise in the target, with the condition that triggers it.
- How each error is meant to be handled or surfaced (caught and logged? bubbled to caller? shown to end-user?) — from code and any logging statements found.
- Common failure modes mentioned in commit history or TODO comments that aren't yet reflected in actual error handling.
