import os
import subprocess
import json
import pytest

def get_trial_id():
    with open("/logs/trial_id", "r") as f:
        return f.read().strip()

def test_github_repo_is_starred():
    trial_id = get_trial_id()
    repo_name = f"zealt-user01/discovery-test-{trial_id}"
    
    result = subprocess.run([
        "gh", "repo", "view", repo_name, "--json", "isStargazer"
    ], capture_output=True, text=True)
    assert result.returncode == 0
    data = json.loads(result.stdout)
    assert data.get("isStargazer") is True, f"Repository {repo_name} is not starred by zealt-user01."
