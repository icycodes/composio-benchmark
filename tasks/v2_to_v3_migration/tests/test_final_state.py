import os
import pytest

NEW_SCRIPT = "/home/user/new_script.py"
LOG_FILE = "/home/user/tools_v3.log"

def test_new_script_exists():
    assert os.path.isfile(NEW_SCRIPT), "new_script.py not found."

def test_new_script_v3_syntax():
    with open(NEW_SCRIPT, "r") as f:
        content = f.read()
    assert "actions()" not in content, "The new script still contains 'actions()'."
    assert "update_toolkits()" not in content, "The new script still contains 'update_toolkits()'."
    assert "tools()" in content, "The new script should use 'tools()'."

def test_log_file_exists():
    assert os.path.isfile(LOG_FILE), "Log file tools_v3.log not found."
    with open(LOG_FILE, "r") as f:
        assert len(f.read().strip()) > 0, "Log file is empty."
