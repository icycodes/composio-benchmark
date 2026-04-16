# Create a Custom GitHub Extension Tool with Composio Python SDK

## Background
Composio allows you to extend existing toolkits with custom business logic. Extension tools inherit the authentication of the toolkit they extend. In this task, you will create a custom tool that extends the `github` toolkit to perform a specialized action: creating a repository and immediately adding a specific label to it.

## Requirements
- Create a Python script named `custom_tool.py` in `/home/user/custom-tool-task`.
- The script must use the `composio` Python SDK and the `experimental` custom tool API.
- **Define a Custom Tool**:
  - Name: `CREATE_REPO_WITH_LABEL`.
  - Extends Toolkit: `github`.
  - Input Parameters: `repo_name` (string).
  - Execution Logic:
    1. Use `ctx.execute('GITHUB_CREATE_A_REPOSITORY_FOR_THE_AUTHENTICATED_USER', {'name': repo_name})` to create the repo.
    2. Use `ctx.execute('GITHUB_CREATE_A_LABEL_FOR_A_REPOSITORY', {'owner': 'zealt-user01', 'repo': repo_name, 'name': 'custom-label', 'color': 'ff0000'})` to add a label.
- **Execute the Tool**:
  - Read the `trial_id` from `/logs/trial_id`.
  - Set `repo_name` to `custom-repo-${trial_id}`.
  - Create a session for `zealt-user01` and register the custom tool.
  - Execute the custom tool within the session.
  - Print the result of the execution.

## Implementation Guide
1. Import `Composio` and `BaseModel`, `Field` from `pydantic`.
2. Define the input model `CreateRepoInput`.
3. Use `@composio.experimental.tool(extends_toolkit='github')` to define the tool.
4. In the session creation, pass `experimental={'custom_tools': [your_tool]}`.
5. Call `session.execute('CREATE_REPO_WITH_LABEL', {'repo_name': ...})`.

## Constraints
- Project path: /home/user/custom-tool-task
- Language: Python
- User ID: `zealt-user01`
- Repository name: `custom-repo-${trial_id}`

## Integrations
- Composio
- GitHub
