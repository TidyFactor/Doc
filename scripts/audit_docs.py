#!/usr/bin/env python3
"""
TidyFactor Documentation Quality & Hygiene Auditor
Deterministic AST and pattern scanner for documentation files under /docs and root README.
Audits for sensitive data leaks, banned absolute URLs, relative link integrity,
and Docsify / MkDocs structural requirements.
"""

import sys
import os
import re
import json
import argparse
from pathlib import Path

# Ensure UTF-8 output on Windows console
if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if sys.stderr and hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

SENSITIVE_PATTERNS = [
    (r"(?i)(password|passwd|pwd)\s*[:=]\s*['\"][^'\"]+['\"]", "Hardcoded plain password"),
    (r"(?i)(secret_key|secret|api_key|apikey|token)\s*[:=]\s*['\"][a-zA-Z0-9_\-\.]{12,}['\"]", "Hardcoded secret / API token"),
    (r"(?i)cpanel_[a-zA-Z0-9_]+_pass", "cPanel credential pattern"),
    (r"(?i)whm_[a-zA-Z0-9_]+_token", "WHM access token pattern"),
    (r"ghp_[a-zA-Z0-9]{20,}", "GitHub Personal Access Token"),
    (r"xox[baprs]-[0-9a-zA-Z]{10,}", "Slack Token"),
    (r"AKIA[0-9A-Z]{16}", "AWS Access Key"),
]

BANNED_URL_PATTERNS = [
    (r"file:///[a-zA-Z]:[/\\]", "Banned machine-specific absolute file URL"),
    (r"file://c:/", "Banned Windows drive path URL"),
    (r"[a-zA-Z]:\\wamp64\\www\\", "Banned internal workstation local path"),
]

# Standard Keep a Changelog v1.1.0 sections
VALID_CHANGELOG_SECTIONS = {"Added", "Changed", "Deprecated", "Removed", "Fixed", "Security"}
CHANGELOG_VERSION_PATTERN = re.compile(r"^##\s+\[(?:\d+\.\d+\.\d+|Unreleased)\](?:\s+-\s+\d{4}-\d{2}-\d{2})?$")

def audit_doc_file(file_path: Path, check_links: bool = True) -> list:
    issues = []
    try:
        content = file_path.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        return [{"file": str(file_path), "severity": "high", "type": "read_error", "message": str(e)}]

    lines = content.splitlines()
    is_changelog = file_path.name.lower().startswith("changelog")

    for idx, line in enumerate(lines, start=1):
        # 1. Check for sensitive data leaks
        for pattern, desc in SENSITIVE_PATTERNS:
            if re.search(pattern, line):
                # Ignore placeholders like YOUR_API_KEY, REDACTED, example
                if not re.search(r"(?i)(your_|example|redacted|\.\.\.|placeholder|<.+>|dummy)", line):
                    issues.append({
                        "file": str(file_path),
                        "line": idx,
                        "severity": "critical",
                        "type": "sensitive_data_leak",
                        "message": f"Potential sensitive data leak detected: {desc}."
                    })

        # 2. Check for banned absolute workstation paths & file:/// URLs
        for pattern, desc in BANNED_URL_PATTERNS:
            if re.search(pattern, line):
                # Ignore lines explaining the ban, rule definitions, or dummy placeholders
                if not re.search(r"(?i)(prohibit|banned|prevent|never|don't|no\s+|avoid|clean relative|mandate|your_|example|redacted|\.\.\.|placeholder|<.+>|dummy)", line):
                    issues.append({
                        "file": str(file_path),
                        "line": idx,
                        "severity": "high",
                        "type": "banned_absolute_path",
                        "message": f"Banned workstation-specific path detected: {desc}. Use clean relative links or public URLs."
                    })

        # 3. Check relative link integrity (strip code spans first to avoid flagging examples)
        if check_links:
            # Remove inline code backticks before checking active markdown links
            line_no_code = re.sub(r"`[^`]*`", "", line)
            # Match markdown links: [text](path)
            for match in re.finditer(r"\[(?:[^\]]*)\]\(([^)]+)\)", line_no_code):
                target_url = match.group(1).strip()
                # Skip external, anchor-only, mailto, tel
                if re.match(r"^(?:https?://|mailto:|tel:|#)", target_url, re.IGNORECASE):
                    continue
                # Strip anchor or query params
                clean_target = target_url.split("#")[0].split("?")[0].strip()
                if not clean_target:
                    continue
                # Resolve relative path
                resolved = (file_path.parent / clean_target).resolve()
                if not resolved.exists():
                    issues.append({
                        "file": str(file_path),
                        "line": idx,
                        "severity": "high",
                        "type": "broken_relative_link",
                        "message": f"Broken relative link '{target_url}' — target '{clean_target}' does not exist on disk."
                    })

    # 4. CHANGELOG.md specific structure validation
    if is_changelog:
        version_headers = [l.strip() for l in lines if l.startswith("## ")]
        if not version_headers:
            issues.append({
                "file": str(file_path),
                "line": 1,
                "severity": "high",
                "type": "invalid_changelog_format",
                "message": "CHANGELOG.md lacks standard release headers (expected format: '## [x.y.z] - YYYY-MM-DD' or '## [Unreleased]')."
            })
        else:
            for vh in version_headers:
                if not CHANGELOG_VERSION_PATTERN.match(vh):
                    issues.append({
                        "file": str(file_path),
                        "line": 1,
                        "severity": "low",
                        "type": "non_standard_version_header",
                        "message": f"Changelog version header '{vh}' does not strictly match Keep a Changelog SemVer pattern '## [X.Y.Z] - YYYY-MM-DD'."
                    })

    return issues

