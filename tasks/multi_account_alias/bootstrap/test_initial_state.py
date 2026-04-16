import os
import shutil
import pytest

PROJECT_DIR = "/home/user/alias-task"

def test_composio_installed():
    import subprocess
    result = subprocess.run(["pip3", "show", "composio"], capture_output=True, text=True)
    assert result.returncode == 0, "Composio SDK is not installed."

def test_project_dir_exists():
    assert os.path.isdir(PROJECT_DIR), f"Project directory {PROJECT_DIR} does not exist."

def test_composio_api_key_set():
    assert "COMPOSIO_API_KEY" in os.environ, "COMPOSIO_API_KEY environment variable is not set."

def test_user_has_connections():
    # Verify zealt-user01 has at least one github and one slack connection
    check_script = """
from composio import Composio
import os
composio = Composio(api_key=os.environ['COMPOSIO_API_KEY'])
accounts = composio.connected_accounts.list(user_ids=['zealt-user01'])
toolkits = [a.toolkit.slug for a in accounts.items]
print('github' in toolkits and 'slack' in toolkits)
"""
    import subprocess
    result = subprocess.run(["python3", "-c", check_script], capture_output=True, text=True)
    assert "True" in result.stdout, "User zealt-user01 is missing required connections (github and slack)."
