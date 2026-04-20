#!/usr/bin/env python

"""
1.X.Y to 2.0.0 settings migration script.

Please supply sane settings entry value(s) else the type validation
would discard the entry value(s).

E.g. brightness-ratio of false in the JSON makes no sense
"""

import json
import sys
import argparse
import os
import ast


# ------------- #
# Schema Config #
# ------------- #


def get_mapping_config():
    P = "xyz"
    return {
        "target_prefix": P,
        "suffix_groups": {
            f"{P}-modes": [
                "rtz-mode", "flex-max-mode", "typewriter-mode",
                "typewriter-mode-opacity", "reverse-mode",
                "editor-writing", "editor-writing-indentation",
            ],
            f"{P}-a11y": ["brightness-ratio"]
        },
        "types": {
            "rtz-mode": bool,
            "flex-max-mode": bool,
            "typewriter-mode": bool,
            "typewriter-mode-opacity": (float, int),
            "reverse-mode": bool,
            "editor-writing": bool,
            "editor-writing-indentation": (float, int),
            "brightness-ratio": (float, int)
        },
        "defaults": {
            "typewriter-mode-opacity": 0.55,
            "editor-writing-indentation": 16,
            "brightness-ratio": 1.0
        },
        "discard_if_true": [],
        "select_groups": {
            "select-mode": {
                "members": ["rtz-mode", "flex-max-mode"],
                "discard_if_true": ["flex-max-mode"]
            }
        },
        "exact_matches": {}
    }


# ----------------- #
# Main Mapper Logic #
# ------------------ #

class GroupStatus:
    """Tracks the state of a specific settings group during migration."""

    def __init__(self):
        self.mentioned = False
        self.satisfied = False
        self.silenced = False
        self.poisoned = False

    @property
    def needs_fallback(self):
        """Returns True if the group should result in a 'none' state."""
        return (
            self.mentioned and not
            (self.satisfied or self.silenced or self.poisoned)
        )


class SettingsMapper:
    """Handles migration with strict type safety and group state management."""

    def __init__(self, config):
        self.config = config
        self.prefix = config.get("target_prefix", "")
        self.lookup = self._build_group_lookup()
        self.select_map = self._build_select_lookup()

    def _build_group_lookup(self):
        return {
            f"{self.prefix}-{sfx}": group
            for group, suffixes in self.config.get("suffix_groups", {}).items()
            for sfx in suffixes
        }

    def _build_select_lookup(self):
        mapping = {}
        for target, cfg in self.config.get("select_groups", {}).items():
            for m in cfg.get("members", []):
                mapping[m] = {"target": target, "type": "member"}
            for d in cfg.get("discard_if_true", []):
                mapping[d] = {"target": target, "type": "discard"}
        return mapping

    def _is_invalid_type(self, base_name, value):
        """Strict type checking: rejects bools when numbers are expected."""
        expected = self.config.get("types", {}).get(base_name)
        if not expected:
            return False

        # If value is bool, it's only valid if expected is explicitly bool
        if isinstance(value, bool):
            return expected is not bool

        # Standard check for other types
        return not isinstance(value, expected)

    def _handle_select_logic(self, base_name, value, group_prefix):
        """Processes select logic with internal type validation."""
        info = self.select_map.get(base_name)
        if not info:
            return None

        target = info["target"]
        if self._is_invalid_type(base_name, value):
            return "__INVALID_TYPE__", target

        if info["type"] == "discard" and value is True:
            return "__FORCE_SILENCE_GROUP__", target

        if value is True:
            return (f"{group_prefix}@@{self.prefix}-{target}",
                    f"{self.prefix}-{base_name}")

        return "__DISCARD__", target

    def _apply_rules(self, key, value):
        """Pipeline to transform keys with strict signaling."""
        if key in self.config.get("exact_matches", {}):
            return self.config["exact_matches"][key], value

        name = key.split('@@')[-1]
        group_prefix = self.lookup.get(name)
        if not group_prefix:
            return key, value

        base_name = name.replace(f"{self.prefix}-", "")

        # Select Logic Check
        select_res = self._handle_select_logic(base_name, value, group_prefix)
        if select_res:
            return select_res

        # Type Safety (Catch bools for numeric types)
        if self._is_invalid_type(base_name, value):
            return "__INVALID_TYPE__", None

        # Defaults Discard
        defaults = self.config.get("defaults", {})
        if base_name in defaults and value == defaults[base_name]:
            return "__DISCARD__", None

        # Logic for bool types
        if isinstance(value, bool):
            is_disc = base_name in self.config.get("discard_if_true", [])
            if not value or (is_disc and value is True):
                return "__DISCARD__", None

        return f"{group_prefix}@@{name}", value

    def map_settings(self, old_data):
        """Main loop with prioritized state tracking."""
        res, groups = {}, {
            t: GroupStatus() for t in self.config["select_groups"]
        }

        for k, v in old_data.items():
            base = k.split('@@')[-1].replace(f"{self.prefix}-", "")
            info = self.select_map.get(base)
            if info:
                groups[info["target"]].mentioned = True

            new_k, new_v = self._apply_rules(k, v)

            if new_k == "__INVALID_TYPE__":
                if new_v in groups:
                    groups[new_v].poisoned = True
                continue

            if new_k in [None, "__DISCARD__"]:
                continue

            if new_k == "__FORCE_SILENCE_GROUP__":
                if new_v in groups:
                    groups[new_v].silenced = True
                continue

            res[new_k] = new_v
            for g_name in groups:
                if f"{self.prefix}-{g_name}" in new_k:
                    groups[g_name].satisfied = True

        return self._apply_fallbacks(res, groups)

    def _apply_fallbacks(self, data, groups):
        """Applies 'none' state to mentioned but unsatisfied groups."""
        for name, status in groups.items():
            if status.needs_fallback:
                cfg = self.config["select_groups"][name]
                m_list = cfg.get("members") or cfg.get("discard_if_true")
                prefix = self.lookup.get(f"{self.prefix}-{m_list[0]}")
                data[f"{prefix}@@{self.prefix}-{name}"] = "none"
        return data

