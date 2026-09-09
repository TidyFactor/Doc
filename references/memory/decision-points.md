# Memory: decision-points

<!-- last-verified: 2026-09-08 -->

Operational decision framework for documentation architecture and codebase interview governance. Enforces Contextual Decision Layer (CDL v2.0) and Dual-Mode Decision Architect (DM-DA) protocols.

---

## 🏛️ Decision Dimensions (D1–D5)

| Code | Decision Dimension | Options (Reference SSOT) | Default Fallback | Ambiguity / Trigger Condition |
|:---:|---|---|---|---|
| **D1** | **Documentation Purpose & Scope** | • `full_codebase` (Complete API surface + architecture guides)<br>• `api_surface_only` (Public exports, routes, and client SDKs)<br>• `internal_architecture` (Developer onboarding, ADRs, module contracts)<br>• `end_user_docs` (User guides, tutorials, setup walkthroughs) | `full_codebase` | When request asks to "document this project" without specifying audience or depth. |
| **D2** | **Publishing Platform Engine** | • `mkdocs_material` (Static HTML compilation, lunr offline search, bilingual i18n)<br>• `docsify_spa` (Zero-build client runtime SPA, instant markdown preview)<br>• `static_markdown` (Raw markdown files under `/docs` with root README) | `mkdocs_material` (if python available) / `docsify_spa` | When user has not configured `mkdocs.yml` or `docs/index.html`. |
| **D3** | **Target Persona & Linguistic Register** | • `bilingual_developer` (Arabic/English parallel guides, technical terminology)<br>• `api_consumer` (Strict English technical docs, contract signatures)<br>• `internal_maintainer` (Architecture rationale, git commit history context)<br>• `end_user` (Simplified bilingual non-technical user documentation) | `bilingual_developer` | When project has not specified language or target reader in `brand.yaml`. |
| **D4** | **Hygiene & Redaction Policy** | • `strict_zero_leak` (Mandatory automated regex masking of all IPs, DB passwords, API tokens)<br>• `public_sdk_redaction` (Scrub all internal routes, mock endpoints only)<br>• `internal_audit_permissive` (Permit local loopback `127.0.0.1` and dummy sample envs) | `strict_zero_leak` | Mandatory for all public or open-source documentation generation. |
| **D5** | **Collection Depth & Extraction Dimensions** | • `full_5_dimensions` (Source AST + Git commit rationale + Env vars + Personas + Error patterns)<br>• `signatures_and_types` (Public function/class docblocks only)<br>• `architecture_and_rationale` (Module boundaries, ADRs, and commit history) | `full_5_dimensions` | Decides computational depth of subsequent `collect` workflow. |

---

## 🧭 Dual Operational Modes (DM-DA)

```
[CDL v2.0 Protocol]
       │
       ▼
 Context Delta Resolution ──(Unknowns = ∅)──► Instant Baseline Confirmation
       │
       ├─► [MODE A] 🎯 Smart 3-Round Protocol (Deterministic alignment in 3 rounds)
       │         Round 1: Purpose & Target Audience
       │         Round 2: Engine & Architecture
       │         Round 3: Boundaries, Hygiene & Safe Defaults
       │         └── Escalation Gate: Confirm OR Escalate to Mode B
       │
       └─► [MODE B] 🔥 Relentless Debate & Interview (Debate Mode)
                 Continuous multi-turn interrogation challenging assumptions
                 Forces binary trade-offs (static vs SPA, brevity vs depth)
                 Terminates strictly on: "END DEBATE" / "اعتماد"
                 Emits: architectural_debate_synthesis.md
```

### [MODE A] 🎯 Smart 3-Round Protocol (الارتجال الذكي المقيد)
- **Round 1: Purpose & Scope (D1 + D3)**: Pinpoint primary documentation consumer and technical scope.
- **Round 2: Architecture & Engine (D2 + D5)**: Select publishing engine and depth of code extraction.
- **Round 3: Hygiene & Safe Defaults (D4 + Remaining)**: Enforce security scrubbing rules and apply defaults.
- **Strict Termination**: Finishes at Round 3, saves snapshot, and presents the Escalation Gate:
  > *"هل تعتمد هذه البنية المبدئية للبدء فوراً، أم تفضل تفعيل [نمط المناظرة 🔥 Debate Mode] لتفكيك الافتراضات واختبار صلابة الهيكلية التوثيقية؟"*

### [MODE B] 🔥 Relentless Debate & Interview (الاستجواب والمناظرة اللانهائية — Debate Mode)
- **Activation**: Direct `/debate`, or Mode A Round 3 escalation.
- **Behavior**:
  - Relentless multi-turn counter-questioning challenging documentation choices:
    - *"Why choose Docsify client-side SPA if SEO and offline indexability are critical for external developers?"*
    - *"Why document internal private methods if the primary goal is public API adoption?"*
    - *"How will the team prevent confidential server IPs and auth secrets from slipping into generated guides?"*
    - *"If the documentation is bilingual Arabic/English, how will code snippets and RTL UI callouts remain visually coherent without layout breakages?"*
  - Exposes anti-patterns: bloated doc sets nobody reads, duplicate API references, undocumented environment configurations.
  - Forces binary, uncompromising trade-offs.
- **Termination**: Ends **only** when user signals `"END DEBATE"` or `"اعتماد"`.
- **Deliverables**:
  - Generates formal synthesis: `docs/architectural_debate_synthesis.md`.
  - Persists confirmed parameters to `.tidyfactor/doc-brief.snapshot.yaml` and `.tidyfactor/doc-brief.md`.

---

## ⚡ Boolean Skip Conditions (Deterministic Bypass)

Skip interactive questioning and adopt safe defaults immediately if ANY condition is met:
1. **Existing Snapshot**: `.tidyfactor/doc-brief.snapshot.yaml` exists and `track_staleness` confirms zero file drift.
2. **Explicit User Declaration**: User specifies complete parameters in the prompt (e.g. *"Init MkDocs Material docs for public API with strict redaction"*).
3. **Direct Stack Command**: User calls specific engine commands directly (`/mkdocs` or `/docsify`).
4. **Maintenance Mode**: An audit (`audit_docs`) or validation run (`validate_skill.py`) preserves current configurations.
