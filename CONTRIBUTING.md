# Contribution Guide

Welcome! We are excited that you wish to contribute to our project.
Before you start, please take a moment to read and understand our [Code of Conduct](./CODE_OF_CONDUCT.md).

By contributing, you **agree to abide by its terms.**

## Contribute

Code is not the only thing you can contribute. I truly appreciate contributions
in the form of:

- Fixing typos.
- Improving docs.
- Triaging issues.
- Reviewing pull requests.
- Sharing your opinion on issues.

## Issues

- Before opening a new issue, look for existing issues (even closed ones).
- Do not needlessly bump issues.
- If you are reporting a bug, include as much information as possible. Ideally,
  include a test case that reproduces the bug. For example, `x plugin's modals
look funky with the theme`. Even better, submit a pull request or a video
  demonstration to make reproducing the bug easier.

## Pull requests

Pull requests should follow the following conventions.

- Prefer official
[Obsidian CSS variables](https://docs.obsidian.md/Reference/CSS+variables/About+styling)
when it makes sense (sufficiently documented and stable)
- Follow the existing directory structure
- Clear variables names
- Pass the linter checks
- Only edit parts of the source code where necessary
- Test if the added features or fixes works as intended
- Check that your feature works with minAppVersion of Obsidian 1.6.3
  - last Electron update to v28.2.3 was in Obsidian 1.5.8
  - Electron v28.2.23 uses Chromium 120.0.6099.283
  - You can look up MDN whether specific CSS features are supported or not
  - If not, document and specify the minimum version for the feature to work
- [Do not attempt to add these](./README.md#what-this-theme-does-not-have)

### Prerequisite

- If the changes are large or breaking, open an issue discussing it first.
- Do not open a pull request if you don't plan to see it through. Maintainers
  waste a lot of time giving feedback on pull requests that eventually go stale.
- Do not do unrelated changes.
- Adhere to the existing code style.
- If relevant, add tests, check for typos, and add docs and types.
- Do not add editor-specific metafiles. Those should be added to your own global
  `.gitignore`.
- Do not be sloppy. I expect you to do your best.
- Double-check your contribution by going over the diff of your changes before
  submitting a pull request. It is a good way to catch bugs/typos and find ways to
  improve the code.

## Submission

- Give the pull request a clear title and description. It is up to you to
  convince the maintainers why your changes should be merged.
- If the pull request fixes an issue, reference it in the pull request
  description using the syntax `Fixes #123`.
- Make sure the “Allow edits from maintainers” checkbox is checked. That way I
  can make certain minor changes myself, allowing your pull request to be merged sooner.

## Review

- Push new commits when doing changes to the pull request. Do not squash as it
  makes it hard to see what changed since the last review.
- It is better to present solutions than just asking questions.
- Review the pull request diff after each new commit. It is better that you
  catch mistakes early than the maintainers pointing it out and having to go back
  and forth.
- Be patient. Maintainers often have a lot of pull requests to review. Feel free
  to bump the pull request if you haven't received a reply in a couple of weeks.
  (Hopefully not)
- And most importantly, have fun!
