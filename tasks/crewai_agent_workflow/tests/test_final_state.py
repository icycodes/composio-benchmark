import os
import subprocess
import json
import pytest

SCRIPT_FILE = "/home/user/crewai-task/crew_workflow.py"

def test_script_exists():
    """Priority 3 fallback: basic file existence check."""
    assert os.path.isfile(SCRIPT_FILE), f"Script not found at {SCRIPT_FILE}"

def test_script_uses_crewai_provider():
    """Priority 3 fallback: verify use of CrewAIProvider in the script."""
    with open(SCRIPT_FILE, 'r') as f:
        content = f.read()
    assert "CrewAIProvider" in content, f"Expected use of CrewAIProvider in {SCRIPT_FILE}."

def test_script_defines_agents_and_tasks():
    """Priority 3 fallback: verify agent and task definitions."""
    with open(SCRIPT_FILE, 'r') as f:
        content = f.read()
    assert "Agent" in content, "Expected agent definitions in the script."
    assert "Task" in content, "Expected task definitions in the script."
    assert "Crew" in content, "Expected crew definition in the script."

def test_slack_message_posted():
    """Priority 1: Use Slack API to verify the research report was posted."""
    slack_token = os.environ["SLACK_TOKEN"]
    
    # 1. Get channel ID for #general
    result = subprocess.run([
        "curl", "-sS", "-H", f"Authorization: Bearer {slack_token}",
        "https://slack.com/api/conversations.list?types=public_channel"
    ], capture_output=True, text=True)
    data = json.loads(result.stdout)
    channel_id = next((c["id"] for c in data.get("channels", []) if c["name"] == "general"), None)
    assert channel_id, "Channel #general not found."
    
    # 2. Get history and check for commit messages or GitHub mentions
    result = subprocess.run([
        "curl", "-sS", "-H", f"Authorization: Bearer {slack_token}",
        f"https://slack.com/api/conversations.history?channel={channel_id}&limit=20"
    ], capture_output=True, text=True)
    history = json.loads(result.stdout)
    all_text = " ".join([m.get("text", "") for m in history.get("messages", [])])
    
    assert "Composio" in all_text or "GitHub" in all_text or "commit" in all_text.lower(), \
        f"Expected research report in Slack, but content looks wrong: {all_text}"
