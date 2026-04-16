import os
import shutil
import pytest

def test_python3_available():
    assert shutil.which("python3") is not None, "python3 binary not found in PATH."

def test_composio_api_key_set():
    assert "COMPOSIO_API_KEY" in os.environ, "COMPOSIO_API_KEY environment variable is not set."

def test_openai_api_key_set():
    assert "OPENAI_API_KEY" in os.environ, "OPENAI_API_KEY environment variable is not set."

def test_slack_token_set():
    assert "SLACK_TOKEN" in os.environ, "SLACK_TOKEN environment variable is not set."
