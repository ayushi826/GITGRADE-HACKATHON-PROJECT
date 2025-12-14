import requests

class GitHubService:
    BASE_URL = "https://api.github.com"

    def fetch_repo(self, owner, repo):
        url = f"{self.BASE_URL}/repos/{owner}/{repo}"
        return requests.get(url).json()

    def fetch_tree(self, owner, repo):
        url = f"{self.BASE_URL}/repos/{owner}/{repo}/git/trees/main?recursive=1"
        return requests.get(url).json()

    def fetch_commits(self, owner, repo):
        url = f"{self.BASE_URL}/repos/{owner}/{repo}/commits"
        return requests.get(url).json()

    def fetch_languages(self, owner, repo):
        url = f"{self.BASE_URL}/repos/{owner}/{repo}/languages"
        return requests.get(url).json()
