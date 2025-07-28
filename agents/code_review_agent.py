import subprocess
from utils.github_utils import clone_github_repo

def code_review_agent(file_path=None, repo_url=None):
    if repo_url:
        repo_path = clone_github_repo(repo_url)
        target = repo_path
    else:
        target = file_path

    result = subprocess.run(["flake8", target], capture_output=True, text=True)
    issues = result.stdout.splitlines() if result.stdout else []
    suggestions = ["Refactor long functions", "Add docstrings"]
    return {"issues": issues or ["No major issues found"], "suggestions": suggestions}
