# Morning Sweep Agent with Multiple Accounts

## Background
Composio allows you to manage multiple connected accounts for a single user (e.g., work vs. personal). In this task, you will implement a "Morning Sweep" agent that fetches data from two different GitHub accounts for the same user.

## Requirements
- Use the user `zealt-user01`.
- The user has two GitHub accounts connected (account IDs: `work-github` and `personal-github` - assume these or create them if needed, but for the task, the agent should handle two accounts).
- The agent should:
    1. Use the `Composio` SDK to list all connected accounts for GitHub for `zealt-user01`.
    2. For each account, fetch the last 3 issues from any repository.
    3. Combine the results into a single summary report.
- Save the report to `/home/user/morning_sweep.txt`.

## Implementation Guide
1. Use `session.connected_accounts()` or similar to list accounts.
2. When creating a session or executing a tool, specify the `connected_account_id` to differentiate between them.
3. The agent should be able to handle the case where multiple accounts exist for the same toolkit.

## Constraints
- Project path: /home/user
- Report file: /home/user/morning_sweep.txt
- User ID: `zealt-user01`

## Integrations
- Composio
- GitHub
