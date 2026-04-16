# Multi-App Agent with Vercel AI SDK and Composio

## Background
Composio's native tools integrate seamlessly with the Vercel AI SDK. This allows you to build powerful agents that can act across multiple services. In this task, you will create a TypeScript agent that fetches information about a GitHub user and posts a summary to Slack.

## Requirements
- Create a TypeScript project in `/home/user/vercel-agent-task`.
- Use `@composio/core`, `@composio/vercel`, `ai`, and `@ai-sdk/openai`.
- The script must use the user `zealt-user01`.
- **Agent Logic**:
  1. Fetch the GitHub profile of the user `composiohq` using the `GITHUB_GET_A_USER` tool.
  2. Extract the user's `bio` and `public_repos` count.
  3. Post a message to a Slack channel named `agent-results-${trial_id}` (read `trial_id` from `/logs/trial_id`) with the summary: "User composiohq has {public_repos} repos. Bio: {bio}".
- The script should be named `agent.ts` and be runnable with `npx tsx agent.ts`.

## Implementation Guide
1. Initialize a new Node.js project and install dependencies.
2. Read `trial_id` from `/logs/trial_id`.
3. Initialize `Composio` with `VercelProvider`.
4. Create a session for `zealt-user01`.
5. Use `generateText` from the `ai` package.
6. Pass the session's tools to the `tools` parameter of `generateText`.
7. Provide a prompt that instructs the agent to perform the steps.

## Constraints
- Project path: /home/user/vercel-agent-task
- Language: TypeScript
- User ID: `zealt-user01`
- Channel name: `agent-results-${trial_id}`

## Integrations
- Composio
- GitHub
- Slack
- OpenAI
