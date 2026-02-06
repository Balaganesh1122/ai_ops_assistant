import os
import requests

GITHUB_API = "https://api.github.com"

def search_repositories(query: str, top_k: int = 5):
    token = os.getenv("GITHUB_TOKEN")
    headers = {"Authorization": f"token {token}"} if token else {}

    url = f"{GITHUB_API}/search/repositories?q={query}&sort=stars&order=desc&per_page={top_k}"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return {"error": response.text}

    data = response.json()
    results = []
    for item in data.get("items", []):
        results.append({
            "name": item["full_name"],
            "stars": item["stargazers_count"],
            "url": item["html_url"],
            "description": item["description"]
        })
    return results
