from datetime import datetime


def normalize_repository(repo):
    return {
        "repo_id": repo.get("id"),
        "name": repo.get("name"),
        "full_name": repo.get("full_name"),
        "language": repo.get("language"),
        "stars": repo.get("stargazers_count", 0),
        "forks": repo.get("forks_count", 0),
        "open_issues": repo.get("open_issues_count", 0),
        "last_updated": repo.get("updated_at"),
        "url": repo.get("html_url"),
    }


def normalize_repositories(raw_repos):
    return [normalize_repository(repo) for repo in raw_repos]
