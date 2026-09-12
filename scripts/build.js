const sass = require('sass');
const fs = require('node:fs');

const styles = {
  flexcyon: { file: '_flexcyon.scss', style: 'expanded' },
  foundations: { file: 'foundations.scss', style: 'compressed' },
  new_tab: { file: 'new_tab.scss', style: 'compressed' },
  style_settings: { file: 'style_settings.scss', style: 'compressed' },
  others: { file: 'others.scss', style: 'compressed' },
  modifiers: { file: '_modifiers.scss', style: 'expanded' },
  plugins: { file: 'plugins.scss', style: 'compressed' },
  snippets: { file: 'snippets.scss', style: 'compressed' },
};

function build() {
  const tempFiles = {};
  for (const [name, { file, style }] of Object.entries(styles)) {
    const tempFile = `.tmp-${name}.css`;
    const srcFile = `scss/${file}`;
    const result = sass.compile(srcFile, {
      style,
      sourceMap: false,
      loadPaths: ['scss'],
    });
    fs.writeFileSync(tempFile, result.css);
    tempFiles[name] = tempFile;
  }

  const parts = [];
  for (const [name, tempFile] of Object.entries(tempFiles)) {
    const css = fs.readFileSync(tempFile, 'utf8');
    // Push any rule that got glued to the tail of a loud comment (`*/body{...}`)
    // onto its own line, without eating the `/` that opens a following comment.
    // Sass compressed output concatenates adjacent loud comments as `*//*!...`,
    // so the naive `*/X` -> `*/\nX` rewrite corrupted every `@settings` block
    // that followed another comment.
    const clean = css
      .replace(/@charset "UTF-8";\n/g, '')
      .replace(/^\uFEFF/, '')
      .replace(/\*\/(?![\/*\n])/g, '*/\n');
    parts.push(clean);
    fs.unlinkSync(tempFile);
  }

  const header = `/*!
Flexcyon: Made by mixing the Flexoki, Halcyon and Origami color scheme
License: MIT
Repository: https://github.com/bladeacer/flexcyon
Documentation (English): https://flexcyon.github.io/docs-en
Documentation (Chinese): https://flexcyon.github.io/docs-en/zh
*/

`;

  fs.writeFileSync('theme.css', header + parts.join('\n') + '\n');
}

if (process.argv.includes('--watch')) {
  const onchange = require('onchange');
  onchange('scss/**/*.scss', { persistent: true }, () => build());
} else {
  build();
}
