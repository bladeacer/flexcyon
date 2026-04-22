#!/usr/bin/env python

"""
Dynamic Unit Tests for 1.X.Y to 2.0.0 settings migration.
"""

import json
from migrator import SettingsMapper, get_mapping_config, get_schema


def _std_key(p, sfx):
    return f"{p}@@{p}-{sfx}"


def _get_all_poison_samples(name, types_cfg):
    """
    Returns a list of (type_name, value) tuples for every type
    NOT allowed by the schema for this key.
    """
    expected = types_cfg.get(name)
    if not isinstance(expected, tuple):
        expected = (expected,)

    # Define our pool of standard test types
    samples = [
        ("bool", True),
        ("int", 123),
        ("float", 45.67),
        ("str", "poison_string")
    ]

    # Filter out samples that match any of the expected types
    poisons = []
    for t_name, val in samples:
        if not any(isinstance(val, t) for t in expected):
            poisons.append((t_name, val))
    return poisons


def _get_std_cases(name, exp_type, p, group, default, types_cfg):
    k = _std_key(p, name)
    target = f"{group}@@{p}-{name}"

    if exp_type is str:
        valid_val = f"custom-{default}"
    elif exp_type in [(float, int), float, int]:
        valid_val = 0.8 if default != 0.8 else 0.4
    else:
        valid_val = not default

    cases = [(f"Valid: {name}", {k: valid_val}, {target: valid_val})]

    # Add exhaustive bad type cases
    for t_name, p_val in _get_all_poison_samples(name, types_cfg):
        cases.append((
            f"Bad Type [{t_name}]: {name}",
            {k: p_val},
            {}
        ))

    if default is not None:
        cases.append((f"Default: {name}", {k: default}, {}))

    return [{"name": n, "input": i, "expected": e} for n, i, e in cases]


def _get_select_cases(g_name, g_cfg, p, lookup, types_cfg):
    mems = g_cfg["members"]
    discs = g_cfg.get("discard_if_true", [])
    always = g_cfg.get("discard_always", [])
    active_keys = list(set(mems + discs))
    target_key = f"{lookup[mems[0]]}@@{p}-{g_name}"
    cases = []

    # 1. Exhaustive Type Poisoning for all active keys
    for m in active_keys:
        for t_name, p_val in _get_all_poison_samples(m, types_cfg):
            cases.append((
                f"Select Poison {m} [{t_name}]",
                {_std_key(p, m): p_val},
                {}
            ))

    # 2. Winner logic
    for m in [m for m in mems if m not in discs]:
        cases.append((f"Win: {m}", {_std_key(p, m): True},
                      {target_key: f"{p}-{m}"}))

    # 3. Always Discard
    for a in always:
        cases.append((f"Group Discard: {a}", {_std_key(p, a): True}, {}))

    # 4. Fallback Logic
    all_known = list(set(active_keys + always))
    cases.append((f"Fallback: {g_name}",
                  {_std_key(p, m): False for m in all_known},
                  {target_key: "none"}))

    # 5. Silence Logic
    for d in discs:
        cases.append((f"Silence: {d}", {_std_key(p, d): True}, {}))

    return [{"name": n, "input": i, "expected": e} for n, i, e in cases]


def generate_test_cases(cfg, schema):
    p = cfg["target_prefix"]
    types_cfg = cfg["types"]
    lookup = {s: g for g, sfxs in cfg["suffix_groups"].items() for s in sfxs}
    tests = []

    always_discards = set(cfg.get("discard_always", []))
    for g in cfg["select_groups"].values():
        always_discards.update(g.get("discard_always", []))

    mems = {m for g in cfg["select_groups"].values() for m in g["members"]}
    discs = {d for g in cfg["select_groups"].values()
             for d in g.get("discard_if_true", [])}

    for name, exp_type, default, _ in schema:
        if name in always_discards or name in mems or name in discs:
            continue
        tests.extend(_get_std_cases(
            name, exp_type, p, lookup[name], default, types_cfg
        ))

    for g_name, g_cfg in cfg["select_groups"].items():
        tests.extend(_get_select_cases(g_name, g_cfg, p, lookup, types_cfg))

    for a in cfg.get("discard_always", []):
        tests.append({
            "name": f"Global Discard: {a}",
            "input": {_std_key(p, a): "discard_me"},
            "expected": {}
        })
    return tests


def run_unit_tests(mapper, test_cases):
    passed = 0
    print(f"{'RESULT':<8} | {'TEST NAME':<50}")
    print("-" * 65)

    for case in test_cases:
        result = mapper.map_settings(case["input"])
        if result == case["expected"]:
            print(f"PASS     | {case['name']}")
            passed += 1
        else:
            print(f"FAIL     | {case['name']}")

            input_val = list(case['input'].values())[0]
            print(f"   -> Input Val: {input_val} ({type(input_val).__name__})")
            print(f"   -> Expected:  {case['expected']}")
            print(f"   -> Got:       {result}")

    print("-" * 65)
    print(f"Summary: {passed}/{len(test_cases)} passed.")


def generate_test_json(test_cases, schema, prefix, filename="test.json"):
    """Merges input data following schema order."""
    ordered_input = {}
    for name, _, _, _ in schema:
        key = f"{prefix}@@{prefix}-{name}"
        ordered_input[key] = None

    raw_values = {}
    for case in test_cases:
        raw_values.update(case["input"])

    final_output = {
        k: raw_values[k] for k in ordered_input if k in raw_values
    }

    with open(filename, "w") as f:
        json.dump(final_output, f, indent=2)

    print(f"Generated {filename} ({len(final_output)} keys).")


if __name__ == "__main__":
    config = get_mapping_config()
    mapper = SettingsMapper(config)
    schema = get_schema()
    prefix = config["target_prefix"]

    cases = generate_test_cases(config, schema)
    generate_test_json(cases, schema, prefix)

    print("\nStarting Exhaustive Migration Tests...\n")
    run_unit_tests(mapper, cases)
