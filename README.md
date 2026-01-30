# Repo Analyzer

Repo Analyzer is an API-driven, deterministic data analysis tool that collects
GitHub repository data, processes it through a structured pipeline, and ranks
repositories using transparent, rule-based scoring logic.

The system is designed to demonstrate real-world data engineering and
cross-language system design rather than opaque AI-based ranking.


## Problem Statement

Public platforms like GitHub expose large volumes of repository data, but they
do not provide explainable, customizable ranking tailored to specific criteria.
Repo Analyzer addresses this by building a reproducible pipeline that ingests
live API data and applies deterministic ranking logic that can be inspected,
modified, and justified.


## Architecture Overview

GitHub REST API
↓
Python Ingestion Layer
↓
Data Normalization
↓
SQLite Storage
↓
CSV Export (Data Contract)
↓
C++ Ranking Engine
↓
CLI Output


Each layer has a single responsibility and communicates through explicit,
inspectable interfaces.


## Tech Stack

- **Python** – API ingestion, normalization, orchestration
- **SQLite** – relational persistence
- **C++ (STL)** – deterministic ranking engine
- **GitHub REST API** – live data source


## Ranking Logic (Explainable)

Repositories are scored using a deterministic formula:

score =
(stars * 0.6)

(forks * 0.3)

(open_issues * 0.1)


This favors:
- popularity (stars)
- adoption (forks)
while penalizing:
- maintenance burden (open issues)

No machine learning models are used; all logic is explicit and adjustable.

## How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Set GitHub token
Create a .env file in the project root:
```bash
GITHUB_TOKEN=your_personal_access_token
```

### 3. Build C++ ranking engine
```bash
g++ -std=c++17 cpp_engine/src/ranker.cpp -o cpp_engine/ranker
```

### 4. Run full pipeline
```bash
python -m scripts.run_pipeline
```

This will:
-fetch live GitHub data
-normalize and store it
-export a CSV contract
-rank repositories using C++
-print ranked results via CLI

## Sample Output
```bash
Top Ranked Repositories
-----------------------
1. donnemartin/system-design-primer | score: 216552
2. vinta/awesome-python            | score: 176538
3. practical-tutorials/project-based-learning | score: 164330
...
```

## Design Philosophy
-Real-world data, not static datasets
-Explainable logic over black-box models
-Clear separation of concerns
-Reproducible, inspectable pipeline

## Possible Extensions
-Time-decay factor for recent activity
-Configurable scoring weights
-Support for additional data domains

## Author
Built as an industrial-style data pipeline project to demonstrate
system design, data engineering, and cross-language integration.


2. Commit it:

```bash
git add README.md
git commit -m "docs: add recruiter-ready project README"
git push
