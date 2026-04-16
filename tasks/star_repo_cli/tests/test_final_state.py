import os
import subprocess
import json
import pytest

def test_repo_is_starred():
    """Priority 1: Use GitHub CLI to verify that the repository is starred."""
    repo = "composiohq/composio"
    # gh api user/starred/{owner}/{repo} returns 204 if starred, 404 if not
    result = subprocess.run(
        ["gh", "api", f"user/starred/{repo}", "--include"],
        capture_output=True, text=True
    )
    # The command might exit with 0 even for 404 depending on how gh api handles it,
    # but usually it returns non-zero for 4xx errors unless --silent is used.
    # We check for "204 No Content" in the output.
    assert "204 No Content" in result.stdout or "204 No Content" in result.stderr, \
        f"Repository {repo} is not starred. Output: {result.stdout} {result.stderr}"

def test_composio_execution_log():
    """Optional: Check if there's any evidence of composio execution if needed, 
    but the primary goal is the effect on GitHub."""
    pass
