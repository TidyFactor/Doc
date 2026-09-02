# Brain BaaS & Sovereign Knowledge Base Integration

<!-- last-verified: 2026-09-02 -->

> **Tier**: Core Intelligence Layer Contract  
> **Authority**: Sovereign Self-Hosted & Local Multi-Tenant Architecture  
> **Protocol**: Model B (Fail-Open Sovereign Agent Protocol)

---

## 🏛️ Architectural Doctrine & Deployment Model

TidyFactor is strictly the **Intelligence, Context & Operating Layer** for AI agents. `tidyfactor-doc` operates under **Model B (Sovereign Self-Hosted Architecture)**:

1. **Zero Centralized Data Exposure**: Codebase documentation, API schemas, and technical architectures are never transmitted to a centralized multi-tenant cloud service.
2. **Local Multi-Tenant Isolation**: Each client or project maintains an isolated local SQLite knowledge base (`data/tenants/{tenant_id}_brain.sqlite`) or filesystem cache (`~/.gemini/knowledge/projects/{project_id}/`).
3. **Fail-Open Invariant**: Brain MCP integration is completely optional at runtime. If `tidyfactor-brain` MCP is unavailable or disabled, `tidyfactor-doc` executes directly via local filesystem AST parsing and markdown generation with **0ms latency penalty** and zero connection errors.

```
┌────────────────────────────────────────────────────────┐
│               AI Coding Agent Session                  │
│       (Google Antigravity, Claude Code, Cursor)       │
└───────────────────────────┬────────────────────────────┘
                            │
              [1] Check Active Tool Manifest
                            │
         ┌──────────────────┴──────────────────┐
         │                                     │
   [Brain MCP Active]                 [Brain MCP Absent]
         │                                     │
  [2] search_knowledge_base()                  │
  (Doc Tree, APIs, Routes)                     │
         │                                     │
   (Found?)                                    │
   ├── YES ──► Ingest KI Context               │
   └── NO  ──► Direct Codebase Scan ◄──────────┘ (0ms Fail-Open)
                            │
               [3] Execute Doc Workflow
               (init / collect / generate / site)
                            │
               [4] Persist /docs/ Artifacts
                            │
              (Optional: --sync-brain)
                            │
             [5] extract_knowledge_item()
```

---

## 📋 Documentation Knowledge Item (KI) Payload Schema

When persisting documentation structures or API contracts to the Brain via `--sync-brain`, payload objects MUST conform to the standard KI schema:

```json
{
  "title": "Documentation Architecture: [Project Name]",
  "category": "technical_architecture",
  "scope": "project",
  "tags": ["documentation", "api-reference", "mkdocs", "docsify", "architecture"],
  "content": "### Codebase Overview\n...",
  "metadata": {
    "skill": "tidyfactor-doc",
    "version": "1.4.0",
    "site_engine": "mkdocs|docsify|none",
    "doc_root": "docs/",
    "entry_point": "docs/index.md",
    "sidebar_configured": true,
    "api_endpoints_count": 14,
    "stacks": ["php", "typescript", "python"],
    "i18n_enabled": true
  }
}
```

---

## ⚡ Fail-Open Context Resolution Flow

Every documentation command (`init`, `collect`, `generate`, `site`) executes context resolution deterministically:

1. **Local Filesystem Scan**: Inspect `docs/`, `mkdocs.yml`, `_sidebar.md`, and project manifest (`package.json`, `composer.json`, `pyproject.toml`).
2. **Optional Brain MCP Query**: If `search_knowledge_base` is active, retrieve existing architecture KIs for cross-referencing.
3. **Silent Bypass**: If no Brain tool exists, complete the documentation task directly without prompting the user about server status.
