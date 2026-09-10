# Workflow: generate-llmstxt

One outcome: An authoritative, valid `/llms.txt` index file and `/llms-full.txt` bundle generated under `/docs` (or project root) conforming to the [llmstxt.org](https://llmstxt.org/) standard.

---

## Steps

### 1. Identify Project Identity & Summary
1. Read project root metadata (`package.json`, `composer.json`, `brand.yaml`, or root `README.md`).
2. Extract the canonical project name for the required single `# H1` header.
3. Formulate a dense 1-3 sentence blockquote summary (`> ...`) stating the project's purpose, key capabilities, and architecture.

### 2. Crawl and Categorize Documentation
1. Scan `/docs` (or existing documentation tree) for markdown files (`*.md`).
2. Exclude internal files (`.doc-manifest.json`, changelog drafts, or raw collection dumps).
3. Group discovered documents into clear `## H2` categories:
   - `## Core Documentation` (Overview, Quickstart, Installation).
   - `## Architecture & Governance` (ADRs, design patterns, invariants).
   - `## API References` (endpoints, interfaces, contracts).
   - `## Guides & Workflows` (how-tos, tutorials).

### 3. Generate `/llms.txt` Index
1. Format each entry as an annotated markdown item:
   `- [Page Title](relative_or_canonical_url): Concise description of what this doc provides.`
2. Ensure descriptions explicitly inform AI models when to load the page.
3. Write the output to `docs/llms.txt` (and create a symlink or root copy at `llms.txt` if requested).

### 4. Generate `/llms-full.txt` Bundle
1. Concatenate the full markdown content of each categorized file in logical order.
2. Separate each document with horizontal rules (`---`).
3. Strip heavy base64 encoded images or redundant navigational chrome, retaining pure semantic markdown.
4. Write the output to `docs/llms-full.txt`.

### 5. Inject Discovery Headers
1. If VitePress is used (`docs/.vitepress/config.mjs`), inject the `<link>` tag into `head`:
   ```javascript
   head: [
     ['link', { rel: 'alternate', type: 'text/markdown', href: '/llms.txt', title: 'LLM Overview' }],
     ['link', { rel: 'alternate', type: 'text/markdown', href: '/llms-full.txt', title: 'Full LLM Documentation' }]
   ]
   ```
2. If MkDocs is used (`mkdocs.yml`), register in extra head or include in template.
3. If Docsify is used (`docs/index.html`), inject `<link rel="alternate" ...>` into `<head>`.

---

## Validation checklist

- [ ] Single unique `# H1` header present at line 1
- [ ] Blockquote summary (`> ...`) immediately follows the H1 header
- [ ] All documented links use annotated format `- [Title](url): Description`
- [ ] Grouped logically under `## H2` categories
- [ ] Generated `docs/llms.txt` and `docs/llms-full.txt` without syntax errors
- [ ] No local machine absolute drive paths (`file:///C:/...` or `c:\...`) included in output
- [ ] Discovery links (`<link rel="alternate" ...>`) documented or configured for the active doc engine
