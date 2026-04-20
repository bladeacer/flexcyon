#!/usr/bin/env python

"""
Dynamic Unit Tests for 1.X.Y to 2.0.0 settings migration.
"""

import json
from migrator import SettingsMapper, get_mapping_config


def generate_test_cases(cfg):
    """
    Generates exhaustive test cases based on the provided config schema.
    """
    p = cfg["target_prefix"]
    tests = []

    # Reverse lookup for group mapping
    val_to_group = {
        sfx: g for g, sfxs in cfg["suffix_groups"].items() for sfx in sfxs
    }

    # 1. Generate Standard Field Tests (Non-Select Groups)
    for name, expected_type in cfg["types"].items():
        is_select = any(
            name in g["members"] or name in g.get("discard_if_true", [])
            for g in cfg["select_groups"].values()
        )
        if is_select:
            continue

        group = val_to_group.get(name)
        full_key = f"{p}@@{p}-{name}"
        target_key = f"{group}@@{p}-{name}"

        # Scenario: Valid Value
        val = 0.8 if expected_type in [(float, int), float, int] else True
        tests.append({
            "name": f"Type Validity: {name} (Valid)",
            "input": {full_key: val},
            "expected": {target_key: val}
        })

        # Scenario: Default Value Discard
        if name in cfg["defaults"]:
            tests.append({
                "name": f"Default Discard: {name}",
                "input": {full_key: cfg["defaults"][name]},
                "expected": {}
            })

        # Scenario: Type Mismatch (String Discard)
        tests.append({
            "name": f"Type Validity: {name} (String Discard)",
            "input": {full_key: "invalid_string"},
            "expected": {}
        })

        # Scenario: Specific Type Mismatch (Int for Bool or Bool for Int)
        if expected_type is bool:
            tests.append({
                "name": f"Type Validity: {name} (Int Discard)",
                "input": {full_key: 1},
                "expected": {}
            })
        elif expected_type in [(float, int), float, int]:
            tests.append({
                "name": f"Type Validity: {name} (Bool Discard)",
                "input": {full_key: True},
                "expected": {}
            })

    # 2. Generate Select Group Logic Tests
    for g_name, g_cfg in cfg["select_groups"].items():
        members = g_cfg["members"]
        discards = g_cfg.get("discard_if_true", [])
        all_keys = list(set(members + discards))
        
        group_label = val_to_group.get(members[0])
        target_select = f"{group_label}@@{p}-{g_name}"

        # Scenario: Individual Member Type Poisoning
        for m in all_keys:
            m_type = cfg["types"].get(m)
            bad_val = 1 if m_type is bool else "bad_string"
            tests.append({
                "name": f"Type Validity: Select Member {m} (Poison)",
                "input": {f"{p}@@{p}-{m}": bad_val},
                "expected": {}
            })

        # Scenario: Each member winning
        for m in members:
            if m in discards:
                continue
            tests.append({
                "name": f"Select Group: {g_name} ({m} Wins)",
                "input": {f"{p}@@{p}-{m}": True},
                "expected": {target_select: f"{p}-{m}"}
            })

        # Scenario: Discard if True (Silencing)
        for d in discards:
            tests.append({
                "name": f"Select Group: {g_name} ({d} Silence)",
                "input": {f"{p}@@{p}-{d}": True},
                "expected": {}
            })

        # Scenario: All False (Fallback to none)
        all_false = {f"{p}@@{p}-{m}": False for m in all_keys}
        tests.append({
            "name": f"Select Group: {g_name} (Both False Fallback)",
            "input": all_false,
            "expected": {target_select: "none"}
        })

        # Scenario: Multi-Poison (The original missing test)
        multi_poison = {f"{p}@@{p}-{m}": "bad" for m in members}
        tests.append({
            "name": f"Select Group: {g_name} (All Bad Types Poison)",
            "input": multi_poison,
            "expected": {}
        })

    return tests


def generate_test_json(test_cases, filename="test.json"):
    """Merges input data from all test cases into one file."""
    raw_input_data = {}
    for case in test_cases:
        raw_input_data.update(case["input"])
    with open(filename, "w") as f:
        json.dump(raw_input_data, f, indent=2)
    print(f"Generated {filename} with {len(raw_input_data)} keys.")


def run_unit_tests(mapper, test_cases):
    """Execution engine for generated assertions."""
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

    print(f"\nSummary: {passed}/{len(test_cases)} passed.")


if __name__ == "__main__":
    config = get_mapping_config()
    mapper = SettingsMapper(config)

    # Automatically generate cases based on config
    cases = generate_test_cases(config)

    # Optional: generate the full JSON blob for integration testing
    generate_test_json(cases)

    print("-" * 40)
    run_unit_tests(mapper, cases)
