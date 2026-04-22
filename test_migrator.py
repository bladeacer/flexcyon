#!/usr/bin/env python

"""
Dynamic Unit Tests for 1.X.Y to 2.0.0 settings migration.
"""

import json
from migrator import SettingsMapper, get_mapping_config


def _get_full_name(p, suffix, prefix_map, original_base=None):
    # Use the original name to find the prefix rule if this is a replacement
    lookup_key = original_base if original_base else suffix.split('@@', 1)[0]
    should_prefix = prefix_map.get(lookup_key, True)
    return f"{p}-{suffix}" if should_prefix else suffix


def _std_key(p, sfx, prefix_map):
    """Generates the 1.X.Y style input key."""
    # Input keys are assumed to follow the schema's prefix rule
    return f"{p}@@{_get_full_name(p, sfx, prefix_map)}"


def _get_all_poison_samples(name, types_cfg):
    expected = types_cfg.get(name)
    if not isinstance(expected, tuple):
        expected = (expected,)

    samples = [
        ("bool", True),
        ("int", 123),
        ("float", 45.67),
        ("str", "poison_string")
    ]

    poisons = []
    for t_name, val in samples:
        if not any(isinstance(val, t) for t in expected):
            poisons.append((t_name, val))
    return poisons


def _get_std_cases(name, exp_type, p, group, default, cfg):
    prefix_map = cfg["prefix_map"]
    replacements = cfg.get("replacements", {})
    types_cfg = cfg["types"]

    k = _std_key(p, name, prefix_map)

    # Apply replacement if it exists
    final_base = replacements.get(name, name)

    name_part = _get_full_name(p, final_base, prefix_map, original_base=name)
    target = f"{group}@@{name_part}"
    # -----------------------

    # Determine a valid value that isn't the default
    if exp_type is str:
        valid_val = f"custom-{default}"
    elif exp_type in [(float, int), float, int]:
        valid_val = 0.8 if default != 0.8 else 0.4
    else:
        valid_val = not default

    cases = [(f"Valid: {name}", {k: valid_val}, {target: valid_val})]

    cases = [(f"Valid: {name}", {k: valid_val}, {target: valid_val})]

    # Poison cases
    for t_name, p_val in _get_all_poison_samples(name, types_cfg):
        cases.append((
            f"Bad Type [{t_name}]: {name}",
            {k: p_val},
            {}
        ))

    # Default cases
    if default is not None:
        keep_if_default = cfg.get("keep_if_default", [])
        expected_on_default = {target: default} if name in keep_if_default else {}
        cases.append((f"Default: {name}", {k: default}, expected_on_default))

    return [{"name": n, "input": i, "expected": e} for n, i, e in cases]


def _get_select_cases(g_name, g_cfg, p, lookup, cfg):
    prefix_map = cfg["prefix_map"]
    types_cfg = cfg["types"]
    mems = g_cfg["members"]
    discs = g_cfg.get("discard_if_true", [])
    always = g_cfg.get("discard_always", [])
    active_keys = list(set(mems + discs))

    # Select group targets usually follow the member's group prefix
    target_key = f"{lookup[_get_full_name(p, mems[0], prefix_map)]}@@{p}-{g_name}"
    cases = []

    for m in active_keys:
        for t_name, p_val in _get_all_poison_samples(m, types_cfg):
            cases.append((
                f"Select Poison {m} [{t_name}]",
                {_std_key(p, m, prefix_map): p_val},
                {}
            ))

    for m in [m for m in mems if m not in discs]:
        cases.append((f"Win: {m}", {_std_key(p, m, prefix_map): True},
                      {target_key: f"{p}-{m}"}))

    for a in always:
        cases.append(
            (f"Group Discard: {a}", {_std_key(p, a, prefix_map): True}, {})
        )

    all_known = list(set(active_keys + always))
    cases.append((f"Fallback: {g_name}",
                  {_std_key(p, m, prefix_map): False for m in all_known},
                  {target_key: "none"}))

    for d in discs:
        cases.append((f"Silence: {d}", {_std_key(p, d, prefix_map): True}, {}))

    return [{"name": n, "input": i, "expected": e} for n, i, e in cases]


def generate_test_cases(cfg, schema):
    p = cfg["target_prefix"]
    prefix_map = cfg["prefix_map"]
    tests = []

    # Build flat lookup following the mapper's prefix logic
    lookup = {}
    for g_label, sfxs in cfg["suffix_groups"].items():
        for s in sfxs:
            name_key = _get_full_name(p, s, prefix_map)
            lookup[name_key] = g_label

    always_discards = set(cfg.get("discard_always", []))
    for g in cfg["select_groups"].values():
        always_discards.update(g.get("discard_always", []))

    mems = {m for g in cfg["select_groups"].values() for m in g["members"]}
    discs = {d for g in cfg["select_groups"].values()
             for d in g.get("discard_if_true", [])}

    for row in schema:
        name, exp_type, default, group_sfx = row[:4]
        if name in always_discards or name in mems or name in discs:
            continue

        full_name = _get_full_name(p, name, prefix_map)
        tests.extend(_get_std_cases(
            name, exp_type, p, lookup[full_name], default, cfg
        ))

    for g_name, g_cfg in cfg["select_groups"].items():
        tests.extend(_get_select_cases(g_name, g_cfg, p, lookup, cfg))

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
            input_key = list(case['input'].keys())[0]
            input_val = case['input'][input_key]
            print(f"   -> Input:     {input_key}: {input_val}")
            print(f"   -> Expected:  {case['expected']}")
            print(f"   -> Got:       {result}")

    print("-" * 65)
    print(f"Summary: {passed}/{len(test_cases)} passed.")


def generate_test_json(test_cases, schema, prefix, filename="test.json"):
    """Merges input data following schema order."""
    prefix_map = {row[0]: (row[4] if len(row) > 4 else True) for row in schema}
    ordered_input = {}

    for row in schema:
        name = row[0]
        # Use the prefixing rule to generate the correct key for the JSON file
        use_p = prefix_map.get(name, True)
        name_part = f"{prefix}-{name}" if use_p else name
        key = f"{prefix}@@{name_part}"
        ordered_input[key] = None

    raw_values = {}
    for case in test_cases:
        raw_values.update(case["input"])

    final_output = {
        k: raw_values[k] for k in ordered_input if k in raw_values
    }

    with open(filename, "w") as f:
        json.dump(final_output, f, indent=2)


if __name__ == "__main__":
    config = get_mapping_config()
    mapper = SettingsMapper(config)
    schema_ref = config["schema"]
    prefix_ref = config["target_prefix"]

    cases_ref = generate_test_cases(config, schema_ref)
    generate_test_json(cases_ref, schema_ref, prefix_ref)

    print("\nStarting Exhaustive Migration Tests...\n")
    run_unit_tests(mapper, cases_ref)
