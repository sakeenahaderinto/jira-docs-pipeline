# Jira docs ingestion pipeline

A Python pipeline with four labelled sections in `pipeline.py`: loader, chunker,
embed, and upsert. Only the loader is implemented; the remaining sections are
reserved for later stages.

The loader reads JSON files recursively from `exports/` and collects their `docs`
records. No external dependencies are required. Use Python 3.10 or newer:

```sh
python pipeline.py
```
