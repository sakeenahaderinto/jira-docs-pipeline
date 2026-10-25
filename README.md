# Jira docs ingestion pipeline

A Python pipeline with four labelled sections in `pipeline.py`: loader, chunker,
embed, and upsert. Only the loader is implemented; the remaining sections are
reserved for later stages.

The loader reads every JSON export recursively from `exports/jira-help-2025-03-07/`
and inventories every record in `docs`. It prints the source file, title, URL,
last updated date, and headings, followed by any lineage flags and page/gap totals.
Source files, titles, and URLs must be non-empty strings. Dates must be real calendar dates
in `YYYY-MM-DD` format. Headings must be a non-empty list matching all lines
starting with `#` in the Markdown body, including H1, in order (heading markers
are removed). JSON-encoded strings are flagged as not lists, without coercion.
For diagnostics only, JSON-encoded headings are decoded to flag repeated section titles within a page. Shared URLs are flagged on every affected page with the titles and source files of all matching records. Gap totals count affected pages per field, even when a page has multiple reasons. Fields with no gaps explicitly report zero.
The loader also flags exports whose declared `record_count` differs from the
number of page entries actually present in `docs`.

No external dependencies are required. Use Python 3.10 or newer:

```sh
python pipeline.py
```
