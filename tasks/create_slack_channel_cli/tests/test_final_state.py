import os
import subprocess
import json
import pytest

def get_trial_id():
    with open("/logs/trial_id", "r") as f:
        return f.read().strip()

def test_slack_channel_and_message():
    trial_id = get_trial_id()
    channel_name = f"test-chan-{trial_id}"
    slack_token = os.environ["SLACK_TOKEN"]
    
    # 1. Verify channel exists
    result = subprocess.run([
        "curl", "-sS", "-H", f"Authorization: Bearer {slack_token}",
        "https://slack.com/api/conversations.list?types=public_channel"
    ], capture_output=True, text=True)
    assert result.returncode == 0
    data = json.loads(result.stdout)
    assert data.get("ok"), f"Slack API error: {data}"
    
    channels = data.get("channels", [])
    channel = next((c for c in channels if c["name"] == channel_name), None)
    assert channel is not None, f"Slack channel {channel_name} not found."
    
    channel_id = channel["id"]
    
    # 2. Verify message exists
    result = subprocess.run([
        "curl", "-sS", "-H", f"Authorization: Bearer {slack_token}",
        f"https://slack.com/api/conversations.history?channel={channel_id}&limit=10"
    ], capture_output=True, text=True)
    assert result.returncode == 0
    data = json.loads(result.stdout)
    assert data.get("ok"), f"Slack API error: {data}"
    
    messages = data.get("messages", [])
    expected_message = f"Welcome to Harbor trial {trial_id}"
    message_texts = [m.get("text") for m in messages]
    assert expected_message in message_texts, f"Expected message '{expected_message}' not found in channel history."
