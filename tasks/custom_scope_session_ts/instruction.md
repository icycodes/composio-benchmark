# Custom Scope Session with TS SDK

## Background
Composio allows you to configure sessions with specific authentication scopes. In this task, you will create a session for GitHub with a custom list of scopes.

## Requirements
- Create a TypeScript project in `/home/user/project`.
- Install `@composio/core`.
- Write a script `session.ts` that:
    1. Connects to Composio.
    2. Creates a session for `zealt-user01`.
    3. Sets the GitHub auth configuration to include the scopes `['repo', 'read:org', 'user']`.
    4. Retrieves the session details (including the auth config) and saves them to `/home/user/session_config.json`.
- Run the script and log the output to `/home/user/session.log`.

## Implementation Guide
1. Use `composio.create('zealt-user01', { authConfigs: { github: { scopes: ['repo', 'read:org', 'user'] } } })` (or similar depending on the exact SDK version/syntax).
2. Save the resulting session object or its configuration to the specified JSON file.

## Constraints
- Project path: /home/user/project
- Output file: /home/user/session_config.json
- User ID: `zealt-user01`

## Integrations
- Composio
