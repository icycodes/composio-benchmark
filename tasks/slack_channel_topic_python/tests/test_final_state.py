import os
import subprocess
import json
import pytest

def get_trial_id():
    with open("/logs/trial_id", "r") as f:
        return f.read().strip()

def test_slack_channel_topic():
    trial_id = get_trial_id()
    channel_name = f"topic-test-{trial_id}"
    slack_token = os.environ["SLACK_TOKEN"]
    
    # 1. Verify channel exists and check topic
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
    
    expected_topic = f"Topic for trial {trial_id}"
    actual_topic = channel.get("topic", {}).get("value", "")
    assert actual_topic == expected_topic, f"Expected topic '{expected_topic}', got '{actual_topic}'."
