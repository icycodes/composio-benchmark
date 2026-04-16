import os
import json
import pytest

PROJECT_DIR = "/home/user/modifier-task"
SCHEMA_FILE = os.path.join(PROJECT_DIR, "modified_schema.json")

def test_schema_file_exists():
    assert os.path.isfile(SCHEMA_FILE), f"Modified schema file {SCHEMA_FILE} not found."

def test_schema_content():
    with open(SCHEMA_FILE, "r") as f:
        schema = json.load(f)
    
    # In Composio v3, the tool object might have input_parameters or parameters
    # The task description says extraction from tool object.
    # Assuming standard JSON schema structure in input_parameters
    
    input_params = schema.get("input_parameters", {})
    properties = input_params.get("properties", {})
    required = input_params.get("required", [])
    
    assert "page" not in properties, "The 'page' argument should have been removed."
    assert "size" in required, "The 'size' argument should be required."
