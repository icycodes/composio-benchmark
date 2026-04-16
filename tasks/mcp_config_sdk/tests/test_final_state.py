import os
import subprocess
import json
import pytest

PROJECT_DIR = "/home/user/mcp-task"
ID_FILE = os.path.join(PROJECT_DIR, "server_id.txt")

def test_id_file_exists():
    assert os.path.isfile(ID_FILE), f"Server ID file {ID_FILE} not found."

def test_mcp_config_details():
    with open(ID_FILE, "r") as f:
        server_id = f.read().strip()
    
    # Use the SDK to verify the config
    check_script = f"""
from composio import Composio
import os
import json
composio = Composio(api_key=os.environ['COMPOSIO_API_KEY'])
server = composio.mcp.get('{server_id}')
print(json.dumps(server))
"""
    result = subprocess.run(["python3", "-c", check_script], capture_output=True, text=True)
    assert result.returncode == 0, f"Failed to get MCP config: {result.stderr}"
    
    server = json.loads(result.stdout)
    assert server["name"] == "github-mcp-server", f"Expected name 'github-mcp-server', got {server['name']}"
    
    # Allowed tools might be objects or strings depending on version, 
    # but let's check for the slugs.
    allowed_tools = server.get("allowed_tools", [])
    # Handle both list of strings and list of dicts
    tool_slugs = [t if isinstance(t, str) else t.get("slug") for t in allowed_tools]
    
    assert "GITHUB_GET_THE_AUTHENTICATED_USER" in tool_slugs, "Missing tool GITHUB_GET_THE_AUTHENTICATED_USER"
    assert "GITHUB_LIST_REPOS" in tool_slugs, "Missing tool GITHUB_LIST_REPOS"
