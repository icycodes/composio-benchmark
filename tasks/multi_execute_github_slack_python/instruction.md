# Multi-Tool Execution with Python SDK

## Background
Composio allows you to execute multiple tools in parallel or sequence. In this task, you will use the Python SDK to create a file on GitHub and post a notification to Slack.

## Requirements
- Read the current `trial_id` from `/logs/trial_id`.
- Create a new public GitHub repository named `multi-test-${trial_id}` under `zealt-user01`.
- Write a Python script `/home/user/multi_exec.py` that:
    1. Connects to Composio and creates a session for `zealt-user01`.
    2. Uses the `MULTI_EXECUTE_TOOL` (or the session's execution methods) to:
        a. Create a file named `harbor.txt` in the repository `zealt-user01/multi-test-${trial_id}` with the content "Harbor trial ${trial_id}".
        b. Post a message to the Slack channel `general` saying "File harbor.txt created in trial ${trial_id}".
- Run the script and log the output to `/home/user/multi_exec.log`.

## Implementation Guide
1. Use `gh repo create` for the initial setup.
2. In the Python script, use `session.execute()` with a list of actions or use the `COMPOSIO_MULTI_EXECUTE_TOOL` directly.
3. Ensure you have the correct tool slugs for GitHub file creation and Slack message posting.

## Constraints
- Project path: /home/user
- Log file: /home/user/multi_exec.log
- User ID: `zealt-user01`

## Integrations
- Composio
- GitHub
- Slack
