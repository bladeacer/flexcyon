import { execSync } from 'node:child_process';

const pm = (process.env.npm_config_user_agent || 'npm').split('/')[0];
const args = process.argv.slice(2);
const cachePath = `.cache/stylelint/${pm}/.stylelintcache`;

const command = `stylelint 'scss/**/*.scss' --cache-location ${cachePath} ${args.join(' ')}`;

process.on('SIGINT', () => {
  console.log('\nExiting linting...');
  process.exit(0);
});

try {
  execSync(command, { stdio: 'inherit' });
} catch (err) {
  if (err.signal === 'SIGINT' || err.status === 130) {
    process.exit(0);
  }
  process.exit(err.status || 1);
}
