# Migrate Composio Script from v2 to v3

## Background
Composio v3 introduced significant changes, including renaming "Actions" to "Tools" and making sessions immutable. In this task, you will refactor an old v2 script to work with v3.

## Requirements
- You have an old script `/home/user/old_script.py` that uses v2 syntax (e.g., `session.actions()`, `session.update_toolkits()`).
- Refactor this script into `/home/user/new_script.py` using v3 syntax.
- The new script should:
    1. Use `session.tools()` instead of `session.actions()`.
    2. Handle session immutability (if toolkits need to change, create a new session instead of updating).
    3. Successfully list tools for the user `zealt-user01`.
- Save the tool list to `/home/user/tools_v3.log`.

## Implementation Guide
1. Review the migration guide in the research plan (Friction Points section).
2. Replace `actions()` with `tools()`.
3. If the old script tried to `update()` a session, change it to `create()` a new one with the desired toolkits.

## Constraints
- Project path: /home/user
- Old script: /home/user/old_script.py
- New script: /home/user/new_script.py
- User ID: `zealt-user01`

## Integrations
- Composio
