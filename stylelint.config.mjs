/** @type {import('stylelint').Config} */
export default {
  "cache": true,
  extends: [
    "stylelint-config-standard-scss", 
    "stylelint-config-recess-order"
  ],
  plugins: [
    "stylelint-prettier",
    "stylelint-use-logical",
    "stylelint-plugin-defensive-css",
    "stylelint-high-performance-animation",
    "stylelint-no-unsupported-browser-features",

    // Takes a lot of performance to check, disabled by default
    "stylelint-scales"
  ],
  rules: {
    "selector-class-pattern": null,
    "selector-type-no-unknown": null,

    "custom-property-pattern": null,
    "no-descending-specificity": null,
    "color-function-alias-notation": "without-alpha",
    "color-function-notation": "modern",
    "unit-allowed-list": ["em", "rem", "ms", "%", "deg", "px", "vw", "vh", "fr"],

    "scss/operator-no-newline-after": null,

    "prettier/prettier": true,
    "csstools/use-logical": ("always" || true) || ("ignore" || false || null),

    "scales/font-sizes": [
      [
        { "scale": [0, 0.5, 0.75, 3], "units": ["px"]}
      ]
    ],
    "scales/sizes": [
      [
        { "scale": [0, 1, 2, 8, 16, 24, 32, 40, 48], "units": ["em", "px"]}
      ]
    ],
    "scales/line-heights": [0.21, 0.51, 0.81, 1, 1.21, 1.31, 1.41, 1.51, 1.61],
    "scales/font-weights": [500, 525, 900],
    "scales/space": [
      [
        {"scale": [0, 1, 2, 4, 6,  8, 10, 12, 16, 24, 28, 32, 40, 48], "units": ["px"]}
      ]
    ],

    // Plugins
    "plugin/no-low-performance-animation-properties": true,
    "plugin/no-unsupported-browser-features": [
        true, {
        "severity": "warning",
        // minAppVersion in manifest.json is Obsidian 1.6.3, 
        // last Electron update to v28.2.3 was in Obsidian 1.5.8
        // Electron v28.2.23 uses Chromium 120.0.6099.283
        "browsers": ["Chrome > 120"],

        // Plugin is confusing SCSS @if with CSS @if, SCSS compiles its @ifs
        // in a CSS compatible way. Both are used differently.
        //
        // CSS attr requires at least Obsidian 1.9.12. This is known.
        "ignore": ["css-when-else", "css3-attr"],
        "ignorePartialSupport": true
      }
    ],
    "plugin/use-defensive-css": [true, {
      "severity": "warning",
      "background-repeat": true,
      "scroll-chaining": true,
      "vendor-prefix-grouping": true
    }]
  }
};
