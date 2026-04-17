# Update GitHub Repository Description with Composio CLI

## Background
Composio CLI allows you to execute GitHub tools directly. In this task, you will update the description of a repository.

## Requirements
- Read the current `trial_id` from `/logs/trial_id`.
- Create a new public GitHub repository named `desc-test-${trial_id}` under `zealt-user01`.
- Use the `composio run` command to update the description of `zealt-user01/desc-test-${trial_id}` to "Harbor trial ${trial_id} repo".
- Log the result of the command to `/home/user/github_desc.log`.

## Implementation Guide
1. Use `gh repo create` for the initial setup.
2. Use `composio run github_repos_update --params '{"owner": "zealt-user01", "repo": "desc-test-<trial_id>", "description": "Harbor trial <trial_id> repo"}'`.
3. Ensure you use the correct tool slug and parameter names.

## Constraints
- Project path: /home/user
- Log file: /home/user/github_desc.log
- User ID: `zealt-user01`

## Integrations
- Composio
- GitHub
