# GitHub Label Commenter with Python SDK

## Background
Composio's Python SDK allows you to automate GitHub workflows. In this task, you will find issues with a specific label and add a comment to them.

## Requirements
- Read the current `trial_id` from `/logs/trial_id`.
- Create a new public GitHub repository named `issue-test-${trial_id}` under `zealt-user01`.
- Create an issue in that repository with the title "Bug in trial ${trial_id}" and the label `bug`.
- Write a Python script `/home/user/comment_issues.py` that:
    1. Connects to Composio and creates a session for `zealt-user01`.
    2. Finds all issues in `zealt-user01/issue-test-${trial_id}` with the label `bug`.
    3. Adds a comment "Fixed in trial ${trial_id}" to each of those issues.
- Run the script and log the output to `/home/user/github_comment.log`.

## Implementation Guide
1. Use `gh repo create` and `gh issue create` for the initial setup.
2. Use the `composio` Python SDK.
3. Search for tools like `GITHUB_ISSUES_LIST_FOR_REPO` and `GITHUB_ISSUES_CREATE_COMMENT` (or use the generic tool search).
4. Ensure you use the correct repository name with the `trial_id` suffix.

## Constraints
- Project path: /home/user
- Log file: /home/user/github_comment.log
- User ID: `zealt-user01`

## Integrations
- Composio
- GitHub
