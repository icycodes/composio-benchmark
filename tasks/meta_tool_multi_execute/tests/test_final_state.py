import os
import subprocess
import json
import pytest

RESULT_FILE = "/home/user/multi-execute-task/result.json"

def test_result_file_exists():
    """Priority 3 fallback: basic file existence check."""
    assert os.path.isfile(RESULT_FILE), f"Result file not found at {RESULT_FILE}"

def test_result_file_content():
    """Priority 3 fallback: check for correct data in the JSON output."""
    with open(RESULT_FILE, 'r') as f:
        data = json.load(f)
    
    content = json.dumps(data)
    # Check for user profile info (login)
    assert "zealt-user01" in content, f"Expected 'zealt-user01' in results, got: {content}"
    # Check for issue info (slug or title)
    assert "issue" in content.lower(), f"Expected issue data in results, got: {content}"

def test_repo_is_starred():
    """Priority 1: Use GitHub CLI to verify the repository is starred."""
    username = "zealt-user01"
    repo = "ComposioHQ/composio"
    
    result = subprocess.run(
        ["gh", "api", f"user/starred/{repo}", "--silent"],
        capture_output=True, text=True
    )
    assert result.returncode == 0, \
        f"Expected repository '{repo}' to be starred by user, but it's not. Error: {result.stderr}"

def test_script_uses_multi_execute():
    """Priority 3 fallback: verify use of MULTI_EXECUTE_TOOL in the script."""
    script_file = "/home/user/multi-execute-task/multi_execute.py"
    assert os.path.isfile(script_file), f"Script not found at {script_file}"
    with open(script_file, 'r') as f:
        content = f.read()
    assert "MULTI_EXECUTE_TOOL" in content or "multi_execute" in content.lower(), \
        f"Expected use of MULTI_EXECUTE_TOOL in {script_file}, but it's not found."
