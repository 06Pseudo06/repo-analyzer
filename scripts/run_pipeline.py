import subprocess
from analyzer.ingestion.github_client import fetch_repositories
from analyzer.processing.normalizer import normalize_repositories
from analyzer.storage.sqlite_store import initialize_db, insert_repositories

KEYWORD = "python"
PAGES = 1

def run():
    print("=== Repo Analyzer Pipeline ===")

    print("[1] Fetching data from GitHub...")
    raw = fetch_repositories(KEYWORD, pages=PAGES)

    print("[2] Normalizing data...")
    normalized = normalize_repositories(raw)

    print("[3] Initializing database...")
    initialize_db()

    print("[4] Persisting data...")
    insert_repositories(normalized)

    print("[5] Exporting CSV...")
    subprocess.run(
        ["python", "scripts/export_csv.py"],
        check=True
    )

    print("[6] Running C++ ranking engine...\n")
    subprocess.run(
        ["cpp_engine/ranker.exe"] if subprocess.os.name == "nt"
        else ["./cpp_engine/ranker"],
        check=True
    )

if __name__ == "__main__":
    run()
