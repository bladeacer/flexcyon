---
icon: material/script-text
title: Changelogs
---

#### Note
The changelogs show versions in order of most recent to least recent. Or, if you prefer the changelogs in chronological order, you can use sidebar or hamburger menu to view the relevant sub-pages.

___
## Version 0.4.x
### Version 0.4.1 Quickfix Update
- Fix TUI rendering in light mode
- Fix left sidebar toggle when ribbon is not enabled
- Fix text highlight bg specifically with suggestion-highlight
- Fix embeds not displaying

### Version 0.4.0 Light Mode Update
- Changed sidebar background brightness setting default to `unset`. Was previously causing issues like blurring Calender plugin content.
- WIP light theme (mixes flexoki light + origami colour palette)
- Others misc changes
  - Added toggle for extended colour palette, on by default
  - Added table header size option 
  - Updated documentation to show a small preview of colors/opacity applied by the theme
  - Added web showcase of the theme's features
  - Remove Easter Egg mode
- Style color picker for light and dark mode options
- ASCII Art and quotes now inherit from the interface font
- Improved prompt styling and tree item padding
- Return to Zero (ultra minimalist mode) inspired by Shimmering Focus theme

## Version 0.3.x
### Version 0.3.6 Canvas Menu Update
- Fixed sidebar background issues
- Prevented heading indicators from showing up outside markdown editor instances
- Minor codebase refactor
- Slight change in accent color
- Added canvas card menu alignment options (plenty of options)

### Version 0.3.5 Configuration Update
- Documentation now has its own site.
- Added soft glow option for headings
- Added toggleable rainbow metadata icons
- Added accessibility options for global brightness, contrast and saturation ratios
- Added option to enable heading indicators globally, customisable for different heading levels.
  - Heading indicators now better inherit from the heading's base color
- Added option to configure popup callout animation duration
- Added option to configure metadata container left padding

### Version 0.3.4 Easter Egg Mode
- Made translation for hide until hover status bar configurable, useful for longer status bars
- Fixed file explorer background being broken
- Added markdown file tree option for folder style
- Added list style callout metadata utilities
- Added toggleable Easter egg mode

### Version 0.3.3 QOL Update
- Added configurable indentation factor and dimming of collapsed headers for Style Settings menu
- Added writing mode callout metadata utility, it increases text indent and paragraph spacing
  - It also has a CSS class provider which allows you to apply the same text indent and paragraph spacing increments to the target note
- Add rhombus editor background option
- You can now use grid, dotted or rhombus as background options for the left and right sidebar
  - These override the left and right sidebar background url options
- Quote now uses the same color as the ASCII art
  - Default quote is updated to not be a rickroll
- Added support for Kanban plugin
- Add before new tab empty state title now default to none:
  - If you are using quotes or ASCII art, do re-enable it
  - You can now configure the background color for the quotes or ASCII art
  - Changes may need an app reload/restart to take effect

### Version 0.3.2 Animations
- Styling Tweaks to community store item, existing layouts
- Animations are back, current options include:
  - Slide in Left to Right
  - Slide in Right to Left
  - Slide in Top to Bottom
  - Slide in Bottom to Top
  - Rotate in Bottom to Top
  - Rotate in Right to Left
- Added layout and status style for Powerlevel10k
- Added flashcard callout metadata utility
- Added option to add custom quote before empty state title
  - Is not selectable with ASCII art, ASCII art is selected by default
- Added option to angle grid editor background 
- Added background image option for modals (background image for settings, prompts etc)

### Version 0.3.1 Tidying Up
- Added callout metadata utilities for:
  - grid and dotted background
  - italic and oblique title and content
  - dashed, dotted, double, overline, underline and line-through for title and content
  - Apply Heading 1 to 6 styles for title
  - font weight for title and content
- Added headings font size option
- Fixed smiley icons (hopefully for the last time)
- Added options to add and configure image backgrounds in the left and right sidebars
- Slight modifications to navigation items on hover, Calendar plugin styling
- Slight tweaks to editor background dotted and grid background styling. 
- Tab title bar now adapts to the layout style selected
- Added option to blur inactive Canvas nodes for core Canvas plugin
- Editor background changes now affect the core Canvas plugin.
  - May need app reload/restart for Style Settings changes to show up in the Canvas
- Tweaked styling of canvas controls and card menu
- Changed breadcrumbs styling to use ASCII instead of emoji

### Version 0.3.0 TUI Layout
- Added TUI inspired add-on to cards layout
  - Enabled by default
- Changes to table styling
- Added cssclasses for heading indicators, callout metadata for tilting callout title and content
- Added support for Calendar plugin
- Tweaked exisitng styling for Full Calendar plugin
- Tweaked community item styling
- Fixed smiley icons alignment issue
- Angled layout applies to more UI elements now
- Active line gutter should now be more visible
- Added prompt alignment options, configure using style settings:
  - Top left
  - Top center
  - Center left
  - Bottom left
  - Bottom center
- See the [documentation](https://github.com/bladeacer/flexcyon/tree/master/docs/docs.md) for more details 

___
## Version 0.2.x
### Version 0.2.2 Layout styling
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

### Version 0.2.1 Small Update
- Removed Window animations as they are not performant.
- Updated Extended colors so that `*-color1-color2` and `*-color-2-color` will always return the same color mix when using in callout metadata utilities.
- Made active file background effect more consistent
- Added ASCII Art Line Height option
- Added cssclasses for dotted and grid editor background options
- Added styling options for inline title

### Version 0.2.0 Aesthetics Update
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

___
## Version 0.1.x
### Version 0.1.1 Hotfixes
- Added option to change ASCII checkboxes font size
- Fixed smiley icons on mobile
- Added title and background color callout metadata utilities
- Added options to toggle visibility of properties in reading mode and live preview
- Added support for Dataview plugin
- Added rainbow bullet points (disabled by default)
- More UI elements are dimmed for consistency
- Media embeds now have vertical margin which can be set

### Version 0.1.0: Utilities Update
- Added support for Spaced Repetition Plugin
- Added support for Breadcrumbs Plugin
- Added underline option for headings
- Added alternate active item effects in settings
- Added customisation options for prompts
- Added alternate file explorer style
- Added options to change link color
- Added ASCII checkboxes
- Added callout utilities for
  - No Icon
  - No Title
  - Transparent Background
  - Capitalize, uppercase, lowercase Title and Content
  - RTL, LTR, Center Title and Content
  - Tategaki (Vertical RTL)
  - Vertical LTR
- Added cssclasses for
  - Tategaki (Vertical RTL)
  - Vertical LTR
- See the [documentation](https://github.com/bladeacer/flexcyon/tree/master/docs/docs.md) for more details 

Credits: 

- `@OWA/bennyyip` on the Obisidian Members' Group Discord for the tategaki snippet

- `@Tuck` on the Obsidian Members' Group Discord for options to change link color

### Version 0.0.5: Minor Changes
- Made ASCII art responsive, you can set a font size limit on it
- Status bar does not overlap with command mode input text
- Added option to enabled status bar on mobile
- Added line height option in typography for headings
- Add option to hide the left sidedock ribbon
- Add option to align top actions globally