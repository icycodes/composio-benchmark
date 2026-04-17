# Update Slack Channel Topic with Python SDK

## Background
Composio's Python SDK allows you to manage Slack channel properties. In this task, you will create a channel and then update its topic.

## Requirements
- Read the current `trial_id` from `/logs/trial_id`.
- Create a new public Slack channel named `topic-test-${trial_id}` using the `composio` CLI or SDK.
- Write a Python script `/home/user/update_topic.py` that:
    1. Connects to Composio and creates a session for `zealt-user01`.
    2. Finds the channel `topic-test-${trial_id}`.
    3. Updates the channel topic to "Topic for trial ${trial_id}".
- Run the script and log the output to `/home/user/slack_topic.log`.

## Implementation Guide
1. Use `composio run slack_conversations_create --params '{"name": "topic-test-<trial_id>"}'` for the initial setup.
2. In the Python script, use `session.tools()` to find the `SLACK_CONVERSATIONS_SET_TOPIC` tool.
3. Execute the tool with the correct `channel` ID and `topic` string.
4. You may need to use `SLACK_CONVERSATIONS_LIST` to find the channel ID first.

## Constraints
- Project path: /home/user
- Log file: /home/user/slack_topic.log
- User ID: `zealt-user01`

## Integrations
- Composio
- Slack
