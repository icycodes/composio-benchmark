import os
import subprocess
import json
import pytest

def get_trial_id():
    with open("/logs/trial_id", "r") as f:
        return f.read().strip()

def test_repo_exists_and_starred():
    trial_id = get_trial_id()
    repo_name = f"zealt-user01/star-test-{trial_id}"
    
    # Check if repo exists
    result = subprocess.run(
        ["gh", "repo", "view", repo_name, "--json", "isStargazer"],
        capture_output=True, text=True
    )
    assert result.returncode == 0, f"gh repo view failed: {result.stderr}"
    
    data = json.loads(result.stdout)
    assert data.get("isStargazer") is True, f"Repository {repo_name} is not starred by zealt-user01."
