# Manual OAuth Flow with Composio Python SDK

## Background
Composio allows developers to manually initiate authentication flows for users. This is useful when you want to control when and how a user connects their account. In this task, you will use the Composio Python SDK to initiate an OAuth flow for Slack.

## Requirements
- Create a Python script named `initiate_slack.py` in `/home/user/auth-task`.
- The script must use the Composio Python SDK to create a session for the user `zealt-user01`.
- Use the session to initiate an authorization flow for the `slack` toolkit.
- The script must print the `redirect_url` to the console and also save it to a file named `redirect.url` in the project directory.

## Implementation Guide
1. Initialize the `Composio` client.
2. Create a session using `composio.create(user_id='zealt-user01')`.
3. Call `session.authorize('slack')` to get a connection request.
4. Access the `redirect_url` property from the connection request.
5. Write the `redirect_url` to `/home/user/auth-task/redirect.url`.

## Constraints
- Project path: /home/user/auth-task
- Language: Python
- SDK: `composio`
- User ID: `zealt-user01`

## Integrations
- Composio
- Slack
