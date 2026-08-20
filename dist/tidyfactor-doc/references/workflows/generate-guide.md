# Workflow: generate-guide

One outcome: a single technical guide file under `docs/guides/`, built from `docs/.collected/<target>.md` and the guide shape in `memory/doc-templates.md`. One guide = one purpose (setup, architecture, or a specific workflow) — a request covering two purposes ("how to set up AND how deploys work") is two guides, run this workflow twice.

## Steps

1. **Identify the guide's single purpose** — setup/getting-started, architecture overview, or a specific operational workflow (e.g., "how releases work"). If the request bundles more than one, split it before continuing.
2. **Load the findings** from `docs/.collected/<target>.md`. If it doesn't exist, stop — see constraint 2 in `SKILL.md`.
3. **Pull the guide shape** from `memory/doc-templates.md` (guide section) for the identified purpose.
4. **Write `docs/guides/<purpose-slug>.md`**, prioritizing facts for the persona that reads this kind of guide (per persona-tracing findings — usually an internal maintainer or a new contributor, not an external API consumer). Ensure all configuration code blocks, commands, IPs, and tokens use safe placeholders. Use clean relative links for cross-references.
5. **Update `docs/.doc-manifest.json`**'s `generated` section.

## Validation

- [ ] The guide covers exactly one purpose — no bundled setup+architecture+workflow content in one file
- [ ] `docs/guides/<purpose-slug>.md` exists and follows the shape in `memory/doc-templates.md`
- [ ] Every step/claim traces to the findings — nothing assumed
- [ ] Zero sensitive data leaked: all server IPs, DB credentials, API keys, or private paths replaced with placeholders
- [ ] All internal links are clean relative markdown links; no `file:///` or local drive paths
- [ ] `docs/.doc-manifest.json` updated
