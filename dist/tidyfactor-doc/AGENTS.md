# AGENTS.md — TidyFactor Doc Governance Rules

This file governs all AI coding agents working on or with `tidyfactor-doc`.

## Core Invariants
1. **SSOT Rule:** `tidyfactor-doc` in `c:\wamp64\www\TidyFactor\Skills\Skills-LAB\tidyfactor-doc\` is the single source of truth.
2. **Docs in `/docs` Only:** Generated documentation artifacts MUST live under `/docs` (except root `README.md`).
3. **No Assumed Details:** `generate` never invents facts or env vars not gathered during `collect`.
4. **Docsify Persistence:** Always generate `alias: { '/.*/_sidebar.md': '/_sidebar.md' }` and root-relative paths.
5. **SemVer SSOT:** All changes must bump version and update `CHANGELOG.md`.
