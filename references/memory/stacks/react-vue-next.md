# Memory: stacks/react-vue-next

Component-level documentation conventions, layered on top of `js-ts.md` (still use JSDoc/TSDoc block syntax — this file adds what's specific to components, pages, and routes).

## React — props, not just function signature

```tsx
/**
 * <one-line summary of what the component renders/does>
 */
interface ButtonProps {
  /** Description of this prop. */
  label: string;
  /** Optional, defaults to 'primary'. */
  variant?: 'primary' | 'secondary';
  /** Called when clicked. */
  onClick?: () => void;
}
```

- Document props via the `interface`/`type` block (per-member comments), not a `@param` list on the component function — that's the idiomatic React pattern and what most tooling (Storybook, TypeDoc) expects.
- Note default values from the actual destructured defaults or `defaultProps`, not assumed.

## Vue — SFC `<script>` block comments + `defineProps`

```vue
<script setup lang="ts">
/**
 * <one-line summary>
 */
defineProps<{
  /** Description. */
  label: string;
  /** Optional, defaults to 'primary'. */
  variant?: 'primary' | 'secondary';
}>();
</script>
```

- For Options API components (no `<script setup>`), document each prop inside the `props: {}` object with a comment above it instead.
- Emitted events (`defineEmits` / `this.$emit`) get documented the same way props do — name, payload type, when it fires (from code parsing + error-patterns findings if it's an error event).

## Next.js — pages/routes get a route-level note, not just a component doc

- For a page/route file, prepend a comment noting the route path, whether it's a Server or Client Component, and any `params`/`searchParams` it reads — this is route contract, not just component contract.
- API routes (`route.ts`/`route.js` under `app/api/`, or `pages/api/`) are documented as API reference (`generate-api`, using `js-ts.md`'s function conventions for the handler), not as component docs.

## What NOT to document

- Purely presentational/internal sub-components not exported from the module's public entry point: skip the full prop-table treatment unless they're complex enough that the error-patterns or persona-tracing findings flagged them as maintainer-relevant.
