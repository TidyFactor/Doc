# Memory: doc-templates

Shapes for each doc type `generate` produces. Templates, not prose — fill in from `collect` findings.

## API reference (`docs/api/<target>.md`)

```markdown
# <Target> API Reference

<one-line purpose, from code parsing findings>

## <FunctionOrMethodName>

<signature, stack-formatted per the matching stacks/*.md file>

**Parameters**
| Name | Type | Required | Description |
|---|---|---|---|

**Returns**: <type> — <description>

**Throws / Errors**: <from error-patterns findings>

**Example**
<minimal usage example>

---
<!-- repeat per public function/method/endpoint/component -->

## See also
<cross-links to related target docs, if any>
```

## README (project root `README.md`)

```markdown
# <Project Name>

<one-line description>

## Requirements
<software dependencies + version constraints, from runtime & environment findings>

## Setup
<install steps, from runtime & environment findings>

## Environment variables
| Variable | Required | Default | Description |
|---|---|---|---|

## Usage
<minimal example>

## Documentation
Full reference: [`/docs`](./docs/README.md)
```

## Guide (`docs/guides/<purpose-slug>.md`)

```markdown
# <Guide Title>

<one-line: what this guide covers and who it's for, from persona-tracing findings>

## <Section per logical step or concept>
<content, prioritized for the target persona>

## Related
<links to other guides or API docs, if any>
```
