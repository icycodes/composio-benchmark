# Use Schema Modifiers in TS SDK

## Background
Composio allows you to modify tool schemas before passing them to an agent. This is useful for hiding sensitive arguments or simplifying the interface. In this task, you will use a Schema Modifier to hide the `body` argument from the `SLACK_CHAT_POST_MESSAGE` tool.

## Requirements
- Create a TypeScript project in `/home/user/project`.
- Install `@composio/core`.
- Create a script `modify.ts`.
- Create a session for `zealt-user01`.
- Use a `SchemaModifier` to hide the `text` (or `body`) argument from the Slack post message tool.
- Retrieve the tools from the session and find the modified tool.
- Print the modified tool's schema to `/home/user/schema.json`.

## Implementation Guide
1. Import `Composio` and `SchemaModifier` from `@composio/core`.
2. Create a modifier: `new SchemaModifier().hide('slack', 'chat_post_message', ['text'])`.
3. Create a session with the modifier: `composio.create('zealt-user01', { modifiers: [modifier] })`.
4. Get tools and find the one for Slack post message.
5. Write its `inputSchema` to a file.

## Constraints
- Project path: /home/user/project
- Output file: /home/user/schema.json
- User ID: `zealt-user01`

## Integrations
- Composio
