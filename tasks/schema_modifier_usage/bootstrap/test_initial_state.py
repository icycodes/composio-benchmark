import os
import shutil
import pytest

PROJECT_DIR = "/home/user/modifier-task"

def test_composio_installed():
    import subprocess
    result = subprocess.run(["pip3", "show", "composio"], capture_output=True, text=True)
    assert result.returncode == 0, "Composio SDK is not installed."

def test_project_dir_exists():
    assert os.path.isdir(PROJECT_DIR), f"Project directory {PROJECT_DIR} does not exist."

def test_composio_api_key_set():
    assert "COMPOSIO_API_KEY" in os.environ, "COMPOSIO_API_KEY environment variable is not set."
