import os
import shutil
import pytest

def test_composio_cli_available():
    assert shutil.which("composio") is not None, "composio CLI not found in PATH."

def test_gh_cli_available():
    assert shutil.which("gh") is not None, "gh CLI not found in PATH."

def test_composio_api_key_set():
    assert "COMPOSIO_API_KEY" in os.environ, "COMPOSIO_API_KEY environment variable is not set."

def test_gh_token_set():
    assert "GH_TOKEN" in os.environ, "GH_TOKEN environment variable is not set."
