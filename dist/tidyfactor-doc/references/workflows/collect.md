# Workflow: collect

One outcome: a structured findings file — `docs/.collected/<target>.md` — that `generate` can turn into any doc type without re-deriving facts from the codebase itself. `<target>` is the module, package, API surface, or component named by the request (or the whole project if none was named).

---

## 📋 Step 0: Context Delta Resolution & Auto-Sensing

Before prompting the user for scope or parameters, execute the mechanical resolution formula:

$$\text{Unknowns} = \text{Required Decisions} - (\text{Discovered Facts} \cup \text{Brain KIs})$$

1. **Auto-Sensing on Disk**:
   - Inspect `mkdocs.yml`, `docs/index.html`, `docs/.doc-manifest.json`, and codebase structure.
   - For sources marked with `track_staleness: true`, compare hash/mtime against stored snapshot.
   - Any parameter resolved from disk is removed from $\text{Unknowns}$.

2. **Fail-Open Brain MCP Acceleration**:
   - Check if architecture KIs exist via `search_knowledge_base(query="architecture routes apis", scope="project")`.
   - If Brain MCP is absent, offline, or returns empty, proceed with 0ms delay directly to Step 1 without warnings.

---

## 🔍 Step 1: Codebase Collection Dimensions

Run all five collection dimensions from `memory/collection-sources.md` against the target:

1. **Code parsing**: Extract existing docblocks/comments, function/method/class signatures, exported types, and public surface area directly from source. Flag anything already documented inline.
2. **Commit history**: Read `git log` and available PR descriptions for target files. Pull out *why* behind non-obvious code (tradeoffs, rationale, bug fixes).
3. **Runtime & environment**: Enumerate required environment variables, config files, software dependencies (with version constraints), and resource limits. **MANDATORY**: Scrub and redact any actual secrets, production server IPs, database passwords, or private API tokens—record only variable names and generic placeholders.
4. **User persona tracing**: Identify who reads docs for this target (API consumers, internal maintainers, end-users) and map facts accordingly.
5. **Error patterns**: Collect how the code fails: thrown exceptions, error codes, logged failure messages, and resolution steps. Scrub local workstation paths.

---

## 💾 Step 2: Persist Findings & Outbound Push

1. Write structured notes to `docs/.collected/<target>.md` under five headings matching the dimensions above.
2. Update `docs/.doc-manifest.json` with `<target>` and timestamp.
3. Save local snapshot `.tidyfactor/doc-brief.snapshot.json` for deterministic drift detection.
4. **Anti-Dual-Write Outbound Push (`--sync-brain`)**:
   - Local markdown files are the sole Single Source of Truth.
   - When `--sync-brain` is explicitly provided, export extracted architecture facts to Brain MCP via `extract_knowledge_item`.

---

## ## Validation checklist

- [ ] Context Delta Resolution executed before prompting user.
- [ ] `docs/.collected/<target>.md` exists and has content under all five dimension headings.
- [ ] Every fact traces to verified code, history, config, or logs — zero hallucination.
- [ ] Zero sensitive data leaked: all real API keys, passwords, private IPs, and secrets replaced with generic placeholders.
- [ ] No local workstation drive paths (`C:\...`, `file:///...`) exist; all paths are normalized to project-relative paths.
- [ ] Deterministic audit passed via `python scripts/audit_docs.py docs/.collected/<target>.md`.
- [ ] `docs/.doc-manifest.json`'s `collected` section includes `<target>`.
- [ ] Findings organized by dimension, not pre-formatted as any particular doc type.
