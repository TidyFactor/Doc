# Command: audit

Runtime entry point for "audit docs quality" / "scan documentation hygiene" / "check broken doc links" / "verify changelog structure."

## Dispatch steps

1. Identify the target path to audit (defaults to `docs/` and root `README.md`, `CHANGELOG.md` if not explicitly specified).
2. Load `../workflows/audit.md` — the step-by-step documentation quality audit sequence.
3. Run the workflow.

## Does NOT

- Does not rewrite or author documentation files automatically without user review.
- Does not publish documentation sites (that's `site` / `mkdocs` / `docsify` / `vitepress`).
- Does not modify code or package configurations.
