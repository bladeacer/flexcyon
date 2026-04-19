#!/usr/bin/env python

"""
1.X.Y to 2.0.0 settings migration script.
"""

import json
import sys
import argparse
import os
import ast


def get_mapping_config():
    P = "flexcyon"
    return {
        "target_prefix": P,
        "suffix_groups": {
            f"{P}-modes": ["rtz-mode", "flex-max-mode", "typewriter-mode"],
            f"{P}-a11y": ["brightness-ratio"]
        },
        "discard_if_true": [],
        "select_groups": {
            "select-mode": {
                "members": ["rtz-mode"],
                "discard_if_true": ["flex-max-mode"]
            }
        },
        "exact_matches": {}
    }


class SettingsMapper:
    def __init__(self, config):
        self.config = config
        self.prefix = config.get("target_prefix", "")
        self.lookup = {}
        for group_name, suffixes in config.get("suffix_groups", {}).items():
            for sfx in suffixes:
                self.lookup[f"{self.prefix}-{sfx}"] = group_name

    def _apply_rules(self, key, value):
        if key in self.config.get("exact_matches", {}):
            return self.config["exact_matches"][key], value

        name = key.split('@@')[-1]
        group_prefix = self.lookup.get(name)
        if not group_prefix:
            return key, value

        base_name = name.replace(f"{self.prefix}-", "")

        # 1. Exclusive Select Group Logic
        for target_suffix, group_cfg in self.config.get("select_groups", {}).items():
            members = group_cfg.get("members", [])
            discards = group_cfg.get("discard_if_true", [])

            # Check if this is a "Nuclear Discard" flag
            if base_name in discards and value is True:
                return "__FORCE_SILENCE_GROUP__", target_suffix

            # Check if this is a standard member
            if base_name in members:
                if value is True:
                    return f"{group_prefix}@@{self.prefix}-{target_suffix}", name
                return "__SEEN_BUT_DISCARDED__", target_suffix

        # 2. Standard Boolean Logic (for non-group keys like typewriter)
        if isinstance(value, bool):
            if base_name in self.config.get("discard_if_true", []) and value is True:
                return None, None
            if value is False:
                return None, None

        return f"{group_prefix}@@{name}", value

    def map_settings(self, old_data):
        new_data = {}
        groups_mentioned = set()
        groups_satisfied = set()
        groups_silenced = set()

        for k, v in old_data.items():
            new_k, new_v = self._apply_rules(k, v)

            # Detect if this key belongs to any group in the config
            base_name = k.split('@@')[-1].replace(f"{self.prefix}-", "")
            for target, group_cfg in self.config.get("select_groups", {}).items():
                if base_name in group_cfg.get("members", []) or base_name in group_cfg.get("discard_if_true", []):
                    groups_mentioned.add(target)

            if new_k == "__FORCE_SILENCE_GROUP__":
                groups_silenced.add(new_v)
                continue

            if new_k == "__SEEN_BUT_DISCARDED__":
                continue

            if new_k:
                new_data[new_k] = new_v
                # Check if we satisfied a group target
                for target in self.config.get("select_groups", {}).keys():
                    if f"{self.prefix}-{target}" in new_k:
                        groups_satisfied.add(target)

        # Final pass: check for fallbacks
        for target, group_cfg in self.config.get("select_groups", {}).items():
            # Only add "none" if mentioned, not satisfied, AND not explicitly silenced
            if target in groups_mentioned and target not in groups_satisfied and target not in groups_silenced:
                # Use a member or a discard key to find the group prefix
                sample_key = group_cfg.get("members", group_cfg.get("discard_if_true", []))[0]
                group_prefix = self.lookup.get(f"{self.prefix}-{sample_key}")
                if group_prefix:
                    new_data[f"{group_prefix}@@{self.prefix}-{target}"] = "none"

        return new_data


def validate_json_with_ast(raw_data):
    try:
        json.loads(raw_data)
        return True, None
    except json.JSONDecodeError as e:
        try:
            ast.parse(raw_data)
        except SyntaxError as ast_err:
            return False, f"Line {ast_err.lineno}, Col {ast_err.offset}: {ast_err.msg}"
        return False, f"Line {e.lineno}, Col {e.colno}: {e.msg}"


def main():
    parser = argparse.ArgumentParser(
        description="Settings Migrator: Transforms 1.X.Y settings JSON to 2.0.0 spec.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python migrator.py settings.json           # Read file, write to new_settings.json
  cat settings.json | python migrator.py     # Pipe input, write to file
  python migrator.py test.json --no-write    # Print results to stdout only
        """
    )
    parser.add_argument(
        "input_file", nargs="?", help="Input JSON file path (or use stdin)"
    )
    parser.add_argument(
        "--no-write", action="store_true",
        help="Print to stdout only; do not create a file"
    )
    parser.add_argument(
        "--output", default="new_settings.json",
        help="Output filename (default: new_settings.json)"
    )

    # If no arguments and no piped data, show help and exit
    if len(sys.argv) == 1 and sys.stdin.isatty():
        parser.print_help()
        sys.exit(0)

    args = parser.parse_args()

    # Load Data
    raw_data = ""
    if args.input_file:
        if not os.path.exists(args.input_file):
            print(f"Error: File '{args.input_file}' not found.", file=sys.stderr)
            sys.exit(1)
        with open(args.input_file, 'r') as f:
            raw_data = f.read()
    else:
        # Check if stdin has data
        if sys.stdin.isatty():
            print("Error: No input provided via file or pipe.", file=sys.stderr)
            sys.exit(1)
        raw_data = sys.stdin.read()

    if not raw_data.strip():
        print("Error: Input is empty.", file=sys.stderr)
        sys.exit(1)

    # Validate & Process
    valid, err = validate_json_with_ast(raw_data)
    if not valid:
        print(f"INVALID JSON DETECTED:\n{err}", file=sys.stderr)
        sys.exit(1)

    mapper = SettingsMapper(get_mapping_config())
    try:
        old_settings = json.loads(raw_data)
        output = mapper.map_settings(old_settings)
    except Exception as e:
        print(f"Mapping Error: {e}", file=sys.stderr)
        sys.exit(1)

    output_str = json.dumps(output, indent=2)
    print(output_str)

    if not args.no_write:
        with open(args.output, "w") as f:
            f.write(output_str)
        print(f"\n[Migration complete: {args.output}]", file=sys.stderr)


if __name__ == "__main__":
    main()
