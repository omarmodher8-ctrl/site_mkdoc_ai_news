from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

import yaml
from mkdocs.structure.nav import Navigation, Page


def define_env(env):
    chatter = env.start_chatting("latest-pages")

    def load_source(page: Page) -> Tuple[Dict, List[str]]:
        src_path = getattr(page.file, "abs_src_path", None)
        if not src_path:
            return {}, []
        try:
            text = Path(src_path).read_text(encoding="utf-8")
        except FileNotFoundError:
            chatter(f"Source not found for {page.file.src_path}")
            return {}, []
        lines = text.splitlines()
        front_meta: Dict = {}
        body_start = 0
        if lines and lines[0].strip() == "---":
            front_lines: List[str] = []
            for index, line in enumerate(lines[1:], start=1):
                if line.strip() == "---":
                    body_start = index + 1
                    break
                front_lines.append(line)
            else:
                body_start = len(lines)
            if front_lines:
                try:
                    front_meta = yaml.safe_load("\n".join(front_lines)) or {}
                except yaml.YAMLError as exc:
                    chatter(f"Failed to parse front matter for {page.file.src_path}: {exc}")
        body_lines = lines[body_start:]
        return front_meta, body_lines

    def extract_page_info(page: Page) -> Tuple[Optional[datetime], Optional[str], Optional[str]]:
        page_meta = getattr(page, "meta", {}) or {}
        front_meta, body_lines = load_source(page)
        raw_date = page_meta.get("date") or front_meta.get("date")
        page_date: Optional[datetime]
        if raw_date:
            if isinstance(raw_date, datetime):
                page_date = raw_date
            else:
                try:
                    page_date = datetime.fromisoformat(str(raw_date))
                except ValueError:
                    chatter(f"Skip page {page.file.src_path}: invalid date '{raw_date}'")
                    page_date = None
        else:
            page_date = None
        title = page_meta.get("title") or front_meta.get("title") or page.title
        if not title:
            for line in body_lines:
                stripped = line.strip()
                if stripped.startswith("#"):
                    title = stripped.lstrip("# ")
                    break
        description = page_meta.get("description") or front_meta.get("description")
        if not description:
            src_path = getattr(page.file, "abs_src_path", None)
            if src_path:
                memo_path = Path(src_path).with_suffix(".memo")
                if memo_path.exists():
                    description = memo_path.read_text(encoding="utf-8").strip()
        return page_date, title, description

    def iter_dated_pages(pages: Iterable[Page]):
        for page in pages:
            page_info = extract_page_info(page)
            page_date, title, description = page_info
            if page_date is None:
                continue
            yield page_date, title, description, page

    @env.macro
    def latest_pages(limit: int = 5):
        navigation: Navigation | None = env.variables.get("navigation")
        if navigation is None:
            chatter("No navigation available yet")
            return ""
        dated_pages = list(iter_dated_pages(navigation.pages))
        chatter(f"Found {len(dated_pages)} dated pages")
        dated_pages.sort(key=lambda item: item[0], reverse=True)
        rows = []
        for page_date, title, description, page in dated_pages[:limit]:
            if not title:
                title = page.file.name
            url = getattr(page.file, "src_uri", "") or page.url or page.canonical_url or ""
            if url.endswith("index.html"):
                url = url[:-10]
            date_str = page_date.strftime("%Y-%m-%d")
            row = f"- **{date_str}** | [{title}]({url})"
            if description:
                desc = " ".join(description.strip().split())
                if len(desc) > 120:
                    desc = desc[:117] + "…"
                row += f" — {desc}"
            rows.append(row)
        return "\n".join(rows)
