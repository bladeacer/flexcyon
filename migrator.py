#!/usr/bin/env python

"""
Pre-2.0.0 to 2.0.0 settings migration script, implemented using only Python
standard library.

Default values referenced are based on 1.4.0's.

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

def get_schema():
    """
    Define settings once with all metadata
    Format: (suffix, type, default, group_suffix, use_prefix?)
    """

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

        ("base-01@@dark", str, "#14161c", "editor"),
        ("base-02@@dark", str, "#191d28", "editor"),
        ("base-03@@dark", str, "#24262c", "editor"),
        ("base-04@@dark", str, "#4d566b", "editor"),
        ("base-05@@dark", str, "#6f7685", "editor"),

        ("base-grey-dark@@dark", str, "#898c93", "editor"),
        ("base-grey-light@@dark", str, "#d3d5d3", "editor"),

        ("base-01@@light", str, "#faf7ef", "editor"),
        ("base-02@@light", str, "#edebe5", "editor"),
        ("base-03@@light", str, "#dddcd6", "editor"),
        ("base-04@@light", str, "#d3d3ce", "editor"),
        ("base-05@@light", str, "#b4b3af", "editor"),

        ("base-grey-dark@@light", str, "#797876", "editor"),
        ("base-grey-light@@light", str, "#080808", "editor"),

        ("base-grey-tab", str, "#71777f", "editor"),
        ("base-grey-token", str, "#586582", "editor"),
        ("base-grey-scroll", str, "#3f495e", "editor"),
        ("base-grey-scroll-hover", str, "#5d6782", "editor"),

        ("text-normal@@dark", str, "#d3d5d3", "editor", False),
        ("text-normal@@light", str, "#080808", "editor", False),

    ]
    return schema


def get_mapping_config():
    P = "flexcyon"

    raw_schema = get_schema()

    normalized = [row if len(row) == 5 else (*row, True) for row in raw_schema]

    config = {
        "target_prefix": P,
        "schema": normalized,
        "suffix_groups": {},
        "types": {s: t for s, t, d, g, p in normalized},
        "defaults": {s: d for s, t, d, g, p in normalized},
        "prefix_map": {s: p for s, t, d, g, p in normalized},
        "select_groups": {
            "select-mode": {
                "members": ["rtz-mode", "flex-max-mode"],
                "discard_if_true": ["flex-max-mode"]
            }
        },

        "replacements": {
            "text-normal@@dark": "text-normal-col@@dark",
            "text-normal@@light": "text-normal-col@@light"
        },

        "keep_if_default": [],
        "discard_if_true": [],
        "discard_always": [
            "base-grey-tab", "base-grey-token",
            "base-grey-scroll", "base-grey-scroll-hover"
        ]
    }

    for sfx, _, _, group, _ in normalized:
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
        self.prefix_map = config.get("prefix_map", {})
        self.replacements = config.get("replacements", {})
        self.lookup = self._build_group_lookup()
        self.select_map = self._build_select_lookup()

        self.always_discard = set(config.get("discard_always", []))
        for g_cfg in config.get("select_groups", {}).values():
            self.always_discard.update(g_cfg.get("discard_always", []))

    def _get_full_name(self, suffix, original_base=None):
        """Standardizes the name based on the schema's use_prefix rule."""
        # 1. Identify the base key for the prefix lookup
        # If original_base is provided (from a replacement), use that rule.
        # Otherwise, extract it from the suffix.
        lookup_key = original_base if original_base else suffix.split('@@', 1)[0]

        # 2. Check the prefix map (defaults to True if not found)
        should_prefix = self.prefix_map.get(lookup_key, True)

        return f"{self.prefix}-{suffix}" if should_prefix else suffix

    def _build_group_lookup(self):
        """Maps full 1.X names to their 2.0 Group Prefixes."""
        lookup = {}
        for group, sfxs in self.cfg.get("suffix_groups", {}).items():
            for sfx in sfxs:
                # We map the 'expected' full name to the group label
                lookup[self._get_full_name(sfx)] = group
        return lookup

    def _build_select_lookup(self):
        mapping = {}
        for target, g_cfg in self.cfg.get("select_groups", {}).items():
            for m in g_cfg.get("members", []):
                mapping[m] = (target, MapResult.VALID)
            for d in g_cfg.get("discard_if_true", []):
                mapping[d] = (target, MapResult.SILENCE)
        return mapping

    def _process(self, key, val):
        parts = key.split('@@', 1)
        name = parts[-1]

        # 1. Clean the base (strip xyz- only if it is at the very start)
        base = name[len(self.prefix) + 1:] if name.startswith(f"{self.prefix}-") else name

        # 2. Type/Discard checks on the ORIGINAL base
        if base in self.always_discard:
            return MapResult(MapResult.DISCARD)

        if not self._check_type(base, val):
            target_g = self.select_map.get(base, (None,))[0]
            return MapResult(MapResult.POISON, group=target_g)

        # 3. Apply replacement to base (Do this once)
        final_base = self.replacements.get(base, base)

        # 4. Handle Select Groups
        if base in self.select_map:
            target, role = self.select_map[base]
            if role == MapResult.SILENCE and val is True:
                return MapResult(MapResult.SILENCE, group=target)
            if val is True:
                # We find the group label for the original member
                g_pref = self.lookup.get(self._get_full_name(base))
                new_k = f"{g_pref}@@{self.prefix}-{target}"
                return MapResult(
                    MapResult.VALID, new_k, f"{self.prefix}-{base}"
                )
            return MapResult(MapResult.DISCARD)

        # 5. Default check (Uses original base for default lookup)
        if val == self.cfg.get("defaults", {}).get(base) and \
           base not in self.cfg.get("keep_if_default", []):
            return MapResult(MapResult.DISCARD)

        # 6. Group Lookup
        # Find the group for the ORIGINAL base
        g_prefix = self.lookup.get(self._get_full_name(base))
        if not g_prefix:
            return MapResult(MapResult.VALID, key, val)

        # 7. Final Construction
        final_name = self._get_full_name(final_base, original_base=base)

        return MapResult(MapResult.VALID, f"{g_prefix}@@{final_name}", val)

    def _check_type(self, base, val):
        expected = self.cfg.get("types", {}).get(base)
        if not expected:
            return True
        return isinstance(val, bool) if expected is bool else isinstance(val, expected)

    def _build_ordered_output(self, res, groups):
        data_pool = self._apply_fallbacks(res, groups)
        ordered_final = {}

        for row in self.cfg["schema"]:
            sfx, _, _, group_sfx, _ = row
            g_label = f"{self.prefix}-{group_sfx}"

            target_base = self.replacements.get(sfx, sfx)
            target_name = self._get_full_name(target_base)
            target_key = f"{g_label}@@{target_name}"

            if target_key in data_pool:
                ordered_final[target_key] = data_pool.pop(target_key)

            orig_name = self._get_full_name(sfx)
            orig_key = f"{g_label}@@{orig_name}"
            if orig_key in data_pool:
                ordered_final[orig_key] = data_pool.pop(orig_key)

        for name, status in groups.items():
            m = self.cfg["select_groups"][name]["members"][0]
            g_label = self.lookup.get(self._get_full_name(m))
            target_key = f"{g_label}@@{self.prefix}-{name}"
            if target_key in data_pool:
                ordered_final[target_key] = data_pool.pop(target_key)

        ordered_final.update(sorted(data_pool.items()))
        return ordered_final

    def map_settings(self, data):
        """Coordinates results and returns them in schema-defined order."""
        res, groups = {}, {t: GroupStatus() for t in self.cfg["select_groups"]}

        for k, v in data.items():
            # Separate the prefix from the name accurately
            parts = k.split('@@', 1)
            name = parts[-1]
            base = name.replace(f"{self.prefix}-", "", 1)

            if base in self.select_map:
                groups[self.select_map[base][0]].mentioned = True

            out = self._process(k, v)

            if out.action == MapResult.VALID:
                res[out.key] = out.value
                for g_name in groups:
                    if f"{self.prefix}-{g_name}" in out.key:
                        groups[g_name].satisfied = True
            elif out.action == MapResult.POISON and out.group:
                groups[out.group].poisoned = True
            elif out.action == MapResult.SILENCE and out.group:
                groups[out.group].silenced = True

        # Pass processed results to fallback and sorting logic
        return self._build_ordered_output(res, groups)

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
