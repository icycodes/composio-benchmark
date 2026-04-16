import os
import subprocess
import json
import pytest

trial_id_FILE = "/logs/trial_id"

def get_trial_id():
    with open(trial_id_FILE, "r") as f:
        return f.read().strip()

def test_repo_and_label_exist():
    trial_id = get_trial_id()
    repo_name = f"custom-repo-{trial_id}"
    username = "zealt-user01"
    
    # Check repo exists
    result = subprocess.run(
        ["gh", "repo", "view", f"{username}/{repo_name}", "--json", "name"],
        capture_output=True, text=True
    )
    assert result.returncode == 0, f"Repository {repo_name} not found."
    
    # Check label exists
    result = subprocess.run(
        ["gh", "api", f"repos/{username}/{repo_name}/labels", "--jq", ".[].name"],
        capture_output=True, text=True
    )
    assert result.returncode == 0, f"Failed to list labels for {repo_name}."
    labels = result.stdout.splitlines()
    assert "custom-label" in labels, f"Label 'custom-label' not found in {repo_name}. Labels: {labels}"
