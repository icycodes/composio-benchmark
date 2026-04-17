# Summarize Slack Messages with AI Agent

## Background
Composio allows agents to read and process data from Slack. In this task, you will use an AI agent to fetch recent messages from a Slack channel and summarize them.

## Requirements
- Use the user `zealt-user01`.
- Use OpenAI with Composio tools.
- The agent should:
    1. Find a Slack channel named `general` (or similar available).
    2. Fetch the last 5 messages from that channel.
    3. Summarize the messages into a single paragraph.
    4. Post the summary back to the same channel.
- Save the summary to `/home/user/summary.txt`.

## Implementation Guide
1. Initialize Composio and OpenAI.
2. Create a session for `zealt-user01`.
3. Get tools and pass them to the agent.
4. The agent should use `SLACK_CONVERSATIONS_HISTORY` and `SLACK_CHAT_POST_MESSAGE` (or similar tools found via `SEARCH_TOOLS`). 

## Constraints
- Project path: /home/user
- Summary file: /home/user/summary.txt
- User ID: `zealt-user01`

## Integrations
- Composio
- Slack
- OpenAI
