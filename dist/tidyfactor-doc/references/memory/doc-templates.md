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
| Variable | Required | Default | Description | Example |
|---|---|---|---|---|
| `API_KEY` | Yes | — | Secret authentication token | `EXAMPLE_TOKEN_1234567890ABCDEFGH` |
| `DB_HOST` | Yes | `localhost` | Database host IP or hostname | `203.0.113.10` |
| `DB_PASS` | Yes | — | Database user password | `your_secret_password` |

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
<links to other guides or API docs using relative paths, e.g. [API Overview](../api/project.md)>
```
