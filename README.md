<div align="center">

# 📚 TidyFactor Doc — Code Documentation Builder
### Automated Codebase Interview, API Reference Generator & Docsify Architecture Engine

**Building accurate, maintainable, and browsable documentation for the era of Human-Agent Collaboration.**

[![npm version](https://img.shields.io/npm/v/@alwkala/tidyfactor-doc.svg?color=gold&style=for-the-badge&logo=npm)](https://www.npmjs.com/package/@alwkala/tidyfactor-doc)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg?style=for-the-badge)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-TidyFactor%2FDoc-181717.svg?style=for-the-badge&logo=github)](https://github.com/TidyFactor/Doc)
[![Universal AI Agents](https://img.shields.io/badge/AI%20Agents-Universal%20Compatibility-4285F4.svg?style=for-the-badge)](README.md)
[![RTL Ready](https://img.shields.io/badge/RTL-Native%20Arabic-emerald.svg?style=for-the-badge)](README.ar.md)

[🌐 Official Website](https://tidyfactor.com/) • [📚 Documentation](https://tidyfactor.com/documentation) • [🤝 Partner (Alwkala)](https://alwkala.com/) • [📖 Read in Arabic (بالعربية)](README.ar.md)

</div>

---

## ⚡ What is TidyFactor Doc?

`tidyfactor-doc` is a deterministic code documentation engine for autonomous AI coding agents (*Google Antigravity, Claude Code, Cursor, Codex, Windsurf*). It systematically interviews a codebase (source comments, Git log/PR history, runtime env vars, error patterns) and produces production-grade documentation saved under `/docs` — API references, README files, inline docblocks, and complete Docsify documentation websites.

---

## 🏛️ Commands & Workflows

| User Intent | Slash Command | Routed Workflow & Memory |
| :--- | :--- | :--- |
| **"Set up docs for this project"** | `init` | `workflows/init-docs.md` + `memory/doc-tree.md` |
| **"Document this codebase / API"** | `collect` | `workflows/collect.md` + `memory/collection-sources.md` |
| **"Write API docs / README / Guide"** | `generate` | `workflows/generate-*.md` + `memory/doc-templates.md` + `memory/stacks/*` |
| **"Turn /docs into Docsify site"** | `docsify` | `workflows/docsify.md` + `memory/docsify-config.md` |

---

## 🚀 Quick Start & Injection

Inject `tidyfactor-doc` into any codebase:

```bash
npx @alwkala/tidyfactor-doc add-skill
```

---

## 📜 License & Maintenance

Distributed under the **Apache License 2.0**. Maintained by [TidyFactor](https://tidyfactor.com) & [Alwkala Digital Agency](https://alwkala.com).
