#!/usr/bin/env python3
"""Generate docs/.pages based on subfolder metadata using nav entries.

This utility scans each category folder under docs/, reads its .pages title,
and groups folders by the part before the Japanese divider "｜". The order of
categories is detected automatically: the existing docs/.pages navigation order
is reused when possible, otherwise categories follow discovery order based on
folder names.
"""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Dict, List, Tuple


def extract_category_from_pages(pages_path: Path) -> str | None:
    """Return the category name extracted from a .pages file."""
    try:
        for raw_line in pages_path.read_text(encoding="utf-8").splitlines():
            line = raw_line.lstrip("\ufeff").strip()
            if not line.startswith("title:"):
                continue
            title = line.split(":", 1)[1].strip().strip('"').strip("'")
            if not title:
                return None
            category, _, _ = title.partition("｜")
            return category or None
    except FileNotFoundError:
        return None
    return None


def collect_category_mapping(docs_dir: Path) -> Tuple[Dict[str, List[str]], List[str]]:
    """Build a dictionary mapping category names to folder paths and track order."""
    mapping: Dict[str, List[str]] = {}
    category_order: List[str] = []

    for child in sorted(docs_dir.iterdir(), key=lambda p: p.name):
        if not child.is_dir():
            continue
        if child.name.startswith('.'):
            continue
        if child.name in {"assets", "stylesheets"}:
            continue

        pages_file = child / ".pages"
        category = extract_category_from_pages(pages_file)
        if not category:
            continue

        if category not in mapping:
            mapping[category] = []
            category_order.append(category)

        mapping[category].append(child.name.replace('\\', '/'))

    for paths in mapping.values():
        paths.sort(reverse=True)

    return mapping, category_order


def read_existing_category_order(root_pages_path: Path) -> List[str]:
    """Extract the current top-level section order from docs/.pages nav structure."""
    if not root_pages_path.is_file():
        return []

    order: List[str] = []
    for raw_line in root_pages_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.lstrip("\ufeff").strip()
        if not line.startswith("- "):
            continue
        entry = line[2:]
        if entry == "index.md":
            continue
        if entry.endswith(":"):
            name = entry[:-1].strip()
            if name:
                order.append(name)
    return order


def build_root_pages_content(mapping: Dict[str, List[str]], ordered_categories: List[str]) -> str:
    """Create the YAML content for docs/.pages nav."""
    lines: List[str] = ["nav:", "  - index.md"]

    for category in ordered_categories:
        paths = mapping.get(category)
        if not paths:
            continue
        lines.append(f"  - {category}:")
        for path in paths:
            lines.append(f"      - path: {path}")

    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate docs/.pages from subfolders")
    parser.add_argument("docs_dir", nargs="?", default="docs", help="MkDocs docs directory")
    args = parser.parse_args()

    docs_dir = Path(args.docs_dir).resolve()
    if not docs_dir.is_dir():
        raise SystemExit(f"Docs directory not found: {docs_dir}")

    mapping, discovered_order = collect_category_mapping(docs_dir)
    root_pages_path = docs_dir / ".pages"
    existing_order = read_existing_category_order(root_pages_path)

    ordered_categories = [cat for cat in existing_order if cat in mapping]
    for cat in discovered_order:
        if cat not in ordered_categories:
            ordered_categories.append(cat)

    content = build_root_pages_content(mapping, ordered_categories)
    root_pages_path.write_text(content, encoding="utf-8")
    print(f"Updated {root_pages_path} with {len(mapping)} categories.")


if __name__ == "__main__":
    main()
