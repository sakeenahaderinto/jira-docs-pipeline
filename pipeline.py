"""Load Jira documentation exports for the ingestion pipeline."""

import json
from pathlib import Path


# --- loader ---
def load_documents(exports_dir: Path) -> list[dict]:
    """Load documents from JSON exports under the given directory."""
    documents = []
    for export_path in sorted(exports_dir.rglob("*.json")):
        with export_path.open(encoding="utf-8") as export_file:
            export = json.load(export_file)
        documents.extend(export["docs"])
    return documents


# --- chunker ---
# Comes in a later stage.


# --- embed ---
# Comes in a later stage.


# --- upsert ---
# Comes in a later stage.


if __name__ == "__main__":
    documents = load_documents(Path(__file__).parent / "exports")
    print(f"Loaded {len(documents)} Jira documents.")
