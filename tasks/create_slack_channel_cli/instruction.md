# Create Slack Channel and Send Message with Composio CLI

## Background
Composio CLI allows you to execute tools directly from the command line. In this task, you will create a new Slack channel and post a welcome message.

## Requirements
- Read the current `trial_id` from `/logs/trial_id`.
- Create a new public Slack channel named `test-chan-${trial_id}`.
- Send a message "Welcome to Harbor trial ${trial_id}" to the newly created channel.
- Use the `composio run` command for execution.
- Log the results of both commands to `/home/user/slack_setup.log`.

## Implementation Guide
1. Get `trial_id` from `/logs/trial_id`.
2. Use `composio run slack_conversations_create --params '{"name": "test-chan-<trial_id>"}'`.
3. Use `composio run slack_chat_post_message --params '{"channel": "test-chan-<trial_id>", "text": "Welcome to Harbor trial <trial_id>"}'`.
4. Make sure to use the correct tool slugs and parameter names.

## Constraints
- Project path: /home/user
- Log file: /home/user/slack_setup.log
- Use `zealt-user01` as the user (configured in environment).

## Integrations
- Composio
- Slack
