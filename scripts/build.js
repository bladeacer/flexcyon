const { execSync } = require('child_process');
const fs = require('node:fs');

execSync('npx sass --no-source-map --style=expanded scss/_flexcyon.scss .tmp-flexcyon.css', { cwd: process.cwd() });
execSync('npx sass --no-source-map --style=compressed scss/foundations.scss .tmp-foundations.css', { cwd: process.cwd() });
execSync('npx sass --no-source-map --style=expanded scss/_modifiers.scss .tmp-modifiers.css', { cwd: process.cwd() });

const flexcyonCss = fs.readFileSync('.tmp-flexcyon.css', 'utf8');
const foundationsCss = fs.readFileSync('.tmp-foundations.css', 'utf8');
const modifiersCss = fs.readFileSync('.tmp-modifiers.css', 'utf8');

const stripCharset = (css) => css.replace(/@charset "UTF-8";\n/g, '');
const stripBom = (css) => css.replace(/^\uFEFF/, '');
const fixCompressed = (css) => css.replace('*/body{', '*/\nbody{');

const flexcyonClean = stripCharset(stripBom(flexcyonCss));
const foundationsClean = stripCharset(stripBom(fixCompressed(foundationsCss)));
const modifiersClean = stripCharset(stripBom(modifiersCss));

const header = `/*!
Flexcyon: Made by mixing the Flexoki, Halcyon and Origami color scheme
License: MIT
Repository: https://github.com/bladeacer/flexcyon
Documentation (English): https://flexcyon.github.io/docs-en
Documentation (Chinese): https://flexcyon.github.io/docs-en/zh
*/

`;

fs.writeFileSync('theme.css', header + flexcyonClean + '\n' + foundationsClean + '\n' + modifiersClean);

fs.unlinkSync('.tmp-flexcyon.css');
fs.unlinkSync('.tmp-foundations.css');
fs.unlinkSync('.tmp-modifiers.css');