#!/usr/bin/env python3
"""
TidyFactor Asset Hygiene & Orphan Cleaner
Scans documentation markdown files for referenced image assets, detects orphaned files
in assets/ directory, detects duplicate assets via SHA-256 hashing, and evaluates
potential WebP compression savings.
"""

import sys
import os
import re
import json
import hashlib
import argparse
from pathlib import Path

# Ensure UTF-8 output on Windows console
if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if sys.stderr and hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".bmp", ".ico"}

def get_file_hash(file_path: Path) -> str:
    hasher = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(65536):
                hasher.update(chunk)
        return hasher.hexdigest()
    except Exception:
        return ""

def scan_markdown_image_references(root_dir: Path) -> set:
    referenced_filenames = set()
    md_files = []

    for f in root_dir.rglob("*.md"):
        if any(part in f.parts for part in [".git", "node_modules", "vendor", "dist"]):
            continue
        md_files.append(f)

    for md_file in md_files:
        try:
            content = md_file.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue

        # 1. Match standard markdown image syntax: ![alt](path)
        for match in re.finditer(r"!\[(?:[^\]]*)\]\(([^)]+)\)", content):
            raw_url = match.group(1).strip().split("?")[0].split("#")[0]
            if raw_url.startswith(("http://", "https://", "data:")):
                continue
            referenced_filenames.add(Path(raw_url).name.lower())

        # 2. Match HTML img tags: <img src="path" ... />
        for match in re.finditer(r"""<img[^>]+src=["']([^"']+)["']""", content, re.IGNORECASE):
            raw_url = match.group(1).strip().split("?")[0].split("#")[0]
            if raw_url.startswith(("http://", "https://", "data:")):
                continue
            referenced_filenames.add(Path(raw_url).name.lower())

    return referenced_filenames

def analyze_assets(repo_root: Path, assets_dir: Path, delete_orphans: bool = False) -> dict:
    if not assets_dir.exists() or not assets_dir.is_dir():
        return {"error": f"Assets directory not found: {assets_dir}", "passed": True, "assets": []}

    referenced_names = scan_markdown_image_references(repo_root)

    asset_files = []
    for f in assets_dir.iterdir():
        if f.is_file() and f.suffix.lower() in IMAGE_EXTENSIONS:
            asset_files.append(f)

    # 1. Detect duplicates via SHA-256
    hash_map = {}
    duplicates = []
    orphaned_files = []
    webp_candidates = []
    total_size = 0

    for f in asset_files:
        size = f.stat().st_size
        total_size += size
        f_hash = get_file_hash(f)
        f_name_lower = f.name.lower()

        if f_hash in hash_map:
            duplicates.append({
                "file": str(f.relative_to(repo_root)),
                "duplicate_of": str(hash_map[f_hash]["path"].relative_to(repo_root)),
                "size_bytes": size,
                "sha256": f_hash
            })
        else:
            hash_map[f_hash] = {"path": f, "size": size}

        # Check orphan status
        is_referenced = f_name_lower in referenced_names
        if not is_referenced:
            orphaned_files.append({
                "file": str(f.relative_to(repo_root)),
                "size_bytes": size,
                "deleted": False
            })

        # Check WebP optimization candidate (PNG/JPG > 50KB)
        if f.suffix.lower() in {".png", ".jpg", ".jpeg"} and size > 51200:
            estimated_webp_size = int(size * 0.25) # ~75% reduction
            webp_candidates.append({
                "file": str(f.relative_to(repo_root)),
                "current_size_bytes": size,
                "estimated_webp_bytes": estimated_webp_size,
                "estimated_savings_bytes": size - estimated_webp_size
            })

    # Execute deletion if requested
    if delete_orphans and orphaned_files:
        for item in orphaned_files:
            try:
                target_to_del = repo_root / item["file"]
                target_to_del.unlink()
                item["deleted"] = True
            except Exception as e:
                item["delete_error"] = str(e)

    passed = len(orphaned_files) == 0 and len(duplicates) == 0

    return {
        "repo_root": str(repo_root),
        "assets_dir": str(assets_dir),
        "total_assets_scanned": len(asset_files),
        "total_size_bytes": total_size,
        "orphaned_count": len(orphaned_files),
        "orphaned_files": orphaned_files,
        "duplicates_count": len(duplicates),
        "duplicates": duplicates,
        "webp_optimization_candidates": webp_candidates,
        "passed": passed
    }

def main():
    parser = argparse.ArgumentParser(description="TidyFactor Asset Hygiene & Orphan Cleaner")
    parser.add_argument("repo_root", nargs="?", default=".", help="Root directory of the skill or repo (default: .)")
    parser.add_argument("--assets-dir", default="assets", help="Relative path to assets directory (default: assets)")
    parser.add_argument("--delete-orphans", action="store_true", help="Delete orphaned asset files directly")
    parser.add_argument("--json", action="store_true", help="Output pure JSON format")

    args = parser.parse_args()
    root_path = Path(args.repo_root).resolve()
    assets_path = (root_path / args.assets_dir).resolve()

    result = analyze_assets(root_path, assets_path, delete_orphans=args.delete_orphans)

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        status_str = "[PASS]" if result.get("passed") else "[WARN]"
        print(f"\n{status_str} Asset Hygiene & Orphan Scanner — Scanned: {result.get('total_assets_scanned', 0)} assets ({result.get('total_size_bytes', 0):,} bytes)")
        print(f"Orphaned Assets: {result.get('orphaned_count', 0)} | Duplicate Assets: {result.get('duplicates_count', 0)}\n")

        if result.get("duplicates"):
            print("  ⚠️ Duplicate Assets Found:")
            for d in result["duplicates"]:
                print(f"    - {d['file']} (Duplicate of {d['duplicate_of']}, size: {d['size_bytes']:,} B)")

        if result.get("orphaned_files"):
            print("  ⚠️ Orphaned Assets (Not linked in any .md):")
            for o in result["orphaned_files"]:
                del_str = " [DELETED]" if o.get("deleted") else ""
                print(f"    - {o['file']} ({o['size_bytes']:,} B){del_str}")

        if result.get("webp_optimization_candidates"):
            print("\n  💡 WebP Optimization Recommendations (>50KB PNG/JPG):")
            for w in result["webp_optimization_candidates"]:
                print(f"    - {w['file']} (Current: {w['current_size_bytes']:,} B -> Est. WebP: {w['estimated_webp_bytes']:,} B, Save: ~{w['estimated_savings_bytes']:,} B)")

        print()

    sys.exit(0 if result.get("passed") else 1)

if __name__ == "__main__":
    main()
