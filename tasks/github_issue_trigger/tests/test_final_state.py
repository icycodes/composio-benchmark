import os
import subprocess
import json
import pytest

def get_trial_id():
    with open("/logs/trial_id", "r") as f:
        return f.read().strip()

def test_triggers_log_exists():
    assert os.path.isfile("/home/user/triggers.log"), "Triggers log file not found."

def test_trigger_is_active():
    trial_id = get_trial_id()
    repo_name = f"star-test-{trial_id}"
    
    with open("/home/user/triggers.log", "r") as f:
        content = f.read()
    
    # Check if the log contains the repo name and 'active' status
    assert repo_name in content, f"Trigger for repository {repo_name} not found in log."
    assert "active" in content.lower(), "No active trigger found in log."
