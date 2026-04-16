# Star a GitHub Repository with Composio CLI

## Background
Composio provides a CLI to interact with over 1000+ toolkits. You can execute tools directly from your terminal. In this task, you will use the Composio CLI to star a specific GitHub repository.

## Requirements
- Use the Composio CLI to star the repository `composiohq/composio`.
- The operation must be performed on behalf of the user `zealt-user01`.

## Implementation Guide
1. Ensure you are logged in to Composio (the `COMPOSIO_API_KEY` is already set in your environment).
2. Use the `composio execute` command to call the GitHub star tool.
3. The tool slug for starring a repository is `GITHUB_STAR_A_REPOSITORY_FOR_THE_AUTHENTICATED_USER`.
4. Provide the required arguments: `owner` as `composiohq` and `repo` as `composio`.

## Constraints
- Project path: /home/user/star-task
- Use Composio CLI.
- User ID: `zealt-user01`

## Integrations
- Composio
- GitHub
