# GitHub Star Automation with Composio Python SDK

## Background
Composio allows AI agents to perform authenticated actions on GitHub. In this task, you will build a Python script that uses an AI agent to create a new repository and then star it.

## Requirements
1. Create a Python script `star_repo.py` in `/home/user/star-task`.
2. The script must use the Composio Python SDK and the OpenAI Agents SDK.
3. The script must create a new public repository named `harbor-gh-star-${trial_id}` (where `${trial_id}` is read from `/logs/trial_id`) under the `zealt-user01` account.
4. After creating the repository, the script must star it.
5. The script must use a Composio session for the user `zealt-user01`.

## Implementation Guide
1. Read the `trial_id` from `/logs/trial_id`.
2. Initialize Composio with `OpenAIAgentsProvider`.
3. Create a session for `user_id='zealt-user01'`.
4. Get tools from the session.
5. Initialize an OpenAI Agent with these tools.
6. Prompt the agent to: "Create a public repository named 'harbor-gh-star-<trial_id>' for user 'zealt-user01' and then star it."

## Constraints
- Project path: /home/user/star-task
- Use the test user `zealt-user01`.
- Read `trial_id` from `/logs/trial_id` to name the repository.

## Integrations
- Composio
- GitHub
- OpenAI
