import os
import subprocess
import json
import pytest

SCRIPT_FILE = "/home/user/multi-account-task/multi_slack.py"

def test_script_exists():
    """Priority 3 fallback: basic file existence check."""
    assert os.path.isfile(SCRIPT_FILE), f"Script not found at {SCRIPT_FILE}"

def test_script_enables_multi_account():
    """Priority 3 fallback: verify multi_account mode is enabled in the script."""
    with open(SCRIPT_FILE, 'r') as f:
        content = f.read()
    assert "multi_account" in content and "True" in content, \
        f"Expected multi_account mode to be enabled in {SCRIPT_FILE}."

def test_script_uses_aliases():
    """Priority 3 fallback: verify use of aliases in the script."""
    with open(SCRIPT_FILE, 'r') as f:
        content = f.read()
    assert "work-slack" in content, f"Expected alias 'work-slack' in {SCRIPT_FILE}."
    assert "personal-slack" in content, f"Expected alias 'personal-slack' in {SCRIPT_FILE}."

def test_slack_messages_sent():
    """Priority 1: Use Slack API to verify both messages were sent."""
    slack_token = os.environ["SLACK_TOKEN"]
    
    # 1. Get channel ID for #general
    result = subprocess.run([
        "curl", "-sS", "-H", f"Authorization: Bearer {slack_token}",
        "https://slack.com/api/conversations.list?types=public_channel"
    ], capture_output=True, text=True)
    data = json.loads(result.stdout)
    channel_id = next((c["id"] for c in data.get("channels", []) if c["name"] == "general"), None)
    assert channel_id, "Channel #general not found."
    
    # 2. Get history and check for both messages
    result = subprocess.run([
        "curl", "-sS", "-H", f"Authorization: Bearer {slack_token}",
        f"https://slack.com/api/conversations.history?channel={channel_id}&limit=20"
    ], capture_output=True, text=True)
    history = json.loads(result.stdout)
    messages = [m.get("text", "") for m in history.get("messages", [])]
    
    assert "Hello from Work!" in messages, "Message 'Hello from Work!' not found in Slack."
    assert "Hello from Personal!" in messages, "Message 'Hello from Personal!' not found in Slack."
