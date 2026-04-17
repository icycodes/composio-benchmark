# Trigger Lifecycle Management with TS SDK

## Background
Composio allows you to manage the lifecycle of triggers programmatically. In this task, you will create, list, and disable a trigger using the TypeScript SDK.

## Requirements
- Create a TypeScript project in `/home/user/project`.
- Install `@composio/core`.
- Write a script `trigger.ts` that:
    1. Connects to Composio and creates a session for `zealt-user01`.
    2. Lists the available trigger types for the `github` toolkit.
    3. Creates an active trigger for the `GITHUB_ISSUE_EVENT` (or similar available).
    4. Disables the newly created trigger.
    5. Lists the active triggers for the user and verifies that the trigger is no longer active.
    6. Saves the trigger details and its final status to `/home/user/trigger_status.json`.
- Run the script and log the output to `/home/user/trigger.log`.

## Implementation Guide
1. Use `session.triggers.list_types('github')` to find the correct trigger type.
2. Use `session.triggers.create(trigger_type_slug)` to activate it.
3. Use `session.triggers.disable(trigger_id)` or similar to deactivate it.
4. Ensure you capture the `trigger_id` after creation.

## Constraints
- Project path: /home/user/project
- Output file: /home/user/trigger_status.json
- User ID: `zealt-user01`

## Integrations
- Composio
- GitHub
