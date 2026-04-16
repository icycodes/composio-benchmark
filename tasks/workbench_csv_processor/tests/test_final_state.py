import os
import pytest

DATA_FILE = "/home/user/data.csv"
RESULT_FILE = "/home/user/result.txt"

def test_data_file_exists():
    assert os.path.isfile(DATA_FILE), "Input CSV file not found."

def test_result_file_exists():
    assert os.path.isfile(RESULT_FILE), "Result file not found."

def test_result_is_correct():
    # Read data and calculate expected avg age
    import pandas as pd
    df = pd.read_csv(DATA_FILE)
    expected_avg = df["age"].mean()
    
    with open(RESULT_FILE, "r") as f:
        content = f.read()
    
    # Check if the expected average is in the result file
    assert str(expected_avg) in content or f"{expected_avg:.1f}" in content, \
        f"Expected average age {expected_avg} not found in {RESULT_FILE}. Got: {content}"
