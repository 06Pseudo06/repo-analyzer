import argparse
from asyncio import subprocess
from analyzer.ingestion.github_client import fetch_repositories
from analyzer.processing.normalizer import normalize_repositories
from analyzer.storage.sqlite_store import initialize_db, insert_repositories
subprocess.run(["python", "scripts/run_pipeline.py"])




def main():
    parser = argparse.ArgumentParser(
        prog="repo-analyzer",
        description="Analyze and rank GitHub repositories using deterministic logic"
    )

    parser.add_argument(
        "--keyword",
        type=str,
        required=False,
        help="Keyword or topic to search repositories for"
    )

    parser.add_argument(
        "--top",
        type=int,
        default=10,
        help="Number of top repositories to display"
    )

    args = parser.parse_args()

    if args.keyword:
        print("\nFetching repositories from GitHub...")
        repos = fetch_repositories(args.keyword, pages=1)
        print(f"Fetched {len(repos)} repositories.")

    normalized = normalize_repositories(repos)
    print(f"Normalized {len(normalized)} repositories.")

    initialize_db()
    insert_repositories(normalized)
    print("Stored repositories in database.")




    print("\nRepo Analyzer")
    print("=============")
    print(f"Keyword : {args.keyword}")
    print(f"Top N   : {args.top}")
    print("\n[Phase 1] CLI initialized successfully.")
    print("Next step: GitHub API ingestion.\n")




if __name__ == "__main__":
    main()
