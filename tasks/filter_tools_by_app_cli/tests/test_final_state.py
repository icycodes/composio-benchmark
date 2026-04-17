import os
import pytest

GITHUB_LOG = "/home/user/github_tools.log"
SLACK_LOG = "/home/user/slack_tools.log"

def test_github_tools_log():
    assert os.path.isfile(GITHUB_LOG), "GitHub tools log not found."
    with open(GITHUB_LOG, "r") as f:
        content = f.read().lower()
    assert "github" in content, "GitHub tools log doesn't seem to contain GitHub tools."
    assert "slack" not in content, "GitHub tools log contains Slack tools."

def test_slack_tools_log():
    assert os.path.isfile(SLACK_LOG), "Slack tools log not found."
    with open(SLACK_LOG, "r") as f:
        content = f.read().lower()
    assert "slack" in content, "Slack tools log doesn't seem to contain Slack tools."
    assert "github" not in content, "Slack tools log contains GitHub tools."
