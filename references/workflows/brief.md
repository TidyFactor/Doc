# Workflow: brief

One outcome: a validated documentation architectural brief and local snapshot, establishing all governance parameters before scaffolding or code parsing begins.

---

## 📋 Step 0: Context Delta Resolution (CDL v2.0)

Before querying the user, deterministically evaluate the Context Delta formula:

$$\text{Unknowns} = \text{Required Decisions} - (\text{Discovered Facts} \cup \text{Brain KIs})$$

1. **Local Auto-Sensing on Disk**:
   - Inspect `package.json`, `composer.json`, `tsconfig.json` for stack identification.
   - Check existing documentation markers (`mkdocs.yml`, `docs/index.html`, `docs/.doc-manifest.json`).
   - Read `brand.yaml` (fallback `brand.json`) for project name, audience, and license.
   - Check `.tidyfactor/doc-brief.snapshot.yaml`: if present and file hashes match (`track_staleness: true`), resolve all decisions immediately.
2. **Fail-Open Brain MCP Acceleration**:
   - Query `search_knowledge_base(query="documentation architecture", scope="project")`.
   - If Brain MCP is absent, disabled, or empty, proceed with 0ms silent fallback.
3. **Delta Evaluation**:
   - If $\text{Unknowns} = \emptyset$: Proceed immediately to Step 2 (persist snapshot) with zero conversational overhead.
   - If $\text{Unknowns} \neq \emptyset$: Proceed to Step 1 using the requested Operational Mode.

---

## 🧭 Step 1: Operational Mode Execution (Native Modal Wizard Contract)

> [!IMPORTANT]
> **Zero Static Text Questionnaires (`❌`)**:
> The agent is **STRICTLY FORBIDDEN** from outputting questions, choices, or debate trade-offs as plain written markdown text in the chat.
> The agent **MUST** invoke the platform's native interactive question tool (`ask_question` in Antigravity IDE) to render a structured modal wizard with selectable options and recommended defaults.

---

### [MODE A] 🎯 Smart 3-Round Protocol (الارتجال الذكي المقيد)
*Fast-track structured alignment via native modal wizards.*

- **Round 1: Purpose & Target Persona (D1 & D3)**:
  - Invoke `ask_question`:
    - Question 1: "ما هو النطاق الأساسي لتوثيق المشروع؟"
      Options: `"(Recommended) full_codebase — توثيق شامل للـ API والمعمارية وأدلة التشغيل"`, `"api_surface_only — توثيق نقاط النهاية وواجهات الـ API فقط"`, `"internal_architecture — توثيق المعمارية وتهيئة المطورين الداخليين"`, `"end_user_docs — أدلة استخدام مبسطة للمستخدم النهائي"`
    - Question 2: "ما هي شريحة القراء والتوجه اللغوي المستهدف؟"
      Options: `"(Recommended) bilingual_developer — توثيق فني ثنائي باللغتين العربية والإنجليزية"`, `"api_consumer — توثيق تقني صارم بالإنجليزية لمستهلكي الـ API"`, `"internal_maintainer — توثيق معطيات القرارات وسياق المطورين"`, `"end_user — توثيق مبسط لغير التقنيين"`
- **Round 2: Architecture & Engine (D2 & D5)**:
  - Invoke `ask_question`:
    - Question 1: "ما هو محرك نشر وعرض التوثيق المعتمد؟"
      Options: `"(Recommended) mkdocs_material — توليد موقع ثابت سريع مع بحث محلي ودعم ثنائي"`, `"docsify_spa — موقع تفاعلي فوري خفيف دون الحاجة لأي تجميع (Zero-Build)"`, `"static_markdown — ملفات Markdown خام قياسية تحت مجلد /docs"`
    - Question 2: "ما هو عمق الاستقراء البرمجي المطلوب من الكود؟"
      Options: `"(Recommended) full_5_dimensions — استقراء الأبعاد الخمسة (AST + Git History + Env + Personas + Errors)"`, `"signatures_and_types — مراجع الدوال والأنواع المصدرة فقط"`, `"architecture_and_rationale — المعمارية والحدود وسياق الـ Commits"`
