// Build guard for theme.css — run after scripts/build.js (see "verify" in package.json).
//
// Fails (exit 1) when:
//   1. A module declared as style: "compressed" still emits unminified CSS.
//      dart-sass silently preserves loud /*! comments and their contents,
//      which keeps every rule around them multi-line.
//   2. theme.css does not parse. Catches comment corruption such as the
//      historical `*/[^\n]` rewrite bug that mangled the `*//*!` comment joins
//      and left orphaned "*!" text mid-file.
//   3. A Style Settings @settings block is missing or malformed. Obsidian
//      silently drops all theme defaults and class toggles when they break,
//      which is what killed heading colours and theme cssclasses before.
//
// Usage: node scripts/verify-theme.js

const fs = require('node:fs');
const path = require('node:path');
const sass = require('sass');

// Keep in sync with scripts/build.js
const { styles } = require('./build.js');

let failed = false;
const fail = (...args) => {
  console.error('FAIL:', ...args);
  failed = true;
};
const ok = (...args) => console.log('ok:', ...args);

// ---------------------------------------------------------------------------
// 1. Per-module minification: compressed modules must have no newlines
//    outside loud comments (a preserved /*! comment keeps surrounding rules
//    multi-line, e.g. the earlier gutters/workspace/callouts output).
//    The only loud comments allowed in compressed output are Style Settings
//    @settings metadata blocks; any other comment silently bloats theme.css.
// ---------------------------------------------------------------------------
for (const [name, { file, style }] of Object.entries(styles)) {
  const result = sass.compile(path.join('scss', file), {
    style,
    sourceMap: false,
    loadPaths: ['scss'],
  });
  const css = result.css
    .replace(/@charset "UTF-8";\n/g, '')
    .replace(/^\uFEFF/, '');

  let inComment = false;
  let newlinesOutsideComments = 0;
  for (let i = 0; i < css.length; i++) {
    if (!inComment && css.startsWith('/*', i)) {
      inComment = true;
      i++;
      continue;
    }
    if (inComment && css.startsWith('*/', i)) {
      inComment = false;
      i++;
      continue;
    }
    if (!inComment && css[i] === '\n') newlinesOutsideComments++;
  }

  if (style !== 'expanded' && newlinesOutsideComments > 0) {
    fail(
      `module "${name}" (${file}) is declared style: "compressed" but its output ` +
        `has ${newlinesOutsideComments} newline(s) outside comments — a loud /*! ` +
        `comment is keeping surrounding rules unminified.`,
    );
    continue;
  }

  if (style !== 'expanded') {
    const loudComments = [...css.matchAll(/\/\*[\s\S]*?\*\//g)].map((m) => m[0]);
    // Only Style Settings metadata and obsi-snip-coll snippet markers are
    // meant to survive compression; any other loud comment is a mistake that
    // silently bloats theme.css.
    const unexpected = loudComments.filter(
      (c) => !c.includes('@settings') && !c.includes('obsi-snip-coll'),
    );
    if (unexpected.length > 0) {
      fail(
        `module "${name}" (${file}) is declared style: "compressed" but keeps ` +
          `${unexpected.length} loud comment(s) that are neither @settings metadata ` +
          `nor snippet markers (first: ${JSON.stringify(unexpected[0].slice(0, 60))}). ` +
          `Use a silent comment (// or /* */) so it gets stripped.`,
      );
      continue;
    }
    ok(`module "${name}" is fully minified`);
  }
}

// ---------------------------------------------------------------------------
// 2. Assembled theme.css must parse (postcss), with intact comments.
// ---------------------------------------------------------------------------
const css = fs.readFileSync('theme.css', 'utf8');

if (!css.startsWith('/*!\nFlexcyon: Made by mixing')) {
  fail('theme.css is missing the Flexcyon header comment');
}

// 2a. Balanced comment tokens across the whole file.
{
  let inComment = false;
  for (let i = 0; i < css.length; i++) {
    if (!inComment && css.startsWith('/*', i)) {
      inComment = true;
      i++;
      continue;
    }
    if (inComment && css.startsWith('*/', i)) {
      inComment = false;
      i++;
      continue;
    }
  }
  if (inComment) fail('theme.css has an unterminated comment');
}

// 2b. Orphaned comment fragments outside any comment (e.g. a line that is
//     exactly "*!" or starts with "*!" after a join) indicate corrupted joins.
{
  const orphanLine = css
    .split('\n')
    .findIndex((line) => /^\*![^/]/.test(line));
  if (orphanLine !== -1) {
    fail(
      `theme.css has an orphaned comment fragment at line ${orphanLine + 1} ` +
        `(a "*/" -> next-comment join got corrupted)`,
    );
  }
}

// 4. obsi-snip-coll snippet markers: the snippet extractor scans the built
//    theme.css for `/* obsi-snip-coll start: name */ ... end */`, so every
//    marker in the scss sources must survive the build in canonical form
//    (loud in sources, stripped of "!" in the output).
{
  const sourceStarts = new Set();
  for (const dir of ['scss/flexcyon', 'scss/modifiers']) {
    const walk = (d) => {
      for (const entry of fs.readdirSync(d, { withFileTypes: true })) {
        const p = path.join(d, entry.name);
        if (entry.isDirectory()) walk(p);
        else if (entry.name.endsWith('.scss')) {
          for (const m of fs.readFileSync(p, 'utf8').matchAll(/obsi-snip-coll\s+start:\s*([\w-]+)/g)) {
            sourceStarts.add(m[1]);
          }
        }
      }
    };
    walk(dir);
  }

  const builtStarts = [...css.matchAll(/\/\*\s*obsi-snip-coll\s+start:\s*([\w-]+)/g)].map((m) => m[1]);
  const builtEnds = [...css.matchAll(/\/\*\s*obsi-snip-coll\s+end\s*\*\//g)].length;

  const missing = [...sourceStarts].filter((s) => !builtStarts.includes(s));
  if (missing.length) {
    fail(
      `${missing.length} obsi-snip-coll snippet marker(s) from the scss sources did not ` +
        `survive the build: ${missing.join(', ')}`,
    );
  } else {
    ok(`${builtStarts.length} snippet marker(s) present, all ${sourceStarts.size} source snippet(s) accounted for`);
  }

  if (builtStarts.length !== builtEnds) {
    fail(`unbalanced obsi-snip-coll markers: ${builtStarts.length} start(s) vs ${builtEnds} end(s)`);
  }

  const loudInOutput = [...css.matchAll(/\/\*!\s*obsi-snip-coll/g)].length;
  if (loudInOutput > 0) {
    fail(`${loudInOutput} snippet marker(s) kept their "/*!" form in theme.css — the extractor expects "/*"`);
  }
}

// 3. Style Settings @settings blocks.
const settingsBlocks = [...css.matchAll(/\/\*!\s*\n?@settings\n([\s\S]*?)\*\//g)];
if (settingsBlocks.length === 0) {
  fail('theme.css contains no @settings blocks (Style Settings metadata lost)');
} else {
  const names = settingsBlocks
    .map(([, body]) => (body.match(/^name: (\S+)/m) || [])[1])
    .filter(Boolean);
  if (names.length !== settingsBlocks.length) {
    fail('at least one @settings block is missing its "name:" field');
  } else {
    ok(`${settingsBlocks.length} @settings block(s) intact: ${names.join(', ')}`);
  }
}

try {
  const postcss = require('postcss');
  postcss.parse(css, { from: 'theme.css' });
  ok('theme.css parses cleanly');
} catch (err) {
  fail('theme.css failed to parse:', err.message.slice(0, 200));
}

if (failed) {
  console.error('\ntheme.css verification FAILED');
  process.exit(1);
}
console.log('\ntheme.css verification passed');
