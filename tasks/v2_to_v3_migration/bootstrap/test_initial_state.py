import os
import shutil
import pytest

def test_old_script_exists():
    assert os.path.isfile("/home/user/old_script.py"), "old_script.py not found."

def test_composio_api_key_set():
    assert "COMPOSIO_API_KEY" in os.environ, "COMPOSIO_API_KEY environment variable is not set."

def test_python3_available():
    assert shutil.which("python3") is not None, "python3 binary not found in PATH."
