# Summarize Gmail to Slack with Composio TypeScript SDK

## Background
Composio enables AI agents to work across multiple apps. In this task, you will create a TypeScript script that integrates Gmail and Slack. The script will fetch the last 5 emails and post a summary to a Slack channel.

## Requirements
- Create a TypeScript project in `/home/user/summarize-task`.
- Use the `@composio/core` and `@composio/openai` SDKs.
- The script must use the user `zealt-user01`.
- Fetch the last 5 messages from Gmail using the `GMAIL_LIST_MESSAGES` tool (or search for the appropriate tool).
- Create a summary of the email subjects.
- Post the summary to a Slack channel named `summary-${trial_id}` (read `trial_id` from `/logs/trial_id`).
- The script should be named `index.ts` and be runnable with `npx tsx index.ts`.

## Implementation Guide
1. Initialize a new Node.js project and install dependencies: `@composio/core`, `@composio/openai`, `openai`, `tsx`, `dotenv`.
2. Read `trial_id` from `/logs/trial_id`.
3. Initialize `Composio` with `OpenAIProvider`.
4. Create a session for `zealt-user01`.
5. Use `session.execute` or an LLM agent to fetch the last 5 emails.
6. Format a summary string.
7. Post the message to Slack using `SLACK_CHAT_POST_MESSAGE`.

## Constraints
- Project path: /home/user/summarize-task
- Language: TypeScript
- User ID: `zealt-user01`
- Channel name: `summary-${trial_id}`

## Integrations
- Composio
- Gmail
- Slack
- OpenAI
