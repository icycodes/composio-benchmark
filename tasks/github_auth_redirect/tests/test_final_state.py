import os
import pytest

LOG_FILE = "/home/user/auth_url.log"
PROJECT_DIR = "/home/user/project"

def test_auth_url_log_exists():
    assert os.path.isfile(LOG_FILE), f"Log file {LOG_FILE} not found."

def test_auth_url_content():
    with open(LOG_FILE, "r") as f:
        content = f.read()
    assert "https://" in content, "The log file does not contain a valid redirect URL."
