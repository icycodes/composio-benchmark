import os
import shutil
import pytest

def test_composio_binary_available():
    assert shutil.which("composio") is not None, "composio binary not found in PATH."

def test_composio_api_key_set():
    assert "COMPOSIO_API_KEY" in os.environ, "COMPOSIO_API_KEY environment variable is not set."

def test_home_directory_exists():
    assert os.path.isdir("/home/user"), "/home/user directory does not exist."
