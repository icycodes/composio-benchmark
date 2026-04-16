import os
import subprocess
import pytest

LOG_FILE = "/home/user/toolkits.log"

def test_toolkits_log_exists():
    assert os.path.isfile(LOG_FILE), f"Log file {LOG_FILE} not found."

def test_toolkits_log_content():
    # Priority 1: Use CLI to verify
    result = subprocess.run(
        ["composio", "toolkits", "list", "--connected"],
        capture_output=True, text=True
    )
    assert result.returncode == 0, f"composio toolkits list failed: {result.stderr}"
    
    with open(LOG_FILE, "r") as f:
        log_content = f.read()
    
    # Check if the log contains similar information as the CLI output
    # Since formatting might vary slightly, we check for presence of key words or just exact match if expected
    assert result.stdout.strip() in log_content or log_content.strip() in result.stdout, \
        "Log file content does not match 'composio toolkits list --connected' output."
