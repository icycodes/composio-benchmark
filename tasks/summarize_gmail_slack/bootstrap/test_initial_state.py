import os
import shutil
import subprocess
import pytest

PROJECT_DIR = "/home/user/summarize-task"

def test_node_installed():
    assert shutil.which("node") is not None, "Node.js is not installed."

def test_npm_installed():
    assert shutil.which("npm") is not None, "npm is not installed."

def test_project_dir_exists():
    assert os.path.isdir(PROJECT_DIR), f"Project directory {PROJECT_DIR} does not exist."

def test_composio_api_key_set():
    assert "COMPOSIO_API_KEY" in os.environ, "COMPOSIO_API_KEY environment variable is not set."

def test_slack_token_set():
    assert "SLACK_TOKEN" in os.environ, "SLACK_TOKEN environment variable is not set."
