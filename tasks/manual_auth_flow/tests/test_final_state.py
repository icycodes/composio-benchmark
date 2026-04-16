import os
import pytest

PROJECT_DIR = "/home/user/auth-task"
REDIRECT_FILE = os.path.join(PROJECT_DIR, "redirect.url")

def test_redirect_file_exists():
    assert os.path.isfile(REDIRECT_FILE), f"Redirect URL file {REDIRECT_FILE} not found."

def test_redirect_url_content():
    with open(REDIRECT_FILE, "r") as f:
        url = f.read().strip()
    assert url.startswith("https://connect.composio.dev/link/"), f"Invalid redirect URL: {url}"
