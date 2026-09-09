<!-- last-verified: 2026-09-09 -->
# Memory: VitePress Configuration Spec & Luxury Theme Architecture

Complete architectural specification for scaffolding, configuring, and styling production-grade documentation portals with VitePress, luxury typography, and full RTL layout parity.

---

## 1. Master ESM Configuration Schema (`docs/.vitepress/config.mjs`)

```javascript
import { defineConfig } from 'vitepress';

export default defineConfig({
  title: 'Project Name',
  description: 'Production Documentation Portal',
  head: [
    ['link', { rel: 'icon', href: '/logo.png' }]
  ],

  locales: {
    root: {
      label: 'العربية',
      lang: 'ar',
      dir: 'rtl',
      themeConfig: {
        nav: [
          { text: 'الرئيسية', link: '/' },
          { text: 'دليل الاستخدام', link: '/user_manual.ar' },
          { text: 'المواصفات المعمارية', link: '/specs/architecture_spec.ar' },
          { text: 'GitHub', link: 'https://github.com/organization/repo' }
        ],
        sidebar: [
          {
            text: '🚀 البدء السريع',
            items: [
              { text: 'نظرة عامة', link: '/' },
              { text: 'دليل التثبيت', link: '/guide/getting-started.ar' }
            ]
          }
        ]
      }
    },
    en: {
      label: 'English',
      lang: 'en',
      link: '/en/',
      themeConfig: {
        nav: [
          { text: 'Home', link: '/en/' },
          { text: 'User Manual', link: '/user_manual.ar' }
        ]
      }
    }
  },

  themeConfig: {
    logo: '/logo.png',
    siteTitle: 'Project Name',
    search: {
      provider: 'local'
    },
    footer: {
      message: 'Released under Apache-2.0 License',
      copyright: 'Copyright © 2026 Engineering Team'
    }
  }
});
```

---

## 2. Luxury Design System Tokens (`docs/.vitepress/theme/custom.css`)

```css
@import url('https://fonts.googleapis.com/css2?family=Alexandria:wght@400;500;600;700;800;900&family=Cairo:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

:root {
  --vp-font-family-base: 'Cairo', sans-serif;
  --vp-font-family-headings: 'Alexandria', sans-serif;
  --vp-font-family-mono: 'JetBrains Mono', monospace;
}

/* RTL Navbar Flex Order */
html[dir="rtl"] .VPNavBar .content-body {
  display: flex !important;
  flex-direction: row !important;
  align-items: center !important;
  width: 100%;
}
html[dir="rtl"] .VPNavBarTitle { order: 1 !important; margin-inline-end: 28px !important; }
html[dir="rtl"] .VPNavBarMenu { order: 2 !important; margin-inline-end: auto !important; }
html[dir="rtl"] .VPNavBarSearch { order: 3 !important; }
html[dir="rtl"] .VPNavBarTranslations { order: 4 !important; }
html[dir="rtl"] .VPNavBarAppearance { order: 5 !important; }
html[dir="rtl"] .VPNavBarSocialLinks { order: 6 !important; }

/* Hero Reading Direction in RTL: Text on Right, Logo on Left */
.VPHomeHero .container {
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
}
html[dir="rtl"] .VPHomeHero .container { flex-direction: row !important; }
html[dir="rtl"] .VPHomeHero .main { order: 1 !important; text-align: right !important; flex: 1 1 60% !important; }
html[dir="rtl"] .VPHomeHero .image { order: 2 !important; flex: 1 1 40% !important; display: flex !important; justify-content: center !important; }

/* Single-Row Protected Hero Actions */
.VPHomeHero .actions {
  display: flex !important;
  flex-direction: row !important;
  align-items: center !important;
  gap: 14px !important;
  flex-wrap: nowrap !important;
}
.VPButton {
  min-height: 48px !important;
  height: 48px !important;
  padding: 0 24px !important;
  border-radius: 14px !important;
  font-family: 'Alexandria', sans-serif !important;
  font-weight: 700 !important;
  font-size: 0.95rem !important;
  white-space: nowrap !important;
  word-break: keep-all !important;
}

/* 3-Column Luxury Feature Cards (Column Collapse Fix) */
.VPFeatures .items {
  display: flex !important;
  flex-wrap: wrap !important;
  margin: -10px !important;
}
.VPFeatures .item {
  padding: 10px !important;
  box-sizing: border-box !important;
  width: 100% !important;
  display: flex !important;
}
@media (min-width: 640px) { .VPFeatures .item { width: 50% !important; } }
@media (min-width: 960px) { .VPFeatures .item { width: 33.333333% !important; } }

.VPFeature {
  border: 1px solid var(--vp-c-divider) !important;
  border-radius: 20px !important;
  background: var(--vp-c-bg-soft) !important;
  backdrop-filter: blur(20px) !important;
  padding: 28px !important;
  width: 100% !important;
  height: 100% !important;
  box-sizing: border-box !important;
}
html[dir="rtl"] .VPFeature .title,
html[dir="rtl"] .VPFeature .details {
  text-align: right !important;
  direction: rtl !important;
  unicode-bidi: plaintext !important;
}
```

---

## 3. Quick Navigation Grid Markdown Template

```markdown
## 🧭 جدول المحتويات والمسارات السريعة

<div class="quick-nav-grid">

| 🚀 البدء والأدوات | 💼 التطبيقات وحزم العمل | 🏛️ المعمارية العميقة |
|---|---|---|
| • [دليل التثبيت](/guide/getting-started.ar)<br>• [مرجع الطرفية](/tools/cli.ar) | • [تطبيقات الإنتاجية](/apps/productivity.ar)<br>• [حزمة الأعمال](/apps/office-suite.ar) | • [بنية الذاكرة](/architecture/memory-and-search.ar)<br>• [المواصفات الفنية](/specs/architecture_spec.ar) |

</div>
```
