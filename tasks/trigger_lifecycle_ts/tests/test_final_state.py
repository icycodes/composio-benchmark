import os
import json
import pytest

def test_trigger_status_exists():
    assert os.path.isfile("/home/user/trigger_status.json"), "Trigger status file not found."

def test_trigger_was_disabled():
    with open("/home/user/trigger_status.json", "r") as f:
        status = json.load(f)
    
    # Check if the final status indicates it's disabled or not in the active list
    # The user should have recorded the status after disabling it.
    assert "disabled" in str(status).lower() or "inactive" in str(status).lower() or len(status.get("active_triggers", [])) == 0