# --------------- #
# JSON Validation #
# --------------- #


def validate_json_with_ast(raw_data):
    """Checks for JSON syntax errors using json and ast for better errors."""
    try:
        json.loads(raw_data)
        return True, None
    except json.JSONDecodeError as e:
        try:
            ast.parse(raw_data)
        except SyntaxError as ast_err:
            return False, (f"Line {ast_err.lineno}, "
                           f"Col {ast_err.offset}: {ast_err.msg}")
        return False, f"Line {e.lineno}, Col {e.colno}: {e.msg}"


# ----------------- #
# Main argparse CLI #
# ----------------- #


def load_input_data(input_file):
    """Handles reading data from file or stdin."""
    if input_file:
        if not os.path.exists(input_file):
            return None, f"Error: File '{input_file}' not found."
        with open(input_file, 'r') as f:
            return f.read(), None

    if sys.stdin.isatty():
        return None, "Error: No input provided via file or pipe."

    return sys.stdin.read(), None


def write_output(output_str, filepath, no_write):
    """Writes results to file unless --no-write is specified."""
    print(output_str)
    if not no_write:
        with open(filepath, "w") as f:
            f.write(output_str)
        print(f"\n[Migration complete: {filepath}]", file=sys.stderr)


def setup_args():
    """Configures argparse and returns the parsed arguments."""
    desc = "Settings Migrator: Transforms 1.X.Y settings JSON to 2.0.0 spec."
    epilog = """
Examples:
  python migrator.py settings.json
  cat settings.json | python migrator.py
  python migrator.py test.json --no-write
    """
    parser = argparse.ArgumentParser(
        description=desc, epilog=epilog,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("input_file", nargs="?", help="Input file or stdin")
    parser.add_argument("--no-write", action="store_true", help="Stdout only")
    parser.add_argument(
        "--output", default="new_settings.json", help="Out file"
    )
    return parser


def main():
    """Main entry point with reduced cyclomatic complexity."""
    parser = setup_args()
    if len(sys.argv) == 1 and sys.stdin.isatty():
        parser.print_help()
        return

    args = parser.parse_args()
    raw_data, error = load_input_data(args.input_file)

    if error or not raw_data.strip():
        print(error or "Error: Input is empty.", file=sys.stderr)
        sys.exit(1)

    valid, err = validate_json_with_ast(raw_data)
    if not valid:
        print(f"INVALID JSON DETECTED:\n{err}", file=sys.stderr)
        sys.exit(1)

    mapper = SettingsMapper(get_mapping_config())
    try:
        output = mapper.map_settings(json.loads(raw_data))
        write_output(json.dumps(output, indent=2), args.output, args.no_write)
    except Exception as e:
        print(f"Mapping Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
