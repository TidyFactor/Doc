# Command: adr

Runtime entry point for "Generate Architectural Decision Record (ADR)" / "وثق قرار معماري" / "قم بتوليد سجل قرار معماري يشرح سبب اختيار التقنية [X]".

## Context-Aware Prompts & Auto-Sensing

1. **Auto-Sense Project Context**:
   - Inspect package manifests (`composer.json`, `package.json`, `go.mod`, `Cargo.toml`) and framework configs.
   - Identify active language, runtime version, and primary dependencies.
   - Check `docs/adr/` to discover existing records and determine the next sequence number (`NNNN`).

2. **Extract Decision Parameters**:
   - Technology / Decision subject: e.g. `[VitePress]`, `[Medoo ORM]`, `[SQLite Storage]`, `[TailAdmin]`.
   - If not provided in the user prompt, evaluate recent commit history (`git log -n 10`) or prompt the user via the native modal question tool.

3. **Dispatch to Workflow**:
   - Load `../workflows/generate-adr.md` — the MADR decision-making workflow.
   - Load `../memory/adr-template.md` — the authoritative Markdown ADR schema.
   - Load `../memory/tone-of-voice.md` — technical objectivity and zero fluff policy.
   - Run the workflow.

## Does NOT

- Does not guess technical justifications: facts must trace to actual codebase constraints, benchmarks, or requirements.
- Does not edit application code: ADRs are purely architectural documentation saved under `docs/adr/`.
