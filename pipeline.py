"""Load Jira documentation exports for the ingestion pipeline."""

import json
import re
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path


# --- loader ---
def load_documents(exports_dir: Path) -> list[dict]:
    """Load documents from JSON exports under the given directory."""
    documents = []
    for export_path in sorted(exports_dir.rglob("*.json")):
        with export_path.open(encoding="utf-8") as export_file:
            export = json.load(export_file)
        pages = export["docs"]
        declared_count = export.get("record_count")
        if declared_count is not None and declared_count != len(pages):
            print(
                f"FLAG record_count mismatch in {export_path.name}: "
                f"declared {declared_count}, found {len(pages)} pages in docs"
            )
        documents.extend(pages)
    return documents

def load_pages(exports_dir):
    for path in sorted(exports_dir.glob("*.md")):
        page = parse_front_matter(path)
        fields = page["source_file"], page["title"], page["url"]
        dates, heads = page["last_updated"], page["headings"]
        print(inventory_line(page))

def body_metadata_flags(page: dict) -> list[tuple[str, str]]:
    """Compare repeated lineage values in this export's flat front matter and H1."""
    body = page.get("body_markdown")
    if not isinstance(body, str):
        return []
    lines = body.splitlines()
    flags = []
    content_start = 0
    if lines and lines[0] == "---" and "---" in lines[1:]:
        content_start = lines.index("---", 1) + 1
        field_names = {"title": "title", "source_url": "url", "last_updated": "last_updated"}
        for line in lines[1:content_start - 1]:
            key, separator, value = line.partition(":")
            field = field_names.get(key.strip())
            if not separator or field is None:
                continue
            value = value.strip()
            # The export uses flat scalar metadata, not nested YAML.
            if len(value) >= 2 and value[0] == value[-1] and value[0] in ("'", '"'):
                value = value[1:-1]
            if field in page and page[field] != value:
                flags.append((field, f"disagrees with body_markdown front matter {key.strip()}: "
                              f"record={json.dumps(page[field], ensure_ascii=False)}, "
                              f"body={json.dumps(value, ensure_ascii=False)}"))
    for line in lines[content_start:]:
        if line.startswith("# "):
            title = re.sub(r"\s+#+\s*$", "", line[2:].strip())
            if "title" in page and page["title"] != title:
                flags.append(("title", "disagrees with body_markdown H1: "
                              f"record={json.dumps(page['title'], ensure_ascii=False)}, "
                              f"body={json.dumps(title, ensure_ascii=False)}"))
            break
    return flags


def page_flags(page: dict, url_pages: dict | None = None) -> list[tuple[str, str]]:
    """Return lineage gaps without repairing or coercing export values."""
    flags = []
    for field in ("source_file", "title", "url"):
        value = page.get(field)
        if field not in page:
            flags.append((field, "missing"))
        elif value is None or value == "":
            flags.append((field, "empty"))
        elif not isinstance(value, str) or not value.strip():
            flags.append((field, "must be a non-empty string"))

    updated = page.get("last_updated")
    if "last_updated" not in page:
        flags.append(("last_updated", "missing"))
    elif updated is None or (isinstance(updated, str) and not updated.strip()):
        flags.append(("last_updated", "empty"))
    else:
        try:
            if not isinstance(updated, str) or not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", updated):
                raise ValueError
            date.fromisoformat(updated)
        except ValueError:
            flags.append(("last_updated", "must be a real ISO date (YYYY-MM-DD)"))

    headings = page.get("headings")
    if "headings" not in page:
        flags.append(("headings", "missing"))
    elif headings is None or headings == "" or headings == []:
        flags.append(("headings", "empty"))
    elif not isinstance(headings, list):
        flags.append(("headings", "not a list"))
    else:
        body = page.get("body_markdown")
        if not isinstance(body, str):
            flags.append(("headings", "cannot compare: body_markdown missing or not text"))
        else:
            # Compare every Markdown heading, including the H1, in source order.
            body_headings = [
                re.sub(r"\s+#+\s*$", "", line.lstrip("#").strip())
                for line in body.splitlines()
                if line.startswith("#")
            ]
            if headings != body_headings:
                flags.append(("headings", "disagree with body_markdown"))
    # Decode only for diagnostics; preserve the exported value and its type flag.
    diagnostic_headings = headings
    if isinstance(headings, str):
        try:
            diagnostic_headings = json.loads(headings)
        except json.JSONDecodeError:
            pass
    if isinstance(diagnostic_headings, list):
        repeated = [text for text, count in Counter(
            h for h in diagnostic_headings if isinstance(h, str)
        ).items() if count > 1]
        if repeated:
            flags.append(("headings", "duplicate section headings: " + json.dumps(repeated, ensure_ascii=False)))
    url = page.get("url")
    if url_pages and isinstance(url, str) and len(url_pages.get(url, [])) > 1:
        flags.append(("url", "shared by pages: " + json.dumps(url_pages[url], ensure_ascii=False)))
    flags.extend(body_metadata_flags(page))
    return flags


def print_inventory(documents: list[dict]) -> None:
    """Print one inventory line per page, its flags, and explicit totals."""
    counts = dict.fromkeys(("source_file", "title", "url", "last_updated", "headings"), 0)
    url_pages = defaultdict(list)
    for page in documents:
        url = page.get("url")
        if isinstance(url, str) and url.strip():
            url_pages[url].append({"title": page.get("title"), "source_file": page.get("source_file")})
    flagged_pages = 0
    for page in documents:
        fields = ("source_file", "title", "url", "last_updated", "headings")
        print("PAGE " + " | ".join(
            f"{field}={json.dumps(page.get(field), ensure_ascii=False)}"
            for field in fields
        ))
        flags = page_flags(page, url_pages)
        flagged_pages += bool(flags)
        for field, reason in flags:
            print(f"FLAG {field} {reason}")
        for field in {field for field, _ in flags}:
            counts[field] += 1
    print(f"Total pages: {len(documents)}")
    print(f"Pages with lineage gaps: {flagged_pages}")
    for field, count in counts.items():
        print(f"{field} gaps: {count}")


# --- chunker ---
# Comes in a later stage.


# --- embed ---
# Comes in a later stage.


# --- upsert ---
# Comes in a later stage.


if __name__ == "__main__":
    documents = load_documents(Path(__file__).parent / "exports" / "jira-help-2025-03-07")
    print_inventory(documents)
