# List Available Toolkits with Composio CLI

## Background
Composio provides a CLI to manage toolkits and connections. In this task, you will use the CLI to list all available toolkits.

## Requirements
- Use the Composio CLI to list all available toolkits.
- Filter the list to show only toolkits that are currently connected.
- Save the output of the connected toolkits to a log file.

## Implementation Guide
1. Run `composio toolkits list --connected` to see the connected toolkits.
2. Redirect the output to `/home/user/toolkits.log`.

## Constraints
- Project path: /home/user
- Log file: /home/user/toolkits.log
- Use the `composio` CLI.

## Integrations
- Composio
