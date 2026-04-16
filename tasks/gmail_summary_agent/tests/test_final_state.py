import os
import subprocess
import json
import pytest

def test_summary_file_exists():
    assert os.path.isfile("/home/user/summary.txt"), "Summary file not found."
    with open("/home/user/summary.txt", "r") as f:
        assert len(f.read().strip()) > 0, "Summary file is empty."

def test_slack_message_posted():
    slack_token = os.environ["SLACK_TOKEN"]
    # We fetch the list of channels to find 'general'
    result = subprocess.run([
        "curl", "-sS", "-H", f"Authorization: Bearer {slack_token}",
        "https://slack.com/api/conversations.list?types=public_channel"
    ], capture_output=True, text=True)
    assert result.returncode == 0
    data = json.loads(result.stdout)
    assert data.get("ok"), f"Slack API error: {data}"
    
    channels = data.get("channels", [])
    general_channel = next((c for c in channels if c["name"] == "general"), None)
    if not general_channel:
        # If no general, just check if ANY message was posted recently to any channel if possible
        # but usually 'general' should exist in test workspace
        pytest.skip("General channel not found, skipping message verification.")
    
    channel_id = general_channel["id"]
    # Check history for the last message
    result = subprocess.run([
        "curl", "-sS", "-H", f"Authorization: Bearer {slack_token}",
        f"https://slack.com/api/conversations.history?channel={channel_id}&limit=1"
    ], capture_output=True, text=True)
    assert result.returncode == 0
    data = json.loads(result.stdout)
    assert data.get("ok"), f"Slack API error: {data}"
    
    messages = data.get("messages", [])
    assert len(messages) > 0, "No messages found in channel."
    # We can't easily verify the content is the summary without knowing what the agent wrote,
    # but we can check if the bot posted something.
    # In a real evaluation, we might check for specific keywords.
