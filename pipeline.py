"""Load Jira documentation exports for the ingestion pipeline."""

import json
import re
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

def page_flags(page: dict) -> list[tuple[str, str]]:
    """Return lineage gaps without repairing or coercing export values."""
    flags = []
    for field in ("source_file", "url"):
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
    return flags


def print_inventory(documents: list[dict]) -> None:
    """Print one inventory line per page, its flags, and explicit totals."""
    counts = dict.fromkeys(("source_file", "url", "last_updated", "headings"), 0)
    flagged_pages = 0
    for page in documents:
        fields = ("source_file", "title", "url", "last_updated", "headings")
        print("PAGE " + " | ".join(
            f"{field}={json.dumps(page.get(field), ensure_ascii=False)}"
            for field in fields
        ))
        flags = page_flags(page)
        flagged_pages += bool(flags)
        for field, reason in flags:
            print(f"FLAG {field} {reason}")
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
