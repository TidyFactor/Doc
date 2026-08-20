# Memory: docsify-config

Fixed Docsify setup used by the `docsify` workflow. Not a menu of options — locked, production-tested config for TidyFactor documentation web portals.

## `docs/index.html` Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title><PROJECT_NAME> Documentation</title>
  <meta name="viewport" content="width=device-width,initial-scale=1,minimum-scale=1">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/docsify@4/lib/themes/vue.css">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&family=Inter:wght@400;500;600;700;800&family=Fira+Code:wght@400;500&display=swap">
  <style>
    :root {
      --theme-color: #0A2540;
      --sidebar-width: 300px;
    }
    body {
      font-family: 'Inter', 'Cairo', -apple-system, BlinkMacSystemFont, sans-serif;
      color: #1e293b;
      background-color: #ffffff;
    }
    
    /* Header & Brand styling */
    .app-name-link {
      font-weight: 800 !important;
      font-size: 1.25rem !important;
      color: #0A2540 !important;
      letter-spacing: -0.02em;
    }
    
    /* Fixed Floating Sidebar Toggle Hamburger Button */
    .sidebar-toggle {
      position: fixed !important;
      top: 14px !important;
      left: 14px !important;
      bottom: auto !important;
      z-index: 1000 !important;
      background: #0A2540 !important;
      padding: 10px 12px !important;
      border-radius: 8px !important;
      box-shadow: 0 4px 12px rgba(10, 37, 64, 0.25) !important;
      border: none !important;
      cursor: pointer !important;
      width: auto !important;
      height: auto !important;
      transition: transform 0.2s ease, background 0.2s ease !important;
    }
    .sidebar-toggle:hover {
      background: #081C30 !important;
      transform: scale(1.04);
    }
    .sidebar-toggle .sidebar-toggle-button {
      display: flex !important;
      flex-direction: column !important;
      justify-content: center !important;
      align-items: center !important;
      gap: 4px !important;
      background: transparent !important;
      padding: 0 !important;
      margin: 0 !important;
      border: none !important;
      width: auto !important;
      height: auto !important;
    }
    .sidebar-toggle span {
      display: block !important;
      background-color: #ffffff !important;
      height: 2px !important;
      width: 20px !important;
      margin: 0 !important;
      border-radius: 2px !important;
      float: none !important;
      position: relative !important;
    }
    
    /* Sidebar Layout */
    .sidebar {
      padding-top: 60px !important;
      padding-bottom: 40px !important;
      background-color: #f8fafc !important;
      border-right: 1px solid #e2e8f0 !important;
    }
    .sidebar ul li a {
      font-weight: 500;
      color: #475569;
      transition: all 0.15s ease;
      border-radius: 4px;
    }
    .sidebar ul li a:hover {
      color: #0A2540;
      background-color: #e2e8f0/50;
    }
    .sidebar ul li.active > a {
      color: #0A2540 !important;
      font-weight: 700 !important;
      border-left: 3px solid #0A2540;
      padding-left: 8px;
    }

    /* Content Styling & Typography */
    .markdown-section {
      max-width: 900px !important;
      padding: 40px 45px !important;
    }
    .markdown-section h1, .markdown-section h2, .markdown-section h3, .markdown-section h4 {
      font-family: 'Inter', 'Cairo', sans-serif;
      color: #0F172A;
      font-weight: 700;
      letter-spacing: -0.02em;
    }
    .markdown-section h1 {
      border-bottom: 1px solid #e2e8f0;
      padding-bottom: 12px;
      font-size: 2.1rem;
    }
    .markdown-section h2 {
      font-size: 1.5rem;
      margin-top: 2rem;
    }
    
    /* Code Blocks */
    .markdown-section pre {
      border-radius: 8px !important;
      background-color: #0f172a !important;
      box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    .markdown-section code {
      font-family: 'Fira Code', monospace !important;
      font-size: 0.9em;
    }
    .markdown-section p code {
      background-color: #f1f5f9 !important;
      color: #0f172a !important;
      padding: 3px 6px !important;
      border-radius: 4px !important;
      border: 1px solid #cbd5e1 !important;
    }

    /* Table Styling */
    .markdown-section table {
      display: table !important;
      width: 100% !important;
      border-collapse: collapse !important;
      border: 1px solid #e2e8f0 !important;
      border-radius: 6px !important;
      overflow: hidden !important;
      margin: 20px 0 !important;
    }
    .markdown-section th {
      background-color: #f8fafc !important;
      color: #0f172a !important;
      font-weight: 700 !important;
      border-bottom: 2px solid #e2e8f0 !important;
      padding: 10px 14px !important;
    }
    .markdown-section td {
      border-bottom: 1px solid #e2e8f0 !important;
      padding: 10px 14px !important;
    }

    /* Scrollbars */
    ::-webkit-scrollbar {
      width: 8px;
      height: 8px;
    }
    ::-webkit-scrollbar-track {
      background: #f1f5f9;
    }
    ::-webkit-scrollbar-thumb {
      background: #cbd5e1;
      border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: #94a3b8;
    }
  </style>
</head>
<body>
  <div id="app"></div>
  <script>
    window.$docsify = {
      name: '<PROJECT_NAME>',
      repo: '<REPO_URL>',
      loadSidebar: true,
      alias: {
        '/.*/_sidebar.md': '/_sidebar.md'
      },
      subMaxLevel: 2,
      auto2top: true,
      search: {
        placeholder: 'Search documentation...',
        noData: 'No results found',
        depth: 3
      }
    }
  </script>
  <script src="https://cdn.jsdelivr.net/npm/docsify@4"></script>
  <script src="https://cdn.jsdelivr.net/npm/docsify/lib/plugins/search.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/docsify-copy-code@2"></script>
  <script src="https://cdn.jsdelivr.net/npm/prismjs@1/components/prism-bash.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/prismjs@1/components/prism-php.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/prismjs@1/components/prism-typescript.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/prismjs@1/components/prism-json.min.js"></script>
</body>
</html>
```

Replace `<PROJECT_NAME>` from `docs/.doc-manifest.json`'s `project` field, and `<REPO_URL>` with project repository or developer link (`https://github.com/alwkala/TidyFactor-Go`).

---

## Critical Rules & Lessons Learned

### 1. Subfolder Navigation Sidebar Alias
- **CRITICAL**: Always configure `alias: { '/.*/_sidebar.md': '/_sidebar.md' }` in `window.$docsify`. Without this alias, opening subfolder guides (e.g. `/#/guides/architecture-and-setup`) causes Docsify to look for `guides/_sidebar.md` and hide the sidebar menu!
- **CRITICAL**: Use leading slashes `/` for all links in `_sidebar.md` (`/guides/admin-user-guide.md`, `/api/project.md`) so links resolve relative to the `/docs` root from any route depth.

### 2. Localized Pages Inside Docs Root
- **CRITICAL**: Docsify web root is `/docs`. Never link out of `/docs` using relative `../` paths (e.g. `../README.ar.md`), as Docsify SPA routing will throw `404 - Not Found`.
- Always place localized landing pages inside `/docs` (e.g. `docs/README.ar.md`), rendering smoothly at `/#/README.ar.md`.

### 3. Hamburger Toggle Button (`.sidebar-toggle`) Styling
- Always style `.sidebar-toggle` and `.sidebar-toggle-button` with fixed positioning (`top: 14px; left: 14px; z-index: 1000`) and explicit `<span>` lines (`width: 20px; height: 2px; display: block`) so the hamburger button remains accessible without collapsing or overlapping sidebar text items.

### 4. Cross-Platform Emojis & Typography
- Country flag emojis (`🇸🇦`, `🇺🇸`) render as 2-letter codes (`SA`, `US`) on Windows Chrome/Edge. Use clean text badges (`[عربي]`, `[EN]`) in `_sidebar.md`.
- Always load Google Fonts (`Cairo` for Arabic RTL, `Inter` for English LTR, `Fira Code` for code blocks) in `docs/index.html`.

---

## `_sidebar.md` Generation Rule

Group by audience/purpose, root docs first, using leading slashes `/`:

```markdown
- 🌐 [Overview / النظرة العامة](/README.md)
- 📖 [المقدمة بالعربية](/README.ar.md)
- 💡 [رؤية المنظومة والشركة](/guides/vision-and-ecosystem.md)

- [عربي] أدلة المستخدم (User Guides - AR)
  - [دليل مالك الموقع (Admin User Guide)](/guides/admin-user-guide.md)
  - [دليل تحرير المحتوى (Editing Pages Content)](/guides/pages-editing-guide.md)

- [EN] Developer & Technical Guides
  - [Quick Start Guide](/guides/quick-start.md)
  - [Platform & System Specifications](/guides/system-specifications.md)
  - [AI Coding & Agent Workflows](/guides/ai-agent-workflows.md)
  - [Content Engine Architecture & API](/guides/content-engine.md)
  - [Architecture & Setup Guide](/guides/architecture-and-setup.md)
  - [Database & Storage Architecture](/guides/database-and-storage.md)
  - [Security & System Hardening](/guides/security-and-hardening.md)
  - [Production Deployment & Hosting](/guides/deployment-and-hosting.md)
  - [CMS Content Engine & Backups](/guides/cms-content-engine-and-backups.md)

- 📚 REST API Reference
  - [API Endpoints Specifications](/api/project.md)

---

- 👨‍💻 Developed by [Alwkala](https://github.com/alwkala)
```

Regenerate the whole file each run so it never drifts from what's actually in `/docs`.

---

## Preview

Local static server: `php -S localhost:3001 -t docs` or `npx docsify-cli serve docs`.
