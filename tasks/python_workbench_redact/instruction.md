# Composio Workbench and Schema Modifiers

## Background
Composio's Workbench provides a sandboxed environment for data processing, while Schema Modifiers allow you to control which tool arguments are exposed to the LLM. In this task, you will use both to build a secure data processing pipeline.

## Requirements
1. Create a Python script `workbench_task.py` in `/home/user/workbench-task`.
2. Use the Composio Python SDK and the OpenAI SDK.
3. Use **Schema Modifiers** to hide the `org` argument from the `GITHUB_GET_ORGANIZATION` tool. Instead, hardcode the value `ComposioHQ` in the tool configuration so the LLM cannot change it.
4. Use the **Workbench** to execute a Python script that fetches the organization info and saves a summary to a file named `/home/user/workbench-task/org_summary.txt`.
5. The summary must include the organization name and its public repository count.

## Implementation Guide
1. Initialize Composio with `OpenAIProvider`.
2. Create a session for `zealt-user01`.
3. Apply a Schema Modifier to the `GITHUB_GET_ORGANIZATION` tool to set `org='ComposioHQ'` and hide it from the LLM.
4. Initialize the Workbench.
5. Use an OpenAI agent with the modified tool and the Workbench tool.
6. Prompt the agent to: "Fetch info for the organization 'ComposioHQ' using the modified GitHub tool, then use the Workbench to write a summary (name and public repo count) to '/home/user/workbench-task/org_summary.txt'."

## Constraints
- Project path: /home/user/workbench-task
- Use the test user `zealt-user01`.
- Output file: /home/user/workbench-task/org_summary.txt

## Integrations
- Composio
- GitHub
- OpenAI
