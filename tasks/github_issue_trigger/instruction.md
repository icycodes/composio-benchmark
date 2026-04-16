# Set up GitHub Issue Trigger

## Background
Composio Triggers allow your application to react to external events. In this task, you will set up a trigger that listens for new GitHub issues.

## Requirements
- Use the user `zealt-user01`.
- Create a Python script `/home/user/setup_trigger.py`.
- The script should:
    1. Create an active trigger for the `GITHUB_ISSUE_EVENT` (or similar) on a specific repository `star-test-${trial_id}` (create it if it doesn't exist).
    2. Configure the trigger to send events to a local webhook listener (mocked or just configured).
- Since we cannot easily test a real webhook in this environment, you should use the Composio SDK to list active triggers and verify that your trigger is correctly created and active.
- Save the list of active triggers to `/home/user/triggers.log`.

## Implementation Guide
1. Read `trial_id` from `/logs/trial_id`.
2. Create the repository if needed.
3. Use `session.triggers.create()` to create the trigger.
4. Use `session.triggers.list()` to verify.

## Constraints
- Project path: /home/user
- Log file: /home/user/triggers.log
- User ID: `zealt-user01`
- Repository: `star-test-${trial_id}`

## Integrations
- Composio
- GitHub
