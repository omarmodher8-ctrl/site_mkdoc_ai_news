from pathlib import Path
path = Path('macros/home.py')
text = path.read_text(encoding='utf-8')
old_block = "# Fallback labels when navigation titles are unavailable\r\nCATEGORY_BASE_LABELS: Dict[str, str] = {\r\n    \"ai-generated-news\": \"生成AIニュース\",\r\n    \"ai-overview-news\": \"AI概況ニュース\",\r\n}\r\n\r\n"
if old_block not in text:
    raise SystemExit('expected block not found')
text = text.replace(old_block, '', 1)
text = text.replace("            base_label = CATEGORY_BASE_LABELS.get(base, base.replace(\"-\", \" \" ).title())\r\n", "            base_label = base\r\n")
text = text.replace("        return CATEGORY_BASE_LABELS.get(slug, slug.replace(\"-\", \" \" ).title())\r\n", "        return slug\r\n")
path.write_text(text, encoding='utf-8')
