# List Tools using Python SDK

## Background
Composio's Python SDK allows you to programmatically interact with tools and sessions. In this task, you will create a session and list available tools.

## Requirements
- Create a Python script `/home/user/list_tools.py`.
- Use the `Composio` class from the `composio` package.
- Create a session for the user `zealt-user01`.
- Retrieve the list of tools available in that session.
- Print the tool names to the console.
- Run the script and redirect the output to `/home/user/output.log`.

## Implementation Guide
1. Install `composio` and `composio-openai` (optional but recommended for provider support).
2. Write the script using `composio.create(user_id='zealt-user01')`.
3. Call `session.tools()` to get the tool list.
4. Iterate through the tools and print their names.

## Constraints
- Project path: /home/user
- Log file: /home/user/output.log
- User ID: `zealt-user01`

## Integrations
- Composio
