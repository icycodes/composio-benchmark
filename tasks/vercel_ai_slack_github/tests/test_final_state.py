import os
import subprocess
import json
import pytest

trial_id_FILE = "/logs/trial_id"

def get_trial_id():
    with open(trial_id_FILE, "r") as f:
        return f.read().strip()

def test_slack_message_content():
    trial_id = get_trial_id()
    channel_name = f"agent-results-{trial_id}"
    slack_token = os.environ["SLACK_TOKEN"]
    
    # First find the channel ID
    result = subprocess.run([
        "curl", "-sS", "-H", f"Authorization: Bearer {slack_token}",
        "https://slack.com/api/conversations.list?types=public_channel,private_channel"
    ], capture_output=True, text=True)
    assert result.returncode == 0
    data = json.loads(result.stdout)
    assert data.get("ok"), f"Slack API error: {data}"
    
    channel_id = None
    for c in data.get("channels", []):
        if c["name"] == channel_name:
            channel_id = c["id"]
            break
    
    assert channel_id is not None, f"Channel {channel_name} not found."
    
    # Check messages in the channel
    result = subprocess.run([
        "curl", "-sS", "-H", f"Authorization: Bearer {slack_token}",
        f"https://slack.com/api/conversations.history?channel={channel_id}&limit=10"
    ], capture_output=True, text=True)
    assert result.returncode == 0
    history = json.loads(result.stdout)
    assert history.get("ok"), f"Slack API error: {history}"
    
    found = False
    for msg in history.get("messages", []):
        text = msg.get("text", "")
        if "User composiohq has" in text and "repos" in text:
            found = True
            break
    
    assert found, f"Correct summary message not found in channel {channel_name}."
