import os
import pytest
import re

SUMMARY_FILE = "/home/user/workbench-task/org_summary.txt"
SCRIPT_FILE = "/home/user/workbench-task/workbench_task.py"

def test_summary_file_exists():
    """Priority 3 fallback: basic file existence check."""
    assert os.path.isfile(SUMMARY_FILE), f"Summary file not found at {SUMMARY_FILE}"

def test_summary_file_content():
    """Priority 3 fallback: check for correct organization name and repo count."""
    with open(SUMMARY_FILE, 'r') as f:
        content = f.read()
    assert "ComposioHQ" in content, f"Expected 'ComposioHQ' in summary, got: {content}"
    # Check for a number in the content (repo count)
    assert any(char.isdigit() for char in content), f"Expected repo count (number) in summary, got: {content}"

def test_script_uses_schema_modifier():
    """Priority 3 fallback: verify use of SchemaModifier in the agent script."""
    assert os.path.isfile(SCRIPT_FILE), f"Script not found at {SCRIPT_FILE}"
    with open(SCRIPT_FILE, 'r') as f:
        content = f.read()
    # Check for SchemaModifier or similar terminology from Composio
    # Based on docs: from composio import SchemaModifier
    assert "SchemaModifier" in content or "modifier" in content.lower(), \
        f"Expected use of SchemaModifier in {SCRIPT_FILE}, but it's not found."
    # Check for hardcoded 'ComposioHQ'
    assert "ComposioHQ" in content, f"Expected 'ComposioHQ' to be hardcoded in {SCRIPT_FILE}."

def test_script_uses_workbench():
    """Priority 3 fallback: verify use of Workbench in the agent script."""
    with open(SCRIPT_FILE, 'r') as f:
        content = f.read()
    assert "Workbench" in content or "workbench" in content.lower(), \
        f"Expected use of Workbench in {SCRIPT_FILE}, but it's not found."
