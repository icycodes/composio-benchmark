import os
import subprocess
import json
import pytest

def get_trial_id():
    with open("/logs/trial_id", "r") as f:
        return f.read().strip()

def test_github_issue_comment():
    trial_id = get_trial_id()
    repo_name = f"zealt-user01/issue-test-{trial_id}"
    
    # 1. Get issues with label 'bug'
    result = subprocess.run([
        "gh", "issue", "list", "--repo", repo_name, "--label", "bug", "--json", "number"
    ], capture_output=True, text=True)
    assert result.returncode == 0
    issues = json.loads(result.stdout)
    assert len(issues) > 0, "No issues with label 'bug' found."
    
    issue_number = issues[0]["number"]
    
    # 2. Verify comment on the issue
    result = subprocess.run([
        "gh", "issue", "view", str(issue_number), "--repo", repo_name, "--json", "comments"
    ], capture_output=True, text=True)
    assert result.returncode == 0
    data = json.loads(result.stdout)
    comments = data.get("comments", [])
    expected_comment = f"Fixed in trial {trial_id}"
    comment_bodies = [c.get("body") for c in comments]
    assert any(expected_comment in body for body in comment_bodies), f"Expected comment '{expected_comment}' not found on issue {issue_number}."
