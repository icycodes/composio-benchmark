import os
import pytest

REPORT_FILE = "/home/user/morning_sweep.txt"

def test_report_file_exists():
    assert os.path.isfile(REPORT_FILE), "Morning sweep report not found."

def test_report_content():
    with open(REPORT_FILE, "r") as f:
        content = f.read()
    # Check for presence of GitHub-related keywords
    assert "github" in content.lower(), "Report does not contain GitHub data."
    # Ideally we'd check for multi-account identifiers, but that depends on the agent's output.
    assert len(content.strip()) > 0, "Report is empty."
