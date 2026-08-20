# Memory: stacks/php

Documentation conventions for PHP targets. Applies whenever the target's manifest is `composer.json` or files are `.php`.

## Inline comment format — PHPDoc

```php
/**
 * <one-line summary>
 *
 * <optional longer description>
 *
 * @param string $name Description of the parameter.
 * @param int|null $limit Description. Optional, defaults to null.
 * @return array<string, mixed> Description of the return shape.
 * @throws InvalidArgumentException When <condition, from error-patterns findings>.
 */
```

- One blank-line-separated summary + description, then tags.
- Always type-hint `@param`/`@return` even when the function itself is already typed — PHPDoc types can be more specific (e.g. `array<string, int>` vs. plain `array`).
- `@throws` is mandatory whenever the error-patterns findings show this function throwing — never omit it to save space.
- Class-level docblocks get `@package` only if the project already uses PSR-4 namespacing conventions that make it meaningful; skip otherwise.

## API reference formatting

- Signatures shown as the actual PHP declaration line (with type hints), not a paraphrase: `public function createUser(string $email, ?int $roleId = null): User`
- Nullable/union types shown exactly as declared (`?int`, `int|string`).
- Static vs. instance methods both documented the same way — note staticness in the signature itself, not as prose.

## What NOT to document inline

- Private/protected helper methods with obvious single-purpose names don't need a full docblock — a one-line `// ` comment is enough, or none if truly self-evident. Full PHPDoc blocks are for the public API surface.
