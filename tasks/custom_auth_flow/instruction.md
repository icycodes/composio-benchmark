# Manual Authentication Flow with Composio

## Background
While in-chat authentication is convenient, sometimes you need to pre-authenticate users or build a custom connections UI. Composio's `session.authorize()` allows you to generate Connect Links programmatically.

## Requirements
1. Create a Python script `auth_flow.py` in `/home/user/auth-task`.
2. Use the Composio Python SDK.
3. Create a Composio session for a new user `zealt-user-auth-test`.
4. The script must generate a Connect Link for the `github` toolkit.
5. The script must print the redirect URL to the console.
6. The script must use `wait_for_connection()` to wait for the user to complete the authentication (with a timeout of 60 seconds).
7. After the connection is established (or times out), the script must fetch and print the status of all toolkits for this user using `session.toolkits()`.

## Implementation Guide
1. Initialize `Composio`.
2. Create a session for `user_id='zealt-user-auth-test'`.
3. Call `session.authorize('github')`.
4. Print `connection_request.redirect_url`.
5. Call `connection_request.wait_for_connection(60000)`.
6. Call `session.toolkits()` and iterate through items to print their name and connection status.

## Constraints
- Project path: /home/user/auth-task
- Use the user ID `zealt-user-auth-test`.
- Use the `github` toolkit.

## Integrations
- Composio
- GitHub
