/** @type {import('stylelint').Config} */
export default {
  extends: ["stylelint-config-standard-scss"],
  plugins: [
    "stylelint-prettier",
    "stylelint-no-unsupported-browser-features",
    "stylelint-use-logical",
    "stylelint-high-performance-animation"
  ],
  rules: {
    "prettier/prettier": true,
    "csstools/use-logical": ("always" || true) || ("ignore" || false || null),
    "selector-class-pattern": null,
    "selector-type-no-unknown": null,
    "custom-property-pattern": null,
    "no-descending-specificity": null,
    "plugin/no-low-performance-animation-properties": true,
    "color-function-alias-notation": "without-alpha",
    "color-function-notation": "modern",
    // List of allowed units
    "unit-allowed-list": ["em", "rem", "ms", "%", "deg", "px", "vw", "vh"],
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
  }
};
