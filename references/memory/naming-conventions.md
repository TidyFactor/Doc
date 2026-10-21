<!-- last-verified: 2026-09-09 -->
# Memory: naming-conventions

Authoritative naming conventions across supported code stacks and documentation files.

## 1. Documentation File System Conventions

| Element | Format | Example | Anti-Pattern |
|---|---|---|---|
| Guide Slugs | `kebab-case.md` | `setup-guide.md` | `Setup_Guide.MD` |
| ADR Records | `NNNN-kebab-case.md` | `0001-database-choice.md` | `1_db.md` |
| Localized Guides | `[slug].[locale].md` | `architecture.ar.md` | `architecture_arabic.md` |
| API References | `[component-or-class].md` | `user-service.md` | `UserServiceAPI.md` |
| Internal Findings | `docs/.collected/[target].md` | `docs/.collected/auth.md` | `docs/.collected/Auth-Module.md` |

## 2. Multi-Language Code Symbol Conventions

### PHP (PSR-1 / PSR-12)
- **Namespaces**: `PascalCase` (`App\Core\Registry`, `App\Modules\Blog`)
- **Classes / Interfaces / Traits**: `PascalCase` (`AuthService`, `ModuleInterface`)
- **Methods**: `camelCase` (`validateSession()`, `getUserById()`)
- **Constants**: `UPPER_SNAKE_CASE` (`DEFAULT_TIMEOUT`, `MAX_RETRIES`)
- **Variables / Properties**: `camelCase` (`$userId`, `$databaseConnection`)

### TypeScript & JavaScript (ESM)
- **Files & Modules**: `kebab-case.ts` (`auth-service.ts`) or `PascalCase.tsx` for React components (`UserProfile.tsx`)
- **Types / Interfaces / Enums**: `PascalCase` (`UserSession`, `ApiResponse<T>`, `LogLevel`)
- **Functions / Methods**: `camelCase` (`parseManifest()`, `fetchUserData()`)
- **Constants**: `UPPER_SNAKE_CASE` (`API_BASE_URL`, `TOKEN_EXPIRATION`)

### Python (PEP 8)
- **Modules / Packages**: `snake_case` (`audit_docs.py`, `clean_orphaned_assets.py`)
- **Classes**: `PascalCase` (`DocumentationAuditor`, `MarkdownLinkScanner`)
- **Functions / Methods**: `snake_case` (`scan_file()`, `check_relative_links()`)
- **Constants**: `UPPER_SNAKE_CASE` (`SENSITIVE_PATTERNS`, `DEFAULT_SCORE`)

## 3. REST API & Route Conventions

- **Resource URIs**: Lowercase `kebab-case` plural nouns (`/api/v1/user-profiles`, `/api/v1/projects`).
- **Query Parameters**: `snake_case` or `camelCase` (must be uniform per project, e.g. `page_size` or `pageSize`).
