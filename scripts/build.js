const sass = require('sass');
const fs = require('node:fs');

// Every module is compiled separately and concatenated into theme.css in the
// order its @use appears in scss/theme.scss — which also documents, per line,
// how each module is compiled. Keep the two files in sync.
//
// Every module is compiled minified. Loud /*! comments (e.g. the Style
// Settings @settings metadata in the style_settings module) survive
// compression on purpose; regular silent comments do not. Run
// `node scripts/verify-theme.js` after building to enforce both.
//
// Exceptions that must stay expanded (whitespace-sensitive output):
//   - style_settings: the @settings metadata files (and their ASCII-art
//     default) must survive compression; only _style_settings_styles.scss
//     (the CSS styling the Style Settings UI) is minified.
//   - ascii_art: compressed output collapses the ASCII art's `\a\` line
//     continuations into `\ `, destroying every line's leading spaces.
const styles = {
  flexcyon: { file: '_flexcyon.scss', style: 'compressed' },
  foundations: { file: 'foundations.scss', style: 'compressed' },
  ascii_art: {
    file: 'flexcyon/new_tab/new-tab-modules/_ascii-art.scss',
    style: 'expanded',
  },
  new_tab: {
    file: 'flexcyon/new_tab/_new_tab.scss',
    style: 'compressed',
  },
  style_settings_styles: {
    file: 'flexcyon/style_settings/_style_settings_styles.scss',
    style: 'compressed',
  },
  style_settings: { file: 'style_settings.scss', style: 'expanded' },
  others: { file: 'flexcyon/others/_others.scss', style: 'compressed' },
  plugins: { file: 'plugins.scss', style: 'compressed' },
  snippets: { file: 'snippets.scss', style: 'compressed' },
};

function build() {
  // Compile every module in memory and assemble theme.css in a single write.
  // No temp files: concurrent builds (rapid watch events, overlapping `pnpm dev`
  // invocations) used to race on shared `.tmp-*.css` files — one build could
  // unlink a temp file another build was about to read (ENOENT).
  const header = `/*!
Flexcyon: Made by mixing the Flexoki, Halcyon and Origami color scheme
License: MIT
Repository: https://github.com/bladeacer/flexcyon
Documentation (English): https://flexcyon.github.io/docs-en
Documentation (Chinese): https://flexcyon.github.io/docs-en/zh
*/

`;

  const parts = [];
  for (const [name, { file, style }] of Object.entries(styles)) {
    const result = sass.compile(`scss/${file}`, {
      style,
      sourceMap: false,
      loadPaths: ['scss'],
    });
    // Push any rule that got glued to the tail of a loud comment (`*/body{...}`)
    // onto its own line, without eating the `/` that opens a following comment.
    // Sass compressed output concatenates adjacent loud comments as `*//*!...`,
    // so the naive `*/X` -> `*/\nX` rewrite corrupted every `@settings` block
    // that followed another comment.
    //
    // The obsi-snip-coll snippet markers are kept loud in the scss sources so
    // they survive compression, then stripped of `!` here — the snippet
    // extractor expects the canonical `/* obsi-snip-coll ... */` form.
    parts.push(
      result.css
        .replace(/@charset "UTF-8";\n/g, '')
        .replace(/^\uFEFF/, '')
        .replace(/\/\*! (obsi-snip-coll )/g, '/* $1')
        .replace(/\*\/(?![\/*\n])/g, '*/\n'),
    );
  }

  fs.writeFileSync('theme.css', header + parts.join('\n') + '\n');
}

if (require.main === module) {
  if (process.argv.includes('--watch')) {
    // onchange v7 API: onchange({ matches, command, ... }) — the module
    // exports the function as a named property, not as module.exports.
    const { onchange } = require('onchange');
    onchange({
      matches: 'scss/**/*.scss',
      command: ['node', 'scripts/build.js'],
      // Build theme.css once on startup so a fresh `pnpm dev` is never stale.
      initial: true,
    });
  } else {
    build();
  }
}

module.exports = { styles };
