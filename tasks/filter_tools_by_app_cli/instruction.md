# Filter Tools by App with Composio CLI

## Background
Composio provides a CLI to explore available tools. In this task, you will use the CLI to list tools filtered by their application.

## Requirements
- Use the Composio CLI to list all available tools for the `github` application.
- Save the output to `/home/user/github_tools.log`.
- Use the Composio CLI to list all available tools for the `slack` application.
- Save the output to `/home/user/slack_tools.log`.
- Ensure each log file contains only tools relevant to that specific application.

## Implementation Guide
1. Use `composio tools list --app github` (or similar filtering flags).
2. Redirect the output to the specified log files.
3. Check the CLI help `composio tools list --help` to find the correct filtering flag.

## Constraints
- Project path: /home/user
- Log files: /home/user/github_tools.log, /home/user/slack_tools.log
- Use the `composio` CLI.

## Integrations
- Composio
