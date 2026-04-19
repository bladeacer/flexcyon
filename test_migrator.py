#!/usr/bin/env python

"""
Unit tests from 1.X.Y to 2.0.0 settings migration script.
"""

from migrator import SettingsMapper, get_mapping_config
import json


def get_test_cases(prefix):
    """
    Returns the centralized list of test cases.
    Using f-strings to respect the dynamic prefix.
    """
    return [
        {
            "name": "Special Mode Transform (True)",
            "input": {f"{prefix}@{prefix}-rtz-mode": True},
            "expected": {f"{prefix}-modes@{prefix}-rtz-mode": f"{prefix}-rtz-mode"}
        },
        {
            "name": "Special Mode Transform (False/Discard)",
            "input": {f"{prefix}@{prefix}-rtz-mode": False},
            "expected": {}
        },
        {
            "name": "Special Mode Transform (True) - Flex Max",
            "input": {f"{prefix}@{prefix}-flex-max-mode": True},
            "expected": {f"{prefix}-modes@{prefix}-flex-max-mode": f"{prefix}-flex-max-mode"}
        },
        {
            "name": "Standard Prefix Update - Typewriter",
            "input": {f"{prefix}@typewriter-mode": True},
            "expected": {f"{prefix}-modes@typewriter-mode": True}
        },
        {
            "name": "A11y Mapping",
            "input": {f"{prefix}@{prefix}-brightness-ratio": 0.8},
            "expected": {f"{prefix}-a11y@{prefix}-brightness-ratio": 0.8}
        },
        # {
        #     "name": "Exact Match Priority",
        #     "input": {"xyz@old-legacy-key": "some-value"},
        #     "expected": {f"{prefix}-core@new-standard-key": "some-value"}
        # }
    ]


def generate_test_json(test_cases, filename="test.json"):
    """
    Extracts 'input' data from all test cases and merges them into 
    a single raw JSON file for the main migrator.
    """
    raw_input_data = {}
    for case in test_cases:
        # Update dictionary with the input pairs from this test case
        raw_input_data.update(case["input"])

    with open(filename, "w") as f:
        json.dump(raw_input_data, f, indent=2)

    print(f"Successfully generated {filename} from test cases.")


def run_unit_tests(mapper, test_cases):
    """Runs individual assertions for each test case."""
    passed = 0
    for case in test_cases:
        result = mapper.map_settings(case["input"])
        if result == case["expected"]:
            print(f"PASS: {case['name']}")
            passed += 1
        else:
            print(f"FAIL: {case['name']}")
            print(f"   Expected: {case['expected']}")
            print(f"   Got:      {result}")

    print(f"\nUnit Test Summary: {passed}/{len(test_cases)} passed.")


if __name__ == "__main__":
    config = get_mapping_config()
    prefix = config.get("target_prefix", "xyz")
    mapper = SettingsMapper(config)

    cases = get_test_cases(prefix)

    generate_test_json(cases)

    print("-" * 30)
    run_unit_tests(mapper, cases)
