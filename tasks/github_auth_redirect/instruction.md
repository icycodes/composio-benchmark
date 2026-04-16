# GitHub Auth Redirect using TS SDK

## Background
Composio's TypeScript SDK allows you to initiate OAuth flows for users. In this task, you will create a session and get the redirect URL for GitHub authentication.

## Requirements
- Create a TypeScript project in `/home/user/project`.
- Install `@composio/core`.
- Create a script `auth.ts` that uses the `Composio` class.
- Create a session for the user `zealt-user01`.
- Call `session.authorize('github')` to get a `connectionRequest`.
- Print the `redirectUrl` to the console.
- Compile and run the script, and redirect the output to `/home/user/auth_url.log`.

## Implementation Guide
1. Initialize a Node.js project: `npm init -y`.
2. Install `@composio/core` and `ts-node` (for easier execution).
3. Write the script using `await session.authorize('github')`.
4. Log the `redirectUrl` property.

## Constraints
- Project path: /home/user/project
- Log file: /home/user/auth_url.log
- User ID: `zealt-user01`

## Integrations
- Composio
