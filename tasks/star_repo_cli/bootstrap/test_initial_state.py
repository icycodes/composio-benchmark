import os
import shutil
import subprocess
import pytest

PROJECT_DIR = "/home/user/star-task"

def test_composio_binary_available():
    assert shutil.which("composio") is not None, "composio binary not found in PATH."

def test_gh_binary_available():
    assert shutil.which("gh") is not None, "gh binary not found in PATH."

def test_project_dir_exists():
    assert os.path.isdir(PROJECT_DIR), f"Project directory {PROJECT_DIR} does not exist."

def test_composio_api_key_set():
    assert "COMPOSIO_API_KEY" in os.environ, "COMPOSIO_API_KEY environment variable is not set."

def test_gh_token_set():
    assert "GH_TOKEN" in os.environ, "GH_TOKEN environment variable is not set."
