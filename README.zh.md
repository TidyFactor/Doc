<div align="center">

# tidyfactor-doc `v1.3.0`

**面向 AI 智能体的代码库文档自动生成与双引擎发布平台 (MkDocs & Docsify)**

[![npm version](https://img.shields.io/npm/v/@alwkala/tidyfactor-doc.svg?style=for-the-badge&color=0284C7)](https://www.npmjs.com/package/@alwkala/tidyfactor-doc)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg?style=for-the-badge)](LICENSE)

[ English ](README.md) • [ العربية ](README.ar.md) • [ فارسی ](README.fa.md) • [ Español ](README.es.md) • [ Português ](README.pt.md) • [ 简体中文 ](README.zh.md) • [ Deutsch ](README.de.md) • [ Français ](README.fr.md)

</div>

---

## ⚡ 快速上手 (Quickstart)

```bash
# 通过 NPX 快速运行
npx @alwkala/tidyfactor-doc
```

或在 AI 编码助手 (*Google Antigravity, Claude Code, Cursor, Codex*) 中调用：
```text
/tidyfactor-doc
```

---

## 📋 核心命令矩阵

| 命令 | 目标与产出 | 执行工作流 |
|---|---|---|
| `/init` | Inicialización de estructura de documentación | `workflows/init.md` |
| `/collect` | Entrevista y análisis de código fuente | `workflows/collect.md` |
| `/generate` | Generación de especificaciones API y READMEs | `workflows/generate.md` |
| `/mkdocs` | Compilación de portal estático MkDocs Material | `workflows/mkdocs.md` |
| `/docsify` | Despliegue de SPA ligera Docsify sin compilación | `workflows/docsify.md` |

---

## 📖 完整技术规范与文档

如需查看深层架构设计、完整 JSON Schema 契约和原生代码，请参阅[英文权威技术文档 (README.md)](README.md)。
