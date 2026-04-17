import os
import shutil
import pytest

def test_node_available():
    assert shutil.which("node") is not None, "node binary not found in PATH."

def test_npm_available():
    assert shutil.which("npm") is not None, "npm binary not found in PATH."

def test_composio_api_key_set():
    assert "COMPOSIO_API_KEY" in os.environ, "COMPOSIO_API_KEY environment variable is not set."
