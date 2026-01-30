import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()

GITHUB_API_URL = "https://api.github.com/search/repositories"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")


def fetch_repositories(keyword, per_page=30, pages=1):
    if not GITHUB_TOKEN:
        raise RuntimeError("GitHub token not found in environment variables")

    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    all_items = []

    for page in range(1, pages + 1):
        params = {
            "q": keyword,
            "sort": "stars",
            "order": "desc",
            "per_page": per_page,
            "page": page
        }

        response = requests.get(GITHUB_API_URL, headers=headers, params=params)

        if response.status_code != 200:
            raise RuntimeError(
                f"GitHub API error {response.status_code}: {response.text}"
            )

        data = response.json()
        all_items.extend(data.get("items", []))

        time.sleep(1)  

    return all_items