def audit_docs_directory(target_dir: Path) -> dict:
    all_issues = []
    files_scanned = 0

    if target_dir.is_file():
        files_to_check = [target_dir]
    elif target_dir.is_dir():
        files_to_check = list(target_dir.rglob("*.md"))
    else:
        return {"error": f"Target path does not exist: {target_dir}", "passed": False}

    for f in files_to_check:
        # Skip vendor/node_modules/.git
        if any(part in f.parts for part in [".git", "node_modules", "dist", "vendor"]):
            continue
        files_scanned += 1
        issues = audit_doc_file(f)
        all_issues.extend(issues)

    critical_count = len([i for i in all_issues if i.get("severity") == "critical"])
    high_count = len([i for i in all_issues if i.get("severity") == "high"])

    score = max(0, 100 - (critical_count * 30) - (high_count * 15))
    passed = critical_count == 0 and high_count == 0

    return {
        "target": str(target_dir),
        "files_scanned": files_scanned,
        "score": score,
        "passed": passed,
        "critical_issues": critical_count,
        "high_issues": high_count,
        "total_issues": len(all_issues),
        "issues": all_issues,
        "timestamp": "2026-09-02T06:00:00Z"
    }

def main():
    parser = argparse.ArgumentParser(description="TidyFactor Documentation Quality & Hygiene Auditor")
    parser.add_argument("target", nargs="?", default="docs", help="Directory or markdown file to audit (default: docs)")
    parser.add_argument("--json", action="store_true", help="Output pure JSON format")

    args = parser.parse_args()
    target_path = Path(args.target)

    result = audit_docs_directory(target_path)

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        status_str = "[PASS]" if result.get("passed") else "[FAIL]"
        print(f"\n{status_str} Documentation Quality & Hygiene Audit — Score: {result.get('score', 0)}/100")
        print(f"Target: {result.get('target')} | Files Scanned: {result.get('files_scanned', 0)}")
        print(f"Issues Found: {result.get('total_issues', 0)} (Critical: {result.get('critical_issues', 0)}, High: {result.get('high_issues', 0)})\n")

        for iss in result.get("issues", []):
            print(f"  - [{iss.get('severity', '').upper()}] {iss.get('file')}:{iss.get('line', '?')} — {iss.get('message')}")
        print()

    sys.exit(0 if result.get("passed") else 1)

if __name__ == "__main__":
    main()
