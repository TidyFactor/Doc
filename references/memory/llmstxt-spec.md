# Memory: llmstxt-spec

<!-- last-verified: 2026-09-10 -->

Technical specification and authoring standards for `/llms.txt` and `/llms-full.txt` files per the community standard ([llmstxt.org](https://llmstxt.org/)).

---

## 1. Overview & Purpose

`llms.txt` is an advisory, machine-readable Markdown file placed at the project or documentation root (`/llms.txt` or `/docs/llms.txt`).
It provides AI models, autonomous agents, and inference systems with a structured map of curated information, eliminating the need to crawl and parse bloated HTML structures.

- **`/llms.txt`**: Fast, lightweight index containing the title, concise summary, and annotated markdown links to core sections.
- **`/llms-full.txt`**: Consolidated bundle containing the complete, unabridged text of all documentation pages concatenated into a single plain-text markdown file.

---

## 2. File Format Specification (`/llms.txt`)

Every `llms.txt` file must adhere strictly to the following syntax rules:

### A. Single H1 Header (Mandatory)
The file must start with exactly one `# H1` heading representing the project or library name:
```markdown
# Project Name
```

### B. Blockquote Summary (Mandatory)
Immediately beneath the `# H1`, a blockquote (`> ...`) must describe the project, its core value proposition, tech stack, and audience in 1–3 concise sentences:
```markdown
> A lightweight modular architecture platform for building AI-agent-compatible web services and applications.
```

### C. H2 Categorized Sections
Group documentation links into logical `## H2` categories (e.g., `## Core Concepts`, `## API Reference`, `## Guides`, `## Optional`):
```markdown
## Documentation

- [Getting Started](https://example.com/docs/intro.md): Quickstart guide to install and configure the platform in under 5 minutes.
- [Architecture](https://example.com/docs/architecture.md): Overview of Kernel contracts, Module interfaces, and dependency isolation.

## API Reference

- [Core API](https://example.com/docs/api/core.md): Detailed parameter and return type references for runtime controllers.
```

### D. Annotated Link Conventions
- Format: `- [Link Title](url): Brief description of content and scope`.
- All URLs should be canonical absolute URLs (or clean root-relative links if self-hosted within the repo).
- Descriptions should explain *what* the document covers and *when* an LLM should retrieve it.

---

## 3. File Format Specification (`/llms-full.txt`)

The consolidated version bundles the actual markdown content of all referenced docs:
1. Starts with the exact same `# H1` and `> Summary` as `llms.txt`.
2. Appends each documentation file separated by standard horizontal markdown dividers (`---`).
3. Each section includes a reference header indicating its source route:
   ```markdown
   # Project Name
   > Summary ...
   
   ---
   
   # Getting Started
   Source: https://example.com/docs/intro.md
   
   [Full Markdown content here...]
   
   ---
   
   # Architecture
   Source: https://example.com/docs/architecture.md
   
   [Full Markdown content here...]
   ```

---

## 4. HTML Discovery Tags & Headers

To ensure web crawlers and autonomous agents discover the `llms.txt` file without blind guessing, inject discovery links:

### HTML `<head>` tag:
```html
<link rel="alternate" type="text/markdown" href="/llms.txt" title="LLM-friendly text overview" />
<link rel="alternate" type="text/markdown" href="/llms-full.txt" title="Full documentation for LLMs" />
```

### HTTP Response Header:
```http
Link: </llms.txt>; rel="describedby"; type="text/markdown"
```
