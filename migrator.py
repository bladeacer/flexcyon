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

def get_prefix():
    P = "flexcyon"
    return P


def get_schema():
    """
    Define settings once with all metadata
    Format: (suffix, type, default, group_suffix, use_prefix?)
    """

    P = get_prefix()

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
        ("status-mobile-enabled", bool, False, "mobile"),

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

        ("text-muted", str, "#6f768599", "editor"),

        ("line-height-normal", (float, int), 1.4, "editor", False),
        ("line-height-tight", (float, int), 1.25, "editor", False),

        ("w-spacing", (float, int), 0, "editor"),
        ("l-spacing", (float, int), 0, "editor"),

        ("highlight-colour", str, "var(--color-cyan)", "editor"),
        ("highlight-opacity", str, "22.5%", "editor"),
        ("highlight-verti-padding", (float, int), 1, "editor"),
        ("highlight-horiz-padding", (float, int), 2.5, "editor"),
        ("highlight-border-radius", (float, int), 4, "editor"),

        ("coloured-headings", bool, True, "editor"),
        ("headings-glow-enabled", bool, False, "editor"),

        ("headings-indicator-h1", bool, False, "editor"),
        ("h1-color", str, "var(--color-blue)", "editor"),
        ("h1-size", (float, int), 1.818, "editor", False),
        ("h1-weight", (float, int), 700, "editor", False),
        ("h1-line-height", (float, int), 1.61, "editor", False),
        ("h1-underline-enabled", bool, False, "editor"),
        ("heading-1-alignment", str, "left", "editor"),

        ("headings-indicator-h2", bool, False, "editor"),
        ("h2-color", str, "var(--color-purple)", "editor"),
        ("h2-size", (float, int), 1.618, "editor", False),
        ("h2-weight", (float, int), 675, "editor", False),
        ("h2-line-height", (float, int), 1.51, "editor", False),
        ("h2-underline-enabled", bool, False, "editor"),
        ("heading-2-alignment", str, "left", "editor"),

        ("headings-indicator-h3", bool, False, "editor"),
        ("h3-color", str, "var(--color-cyan)", "editor"),
        ("h3-size", (float, int), 1.418, "editor", False),
        ("h3-weight", (float, int), 650, "editor", False),
        ("h3-line-height", (float, int), 1.41, "editor", False),
        ("h3-underline-enabled", bool, False, "editor"),
        ("heading-3-alignment", str, "left", "editor"),

        ("headings-indicator-h4", bool, False, "editor"),
        ("h4-color", str, "var(--color-pink)", "editor"),
        ("h4-size", (float, int), 1.218, "editor", False),
        ("h4-weight", (float, int), 625, "editor", False),
        ("h4-line-height", (float, int), 1.31, "editor", False),
        ("h4-underline-enabled", bool, False, "editor"),
        ("heading-4-alignment", str, "left", "editor"),

        ("headings-indicator-h5", bool, False, "editor"),
        ("h5-color", str, "var(--color-green)", "editor"),
        ("h5-size", (float, int), 1.118, "editor", False),
        ("h5-weight", (float, int), 600, "editor", False),
        ("h5-line-height", (float, int), 1.21, "editor", False),
        ("h5-underline-enabled", bool, False, "editor"),
        ("heading-5-alignment", str, "left", "editor"),

        ("headings-indicator-h6", bool, False, "editor"),
        ("h6-color", str, "var(--color-yellow)", "editor"),
        ("h6-size", (float, int), 1.018, "editor", False),
        ("h6-weight", (float, int), 575, "editor", False),
        ("h6-line-height", (float, int), 1.21, "editor", False),
        ("h6-underline-enabled", bool, False, "editor"),
        ("heading-6-alignment", str, "left", "editor"),

        ("inline-title-size", (float, int), 1.802, "editor", False),
        ("inline-title-weight", (float, int), 700, "editor", False),
        ("inline-title-line-height", (float, int), 1.2, "editor", False),
        ("no-inline-title", bool, False, "editor"),

        ("font-ui-smaller", (float, int), 12.9442, "editor", False),
        ("font-ui-small", (float, int), 14.5622, "editor", False),
        ("font-ui-medium", (float, int), 16.1803, "editor", False),
        ("font-ui-large", (float, int), 17.7983, "editor", False),

        ("dimmed", (float, int), 0.55, "editor", False),
        ("block-label-opacity", (float, int), 0.55, "editor"),
        ("status-new-tab-opacity", (float, int), 0.55, "editor"),
        ("status-new-tab-opacity", (float, int), 0.55, "editor"),
        ("callout-bg-opacity", str, "20%", "editor"),
        ("highlight-active-line-opacity", str, "20%", "editor"),
        ("cb-syntax-mode", str, "none", "editor"),
        ("codeblock-fmt-ext", str, "lowercase", "editor"),
        ("codeblock-prefix-ext", bool, False, "editor"),
        ("code-file-ext-prefix", str, ".", "editor"),
        ("code-file-ext-font-w", (float, int), 500, "editor"),

        ("table-border-color", str, "#6f768566", "editor", False),
        ("table-reading-mode-width", str, "100%", "editor"),
        ("table-header-size", str, "var(--font-ui-large)", "editor", False),
        ("th-verti-padding", (float, int), 5, "editor"),
        ("th-horiz-padding", (float, int), 10, "editor"),
        ("th-live-pad-scale", (float, int), 0.2, "editor"),
        ("table-text-size", str, "var(--font-ui-medium)", "editor", False),
        ("td-verti-padding", (float, int), 5, "editor"),
        ("td-horiz-padding", (float, int), 10, "editor"),
        ("td-live-pad-scale", (float, int), 0.2, "editor"),

        ("file-exp-dimmed-file-exts-enabled", bool, False, "editor"),
        ("exp-dimmed-nav-size", (float, int), 13.3623, "editor"),
        ("enable-active-indicator", bool, False, "editor"),
        ("active-indicator", str, ">> ", "editor"),
        ("vertical-nav", bool, False, "editor"),
        ("folder-style", str, "none", "editor"),
        ("is-bg-rainbow", bool, True, "editor"),
        ("minimalist-tree", bool, False, "editor"),
        ("tree-item-verti-padding", (float, int), 2, "editor"),
        ("tree-item-horiz-padding", (float, int), 10, "editor"),
        ("wrap-long-filenames", bool, True, "editor"),
        ("reverse-workspace-content", bool, False, "editor"),

        ("file-line-width", (float, int), 50, "editor", False),
        ("editor-margin-top", (float, int), 50, "editor"),
        ("top-actions-alignment", str, "center", "editor"),

        ("prompt-width", (float, int), 700, "editor", False),
        ("prompt-max-width", (float, int), 80, "editor", False),
        ("prompt-max-height", (float, int), 70, "editor", False),
        ("prompt-alignment", str, "none", "editor"),
        ("suggestion-verti-padding", (float, int), 8, "editor"),
        ("suggestion-horiz-padding", (float, int), 12, "editor"),
        ("titlebar-button-effects", bool, False, "editor"),
        (
            "status-hide-until-trigger", str,
            f"{P}-status-hide-until-hover", "editor"
        ),
        ("status-alignment", str, f"{P}-status-right-align", "editor"),
        ("status-hide-until-hover-text", str, "Show status", "editor"),
        ("status-hide-hover-translation", (float, int), 80, "editor"),
        ("status-hide-hover-duration", (float, int), 325, "editor"),
        ("status-hide-hover-function", str, "ease-out", "editor"),
        ("status-text-mode", bool, False, "editor"),
        ("status-reading-text", str, "READ", "editor"),
        ("status-source-text", str, "SOURCE", "editor"),
        ("status-live-text", str, "LIVE", "editor"),
        ("status-bar-font-size", (float, int), 13.7533, "editor", False),
        ("status-style", str, "none", "editor"),
        ("status-text-enable-color", bool, False, "editor"),
        ("no-status-in-new-tab", bool, False, "editor"),

        ("anim-type", str, "none", "editor"),
        ("modal-anim-type", str, "none", "editor"),
        ("anim-duration", (float, int), 300, "editor"),
        ("anim-easing", str, "ease-in-out", "editor"),
        ("anim-slide-amount", (float, int), 56.6311, "editor"),
        ("anim-style-settings-contain", bool, False, "editor"),
        ("anim-start-scale-amt", (float, int), 0.33, "editor"),
        ("anim-start-opacity", (float, int), 0.55, "editor"),

        ("workspace-layout", str, "none", "editor"),
        ("workspace-cards-tui-ext", bool, True, "editor"),

        ("view-header-breadcrumb-max-w", (float, int), 12.5, "editor"),
        ("mode-view-header-title-verti-padding", (float, int), 4, "editor"),
        ("mode-view-header-title-horiz-padding", (float, int), 12, "editor"),

        ("bg-type", str, "none", "editor"),
        ("editor-bg-rotation", (float, int), 0, "editor"),
        ("editor-bg-width", (float, int), 15, "editor"),
        ("editor-dot-size", (float, int), 2.5, "editor"),

        ("callout-icon-right-padding", (float, int), 4, "editor"),
        ("callout-first-codeblock-margin-top", (float, int), 1, "editor"),
        ("callout-vertical-margin", (float, int), 1, "editor"),
        ("callout-horizontal-margin", (float, int), 0, "editor"),
        ("callout-verti-padding", (float, int), 12, "editor"),
        ("callout-horiz-padding", (float, int), 24, "editor"),
        ("callout-radius", (float, int), 2, "editor", False),
        ("callout-radix", (float, int), 16, "editor"),
        ("callout-style", str, "none", "editor"),
        ("tui-no-icons", bool, False, "editor"),
        ("tui-no-icons", bool, False, "editor"),
        ("callouts-flashcard-width", (float, int), 250, "editor"),
        ("callouts-flashcard-height", (float, int), 250, "editor"),
        ("callout-flashcard-animation-duration", (float, int), 500, "editor"),
        ("callout-pop-animation-duration", (float, int), 200, "editor"),

        ("hr-no-reading", bool, False, "editor"),
        ("hr-color", str, "#393e48", "editor", False),
        ("cust-str-hr", bool, False, "editor"),
        ("cust-hr-str", str, "f", "editor"),
        ("cust-hr-str-font-size", (float, int), 1.118, "editor"),
        ("cust-hr-str-horiz-padding", (float, int), 8, "editor"),

        ("ascii-checkboxes-enabled", bool, False, "editor"),
        ("ascii-checkboxes-font-size", (float, int), 1.2, "editor"),
        ("clip-path-checkboxes-enabled", bool, False, "editor"),
        ("rainbow-bullet-points", bool, False, "editor"),
        ("default-ol-style", str, "decimal", "editor"),

        ("media-embed-vertical-margin", (float, int), 8, "editor"),
        ("img-border-radius", (float, int), 15, "editor", False),

        ("link-color@@dark", str, "#a461c8", "editor"),
        ("link-external-link-color@@dark", str, "#5a8fcd", "editor"),
        ("link-unresolved-color@@dark", str, "#a461c8", "editor"),

        ("link-color@@light", str, "#6f49ae", "editor"),
        ("link-external-link-color@@light", str, "#5c9fe4", "editor"),
        ("link-unresolved-color@@light", str, "#6f49ae", "editor"),
        ("alt-link-style", bool, False, "editor"),
        ("alt-link-opacity", str, "55%", "editor"),
        ("comm-item-opacity", (float, int), 0.89, "editor"),

        ("metadata-display-reading-disabled", bool, False, "editor"),
        ("metadata-display-editing-disabled", bool, False, "editor"),
        ("metadata-rainbow-icons", bool, False, "editor"),
        ("meta-container-padding-left", (float, int), 14, "editor"),
        ("metadata-no-properties-title", bool, False, "editor"),

        ("highlight-active-line", bool, False, "editor"),
        ("enable-rel-nums", bool, False, "editor"),
        ("no-num-with-relative", bool, False, "editor"),
        ("relative-num-only", bool, False, "editor"),
        ("select-relative-num", str, "none", "editor"),
        ("repl-active-line-num-str", bool, False, "editor"),
        ("repl-active-line-str", str, "->", "editor"),
        ("repl-active-str-space", (float, int), 0, "editor"),

        ("cursor-type", str, "auto", "editor"),
        ("enable-smooth-cursor", bool, True, "editor"),
        ("cursor-duration", (float, int), 42.5, "editor"),
        ("cursor-timing-fn", str, "ease-in", "editor"),
        ("cursor-min-width", str, "unset", "editor"),

        ("graph-control-verti-padding", (float, int), 6, "editor", False),
        ("graph-control-horiz-padding", (float, int), 12, "editor", False),

        ("display-os", bool, False, "editor"),
        ("os-detail-padding-l", (float, int), 12, "editor"),
        ("os-detail-padding-r", (float, int), 8, "editor"),
        ("display-screen-dimens", bool, False, "editor"),
        ("screen-dimens-padding-l", (float, int), 16, "editor"),

        ("number-tabs", bool, False, "editor"),
        ("remove-tab-headers", bool, False, "editor"),
        ("reverse-tab-header-container", bool, False, "editor"),

        ("upsize", str, "103%", "editor", False),
        ("expand", str, "110%", "editor", False),
        ("settings-smiley-icons-enabled", bool, False, "editor"),
        ("ascii-icon-set", bool, False, "editor"),
        ("ensure-plugin-icon", bool, True, "editor"),
        ("settings-coloured-icons", bool, False, "editor"),
        ("stylised-pins", bool, True, "editor"),
        ("prevent-accidental-unpin", bool, True, "editor"),

        ("input-radius", (float, int), 0, "editor", False),
        ("input-verti-padding", (float, int), 4, "editor"),
        ("input-horiz-padding", (float, int), 8, "editor"),

        ("settings-comm-item-enabled", bool, True, "settings"),
        (
            "settings-installed-tooltip-left-margin", (float, int),
            1, "settings"
        ),
        ("settings-scrollbar-removed", bool, False, "settings"),
        ("enable-alt-active-item-effect", bool, True, "settings"),
        ("style-settings-indent-width", (float, int), 4, "settings"),
        ("style-settings-dim-collapsed-headings", bool, True, "settings"),

        ("oz-fta-folder-font-size", (float, int), 0.925, "plugins", False),
        (
            "oz-fta-folder-pane-file-name-color", str,
            "#080808", "plugins", False
        ),
        (
            "oz-fta-all-panes-active-text-color", str,
            "#080808", "plugins", False
        ),
        ("oz-fta-file-font-size", (float, int), 0.9, "plugins", False),
        (
            "oz-fta-file-pane-file-name-color", str,
            "#6f768599", "plugins", False
        ),
        ("oz-file-tree-header-disabled", bool, False, "plugins"),
        ("oz-alternate-folder-count", bool, False, "plugins"),
        ("oz-dimmed-file-exts-enabled", bool, False, "plugins"),

        ("fc-dimmed-items-opacity", (float, int), 0.89, "plugins"),

        (
            "dataview-dataview-horizontal-padding", (float, int),
            0.89, "plugins"
        ),

        ("canvas-blur-inactive-nodes", bool, False, "plugins"),
        ("canvas-blur-intensity", (float, int), 1, "plugins"),
        ("canvas-menu-alignment", str, "none", "plugins"),

        ("var-comps-sugg-vert-padding", (float, int), 7, "plugins"),
        ("var-comps-sugg-horiz-padding", (float, int), 12, "plugins"),
        ("var-comps-sugg-compact-mode", bool, False, "plugins"),

        ("omnisearch-no-icons", bool, False, "plugins"),
        ("omnisearch-body-margin-left", (float, int), 1.45, "plugins"),

        ("bases-padding-verti", (float, int), 16, "plugins"),
        ("bases-padding-horiz", (float, int), 16, "plugins"),
        ("bases-embed-padding", (float, int), 4, "plugins", False),
        ("bases-cards-label-opacity", (float, int), 0.85, "plugins"),
        (
            "bases-no-img-str", str,
            "No image path could be found for this file", "plugins", False
        ),
        ("bases-border-r", (float, int), 16, "plugins", False),
        ("bases-cards-group-padding", (float, int), 16, "plugins", False),
        ("bases-card-padding-top", (float, int), 8, "plugins"),
        ("bases-card-padding-right", (float, int), 0, "plugins"),
        ("bases-card-padding-bottom", (float, int), 0, "plugins"),
        ("bases-card-padding-left", (float, int), 2, "plugins"),
        ("bases-card-flex-grow", (float, int), 0.55, "plugins"),

        ("bases-td-padding-l", (float, int), 2, "plugins"),
        ("bases-table-content-alignment", str, "left", "plugins"),
        ("hide-until-hover-bases-title-sidebar", str, "left", "plugins"),

        ("vim-mode-text-enable", bool, True, "others"),
        ("vim-left-positioning", (float, int), 6, "others"),
        ("vim-bottom-positioning", (float, int), -4, "others"),
        ("vim-insert-text", str, "INSERT", "others"),
        ("vim-normal-text", str, "NORMAL", "others"),
        ("vim-command-text", str, "COMMAND", "others"),

        ("new-tab-mod", str, "none", "others"),
        ("new-tab-font-group", str, "var(--font-monospace)", "others"),
        (
            "flexcyon-new-tab-bg-wrapper", str,
            "linear-gradient(to right, var(--text-accent), var(--color-purple))",
            "others"
        ),
        (
            "quote-val", str,
            "This is a placeholder quote\ain the Flexcyon Theme.", "others"
        ),
        ("quote-credit-prefix", str, "-", "others"),
        ("quote-credit", str, "bladeacer", "others"),
        ("quote-font-size", (float, int), 24, "others"),

        ("ascii-max-font-size", (float, int), 14, "others"),
        ("ascii-line-height", (float, int), 1.5, "others"),
        ("ascii-scaling-factor", (float, int), 1, "others"),
        ("ascii-alignment", str, "left", "others"),
        ("empty-state-title-disable", bool, True, "others"),
        ("empty-state-actions-disable", bool, True, "others"),

        ("sidedock-icon-effects", bool, True, "others"),
        ("ribbon-top", bool, False, "others"),
        ("ribbon-vault-switch", bool, False, "others"),
        ("ribbon-vault-reverse", bool, False, "others"),

        ("radius-s", (float, int), 2, "others", False),
        ("radius-m", (float, int), 4, "others", False),
        ("radius-l", (float, int), 6, "others", False),
        ("radius-xl", (float, int), 8, "others", False),

        ("sidebar-bg", str, "none", "others"),
        ("bg-image-sidebar-left-url", str, 'url("")', "others"),
        ("bg-image-sidebar-right-url", str, 'url("")', "others"),
        ("bg-image-blend-mode", str, "darken", "others"),
        ("bg-image-repeat", str, "no-repeat", "others"),
        ("bg-image-blur", (float, int), 0, "others"),
        ("bg-image-brightness", str, "unset", "others"),
        ("bg-image-size", str, "cover", "others"),
        ("bg-image-position", str, "center", "others"),

        ("modal-bg-url", str, 'url("")', "others"),
        ("modal-image-blend-mode", str, "darken", "others"),
        ("modal-image-repeat", str, "no-repeat", "others"),
        ("modal-image-blur", (float, int), 0, "others"),
        ("modal-image-brightness", str, "unset", "others"),
        ("modal-image-size", str, "cover", "others"),
        ("modal-image-position", str, "center", "others"),
        ("modal-dark-intensity", (float, int), 1, "others"),
    ]
    return schema


def get_mapping_config():
    P = get_prefix()

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
            "text-normal@@light": "text-normal-col@@light",
            "flexcyon-dataview-horizontal-padding":
            "flexcyon-dataview-error-horizontal-padding",
            "bases-no-img-str": "flexcyon-bases-no-img-str",
            "flexcyon-new-tab-bg-wrapper": "flexcyon-new-tab-bg-wrapper@@dark"
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

            is_selected = (val is True) or (val in self.cfg["select_groups"].get(
                target, {}).get("members", [])
                                            )
            if is_selected:
                g_pref = self.lookup.get(self._get_full_name(base))
                new_k = f"{g_pref}@@{self.prefix}-{target}"
                # If it's a string selection, the value IS the member name
                final_val = f"{self.prefix}-{val}" if isinstance(val, str) else f"{self.prefix}-{base}"
                return MapResult(MapResult.VALID, new_k, final_val)
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
