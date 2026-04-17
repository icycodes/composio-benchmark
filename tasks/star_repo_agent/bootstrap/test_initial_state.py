import os
import shutil
import pytest

def test_gh_cli_available():
    assert shutil.which("gh") is not None, "gh CLI not found in PATH."

def test_composio_api_key_set():
    assert "COMPOSIO_API_KEY" in os.environ, "COMPOSIO_API_KEY environment variable is not set."

def test_openai_api_key_set():
    assert "OPENAI_API_KEY" in os.environ, "OPENAI_API_KEY environment variable is not set."
