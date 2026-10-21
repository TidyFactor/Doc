# Command: llms

Runtime entry point for generating and maintaining `/llms.txt` and `/llms-full.txt` files per the [llmstxt.org](https://llmstxt.org/) standard.

---

## Dispatch steps

1. Load `../memory/llmstxt-spec.md` — Authoritative syntax rules (Single H1, blockquote summary, annotated link items).
2. Load `../workflows/generate-llmstxt.md` — Crawling docs, building categorized index, concatenating full bundle, and wiring discovery links.
3. Run the workflow.

---

## What It Does

1. Inspects `/docs` and existing markdown files.
2. Extracts concise summaries and logical hierarchy.
3. Produces `docs/llms.txt` (lightweight index for AI model discovery).
4. Produces `docs/llms-full.txt` (single concatenated markdown archive for context injection).
5. Configures discovery `<link>` headers for VitePress, MkDocs Material, or Docsify.

---

## Does NOT

- Does not author brand-new documentation content from scratch (run `generate` first).
- Does not inject binary or base64 assets into text files.
