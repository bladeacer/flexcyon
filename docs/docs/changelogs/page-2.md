---
title: Version 0.2.x
icon: material/numeric-2-box-outline
---

## Version 0.2.0 Aesthetics Update
- Added callout vertical margin, border radius option
- Added image border radius option
- Added extended color palette (can be used as callout metadata utilities or in css variables)
- Added popup callout, adapted from [Ukiyo](https://github.com/technerium/obsidian-ukiyo) Theme by vaykinov and wizentex
- Fixed opacity of top actions like new note, new folder etc
- Added window animations for modals, prompts and settings. Choose from the following options:
  - None (Reverts to default behavior)
  - Slide Down to Up
  - Slide Up to Down
  - Slide Left to Right
  - Slide Right to Left
- You can also configure the animation duration
- Added option to toggle displaying of properties in reading mode and edit mode
  - Do not show properties in reading mode is enabled by default
  - Do not show properties in editing mode is disabled by default
- Added option to enable minimalist (folder/outline) trees
- Added rainbow folders for file explorer
- Added dotted and grid background options
- See the [documentation](https://github.com/bladeacer/flexcyon/tree/master/docs/docs.md) for more details 

## Version 0.2.1 Small Update
- Removed Window animations as they are not performant.
- Updated Extended colors so that `*-color1-color2` and `*-color-2-color` will always return the same color mix when using in callout metadata utilities.
- Made active file background effect more consistent
- Added ASCII Art Line Height option
- Added cssclasses for dotted and grid editor background options
- Added styling options for inline title

## Version 0.2.2 Layout styling
- Fixed double quotes checkbox background color
- Added support for Vault Statistics plugin
- Minor styling tweaks for community item effects
- Added card, angled options for workspace layout 
  - Need app reload or restart if you wish to change layouts
- Vim mode status text and status bar mode (reading/live preview etc) text now has a color option:
  - Toggled off by default
- Add card, angled (inspired by Powerlevel10k) styles for status bar
  - Affects vim mode status text as well
- Added status bar font size option