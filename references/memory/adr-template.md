<!-- last-verified: 2026-09-09 -->
# Memory: adr-template

Authoritative MADR (Markdown Architectural Decision Records) schema for capturing significant architectural choices.

## 1. Single Record Shape (`docs/adr/NNNN-<slug>.md`)

```markdown
# ADR [NNNN]: [Short Title of Solved Problem and Decision]

- **Status**: [Proposed | Accepted | Rejected | Deprecated | Superseded by ADR-XXXX]
- **Date**: YYYY-MM-DD
- **Decision-Makers**: [Architect / Agent / Team]
- **Technical Story / Issue**: [Issue # or Feature Link]

## Context and Problem Statement

[Describe the context and problem statement, e.g., in free form or using 2-3 sentences. What forces are at play, what constraints must be satisfied?]

## Decision Drivers

- [Driver 1, e.g. sub-second build times]
- [Driver 2, e.g. strict RTL and Arabic typography support]
- [Driver 3, e.g. zero external runtime dependencies]

## Considered Options

- **Option 1**: [Name of Option 1]
- **Option 2**: [Name of Option 2]
- **Option 3**: [Name of Option 3]

## Pros and Cons of the Options

### Option 1: [Name]

- Good, because [argument a]
- Good, because [argument b]
- Bad, because [argument c]

### Option 2: [Name]

- Good, because [argument a]
- Bad, because [argument b]
- Bad, because [argument c]

## Decision Outcome

**Chosen Option**: "[Option 1]", because [justification: e.g. it resolves Driver 1 and 2 while maintaining Driver 3].

### Positive Consequences

- [e.g. 80% reduction in asset footprint]
- [e.g. Unified documentation deployment without Node.js runtime]

### Negative Consequences / Trade-offs

- [e.g. Requires manual markdown authoring instead of automated GUI]
- [Mitigation: Automated pre-commit linting and link auditing]

## Pros and Cons Matrix

| Option | Performance | RTL Support | Maintenance Overhead | Ecosystem Maturity |
|---|---|---|---|---|
| Option 1 | High | Native | Low | High |
| Option 2 | Medium | Partial | High | Very High |

## References & Links

- [Official Documentation](https://example.com)
- [Related PR / Commit](https://github.com/org/repo/pull/1)
```

## 2. ADR Master Index Shape (`docs/adr/README.md`)

```markdown
# Architectural Decision Records (ADRs)

This directory documents all significant architectural and technical decisions made in this project.

| Number | Date | Title | Status |
|---|---|---|---|
| [0001](./0001-record-architecture-decisions.md) | 2026-09-09 | Record Architecture Decisions | Accepted |
| [0002](./0002-triple-engine-publishing.md) | 2026-09-09 | Triple-Engine Publishing Platform | Accepted |
```
