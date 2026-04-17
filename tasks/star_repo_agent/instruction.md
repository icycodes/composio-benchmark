# Star a GitHub Repository with AI Agent

## Background
Composio enables AI agents to perform actions on GitHub. In this task, you will use an AI agent (OpenAI) with Composio tools to create a repository and then star it.

## Requirements
- Read the `trial_id` from `/logs/trial_id`.
- Repository name: `star-test-${trial_id}`.
- Use the user `zealt-user01`.
- Use OpenAI with Composio tools.
- The agent should:
    1. Create a public repository named `star-test-${trial_id}` under `zealt-user01`.
    2. Star the newly created repository.
- Save the execution log to `/home/user/agent.log`.

## Implementation Guide
1. Initialize Composio with `OpenAIProvider`.
2. Create a session for `zealt-user01`.
3. Get tools using `session.tools()`.
4. Use OpenAI's tool calling feature to execute the tasks.
5. Ensure you use the `trial_id` correctly to avoid conflicts.

## Constraints
- Project path: /home/user
- Log file: /home/user/agent.log
- User ID: `zealt-user01`
- Repository: `star-test-${trial_id}`

## Integrations
- Composio
- GitHub
- OpenAI
