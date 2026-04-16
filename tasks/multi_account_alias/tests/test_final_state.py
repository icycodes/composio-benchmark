import os
import subprocess
import json
import pytest

PROJECT_DIR = "/home/user/alias-task"
JSON_FILE = os.path.join(PROJECT_DIR, "updated_accounts.json")

def test_json_file_exists():
    assert os.path.isfile(JSON_FILE), f"JSON file {JSON_FILE} not found."

def test_aliases_updated():
    # Use the SDK to verify the aliases
    check_script = """
from composio import Composio
import os
composio = Composio(api_key=os.environ['COMPOSIO_API_KEY'])
accounts = composio.connected_accounts.list(user_ids=['zealt-user01'])
results = {a.toolkit.slug: a.alias for a in accounts.items}
print(results.get('github') == 'primary-github' and results.get('slack') == 'work-slack')
"""
    result = subprocess.run(["python3", "-c", check_script], capture_output=True, text=True)
    assert "True" in result.stdout, "Aliases were not correctly updated in the platform."

def test_json_content():
    with open(JSON_FILE, "r") as f:
        data = json.load(f)
    
    aliases = [item["alias"] for item in data]
    assert "primary-github" in aliases, "JSON missing primary-github alias."
    assert "work-slack" in aliases, "JSON missing work-slack alias."
