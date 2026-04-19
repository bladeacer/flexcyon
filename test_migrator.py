#!/usr/bin/env python

"""
Unit tests from 1.X.Y to 2.0.0 settings migration script.
"""

from migrator import SettingsMapper, get_mapping_config
import json


def get_test_cases(p):
    return [
        {
            "name": "Select Group: RTZ True (Wins)",
            "input": {f"{p}@{p}-rtz-mode": True, f"{p}@{p}-flex-max-mode": False},
            "expected": {f"{p}-modes@{p}-select-mode": f"{p}-rtz-mode"}
        },
        {
            "name": "Select Group: Flex Max (Do Nothing)",
            "input": {f"{p}@{p}-rtz-mode": False, f"{p}@{p}-flex-max-mode": True},
            "expected": {}
        },
        {
            "name": "Select Group: Both False (Fallback to none)",
            "input": {f"{p}@{p}-rtz-mode": False, f"{p}@{p}-flex-max-mode": False},
            "expected": {f"{p}-modes@{p}-select-mode": "none"}
        },
        {
            "name": "Standard Bool (Typewriter True)",
            "input": {f"{p}@{p}-typewriter-mode": True},
            "expected": {f"{p}-modes@{p}-typewriter-mode": True}
        },
        {
            "name": "Standard Bool Discard (Typewriter False)",
            "input": {f"{p}@{p}-typewriter-mode": False},
            "expected": {}
        },
        {
            "name": "A11y Mapping",
            "input": {f"{p}@{p}-brightness-ratio": 0.8},
            "expected": {f"{p}-a11y@{p}-brightness-ratio": 0.8}
        }
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
