import os
import subprocess
import json
import pytest

def get_trial_id():
    with open("/logs/trial_id", "r") as f:
        return f.read().strip()

def test_github_repo_description():
    trial_id = get_trial_id()
    repo_name = f"zealt-user01/desc-test-{trial_id}"
    
    result = subprocess.run([
        "gh", "repo", "view", repo_name, "--json", "description"
    ], capture_output=True, text=True)
    assert result.returncode == 0
    data = json.loads(result.stdout)
    expected_description = f"Harbor trial {trial_id} repo"
    assert data.get("description") == expected_description
