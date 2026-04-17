import os
import json
import pytest

def test_session_config_exists():
    assert os.path.isfile("/home/user/session_config.json"), "Session config file not found."

def test_session_scopes():
    with open("/home/user/session_config.json", "r") as f:
        config = json.load(f)
    
    # The structure might vary, but we look for the scopes
    # Assuming the user saved the session config or the auth config part
    gh_config = config.get("authConfigs", {}).get("github", {}) or config.get("github", {})
    scopes = gh_config.get("scopes", [])
    
    assert "repo" in scopes
    assert "read:org" in scopes
    assert "user" in scopes
