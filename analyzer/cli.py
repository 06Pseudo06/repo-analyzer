import argparse

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

    print("\nRepo Analyzer")
    print("=============")
    print(f"Keyword : {args.keyword}")
    print(f"Top N   : {args.top}")
    print("\n[Phase 1] CLI initialized successfully.")
    print("Next step: GitHub API ingestion.\n")

if __name__ == "__main__":
    main()
