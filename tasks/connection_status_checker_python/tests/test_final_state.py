import os
import json
import pytest

def test_github_status_exists():
    assert os.path.isfile("/home/user/github_status.json"), "GitHub status file not found."

def test_github_is_connected():
    with open("/home/user/github_status.json", "r") as f:
        status = json.load(f)
    
    # Check for status 'CONNECTED' in the connection object
    # The user should have saved the correct connection object
    assert "CONNECTED" in str(status).upper()
