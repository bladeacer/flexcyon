#!/usr/bin/env python

"""
1.X.Y to 2.0.0 settings migration script, implemented using only Python
standard library.

Please supply sane settings entry value(s) else the type validation
would discard the entry value(s).

E.g. brightness-ratio of false in the JSON makes no sense.
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
    P = "flexcyon"

    # Define settings once with all metadata
    # Format: (suffix, type, default, group_suffix)
    schema = [
        ("rtz-mode", bool, False, "modes"),
        ("flex-max-mode", bool, False, "modes"),
        ("typewriter-mode", bool, False, "modes"),
        ("typewriter-mode-opacity", (float, int), 0.55, "modes"),
        ("reverse-mode", bool, False, "modes"),
        ("editor-writing", bool, False, "modes"),
        ("editor-writing-indentation", (float, int), 16, "modes"),

        ("brightness-ratio", (float, int), 1.0, "a11y"),
        ("contrast-ratio", (float, int), 1.0, "a11y"),
        ("saturation-ratio", (float, int), 1.0, "a11y"),
        ("revert-nav-item-alignment", bool, True, "mobile"),

        ("cyan@@dark", str, "#3cb9c2", "editor"),
        ("lime-green@@dark", str, "#a1c05c", "editor"),
        ("orange@@dark", str, "#cc8449", "editor"),
        ("yellow@@dark", str, "#c29e42", "editor"),
        ("purple-lilac@@dark", str, "#a461c8", "editor"),
        ("red-salmon@@dark", str, "#c03a47", "editor"),
        ("blue@@dark", str, "#5a8fcd", "editor"),
        ("pink@@dark", str, "#d458a3", "editor"),

        ("cyan@@light", str, "#3b9ba1", "editor"),
        ("lime-green@@light", str, "#689523", "editor"),
        ("orange@@light", str, "#ed8126", "editor"),
        ("yellow@@light", str, "#e8c62a", "editor"),
        ("purple-lilac@@light", str, "#6f49ae", "editor"),
        ("red-salmon@@light", str, "#eb5325", "editor"),
        ("blue@@light", str, "#5c9fe4", "editor"),
        ("pink@@light", str, "#e389ca", "editor"),

        ("accent@@dark", str, "#92a871", "editor"),
        ("accent@@light", str, "#5770b9", "editor"),

        ("ext-colors-enabled", bool, False, "editor"),
    ]

    config = {
        "target_prefix": P,
        "suffix_groups": {},
        "types": {s: t for s, t, d, g in schema},
        "defaults": {s: d for s, t, d, g in schema},
        "keep_if_default": [],
        "select_groups": {
            "select-mode": {
                "members": ["rtz-mode", "flex-max-mode"],
                "discard_if_true": ["flex-max-mode"]
            }
        },
        "exact_matches": {}
    }

    for sfx, _, _, group in schema:
        g_key = f"{P}-{group}"
        config["suffix_groups"].setdefault(g_key, []).append(sfx)

    return config

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


class MapResult:
    """Internal signal object for the mapping pipeline."""
    DISCARD = 0
    VALID = 1
    POISON = 2
    SILENCE = 3

    def __init__(self, action, key=None, value=None, group=None):
        self.action = action
        self.key = key
        self.value = value
        self.group = group


class SettingsMapper:
    """Handles migration with strict typing and group management."""

    def __init__(self, config):
        self.cfg = config
        self.prefix = config.get("target_prefix", "")
        self.lookup = self._build_group_lookup()
        self.select_map = self._build_select_lookup()

    def _build_group_lookup(self):
        return {
            f"{self.prefix}-{sfx}": group
            for group, sfxs in self.cfg.get("suffix_groups", {}).items()
            for sfx in sfxs
        }

    def _build_select_lookup(self):
        mapping = {}
        for target, g_cfg in self.cfg.get("select_groups", {}).items():
            for m in g_cfg.get("members", []):
                mapping[m] = (target, MapResult.VALID)
            for d in g_cfg.get("discard_if_true", []):
                mapping[d] = (target, MapResult.SILENCE)
        return mapping

    def _check_type(self, base, val):
        expected = self.cfg.get("types", {}).get(base)
        if not expected:
            return True
        if isinstance(val, bool):
            return expected is bool
        return isinstance(val, expected)

    def _process(self, key, val):
        # Change: split only on the FIRST '@@' to separate prefix from the rest
        parts = key.split('@@', 1)
        name = parts[-1]

        g_prefix = self.lookup.get(name)
        if not g_prefix:
            # Fallback if group is missing
            return MapResult(MapResult.VALID, key, val)

        # Base should be the name minus the 'prefix-' part
        base = name.replace(f"{self.prefix}-", "", 1)

        # 1. Type Check
        if not self._check_type(base, val):
            target_g = self.select_map.get(base, (None,))[0]
            return MapResult(MapResult.POISON, group=target_g)

        # 2. Select Group Logic
        if base in self.select_map:
            target, role = self.select_map[base]
            if role == MapResult.SILENCE and val is True:
                return MapResult(MapResult.SILENCE, group=target)
            if val is True:
                new_k = f"{g_prefix}@@{self.prefix}-{target}"
                return MapResult(
                    MapResult.VALID, new_k, f"{self.prefix}-{base}"
                )
            return MapResult(MapResult.DISCARD)

        # 3. Dynamic Default Discard
        # Assumes discard if val == default, unless explicitly whitelisted
        is_default = val == self.cfg.get("defaults", {}).get(base)
        keep_exceptions = self.cfg.get("keep_if_default", [])

        if is_default and base not in keep_exceptions:
            return MapResult(MapResult.DISCARD)

        return MapResult(MapResult.VALID, f"{g_prefix}@@{name}", val)

    def map_settings(self, data):
        """Coordinates individual results into a final state."""
        res, groups = {}, {t: GroupStatus() for t in self.cfg["select_groups"]}

        for k, v in data.items():
            base = k.split('@@')[-1].replace(f"{self.prefix}-", "")

            # 1. Update 'mentioned' status immediately
            if base in self.select_map:
                groups[self.select_map[base][0]].mentioned = True

            # 2. Process the individual key
            out = self._process(k, v)

            # 3. Update Group State based on Action
            if out.action == MapResult.VALID:
                res[out.key] = out.value
                # If this key belongs to a select group, mark it satisfied
                for g_name in groups:
                    if f"{self.prefix}-{g_name}" in out.key:
                        groups[g_name].satisfied = True

            elif out.action == MapResult.POISON and out.group:
                groups[out.group].poisoned = True

            elif out.action == MapResult.SILENCE and out.group:
                groups[out.group].silenced = True

        return self._apply_fallbacks(res, groups)

    def _apply_fallbacks(self, data, groups):
        """Final pass to inject 'none' for unsatisfied groups."""
        for name, status in groups.items():
            if status.needs_fallback:
                # Retrieve group label from any member's prefix
                m = self.cfg["select_groups"][name]["members"][0]
                g_label = self.lookup.get(f"{self.prefix}-{m}")
                data[f"{g_label}@@{self.prefix}-{name}"] = "none"
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
