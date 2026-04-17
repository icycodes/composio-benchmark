import os
import subprocess
import json
import pytest

def get_trial_id():
    with open("/logs/trial_id", "r") as f:
        return f.read().strip()

def test_github_file_content():
    trial_id = get_trial_id()
    repo_name = f"zealt-user01/multi-test-{trial_id}"
    
    result = subprocess.run([
        "gh", "file", "view", "harbor.txt", "--repo", repo_name
    ], capture_output=True, text=True)
    assert result.returncode == 0
    expected_content = f"Harbor trial {trial_id}"
    assert expected_content in result.stdout

def test_slack_message():
    trial_id = get_trial_id()
    slack_token = os.environ["SLACK_TOKEN"]
    
    # Get general channel ID
    result = subprocess.run([
        "curl", "-sS", "-H", f"Authorization: Bearer {slack_token}",
        "https://slack.com/api/conversations.list?types=public_channel"
    ], capture_output=True, text=True)
    assert result.returncode == 0
    data = json.loads(result.stdout)
    channels = data.get("channels", [])
    general_channel = next((c for c in channels if c["name"] == "general"), None)
    assert general_channel is not None
    
    channel_id = general_channel["id"]
    
    # Check history
    result = subprocess.run([
        "curl", "-sS", "-H", f"Authorization: Bearer {slack_token}",
        f"https://slack.com/api/conversations.history?channel={channel_id}&limit=20"
    ], capture_output=True, text=True)
    assert result.returncode == 0
    data = json.loads(result.stdout)
    messages = data.get("messages", [])
    expected_message = f"File harbor.txt created in trial {trial_id}"
    message_texts = [m.get("text") for m in messages]
    assert any(expected_message in text for text in message_texts if text)
