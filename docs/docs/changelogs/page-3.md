---
title: Version 0.3.x
icon: material/numeric-3-box-outline
---

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

### Version 0.3.4 Easter Egg Mode
- Made translation for hide until hover status bar configurable, useful for longer status bars
- Fixed file explorer background being broken
- Added markdown file tree option for folder style
- Added list style callout metadata utilities
- Added toggleable Easter egg mode

### Version 0.3.5 Configuration Update
- Documentation now has its own site.
- Added soft glow option for headings
- Added toggleable rainbow metadata icons
- Added accessibility options for global brightness, contrast and saturation ratios
- Added option to enable heading indicators globally, customisable for different heading levels.
  - Heading indicators now better inherit from the heading's base color
- Added option to configure popup callout animation duration
- Added option to configure metadata container left padding

### Version 0.3.6 Canvas Menu Update
- Fixed sidebar background issues
- Prevented heading indicators from showing up outside markdown editor instances
- Minor codebase refactor
- Slight change in accent color
- Added canvas card menu alignment options (plenty of options)