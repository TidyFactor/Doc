<!-- last-verified: 2026-09-09 -->
# Memory: tone-of-voice

Authoritative tone of voice and technical writing standards for all documentation produced by `tidyfactor-doc`.

## 1. Core Principles

1. **Direct & Action-Oriented**:
   - Start sentences with verbs where possible: *"Install dependencies with `npm install`"*, not *"You may want to proceed by running npm install"*.
   - Eliminate filler words: avoid *"clearly"*, *"obviously"*, *"simply"*, *"just"*, *"as you know"*.

2. **Zero Marketing Fluff**:
   - Technical documentation is not promotional copywriting.
   - Do NOT use exaggerated marketing adjectives like *"revolutionary"*, *"best-in-class"*, *"magical"*, *"effortless"*.
   - State engineering facts, constraints, and verifiable trade-offs objectively.

3. **Semantic Density & Token Efficiency**:
   - Use structured tables for parameters, configuration options, and error codes rather than paragraphs of running text.
   - Favor short, concise bullet points (≤ 15 words) over dense narrative prose.

4. **Clarity Over Cleverness**:
   - Code examples must be minimal, self-contained, and working out of the box.
   - Always document error cases and expected exceptions, not just happy paths.

## 2. Bilingual English & Arabic Standards

- **English**: Concise technical register (Imperative mood, active voice).
- **Arabic**:
  - Clear Modern Standard Arabic (فصحى معاصرة رصينة ومباشرة).
  - Use established technical terminology (e.g. "التوثيق البرمجي", "نقاط النهاية API", "سجل القرارات المعمارية ADR", "المزامنة الذرية").
  - Preserve English code symbols and keyword references within markdown inline code blocks (`code`).
