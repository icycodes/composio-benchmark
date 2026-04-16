# Composio Meta-Tool: Multi-Execute Tool

## Background
Composio's `COMPOSIO_MULTI_EXECUTE_TOOL` allows an agent to execute multiple tools in parallel. This is highly efficient for tasks that require data from multiple sources or performing several actions at once. In this task, you will build a Python script that uses this meta-tool to perform multiple GitHub actions.

## Requirements
1. Create a Python script `multi_execute.py` in `/home/user/multi-execute-task`.
2. Use the Composio Python SDK and the OpenAI SDK.
3. Create a Composio session for the user `zealt-user01`.
4. The script must use the `COMPOSIO_MULTI_EXECUTE_TOOL` meta-tool to perform the following actions in a single call:
   - Star the repository `ComposioHQ/composio`.
   - Fetch the authenticated user's profile information.
   - List the last 2 issues in the `ComposioHQ/composio` repository.
5. The script must use an AI agent to decide and execute this multi-call.
6. Save the combined JSON output of these executions to `/home/user/multi-execute-task/result.json`.

## Implementation Guide
1. Initialize `Composio` with `OpenAIProvider`.
2. Create a session for `zealt-user01`.
3. Get meta-tools from the session.
4. Initialize an OpenAI agent with these meta-tools.
5. Prompt the agent to: "Use the multi-execute tool to star 'ComposioHQ/composio', get my profile info, and list the last 2 issues in 'ComposioHQ/composio' in parallel. Save the results to 'result.json'."

## Constraints
- Project path: /home/user/multi-execute-task
- Use the test user `zealt-user01`.
- Output file: /home/user/multi-execute-task/result.json

## Integrations
- Composio
- GitHub
- OpenAI
