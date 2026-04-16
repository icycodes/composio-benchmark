import os
import subprocess
import pytest

SCRIPT_FILE = "/home/user/auth-task/auth_flow.py"

def test_script_exists():
    """Priority 3 fallback: basic file existence check."""
    assert os.path.isfile(SCRIPT_FILE), f"Script not found at {SCRIPT_FILE}"

def test_script_uses_authorize():
    """Priority 3 fallback: verify use of session.authorize() in the script."""
    with open(SCRIPT_FILE, 'r') as f:
        content = f.read()
    assert "session.authorize" in content or "authorize" in content.lower(), \
        f"Expected use of session.authorize() in {SCRIPT_FILE}, but it's not found."

def test_script_uses_wait_for_connection():
    """Priority 3 fallback: verify use of wait_for_connection() in the script."""
    with open(SCRIPT_FILE, 'r') as f:
        content = f.read()
    assert "wait_for_connection" in content, \
        f"Expected use of wait_for_connection() in {SCRIPT_FILE}, but it's not found."

def test_script_uses_toolkits_status():
    """Priority 3 fallback: verify use of session.toolkits() in the script."""
    with open(SCRIPT_FILE, 'r') as f:
        content = f.read()
    assert "session.toolkits" in content or "toolkits" in content.lower(), \
        f"Expected use of session.toolkits() in {SCRIPT_FILE}, but it's not found."

def test_script_execution_output():
    """Priority 1: Run the script and verify it prints a redirect URL."""
    # We'll run the script. It might timeout waiting for connection, but it should at least print the URL.
    # We'll use a short timeout for the subprocess to avoid waiting too long if it doesn't handle timeout well.
    try:
        result = subprocess.run(
            ["python3", SCRIPT_FILE],
            capture_output=True, text=True, cwd="/home/user/auth-task", timeout=10
        )
        output = result.stdout
    except subprocess.TimeoutExpired as e:
        output = e.stdout.decode() if e.stdout else ""
    
    assert "https://connect.composio.dev/link/" in output or "redirect" in output.lower(), \
        f"Expected redirect URL in output, but got: {output}"
