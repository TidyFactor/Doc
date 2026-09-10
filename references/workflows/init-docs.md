# Workflow: init-docs

One outcome: a working `/docs` scaffold plus an aligned doc manifest, ready for `collect` and `generate` to populate.

---

## 📋 Step 0: Context Delta Resolution (CDL v2.0)

Before prompting the user for documentation configuration, execute the mechanical resolution formula:

$$\text{Unknowns} = \text{Required Decisions} - (\text{Discovered Facts} \cup \text{Brain KIs})$$

1. **Auto-Sensing on Disk**:
   - `doc_engine`: Check for existing `mkdocs.yml` (selects `mkdocs_material`) or `docs/index.html` (selects `docsify_spa`). If neither exists, default to `mkdocs_material`.
   - `target_scope`: Check project structure or `docs/.doc-manifest.json` (defaults to `full_codebase`).
   - `audience_persona`: Read `brand.yaml` (or fallback `brand.json`) for `audience` / persona. If absent, default to `bilingual_developer`.
   - For file sources marked with `track_staleness: true`, compare file hash/mtime against `.tidyfactor/doc-brief.snapshot.yaml`.
2. **Fail-Open Brain MCP Acceleration**:
   - Query `search_knowledge_base(query="documentation stack audience", scope="project")`.
   - If Brain MCP is offline or returns empty, fail open silently (0ms latency penalty).
3. **Structured Interactive Disclosure (DM-DA Mode A)**:
   - Present any genuine $\text{Unknowns}$ in a crisp, non-robotic prompt with clear A/B/C/D choices and recommended defaults.
   - Zero robotic preambles or lectures.
4. **Local Snapshot Persistence (Anti-Dual-Write)**:
   - Persist confirmed parameters to `.tidyfactor/doc-brief.snapshot.yaml`.

---

## 🛠️ Execution Steps

1. **Detect the stack(s) present** in the project root — PHP (`composer.json`), JS/TS (`package.json`, `tsconfig.json`), and any of React/Vue/Next (framework deps or config files). Note more than one if the project is mixed (e.g., a PHP API with a React front end).
2. **Create the folder tree** exactly per `memory/doc-tree.md` — no extra top-level folders, no missing ones. Do not create a folder for a doc type the project doesn't have yet (e.g., skip `docs/api/` for a project with no API surface) — see the "No Empty Structures" note in `doc-tree.md`.
3. **Write `docs/.doc-manifest.json`** using the schema in `memory/doc-tree.md`, pre-filled with: detected stack(s), project name (from `composer.json`/`package.json`), confirmed engine/audience from Step 0, and empty `collected` / `generated` tracking sections.
4. **Write a placeholder `docs/README.md` index** (one paragraph: what this `/docs` folder contains, and a note that it's generated/maintained by TidyFactor Doc) — this is the doc-site landing page, distinct from the project-root `README.md`.
5. **Report** what was created and what stack(s) were detected, and suggest `collect` as the next step.

## Validation checklist

- [ ] Evaluated Context Delta Resolution formula before prompting user
- [ ] Local decision snapshot persisted to `.tidyfactor/doc-brief.snapshot.yaml`
- [ ] `/docs` exists with only the subfolders `doc-tree.md` calls for given the detected stack(s) — nothing extra, nothing missing
- [ ] `docs/.doc-manifest.json` exists, is valid JSON, and matches the schema in `memory/doc-tree.md`
- [ ] `docs/README.md` (doc-site index) exists and is distinct in content from any project-root `README.md`
- [ ] No API/inline/guide content was written — this workflow scaffolds only
