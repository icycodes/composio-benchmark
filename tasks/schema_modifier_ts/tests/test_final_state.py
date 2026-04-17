import os
import json
import pytest

SCHEMA_FILE = "/home/user/schema.json"

def test_schema_file_exists():
    assert os.path.isfile(SCHEMA_FILE), f"Schema file {SCHEMA_FILE} not found."

def test_schema_argument_hidden():
    with open(SCHEMA_FILE, "r") as f:
        schema = json.load(f)
    
    # We expect the 'text' property to be missing from the properties
    properties = schema.get("properties", {})
    assert "text" not in properties, "The 'text' argument should be hidden but was found in the schema."
