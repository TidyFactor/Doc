# Workflow: generate-adr

One outcome: an Architectural Decision Record saved to `docs/adr/NNNN-<slug>.md` and indexed in `docs/adr/README.md`, adhering to the MADR (Markdown Architectural Decision Records) standard.

## Steps

1. **Initialize ADR Directory & Determine Sequence**:
   - Ensure `docs/adr/` exists.
   - Scan existing files matching `docs/adr/NNNN-*.md`.
   - Calculate next number: `0001` if empty, or increment highest existing number (e.g. `0002`, `0003`).

2. **Establish Context & Problem Statement**:
   - State the technical context clearly: What engineering problem or architectural need forced a decision?
   - Identify Decision Drivers: Performance, developer experience, zero-runtime overhead, license compatibility, RTL support, security.

3. **Formulate Considered Options**:
   - List at least 2–3 viable alternatives (e.g. VitePress vs. MkDocs Material vs. Docsify; Medoo vs. Doctrine vs. Eloquent).
   - For every option, provide an objective Pros & Cons analysis based on verifiable engineering facts.

4. **Document Decision Outcome & Rationale**:
   - Selected option: `Chosen option: [Option Name], because [positive arguments]`.
   - Explain why alternatives were rejected without emotional bias.

5. **Map Consequences & System Impact**:
   - **Positive consequences**: Capabilities gained, performance improvements, simplified maintenance.
   - **Negative consequences / Trade-offs**: Learning curve, dependencies introduced, migration effort.
   - **Mitigation plan**: How trade-offs will be handled.

6. **Write ADR & Update Index**:
   - Write file `docs/adr/NNNN-<slug>.md` using `memory/adr-template.md`.
   - Update `docs/adr/README.md` table of contents with status, title, and date.
   - Run `python scripts/audit_docs.py docs/adr/` to verify link and credential hygiene.

## Validation checklist

- [ ] ADR file exists at `docs/adr/NNNN-<slug>.md` with 4-digit sequential numbering.
- [ ] Conforms strictly to MADR structure in `memory/adr-template.md`.
- [ ] At least two realistic alternatives were evaluated with pros/cons.
- [ ] Tone conforms to `memory/tone-of-voice.md` (objective, technical, zero marketing fluff).
- [ ] `docs/adr/README.md` index includes the new record.
- [ ] Audited with `python scripts/audit_docs.py docs/adr/` and passed 100/100.
