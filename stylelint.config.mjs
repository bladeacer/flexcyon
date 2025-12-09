/** @type {import('stylelint').Config} */
export default {
  extends: ["stylelint-config-standard-scss"],
  plugins: [
    "stylelint-prettier",
    "stylelint-no-unsupported-browser-features"
  ],
  rules: {
    "prettier/prettier": true,
    "selector-class-pattern": null,
    "selector-type-no-unknown": null,
    "custom-property-pattern": null,
    "no-descending-specificity": null,
    "number-max-precision": null,
    "color-function-alias-notation": null,
    "color-function-notation": "legacy",
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
