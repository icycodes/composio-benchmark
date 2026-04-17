# Connection Status Checker with Python SDK

## Background
Composio's `COMPOSIO_MANAGE_CONNECTIONS` meta tool allows you to manage user connections programmatically. In this task, you will check the status of a user's GitHub connection.

## Requirements
- Write a Python script `/home/user/check_github_connection.py` that:
    1. Connects to Composio and creates a session for `zealt-user01`.
    2. Uses the `COMPOSIO_MANAGE_CONNECTIONS` meta tool to list the user's connections.
    3. Finds the connection for the `github` toolkit.
    4. Checks if the connection status is `CONNECTED`.
    5. Saves the full connection object to `/home/user/github_status.json`.
    6. Prints "GitHub is connected" to the console if it is connected.
- Run the script and log the output to `/home/user/connection.log`.

## Implementation Guide
1. Use the `composio` Python SDK with `OpenAIProvider` to provide access to meta tools if needed, or call the meta tool directly if the SDK supports it.
2. In the script, execute `COMPOSIO_MANAGE_CONNECTIONS` with the correct parameters to list connections for `zealt-user01`.
3. Filter the results for `github`.

## Constraints
- Project path: /home/user
- Output file: /home/user/github_status.json
- User ID: `zealt-user01`

## Integrations
- Composio
- GitHub
