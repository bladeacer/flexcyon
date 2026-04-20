#!/usr/bin/env python

"""
Dynamic Unit Tests for 1.X.Y to 2.0.0 settings migration.
"""

import json
from migrator import SettingsMapper, get_mapping_config


def _std_key(p, sfx):
    """Helper to format the input key string."""
    # Ensure the input key matches prefix@@prefix-suffix
    return f"{p}@@{p}-{sfx}"


def _get_std_cases(name, exp_type, p, group, default):
    """Generates tests for a single non-select setting."""
    k = _std_key(p, name)
    # The Expected key must follow the group@@prefix-name structure
    target = f"{group}@@{p}-{name}"

    # Logic for valid_val selection
    if exp_type is str:
        valid_val = f"custom-{default}"
    elif exp_type in [(float, int), float, int]:
        valid_val = 0.8 if default != 0.8 else 0.4
    else:
        valid_val = not default

    cases = [
        (f"Valid: {name}", {k: valid_val}, {target: valid_val}),
        (
            f"String Discard: {name}", {k: 123 if exp_type is str else "bad"},
            {}
        ),
    ]

    if default is not None:
        # Default now expects empty dict per "discard if default" logic
        cases.append((f"Default: {name}", {k: default}, {}))

    if exp_type is str:
        wrong_val = True
    else:
        wrong_val = 1 if exp_type is bool else "bad_string"

    cases.append((f"Type Poison: {name}", {k: wrong_val}, {}))
    return [{"name": n, "input": i, "expected": e} for n, i, e in cases]


def _get_poison_val(name, types_cfg):
    """Determines the specific 'wrong' type based on the schema."""
    expected = types_cfg.get(name)
    if expected is str:
        return True  # Boolean is poison for String
    return 1 if expected is bool else "bad_string"


def _get_select_cases(g_name, g_cfg, p, lookup, types_cfg):
    """Generates logic and type tests for a select group."""
    mems, discs = g_cfg["members"], g_cfg.get("discard_if_true", [])
    all_keys = list(set(mems + discs))
    target_key = f"{lookup[mems[0]]}@@{p}-{g_name}"
    cases = []

    # Individual Member Poisoning
    for m in all_keys:
        poison = _get_poison_val(m, types_cfg)
        label = "Int Discard" if poison == 1 else "Bool Discard"
        cases.append((f"Select Member {m} ({label})",
                      {_std_key(p, m): poison}, {}))

    # Winner logic: Setting to True (Valid)
    for m in [m for m in mems if m not in discs]:
        cases.append((f"Win: {m}", {_std_key(p, m): True},
                      {target_key: f"{p}-{m}"}))

    # Fallback logic: All members at False (Default)
    # Note: If default is False, this triggers 'none' fallback
    cases.append((f"None Fallback: {g_name}",
                  {_std_key(p, m): False for m in all_keys},
                  {target_key: "none"}))

    for d in discs:
        cases.append((f"Silence: {d}", {_std_key(p, d): True}, {}))

    # Multi-Poison
    cases.append((f"Multi-Poison: {g_name}",
                  {_std_key(p, m): "bad" for m in mems}, {}))

    return [{"name": n, "input": i, "expected": e} for n, i, e in cases]


def generate_test_cases(cfg):
    """Orchestrates test generation with low cyclomatic complexity."""
    p = cfg["target_prefix"]
    types_cfg = cfg["types"]
    lookup = {s: g for g, sfxs in cfg["suffix_groups"].items() for s in sfxs}
    tests = []

    select_mems = {
        m for g in cfg["select_groups"].values() for m in g["members"]
    }
    select_discs = {d for g in cfg["select_groups"].values()
                    for d in g.get("discard_if_true", [])}

    for name, exp_type in types_cfg.items():
        if name in select_mems or name in select_discs:
            continue
        tests.extend(_get_std_cases(
            name, exp_type, p, lookup[name], cfg["defaults"].get(name)
        ))

    for g_name, g_cfg in cfg["select_groups"].items():
        # Pass types_cfg into the select helper
        tests.extend(_get_select_cases(g_name, g_cfg, p, lookup, types_cfg))

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

    cases = generate_test_cases(config)

    generate_test_json(cases)

    print("-" * 40)
    run_unit_tests(mapper, cases)
