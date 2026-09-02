<!-- last-verified: 2026-09-02 -->
# Memory: MkDocs Material Configuration Spec

Complete architectural specification for scaffolding and compiling production-grade documentation portals with MkDocs Material.

---

## 1. Package Requirements (`requirements.txt`)

```text
mkdocs-material>=9.5
mkdocs-static-i18n>=1.2
```

---

## 2. Master Configuration Schema (`mkdocs.yml`)

```yaml
site_name: Project Documentation
site_url: https://example.com/docs/
site_description: "Production Documentation Portal"
site_author: Engineering Team

docs_dir: docs
site_dir: site

theme:
  name: material
  language: en
  direction: ltr
  custom_dir: overrides

  logo: assets/logo.png
  favicon: assets/favicon.png

  font:
    text: Plus Jakarta Sans
    code: Fira Code

  palette:
    # Light Mode
    - media: "(prefers-color-scheme: light)"
      scheme: tidyfactor-light
      primary: custom
      accent: custom
      toggle:
        icon: material/brightness-7
        name: Switch to Dark Mode

    # Dark Mode
    - media: "(prefers-color-scheme: dark)"
      scheme: tidyfactor-dark
      primary: custom
      accent: custom
      toggle:
        icon: material/brightness-4
        name: Switch to Light Mode

  features:
    - navigation.tracking
    - navigation.tabs
    - navigation.tabs.sticky
    - navigation.sections
    - navigation.expand
    - navigation.path
    - navigation.top
    - navigation.indexes
    - navigation.footer
    - search.suggest
    - search.highlight
    - search.share
    - content.code.copy
    - content.code.annotate
    - content.tabs.link
    - header.autohide
    - toc.follow

plugins:
  - search:
      separator: '[\s\-\.]+'
      lang:
        - en
        - ar

  - i18n:
      docs_structure: suffix
      languages:
        - locale: en
          name: English
          default: true
          build: true
        - locale: ar
          name: العربية
          build: true
          theme:
            language: ar
            direction: rtl
            font:
              text: Tajawal
              code: Fira Code

markdown_extensions:
  - abbr
  - admonition
  - attr_list
  - def_list
  - footnotes
  - md_in_html
  - tables
  - toc:
      permalink: true
      toc_depth: 3
  - pymdownx.arithmatex:
      generic: true
  - pymdownx.betterem:
      smart_enable: all
  - pymdownx.caret
  - pymdownx.details
  - pymdownx.emoji:
      emoji_index: !!python/name:material.extensions.emoji.twemoji
      emoji_generator: !!python/name:material.extensions.emoji.to_svg
  - pymdownx.highlight:
      anchor_linenums: true
      line_spans: __span
      pygments_lang_class: true
  - pymdownx.inlinehilite
  - pymdownx.keys
  - pymdownx.mark
  - pymdownx.smartsymbols
  - pymdownx.superfences:
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:pymdownx.superfences.fence_code_format
  - pymdownx.tabbed:
      alternate_style: true
  - pymdownx.tasklist:
      custom_checkbox: true
  - pymdownx.tilde

extra_css:
  - stylesheets/extra.css

extra_javascript:
  - javascripts/extra.js
```

---

## 3. Bilingual Suffix Rule (i18n)

- English source files: `docs/guides/architecture.md`, `docs/index.md`
- Arabic source files: `docs/guides/architecture.ar.md`, `docs/index.ar.md`
- Rule: Never link directly to `.ar.md` from `.md` files; the `i18n` plugin handles language linking automatically via the header switcher.

---

## 4. Local Apache Subfolder Routing (`.htaccess`)

When hosting the documentation inside a subfolder during local Apache/WAMP development:

```apache
<IfModule mod_rewrite.c>
    RewriteEngine On
    RewriteRule ^site(/.*)?$ - [L]
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteRule ^(.*)$ site/$1 [L]
</IfModule>
```
In production: upload the contents of `site/` directly into `public_html/docs/`.
