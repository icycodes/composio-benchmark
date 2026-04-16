import os
import subprocess
import json
import pytest

TRIAL_ID_FILE = "/logs/trial_id"
CHANNEL_BASENAME = "sentiment"

def get_trial_id():
    with open(TRIAL_ID_FILE, "r") as f:
        return f.read().strip()

def test_slack_channel_and_sentiment_message():
    """Priority 1: Use Slack API to verify the sentiment analysis message."""
    trial_id = get_trial_id()
    channel_name = f"{CHANNEL_BASENAME}-{trial_id}"
    slack_token = os.environ["SLACK_TOKEN"]
    
    # 1. Get channel ID
    result = subprocess.run([
        "curl", "-sS", "-H", f"Authorization: Bearer {slack_token}",
        "https://slack.com/api/conversations.list?limit=200&types=public_channel,private_channel"
    ], capture_output=True, text=True)
    data = json.loads(result.stdout)
    channel_id = next((c["id"] for c in data.get("channels", []) if c["name"] == channel_name), None)
    assert channel_id, f"Channel ID for '{channel_name}' not found."
    
    # 2. Get history
    result = subprocess.run([
        "curl", "-sS", "-H", f"Authorization: Bearer {slack_token}",
        f"https://slack.com/api/conversations.history?channel={channel_id}&limit=10"
    ], capture_output=True, text=True)
    history = json.loads(result.stdout)
    assert history.get("ok"), f"Slack API error: {history}"
    
    messages = history.get("messages", [])
    assert len(messages) > 0, f"No messages found in channel '{channel_name}'."
    
    # 3. Check for sentiment analysis content (expected: "Positive")
    all_text = " ".join([m.get("text", "") for m in messages])
    assert "Positive" in all_text, \
        f"Expected 'Positive' sentiment in channel '{channel_name}', but content looks wrong: {all_text}"

def test_script_uses_trigger():
    """Priority 3 fallback: verify use of trigger subscription in the script."""
    script_file = "/home/user/trigger-task/trigger_agent.py"
    assert os.path.isfile(script_file), f"Script not found at {script_file}"
    with open(script_file, 'r') as f:
        content = f.read()
    assert "subscribe" in content or "trigger" in content.lower(), \
        f"Expected use of trigger subscription in {script_file}, but it's not found."

def test_repo_is_created():
    """Priority 1: Use GitHub CLI to verify the repository exists."""
    trial_id = get_trial_id()
    repo_name = f"harbor-trigger-{trial_id}"
    username = "zealt-user01"
    
    result = subprocess.run(
        ["gh", "repo", "view", f"{username}/{repo_name}", "--json", "name"],
        capture_output=True, text=True
    )
    assert result.returncode == 0, f"gh repo view failed: {result.stderr}"
