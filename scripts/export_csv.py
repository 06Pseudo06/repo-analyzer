import csv
import sqlite3
from pathlib import Path

DB_PATH = Path("data/repos.db")
OUT_PATH = Path("data/repos.csv")

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
SELECT
    full_name,
    stars,
    forks,
    open_issues
FROM repositories
""")

rows = cursor.fetchall()

OUT_PATH.parent.mkdir(exist_ok=True)

with open(OUT_PATH, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["full_name", "stars", "forks", "open_issues"])
    writer.writerows(rows)

conn.close()

print(f"Exported {len(rows)} repositories to {OUT_PATH}")
