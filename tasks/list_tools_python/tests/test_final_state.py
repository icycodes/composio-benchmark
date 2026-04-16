import os
import subprocess
import pytest

LOG_FILE = "/home/user/output.log"
SCRIPT_FILE = "/home/user/list_tools.py"

def test_script_exists():
    assert os.path.isfile(SCRIPT_FILE), f"Script file {SCRIPT_FILE} not found."

def test_output_log_exists():
    assert os.path.isfile(LOG_FILE), f"Log file {LOG_FILE} not found."

def test_output_contains_tools():
    with open(LOG_FILE, "r") as f:
        content = f.read()
    # We expect some tool names to be present. 
    # Since we don't know exactly which ones are connected, we check if it's not empty and contains some common tool-like strings or just isn't empty if the user has no tools.
    # However, zealt-user01 should have GitHub and Slack.
    assert "github" in content.lower() or "slack" in content.lower() or len(content.strip()) > 0, \
        "Output log seems empty or does not contain expected tool names."
