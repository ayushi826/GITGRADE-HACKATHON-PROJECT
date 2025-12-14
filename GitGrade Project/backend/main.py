from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from github_service import GitHubService
from analyzer import Analyzer
from scorer import Scorer
from ai_writer import AIWriter

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/analyze")
def analyze(url: str):
    owner, repo = url.replace("https://github.com/", "").split("/")

    github = GitHubService()
    analyzer = Analyzer()
    scorer = Scorer()
    writer = AIWriter()

    repo_data = github.fetch_repo(owner, repo)
    tree_data = github.fetch_tree(owner, repo)
    commits = github.fetch_commits(owner, repo)
    languages = github.fetch_languages(owner, repo)

    structure = analyzer.analyze_structure(tree_data)
    commit_data = analyzer.analyze_commits(commits)

    score = scorer.calculate_final_score(structure, commit_data, languages)
    level = scorer.level(score)

    summary = writer.generate_summary(score, structure, commit_data)
    roadmap = writer.generate_roadmap(structure, commit_data)

    return {
        "score": score,
        "level": level,
        "summary": summary,
        "roadmap": roadmap
    }
