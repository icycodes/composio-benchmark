# Process CSV with Composio Workbench

## Background
Composio's Workbench is a persistent Python sandbox for bulk data processing. In this task, you will use the Workbench to process a CSV file and upload the result.

## Requirements
- Create a CSV file `/home/user/data.csv` with columns `name` and `age`. Add 5 rows of data.
- Use the user `zealt-user01`.
- Use the `COMPOSIO_REMOTE_WORKBENCH` meta tool (or the `Workbench` class) to:
    1. Upload `data.csv` to the remote sandbox.
    2. Execute Python code in the sandbox to calculate the average age.
    3. Save the result to a new file `result.txt` in the sandbox.
    4. Download `result.txt` from the sandbox to `/home/user/result.txt`.
- Save the average age to `/home/user/avg_age.log`.

## Implementation Guide
1. Initialize Composio and create a session for `zealt-user01`.
2. Use the `session.workbench` methods or the `COMPOSIO_REMOTE_WORKBENCH` tool.
3. Ensure you follow the correct sequence of operations: upload, execute, download.

## Constraints
- Project path: /home/user
- Input: /home/user/data.csv
- Output: /home/user/result.txt
- User ID: `zealt-user01`

## Integrations
- Composio
