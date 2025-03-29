## Changelog
### Version 0.3.2 

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
- @OWA/bennyyip on the Obisidian Members' Group Discord for the tategaki snippet
- @Tuck on the Obsidian Members' Group Discord for options to change link color

### Version 0.0.5: Minor Changes
- Made ASCII art responsive, you can set a font size limit on it
- Status bar does not overlap with command mode input text
- Added option to enabled status bar on mobile
- Added line height option in typography for headings
- Add option to hide the left sidedock ribbon
- Add option to align top actions globally