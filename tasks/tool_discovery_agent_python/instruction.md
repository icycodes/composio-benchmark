# Tool Discovery Agent with OpenAI and Composio

## Background
Composio's `COMPOSIO_SEARCH_TOOLS` meta tool allows agents to find the right tool for a task dynamically. In this task, you will build an agent that discovers a tool to star a GitHub repository and then executes it.

## Requirements
- Read the current `trial_id` from `/logs/trial_id`.
- Create a new public GitHub repository named `discovery-test-${trial_id}` under `zealt-user01`.
- Write a Python script `/home/user/discover_and_star.py` that:
    1. Connects to Composio and creates a session for `zealt-user01`.
    2. Uses OpenAI with the `COMPOSIO_SEARCH_TOOLS` and `COMPOSIO_MULTI_EXECUTE_TOOL` meta tools.
    3. The agent should search for a tool to "star a repository on GitHub".
    4. The agent should execute the found tool to star `zealt-user01/discovery-test-${trial_id}`.
- Run the script and log the tool discovery and execution output to `/home/user/discovery.log`.

## Implementation Guide
1. Use `gh repo create` for the initial setup.
2. In the Python script, initialize the `Composio` client with `OpenAIProvider`.
3. Provide the meta tools to the OpenAI agent.
4. Ensure the agent's prompt instructs it to search for the tool first.

## Constraints
- Project path: /home/user
- Log file: /home/user/discovery.log
- User ID: `zealt-user01`

## Integrations
- Composio
- GitHub
- OpenAI
