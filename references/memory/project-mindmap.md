<!-- last-verified: 2026-09-09 -->
# Memory: project-mindmap

Codified guidelines and Mermaid AST templates for generating clear, interactive architectural mind maps and component topology diagrams in documentation.

## 1. Top-Level Architectural Layering (Mermaid C4 / Graph)

```mermaid
graph TD
    Client["Client Layer (Browser / Agents)"]
    Gateway["API & Router Layer"]
    Core["Core Domain & Business Logic"]
    Storage["Data Layer (SQLite / MySQL / Files)"]

    Client -->|HTTP / JSON-RPC| Gateway
    Gateway --> Core
    Core --> Storage
```

## 2. Component Topology & Responsibility Mind Map

```mermaid
mindmap
  root((System Architecture))
    Presentation Layer
      VitePress SSG
      Docsify SPA
      MkDocs Material
    Core Logic
      Command Dispatcher
      Workflow Engine
      Operational Memory
    Execution Tooling
      Link Integrity Auditor
      AST Docblock Parser
      Asset Hygiene Cleaner
    Data & Context
      Single Source of Truth
      Brain Context Layer
      Local File Snapshots
```

## 3. Data Flow & Execution Sequence Diagram

```mermaid
sequenceDiagram
    autonumber
    actor Dev as Developer / Agent
    participant Dispatcher as SKILL.md Dispatcher
    participant Workflow as Workflow Engine
    participant Collector as Codebase Collector
    participant Target as /docs Surface

    Dev->>Dispatcher: Issue Command (brief / collect / generate)
    Dispatcher->>Workflow: Load Matching Workflow & Memory
    Workflow->>Collector: Scrape Signatures & Env Context
    Collector-->>Workflow: Return 5-Dimension Findings
    Workflow->>Target: Write Clean Markdown Artifacts
    Workflow->>Dev: Emit Success Checklist & Audit Score
```

## 4. Usage Guidelines

1. Place overarching mind maps in `docs/README.md` or `docs/guides/architecture.md`.
2. Do not use raw image screenshots when Mermaid diagrams can represent topology directly in text.
3. Keep node labels concise (≤ 4 words) to maintain high readability across mobile and desktop viewports.
