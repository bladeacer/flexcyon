/** @type {import('stylelint').Config} */
export default {
  extends: ["stylelint-config-standard-scss"],
  rules: {
    "selector-class-pattern": false,
    "selector-type-no-unknown": false,
    "shorthand-property-no-redundant-values": false,
    "color-function-alias-notation": false,
  },
};
