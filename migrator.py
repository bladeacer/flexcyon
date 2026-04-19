#!/usr/bin/env python

"""
xyz 1.X.Y to 2.0.0 settings migration script.
"""

import json
import sys
import argparse
import os
import ast


def get_mapping_config():
    """Centralized configuration for settings migration."""
    return {
        "suffix_groups": {
            "xyz-modes": ["xyz-rtz-mode", "xyz-flex-max-mode", "typewriter-mode"],
            "xyz-a11y": ["xyz-brightness-ratio"]
        },
        "mode_transforms": ["xyz-rtz-mode", "xyz-flex-max-mode"],
        "exact_matches": {
            # "xyz@old-legacy-key": "xyz-core@new-standard-key"
        }
    }


class SettingsMapper:
    def __init__(self, config):
        self.config = config
        # Flatten suffix groups into a direct lookup: {suffix: target_prefix}
        self.lookup = {
            sfx: prefix
            for prefix, suffixes in config.get("suffix_groups", {}).items()
            for sfx in suffixes
        }

    def _handle_mode_transform(self, name, value, prefix):
        """Logic for special boolean mode transformations."""
        if name in self.config.get("mode_transforms", []) and isinstance(value, bool):
            return (f"{prefix}@{name}", name) if value else (None, None)
        return f"{prefix}@{name}", value

    def _apply_rules(self, key, value):
        # 1. Exact Match (Highest Priority)
        if key in self.config.get("exact_matches", {}):
            return self.config["exact_matches"][key], value

        # 2. Lookup Suffix Group
        name = key.split('@')[-1]
        target_prefix = self.lookup.get(name)

        if target_prefix:
            return self._handle_mode_transform(name, value, target_prefix)

        # 3. Fallback
        return key, value

    def map_settings(self, old_data):
        new_data = {}
        for k, v in old_data.items():
            new_k, new_v = self._apply_rules(k, v)
            if new_k:
                new_data[new_k] = new_v
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
    parser = argparse.ArgumentParser(description="Settings Migrator")
    parser.add_argument("input_file", nargs="?", help="Input JSON file path")
    parser.add_argument("--no-write", action="store_true")
    parser.add_argument("--output", default="new_settings.json")
    args = parser.parse_args()

    # Load Data
    raw_data = ""
    if args.input_file and os.path.exists(args.input_file):
        with open(args.input_file, 'r') as f:
            raw_data = f.read()
    else:
        raw_data = sys.stdin.read()

    # Validate & Process
    valid, err = validate_json_with_ast(raw_data)
    if not valid:
        print(f"Error: {err}", file=sys.stderr)
        sys.exit(1)

    mapper = SettingsMapper(get_mapping_config())
    output = mapper.map_settings(json.loads(raw_data))

    output_str = json.dumps(output, indent=2)
    print(output_str)

    if not args.no_write:
        with open(args.output, "w") as f:
            f.write(output_str)


if __name__ == "__main__":
    main()
