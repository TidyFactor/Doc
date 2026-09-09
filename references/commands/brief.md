# Command: brief

Runtime entry point for establishing documentation context, running codebase interview, or conducting architectural debate ("brief", "interview", "debate", "استجوبني", "ناقشني في معمارية التوثيق").

## Dispatch steps

1. Load `../memory/decision-points.md` — the 5 core documentation decision dimensions (D1–D5), operational modes (Mode A / Mode B), and boolean skip conditions.
2. Load `../workflows/brief.md` — the Context Delta Resolution, Dual Operational Mode execution, and persistence sequence.
3. Run the workflow.

## Does NOT

- Does not author actual documentation content (no API entries, no guides, no READMEs). That's `generate`.
- Does not scaffold `/docs` directory structure until baseline decisions are confirmed. That's `init`.
- Does not run code-level AST parsing or git history log collection. That's `collect`.
- Does not load `memory/stacks/*.md` or `memory/docsify-config.md` / `memory/mkdocs-config.md` — those are loaded only during generation or site compilation.
