#!/usr/bin/env python

"""
Unit tests from 1.X.Y to 2.0.0 settings migration script.
"""

from migrator import SettingsMapper, get_mapping_config
import json


def get_test_cases(p):
    return [
        {
            "name": "Type Validity: Select Group Member Bad Type",
            "input": {
                f"{p}@@{p}-rtz-mode": "true",
                f"{p}@@{p}-flex-max-mode": False
            },
            "expected": {}
        },
        {
            "name": "Type Validity: Select Group All Bad Types",
            "input": {
                f"{p}@@{p}-rtz-mode": 1,
                f"{p}@@{p}-flex-max-mode": "no"
            },
            "expected": {}
        },

        {
            "name": "Select Group: RTZ True (Wins)",
            "input": {
                f"{p}@@{p}-rtz-mode": True, f"{p}@@{p}-flex-max-mode": False
            },
            "expected": {f"{p}-modes@@{p}-select-mode": f"{p}-rtz-mode"}
        },
        {
            "name": "Select Group: Both False (Fallback to none)",
            "input": {
                f"{p}@@{p}-rtz-mode": False, f"{p}@@{p}-flex-max-mode": False
            },
            "expected": {f"{p}-modes@@{p}-select-mode": "none"}
        },
        {
            "name": "Select Group: Flex Max (Do Nothing)",
            "input": {
                f"{p}@@{p}-rtz-mode": False, f"{p}@@{p}-flex-max-mode": True
            },
            "expected": {}
        },

        {
            "name": "Standard Bool (Typewriter True)",
            "input": {
                f"{p}@@{p}-typewriter-mode": True
            },
            "expected": {f"{p}-modes@@{p}-typewriter-mode": True}
        },
        {
            "name": "Standard Bool Discard (Typewriter False)",
            "input": {f"{p}@@{p}-typewriter-mode": False},
            "expected": {}
        },

        {
            "name": "Non-Default Value Keep (Opacity)",
            "input": {f"{p}@@{p}-typewriter-mode-opacity": 0.8},
            "expected": {f"{p}-modes@@{p}-typewriter-mode-opacity": 0.8}
        },
        {
            "name": "Default Value Discard (Opacity)",
            "input": {f"{p}@@{p}-typewriter-mode-opacity": 0.55},
            "expected": {}
        },
        {
            "name": "Invalid Bool Value Discard (Opacity)",
            "input": {f"{p}@@{p}-typewriter-mode-opacity": True},
            "expected": {}
        },
        {
            "name": "Invalid String Value Discard (Opacity)",
            "input": {f"{p}@@{p}-typewriter-mode-opacity": "0.55"},
            "expected": {}
        },

        {
            "name": "Standard Bool (Reverse True)",
            "input": {
                f"{p}@@{p}-reverse-mode": True
            },
            "expected": {f"{p}-modes@@{p}-reverse-mode": True}
        },
        {
            "name": "Standard Bool Discard (Reverse False)",
            "input": {f"{p}@@{p}-reverse-mode": False},
            "expected": {}
        },

        {
            "name": "Standard Bool (Writing Mode True)",
            "input": {
                f"{p}@@{p}-editor-writing": True
            },
            "expected": {f"{p}-modes@@{p}-editor-writing": True}
        },
        {
            "name": "Standard Bool Discard (Writing Mode False)",
            "input": {
                f"{p}@@{p}-editor-writing": False
            },
            "expected": {}
        },

        {
            "name": "Non-Default Value Keep (Writing Mode Indentation)",
            "input": {f"{p}@@{p}-editor-writing-indentation": 12},
            "expected": {f"{p}-modes@@{p}-editor-writing-indentation": 12},
        },
        {
            "name": "Default Value Discard (Indentation)",
            "input": {f"{p}@@{p}-editor-writing-indentation": 16},
            "expected": {}
        },

        # a11y

        {
            "name": "Non-Default Brightness Ratio",
            "input": {f"{p}@@{p}-brightness-ratio": 0.8},
            "expected": {f"{p}-a11y@@{p}-brightness-ratio": 0.8}
        },
        {
            "name": "Default Brightness Ratio",
            "input": {f"{p}@@{p}-brightness-ratio": 1.0},
            "expected": {}
        },
        {
            "name": "Type Validity: Int as Float Default (Brightness)",
            "input": {f"{p}@@{p}-brightness-ratio": 1},
            "expected": {}
        },
        {
            "name": "Type Validity: String in Brightness Ratio (Discard)",
            "input": {f"{p}@@{p}-brightness-ratio": "0.8"},
            "expected": {}
        },
        {
            "name": "Type Validity: Bool in Brightness Ratio (Discard)",
            "input": {f"{p}@@{p}-brightness-ratio": False},
            "expected": {}
        },
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
