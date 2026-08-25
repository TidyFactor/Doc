# Command: mkdocs

Runtime entry point for "set up MkDocs" / "build MkDocs Material site" / "compile static documentation".

## Dispatch steps

1. Load `../memory/mkdocs-config.md` — master YAML schema, theme tokens, extensions, i18n rules, and deploy options.
2. Load `../workflows/mkdocs.md` — the setup and build sequence.
3. Confirm `/docs` has real content.
4. Run `workflows/mkdocs.md`.

## Does NOT

- Does not author new documentation content — it generates `mkdocs.yml`, configures themes, and compiles the static site.
- Does not modify source markdown semantics, only removes incompatible raw HTML wrappers.
