import os
import shutil
import subprocess
import pytest

def test_python_packages_available():
    import importlib
    packages = ["composio", "composio_openai", "openai"]
    for pkg in packages:
        try:
            importlib.import_module(pkg)
        except ImportError:
            pytest.fail(f"Python package '{pkg}' not found.")

def test_gh_cli_available():
    assert shutil.which("gh") is not None, "gh CLI not found in PATH."

def test_api_keys_set():
    assert "COMPOSIO_API_KEY" in os.environ, "COMPOSIO_API_KEY environment variable is not set."
    assert "OPENAI_API_KEY" in os.environ, "OPENAI_API_KEY environment variable is not set."
    assert "GH_TOKEN" in os.environ, "GH_TOKEN environment variable is not set."

def test_working_directory_exists():
    assert os.path.isdir("/home/user"), "/home/user directory not found."
