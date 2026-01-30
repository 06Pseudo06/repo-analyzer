import sqlite3
from pathlib import Path

DB_PATH = Path("data/repos.db")
SCHEMA_PATH = Path("database/schema.sql")


def get_connection():
    DB_PATH.parent.mkdir(exist_ok=True)
    return sqlite3.connect(DB_PATH)


def initialize_db():
    conn = get_connection()
    with open(SCHEMA_PATH, "r") as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()


def insert_repositories(repos):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT OR REPLACE INTO repositories (
        repo_id, name, full_name, language,
        stars, forks, open_issues,
        last_updated, url
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """

    data = [
        (
            r["repo_id"],
            r["name"],
            r["full_name"],
            r["language"],
            r["stars"],
            r["forks"],
            r["open_issues"],
            r["last_updated"],
            r["url"]
        )
        for r in repos
    ]

    cursor.executemany(query, data)
    conn.commit()
    conn.close()
