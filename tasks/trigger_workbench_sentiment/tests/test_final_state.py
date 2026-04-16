import os
import subprocess
import json
import pytest

PROJECT_DIR = "/home/user/sentiment-task"

def test_trigger_active():
    """Verify that the GitHub issue opened trigger is active."""
    # We use the Composio CLI or SDK to check active triggers
    # For simplicity in test, we use the SDK via a small python snippet
    check_script = """
from composio import Composio
import os
composio = Composio(api_key=os.environ['COMPOSIO_API_KEY'])
active = composio.triggers.list_active(trigger_names=['GITHUB_ISSUE_OPENED_EVENT'])
found = any(t.trigger_name == 'GITHUB_ISSUE_OPENED_EVENT' for t in active.items)
print(found)
"""
    result = subprocess.run(["python3", "-c", check_script], capture_output=True, text=True)
    assert "True" in result.stdout, "GITHUB_ISSUE_OPENED_EVENT trigger is not active."

def test_script_contains_workbench_call():
    script_path = os.path.join(PROJECT_DIR, "sentiment_pipeline.py")
    with open(script_path, "r") as f:
        content = f.read()
    assert "COMPOSIO_REMOTE_WORKBENCH" in content, "Script does not call COMPOSIO_REMOTE_WORKBENCH."
    assert "GITHUB_ADD_LABELS_TO_AN_ISSUE" in content or "run_composio_tool" in content, \
        "Script does not contain logic to add labels."
