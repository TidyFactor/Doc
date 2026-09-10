# Command: vitepress

Runtime entry point for "Set up VitePress" / "build modern Vue-powered doc portal" / "vitepress".

## Dispatch steps

1. Load `../memory/vitepress-config.md` — complete ESM configuration schema, luxury CSS custom tokens, and script presets.
2. Confirm `/docs` has real content (at least one generated doc beyond the scaffold).
3. Verify Node.js toolchain (`node --version` >= 18).
4. Dispatch `../workflows/vitepress.md`.

## Injects

- `../workflows/vitepress.md`
- `../memory/vitepress-config.md`

## Does NOT

- Does not author any new markdown content — it structures, configures, and publishes what's already in `/docs`.
- Does not use external unverified CSS frameworks; relies strictly on custom luxury design tokens (`Alexandria` + `Cairo` + `JetBrains Mono` + RTL logical properties).
