# Repo Analyzer

A command-line tool that analyzes and ranks GitHub repositories using
transparent, deterministic scoring logic.

## Purpose
To help engineers discover and compare repositories based on activity,
quality, and relevance — without opaque AI models.

## Current Status
Phase 1: CLI skeleton and project structure initialized.

## Planned Pipeline
1. GitHub API ingestion (Python)
2. Data normalization and storage (SQL)
3. Deterministic ranking engine (C++)
4. Ranked output via CLI

## Usage (Current)
```bash
python analyzer/cli.py --keyword python --top 10
