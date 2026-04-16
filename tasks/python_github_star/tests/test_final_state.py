import os
import subprocess
import json
import pytest

TRIAL_ID_FILE = "/logs/trial_id"

def get_trial_id():
    with open(TRIAL_ID_FILE, "r") as f:
        return f.read().strip()

def test_repo_is_created_and_starred():
    """Priority 1: Use GitHub CLI to verify the repository state."""
    trial_id = get_trial_id()
    repo_name = f"harbor-gh-star-{trial_id}"
    username = "zealt-user01"
    
    # 1. Verify repository exists
    result = subprocess.run(
        ["gh", "repo", "view", f"{username}/{repo_name}", "--json", "name"],
        capture_output=True, text=True
    )
    assert result.returncode == 0, \
        f"gh repo view failed: {result.stderr}"
    
    # 2. Verify repository is starred by zealt-user01
    # Check if the repo is in the starred list of the user
    # Or use the specific API endpoint for starring
    # GH API check: GET /user/starred/:owner/:repo returns 204 if starred, 404 if not
    result = subprocess.run(
        ["gh", "api", f"user/starred/{username}/{repo_name}", "--silent"],
        capture_output=True, text=True
    )
    assert result.returncode == 0, \
        f"Expected repository '{repo_name}' to be starred by user, but it's not. Error: {result.stderr}"

def test_python_script_exists():
    """Priority 3 fallback: basic file existence check."""
    assert os.path.isfile("/home/user/star-task/star_repo.py"), \
        "star_repo.py not found at /home/user/star-task/star_repo.py"