- **Round 3: Hygiene & Safe Defaults (D4 & Escalation Gate)**:
  - Invoke `ask_question`:
    - Question: "ما هي سياسة حجب البيانات الحساسة والأمان؟"
      Options: `"(Recommended) strict_zero_leak — حظر وتطهير آلي صارم لكافة المفاتيح وكلمات المرور وعناوين IP"`, `"public_sdk_redaction — حجب المسارات الداخلية مع اعتماد مسارات محاكاة"`, `"internal_audit_permissive — السماح بعناوين Loopback المحلية وعينات التهيئة"`
  - **Escalation Gate (Modal Wizard)**:
    - Invoke `ask_question`:
      - Question: "اكتملت أبعاد التوثيق المبدئية. هل ترغب في اعتمادها فوراً أم تفعيل نمط المناظرة (Debate Mode) لتحدي القرارات؟"
      - Options: `"(Recommended) اعتماد البنية المبدئية والبدء فوراً في التوثيق"`, `"تفعيل نمط المناظرة المعمارية (Debate Mode)"`

---

### [MODE B] 🔥 Relentless Debate & Interview (الاستجواب والمناظرة اللانهائية — Debate Mode)
*Deep architectural interrogation via step-by-step interactive question modals.*

- **Trigger**: Command `/debate`, explicit user prompt ("مناظرة" / "استجوبني"), or escalation from Round 3 of Mode A.
- **Modal Interrogation Protocol**:
  - The agent poses **ONE architectural challenge at a time** strictly via `ask_question`.
  - The question title encapsulates the dilemma (e.g. *"معضلة الصيانة اللغوية: هل نعتمد أتمتة صارمة لكافة اللغات أم نحصر التحديث الحي في لغتين أساسيتين؟"*).
  - The options provide binary, concrete trade-offs with explicit costs:
    - Option 1: `"(Recommended) حصر التحديث الحي المستمر على اللغتين الأساسيتين (AR/EN) واعتماد ملخصات تنفيذية للغات الأخرى"`
    - Option 2: `"فرض أتمتة كاملة في الـ CI للغات الثماني بالتوازي مع إيقاف البناء عند أي نقص"`
  - Each selection by the user leads to the next focused counter-question via `ask_question` exploring dependency and edge cases.
- **Termination Constraint**: Continues turn-by-turn until the user explicitly selects an option marked `اعتماد القرارات المعمارية وإنهاء المناظرة` or types `"END DEBATE"` / `"اعتماد"`.
- **Debate Artifact**: Emits formal synthesis at `docs/architectural_debate_synthesis.md` capturing all settled decisions, discarded alternatives, and technical rationale.

---

## 💾 Step 2: SSOT Local Persistence & Outbound Push

1. **Write Local SSOT**:
   - Write `.tidyfactor/doc-brief.snapshot.yaml` with resolved keys, mtimes, and hashes.
   - Write `.tidyfactor/doc-brief.md` containing human-readable brief summary.
2. **Outbound Push (`--sync-brain`)**:
   - If `--sync-brain` flag was provided, invoke `extract_knowledge_item` to persist documentation metadata to sovereign Brain MCP.
   - Local files remain the authoritative Single Source of Truth.

---

## 🎯 Step 3: Handoff

- If `/docs` directory is uninitialized ➔ Hand off to `workflows/init-docs.md`.
- If `/docs` exists and documentation needs generation ➔ Hand off to `workflows/collect.md` followed by `workflows/generate-*.md`.

---

## Validation checklist

- [ ] Context Delta Resolution computed before asking user any questions
- [ ] No questions asked for facts already discoverable from disk
- [ ] All interactive questions in Mode A and Mode B were presented exclusively via native modal wizard (ask_question), with zero static text surveys in chat
- [ ] Followed selected mode (Mode A terminated at Round 3; Mode B terminated only on "END DEBATE" / "اعتماد")
- [ ] If Mode B was executed, generated `docs/architectural_debate_synthesis.md`
- [ ] Local snapshot persisted to `.tidyfactor/doc-brief.snapshot.yaml`
- [ ] Human-readable brief saved to `.tidyfactor/doc-brief.md`
- [ ] No actual doc pages or API references written during this workflow
