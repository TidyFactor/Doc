# Memory: stacks/js-ts

Documentation conventions for JavaScript and TypeScript targets. Applies whenever the target's manifest is `package.json` and files are `.js`/`.mjs` (JS) or `.ts`/`.tsx` (TS). The two share JSDoc-style block syntax but differ in what needs restating.

## JavaScript — JSDoc (types belong in the comment, since the code itself is untyped)

```js
/**
 * <one-line summary>
 *
 * @param {string} name Description.
 * @param {number} [limit] Optional, defaults to undefined.
 * @returns {Promise<object>} Description of the resolved shape.
 * @throws {RangeError} When <condition, from error-patterns findings>.
 */
```

- Always include `@param`/`@returns` types — JS has no compile-time types, so the comment is the only source of truth.
- Optional params use `[name]` bracket syntax.

## TypeScript — TSDoc (types live in the signature, don't restate them in the comment)

```ts
/**
 * <one-line summary>
 *
 * @param name - Description only, no type (already in the signature).
 * @param limit - Description only.
 * @returns Description only.
 * @throws {RangeError} When <condition, from error-patterns findings>.
 */
function example(name: string, limit?: number): Promise<Result> { ... }
```

- Do NOT restate types already visible in the TS signature (`{string}`, `{number}`) — that's a JSDoc habit that's redundant and can drift out of sync in TS. Description only after the `-`.
- Exported `interface`/`type` declarations get their own TSDoc block above the declaration, one line per member if the member itself isn't self-explanatory.

## API reference formatting

- Show the actual signature from the source (JS: as written; TS: full typed signature).
- For TS, prefer documenting the public exported types directly rather than re-describing them in prose.

## What NOT to document inline

- Non-exported (module-private) helper functions with obvious names: skip full blocks unless the error-patterns findings show them as a common failure point.
