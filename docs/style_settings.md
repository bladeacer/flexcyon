# Documentation for Flexcyon Style Settings
[Back to documentation welcome page](https://github.com/bladeacer/flexcyon/tree/master/docs/docs.md)

## Map of Contents
- [Documentation for Flexcyon Style Settings](#documentation-for-flexcyon-style-settings)
- [Table Of Contents](#table-of-contents)
- [Markdown Navigation tree for Flexcyon's Style Settings](#markdown-navigation-tree-for-flexcyons-style-settings)
- [Editor Section](#editor-section)
    - [Accent Colors](#accent-colors)
    - [Base Colors](#base-colors)
    - [Typography](#typography)
    - [Table](#table)
    - [Files](#files)
    - [Workspace](#workspace)
    - [Callouts](#callouts)
    - [Checkboxes](#checkboxes)
    - [Bullet lists](#bullet-lists)
    - [Media](#media)
    - [Links](#links)
    - [Properties](#properties)
    - [Status Bar](#status-bar)
    - [Title Bar](#title-bar)
- [Settings Section](#settings-section)
    - [Style Settings](#style-settings)
- [Plugins Section](#plugins-section)
    - [Alternate file tree](#alternate-file-tree)
    - [Full Calendar](#full-calendar)
    - [Dataview](#dataview)
    - [Canvas](#canvas)
- [Others Sections](#others-section)
    - [Vim Mode Text](#vim-mode-text)
    - [New Tab Apperance](#new-tab-appearance)
    - [Side Dock Icons](#side-dock-icons)
    - [Tooltip radius](#tooltip-radius)
    - [Background images](#background-images)

## Markdown Navigation tree for Flexcyon's Style Settings
```md
Style Settings
|--...
|-- Flexcyon Style Settings
|   |-- **Editor**
|   |   |-- Accent Colors
|   |   |   |-- Cyan Color
|   |   |   |-- Green Color
|   |   |   |-- Orange Color
|   |   |   |-- Yellow Color
|   |   |   |-- Purple Color
|   |   |   |-- Red Color
|   |   |   |-- Blue Color
|   |   |   |-- Pink Color
|   |   |   |-- Accent Color
|   |   |-- Base Colors
|   |   |   |--  Base Color 01
|   |   |   |--  Base Color 02
|   |   |   |--  Base Color 03
|   |   |   |--  Base Color 04
|   |   |   |--  Base Color 05
|   |   |   |--  Base dark grey
|   |   |   |--  Base light grey
|   |   |   |--  Base grey tab
|   |   |   |--  Base grey token
|   |   |   |--  Base grey scroll
|   |   |   |--  Base grey scroll hover
|   |   |-- Typography
|   |   |   |--  Muted text color
|   |   |   |--  Headings
|   |   |   |   |--  Enable coloured headings
|   |   |   |   |--  Heading 1 font size
|   |   |   |   |--  Heading 2 font size
|   |   |   |   |--  Heading 3 font size
|   |   |   |   |--  Heading 4 font size
|   |   |   |   |--  Heading 5 font size
|   |   |   |   |--  Heading 6 font size
|   |   |   |   |--  Heading 1 font weight
|   |   |   |   |--  Heading 2 font weight
|   |   |   |   |--  Heading 3 font weight
|   |   |   |   |--  Heading 4 font weight
|   |   |   |   |--  Heading 5 font weight
|   |   |   |   |--  Heading 6 font weight
|   |   |   |   |--  Heading 1 line height
|   |   |   |   |--  Heading 2 line height
|   |   |   |   |--  Heading 3 line height
|   |   |   |   |--  Heading 4 line height
|   |   |   |   |--  Heading 5 line height
|   |   |   |   |--  Heading 6 line height
|   |   |   |   |--  Enable underline for Heading 1
|   |   |   |   |--  Enable underline for Heading 2
|   |   |   |   |--  Enable underline for Heading 3
|   |   |   |   |--  Enable underline for Heading 4
|   |   |   |   |--  Enable underline for Heading 5
|   |   |   |   |--  Enable underline for Heading 6
|   |   |   |--  UI Font sizes
|   |   |   |   |--  Smaller UI Font size
|   |   |   |   |--  Small UI Font size
|   |   |   |   |--  Medium UI Font size
|   |   |   |   |--  Large UI Font size
|   |   |-- Table
|   |   |   |-- Table border color
|   |   |   |-- Width of table in reading mode
|   |   |-- Files
|   |   |   |--  Enable dimmed file extensions in file explorer
|   |   |   |--  Select folder style
|   |   |   |--  Enable minimalist tree
|   |   |-- Workspace
|   |   |   |--  File line width
|   |   |   |--  Opacity of dimmed UI elements
|   |   |   |--  Top Actions Alignment
|   |   |   |--  Upscale percentage of icons
|   |   |   |   |--  Upscale percentage of icons 1
|   |   |   |   |--  Upscale percentage of icons 2
|   |   |   |--  Prompts
|   |   |   |   |--  Prompt width
|   |   |   |   |--  Prompt max width
|   |   |   |   |--  Prompt max height
|   |   |   |   |--  Prompt alignment
|   |   |   |--  Animations
|   |   |   |   |--  Animation type
|   |   |   |   |--  Animation duration
|   |   |   |   |--  Animation easing function
|   |   |   |   |--  Animation slide amount
|   |   |   |--  Editor Background
|   |   |   |   |--  Select background type
|   |   |   |   |--  Rotation value for grid and rhombus background
|   |   |   |   |--  Width between each dot/line for editor background
|   |   |   |   |--  Size of dots for dotted background
|   |   |   |--  Layout
|   |   |   |   |--  Select workspace layout
|   |   |   |   |--  Enable TUI add-on for cards layout
|   |   |-- Callouts
|   |   |   |-- Callout Icon Right padding
|   |   |   |-- First Codeblock Margin Top
|   |   |   |-- Callout Metadata Background Opacity
|   |   |   |-- Callout Vertical Margin
|   |   |   |-- Callout Border Radius
|   |   |   |-- Flashcard Callout width
|   |   |   |-- Flashcard Callout height
|   |   |-- Checkboxes
|   |   |   |-- Enable ASCII checkboxes
|   |   |   |-- Enable ASCII checkboxes
|   |   |-- Bullet Lists
|   |   |   |-- Enable rainbow bullet list
|   |   |-- Media
|   |   |   |-- Media embed vertical margin
|   |   |   |-- Image border radius
|   |   |-- Links
|   |   |   |-- Internal link color
|   |   |   |-- External link color
|   |   |   |-- Unresolved link color
|   |   |-- Properties
|   |   |   |-- Do not show properties in reading mode
|   |   |   |-- Do not show properties in live preview mode
|   |   |-- Status Bar
|   |   |   |-- Hide until hover
|   |   |   |-- Text to show when hide until hover is enabled
|   |   |   |-- Transition duration for showing status bar on hover
|   |   |   |-- Transition timing function for showing status bar on hover
|   |   |   |-- Use text instead of icons for mode status
|   |   |   |-- Reading Mode Text
|   |   |   |-- Source Mode Text
|   |   |   |-- Live Preview Mode Text
|   |   |   |-- Display status bar on mobile
|   |   |   |-- Status bar font size
|   |   |   |-- Select status bar style
|   |   |   |-- Enable status bar color
|   |   |-- Title Bar
|   |   |   |-- Titlebar Button Effects
|   |-- **Settings**
|   |   |-- Smiley Toggle Icons in Settings
|   |   |-- Coloured Icons in Settings
|   |   |-- Enable community item effects
|   |   |-- Opacity of community items (unselected)
|   |   |-- Installed tooltip left margin
|   |   |-- Do not show scrollbar in settings
|   |   |-- Enable alternate active item effect in settings
|   |   |-- Style Settings
|   |   |   |-- Indentation width betwen style setting headings
|   |   |   |-- Dim collapsed style settings headings
|   |-- **Plugins**
|   |   |-- Alternate file tree
|   |   |   |-- Folders font size
|   |   |   |-- Folders font color
|   |   |   |-- Active folder color
|   |   |   |-- Files font size
|   |   |   |-- Files font color
|   |   |   |-- Disable folder icons
|   |   |   |-- Disable file tree header
|   |   |   |-- Enable Alternate folder count
|   |   |   |-- Enabled dimmed file extensions in file tree
|   |   |-- Full Calendar
|   |   |   |-- Opacity of dimmed full calendar items
|   |   |-- Dataview
|   |   |   |-- Horizontal padding of dataview error messages
|   |   |-- Canvas
|   |   |   |-- Blur inactive canvas nodes
|   |   |   |-- Blur intensity for inactive canvas nodes
|   |-- **Others**
|   |   |-- Vim Mode Text
|   |   |   |-- Enable Vim Mode Text
|   |   |   |-- Vim mode text left positioning
|   |   |   |-- Vim mode text bottom positioning
|   |   |   |-- Insert Mode Text
|   |   |   |-- Normal Mode Text
|   |   |   |-- Command Mode Text
|   |   |-- New Tab Apperance
|   |   |   |-- Add before Empty State title
|   |   |   |-- Background color for add before empty state title
|   |   |   |-- Quote
|   |   |   |-- Quote max font size
|   |   |   |-- ASCII Art
|   |   |   |-- Disable Empty State title
|   |   |   |-- Disable Empty State actions
|   |   |   |-- ASCII art font size limit
|   |   |-- Side Dock Icons
|   |   |   |-- Enable side dock icon effects
|   |   |   |-- Hide the side dock ribbon
|   |   |-- Tooltip radius
|   |   |   |-- Small radius
|   |   |   |-- Medium radius
|   |   |   |-- Large radius
|   |   |   |-- Extra large radius
|   |   |-- Sidebar Background
|   |   |   |-- Select background in sidebar
|   |   |   |-- Left sidebar background image url
|   |   |   |-- Right sidebar background image url
|   |   |   |-- Sidebar Background image blend mode
|   |   |   |-- Sidebar Background image repeat
|   |   |   |-- Sidebar Background image blur
|   |   |   |-- Sidebar Backgroud image brightness
|   |   |   |-- Sidebar Backgroud image size
|   |   |   |-- Sidebar Backgroud image position
|   |   |-- Modal Background
|   |   |   |-- Modal Background image url
|   |   |   |-- Modal Background image blend mode
|   |   |   |-- Modal Background image repeat
|   |   |   |-- Modal Background image blur
|   |   |   |-- Modal Background image brightness
|   |   |   |-- Modal Backgroud image size
|   |   |   |-- Modal Backgroud image position
|-- ...
```

# Editor Section
## Accent Colors
Defined colors overrides theme defaults for heading colors and other UI elements.
Also includes overriding the accent colors.
> Don't worry, these colors overrides the standard css variables like var(--color-cyan)

Accepted Formats: RGB, HEX

### Cyan Color
CSS Variable(s) targeted: `var(--flexcyon-cyan)`, `var(--color-cyan-rgb)`

Default: #3cb9c2

### Green Color
CSS Variable(s) targeted: `var(--flexcyon-lime-green)`, `var(--color-green-rgb)`

Default: #a1c05c

### Orange Color
CSS Variable(s) targeted: `var(--flexcyon-orange)`, `var(--color-orange-rgb)`

Default: #cc8449

### Yellow Color
CSS Variable(s) targeted: `var(--flexcyon-yellow)`, `var(--color-yellow-rgb)`

Default: #c29e42

### Purple Color
CSS Variable(s) targeted: `var(--flexcyon-purple-lilac)`, `var(--color-purple-rgb)`

Default: #a461c8

### Red Color
CSS Variable(s) targeted: `var(--flexcyon-red-salmon)`, `var(--color-red-rgb)`

Default: #c03a47

### Blue Color
CSS Variable(s) targeted: `var(--flexcyon-blue)`, `var(--color-blue-rgb)`

Default: #5a8fcd

### Pink Color
CSS Variable(s) targeted: `var(--flexcyon-pink)`, `var(--color-pink-rgb)`

Default: #d458a3

### Accent Color
CSS Variable(s) targeted: `var(--flexcyon-accent)`

Default: #92a871

### Enabled Extended Colors
CSS Variable(s) targeted: `var(--flexcyon-ext-colors-enabled)`

Default: false

___
## Base Colors
Defined colors overrides theme defaults for base colors used in the background and other UI elements.

Accepted Formats: HEX
### Base Color 01
CSS Variable(s) targeted: `var(--flexcyon-base-blue-01)`

Default: #14161c

### Base Color 02
CSS Variable(s) targeted: `var(--flexcyon-base-blue-02)`

Default: #191d28

### Base Color 03
CSS Variable(s) targeted: `var(--flexcyon-base-blue-03)`

Default: #24262c

### Base Color 04
CSS Variable(s) targeted: `var(--flexcyon-base-blue-04)`

Default: #4d566b

### Base Color 05
CSS Variable(s) targeted: `var(--flexcyon-base-blue-05)`

Default: #6f7685

### Base dark grey
CSS Variable(s) targeted: `var(--flexcyon-base-grey-dark)`

Default: #898c93

### Base light grey
CSS Variable(s) targeted: `var(--flexcyon-base-grey-light)`

Default: #d3d5d3

### Base grey tab
CSS Variable(s) targeted: `var(--flexcyon-base-grey-token)`

Default: #586582

### Base grey scroll 
CSS Variable(s) targeted: `var(--flexcyon-base-grey-scroll)`

Default: #3f495e

### Base grey scroll hover
CSS Variable(s) targeted: `var(--flexcyon-base-grey-scroll-hover)`

Default: #5d6782

___

## Typography
Defined colors for muted text color, styling for headings, and controlling UI font sizes.

Accepted Formats: HEX, number, px

### Muted text color
CSS Variable(s) targeted: `var(--flexcyon-text-muted)`

Default: #6f768599

___

### Headings
Defines CSS variables for styling related to headings like font weight.

#### Enable coloured headings
CSS Variable(s) targeted: `var(--flexcyon-headings-coloured-enabled)`

Default: true (class toggle)

#### Heading 1 font weight
CSS Variable(s) targeted: `var(--h1-weight)`

Default: 700

#### Heading 2 font weight
CSS Variable(s) targeted: `var(--h2-weight)`

Default: 675

#### Heading 3 font weight
CSS Variable(s) targeted: `var(--h3-weight)`

Default: 650

#### Heading 4 font weight
CSS Variable(s) targeted: `var(--h4-weight)`

Default: 625

#### Heading 5 font weight
CSS Variable(s) targeted: `var(--h5-weight)`

Default: 600

#### Heading 6 font weight
CSS Variable(s) targeted: `var(--h6-weight)`

Default: 575

#### Heading 1 line height
CSS Variable(s) targeted: `var(--h1-line-height)`

Default: 1.2

#### Heading 2 line height
CSS Variable(s) targeted: `var(--h2-line-height)`

Default: 1.2

#### Heading 3 line height
CSS Variable(s) targeted: `var(--h3-line-height)`

Default: 1.3

#### Heading 4 line height
CSS Variable(s) targeted: `var(--h4-line-height)`

Default: 1.4

#### Heading 5 line height
CSS Variable(s) targeted: `var(--h5-line-height)`

Default: 1.5

#### Heading 6 line height
CSS Variable(s) targeted: `var(--h6-line-height)`

Default: 1.5

#### Enable underline for Heading 1
CSS Variable(s) targeted: `var(--flexcyon-h1-underline-enabled)`

Default: false (class toggle)
> The size of the underline scales with your font weight

#### Enable underline for Heading 2
CSS Variable(s) targeted: `var(--flexcyon-h2-underline-enabled)`

Default: false (class toggle)

#### Enable underline for Heading 3
CSS Variable(s) targeted: `var(--flexcyon-h3-underline-enabled)`

Default: false (class toggle)

#### Enable underline for Heading 4
CSS Variable(s) targeted: `var(--flexcyon-h4-underline-enabled)`

Default: false (class toggle)

#### Enable underline for Heading 5
CSS Variable(s) targeted: `var(--flexcyon-h5-underline-enabled)`

Default: false (class toggle)

#### Enable underline for Heading 6
CSS Variable(s) targeted: `var(--flexcyon-h6-underline-enabled)`

Default: false (class toggle)

___
### Inline title
Accepted Formats: em

#### Inline title font size
CSS Variable(s) targeted: `var(--inline-title-size)`

Default: 1.802 (em)

#### Inline title font weight
CSS Variable(s) targeted: `var(--inline-title-weight)`

Default: 700

#### Inline title font height
CSS Variable(s) targeted: `var(--inline-title-height)`

Default: 1.2

___

### UI Font sizes
Overrides default font sizes used in the interface.

#### Smaller UI Font size
CSS Variable(s) targeted: `var(--font-ui-smaller)`

Default: 12 (px)

#### Small UI Font size
CSS Variable(s) targeted: `var(--font-ui-small)`

Default: 13 (px)

#### Medium UI Font size
CSS Variable(s) targeted: `var(--font-ui-medium)`

Default: 15 (px)

#### Large UI Font size
CSS Variable(s) targeted: `var(--font-ui-large)`

Default: 20 (px)
___
## Table
Define color for table borders, and the width of tables in reading mode.

Accepted formats: HEX, %, x.y

### Table border color
CSS Variable(s) targeted: `var(--table-border-color)`

Default: #6f768566

### Width of table in reading mode
CSS Variable(s) targeted: `var(--flexcyon-table-reading-mode-width)`

Default: 100%

___
## Files

### Enable dimmed file extensions in file explorer
CSS Variable(s) targeted: `var(--flexcyon-file-exp-dimmed-file-exts-enabled)`

Default: true (class toggle)

### Select folder style
CSS Variable(s) targeted: `var(--flexcyon-rainbow-folders), var(--flexcyon-alt-folder-style)`

Default: none (class select)
Options:
- Rainbow folders
- Alternate folder style

### Enable minimalist trees
CSS Variable(s) targeted: `var(--flexcyon-minimalist-tree)`

Default: false (class toggle)

___
## Workspace
Defines file line width when readable line length is enabled, opacity of dimmed UI elements, upscale percentage of icons used in effects

Accepted Formats: x.y, px, vw, vh

### File line width
CSS Variable(s) targeted: `var(--file-line-width)`

Default: true (class toggle)

### Opacity of dimmed elements
CSS Variable(s) targeted: `var(--dimmed)`

Default: 0.55

### Top Actions alignment
CSS Variable(s) targeted: `var(--flexcyon-top-actions-alignment)`

Default: center

___
### Upscale percentage of icons 
#### Upscale percentage of icons 1
CSS Variable(s) targeted: `var(--upsize)`

Default: 103%

#### Upscale percentage of icons 2
CSS Variable(s) targeted: `var(--expand)`

Default: 110%

___

### Prompts
#### Prompt width
CSS Variable(s) targeted: `var(--prompt-width)`

Default: 700 (px)

#### Prompt max width
CSS Variable(s) targeted: `var(--prompt-max-width)`

Default: 80 (vw)

### Prompt max height
CSS Variable(s) targeted: `var(--prompt-max-height)`

Default: 70 (vh)

### Prompt alignment
CSS Variable(s) targeted: `var(--flexcyon-prompt-align-bottom-left), var(--flexcyon-prompt-align-bottom-center), var(--flexcyon-prompt-align-center-left), var(--flexcyon-prompt-align-top-left), var(--flexcyon-prompt-align-top-center)`

Default: none (class select)
Options:
  - Top left
  - Top center
  - Center left
  - Bottom left
  - Bottom center

___

### Animations
Configure transition animations of prompts, modals and tab container.

Accepted Formats: s

#### Animation type
CSS Variable(s) targeted: `var(--flexcyon-anims-slide-rtl), var(--flexcyon-anims-slide-ltr), var(--flexcyon-anims-slide-tb), var(--flexcyon-anims-slide-bt), var(--flexcyon-anims-spin-bt), var(--flexcyon-anims-spin-rl)`
> Changes may need an app reload/restart to take effect

Default: none (class select)
Options: 
  - Slide in Left to Right
  - Slide in Right to Left
  - Slide in Top to Bottom
  - Rotate in Bottom to Top
  - Rotate in Right to Left 


#### Animation duration
CSS Variable(s) targeted: `var(--flexcyon-anim-duration)`

Default: 0.5s

#### Animation easing function
CSS Variable(s) targeted: `var(--flexcyon-anim-easing)`

Default: ease-in-out


___
### Editor Background
Accepted formats: px, deg

#### Select Background Type
CSS Variable(s) targeted: `var(--flexcyon-editor-grid), var(--flexcyon-editor-dots), var(--flexcyon-editor-rhombus)`

Default: none (class select)
Options:
- Grid Background
- Dotted Background
- Rhombus Background

#### Rotation value for grid and rhombus background
CSS Variable(s) targeted: `var(--flexcyon-editor-bg-rotation)`

Default: 0 (deg)

#### Width between each dot/line for grid/dotted background
CSS Variable(s) targeted: `var(--flexcyon-editor-bg-width)`

Default: 15 (px)

#### Size of dots for dotted background
CSS Variable(s) targeted: `var(--flexcyon-editor-dot-size)`

Default: 2 (px)

___
### Layout
Configure the workspace layout.

#### Select workspace layout
CSS Variable(s) targeted: `var(--flexcyon-workspace-card-layout), var(--flexcyon-workspace-angled-layout), var(--flexcyon-workspace-pl10k-layout)`

Default: none (class select)

Options:
- Cards Layout
- Angled Layout
- Powerlevel10k Layout

> Workspace layout changes may need app reload or restart to take effect

#### Enable TUI add-on for cards layout
CSS Variable(s) targeted: `var(--flexcyon-workspace-cards-tui-ext)`

Default: true (class toggle)

___
## Callouts
Configure styling of callouts 

Accepted Formats: px, rem, em

### Callout Icon Right padding
CSS Variable(s) targeted: `var(--flexcyon-callout-icon-right-padding)`

Default: 4 (px)

### First Codeblock Margin Top
CSS Variable(s) targeted: `var(--flexcyon-callout-first-codeblock-margin-top)`

Default: 1 (rem)

### Callout Metadata Background Opacity
CSS Variable(s) targeted: `var(--flexcyon-callout-bg-opacity)`

Default: 20%

### Callout Vertical Margin
CSS Variable(s) targeted: `var(--flexcyon-callout-vertical-margin)`

Default: 1 (em)

### Callout Border Radius
CSS Variable(s) targeted: `var(--callout-radius)`

Default: 2 (px)

### Flashcard callout width
CSS Variable(s) targeted: `var(--flexcyon-callouts-flashcard-width)`

Default: 250 (px)

### Flashcard callout height
CSS Variable(s) targeted: `var(--flexcyon-callouts-flashcard-height)`

Default: 250 (px)

___
## Checkboxes
Configure checkboxes in the theme

Accepted formats: rem

### Enable ASCII checkboxes
CSS Variable(s) targeted: `var(--flexcyon-ascii-checkboxes-enabled)`

Default: true (class toggle)

### ASCII checkboxes font size
CSS Variable(s) targeted: `var(--flexcyon-ascii-checkboxes-font-size)`

Default: 1.2 (rem)

___
## Bullet Lists
Configure bullet lists in the theme


### Enable rainbow bullet lists
CSS Variable(s) targeted: `var(--flexcyon-rainbow-bullet-points)`

Default: false (class toggle)
 Might need app restart/reload to take effect.
___
## Media
Configure media related settings

Accepted formats: px

### Media Embed Vertical margin
CSS Variable(s) targeted: `var(--flexcyon-media-embed-vertical-margin)`

Default: 8 (px)

### Image border radius
CSS Variable(s) targeted: `var(--img-border-radius)`

Default: 15 (px)

___
## Links
Configure the color of links.

Accepted formats: HEX

### Internal Link Color
CSS Variable(s) targeted: `var(--flexcyon-link-color)`

Default: #a461c8

### External Link Color
CSS Variable(s) targeted: `var(--flexcyon-external-link-color)`

Default: #5a8fcd

### Unresolved Link Color
CSS Variable(s) targeted: `var(--flexcyon-link-unresolved-color)`

Default: #a461c8

___
## Properties
Configures CSS variables for properties/metadata/YAML of files.

### Do not show properties in reading mode
CSS Variable(s) targeted: `var(--flexcyon-metadata-display-reading-disabled)`

Default: true (class toggle)

### Do not show properties in live preview mode
CSS Variable(s) targeted: `var(--flexcyon-metadata-display-editing-disabled)`

Default: false (class toggle)

___
## Status Bar
Defines CSS variables to configure the status bar

Accepted Formats: s, text, px

### Hide until hover
CSS Variable(s) targeted: `var(--flexcyon-status-hide-until-hover)`

Default: false (class toggle)

### Text when hide until hover enabled
CSS Variable(s) targeted: `var(--flexcyon-status-hide-until-hover-text)`

Default: "Show status"

### Transition duration for showing status bar on hover
CSS Variable(s) targeted: `var(--flexcyon-status-hide-hover-duration)`

Default: 0.35 (s)

### Transition timing function for showing status bar on hover
CSS Variable(s) targeted: `var(--flexcyon-status-hide-hover-function)`

Default: ease-out

### Use text instead of icons for mode status
CSS Variable(s) targeted: `var(--flexcyon-status-text-mode)`

Default: false (class toggle)

### Reading Mode Text
CSS Variable(s) targeted: `var(--flexcyon-status-reading-text)`

Default: "READ"

### Source Mode Text
CSS Variable(s) targeted: `var(--flexcyon-status-source-text)`

Default: "SOURCE"

### Live Preview Mode Text
CSS Variable(s) targeted: `var(--flexcyon-status-live-text)`

Default: "LIVE"

### Show status bar on mobile
CSS Variable(s) targeted: `var(--flexcyon-status-mobile-enabled)`

Default: false (class toggle)

### Status bar font size
CSS Variable(s) targeted: `var(--status-bar-font-size)`

Default: 12.5 (px)

### Select status bar style
CSS Variable(s) targeted: `var(--flexcyon-status-style-angled), var(--flexcyon-status-style-card), var(--flexcyon-status-style-pl10k)`

Default: none (class select)
Options:
- Angled
- Cards
- Powerlevel10k 

### Enable status text color
CSS Variable(s) targeted: `var(--flexcyon-status-text-enable-color)`

Default: false (class toggle)

___
## Title Bar
For configuration of the titlebar, enable rainbow hover effects on titlebar buttons

### Titlebar Button Effects
CSS Variable(s) targeted: `var(--flexcyon-titlebar-button-effects)`

Default: true (class toggle)

___
# Settings Section
Customise the appearance of settings

Accepted Formats: x.y, rem

## Smiley Toggle Icons in Settings
CSS Variable(s) targeted: `var(--flexcyon-settings-smiley-icons-enabled)`

Default: true (class toggle)

### Coloured Icons in Settings
CSS Variable(s) targeted: `var(--flexcyon-settings-coloured-icons)`

Default: false (class toggle)

### Enable community item effects
CSS Variable(s) targeted: `var(--flexcyon-settings-comm-item-enabled)`

Default: true (class toggle)

### Opacity of community items (unselected)
CSS Variable(s) targeted: `var(--flexcyon-comm-item-opacity)`

Default: 0.89

### Installed tooltip left margin
CSS Variable(s) targeted: `var(--flexcyon-settings-installed-tooltip-left-margin)`

Default: 1 (rem)

### Do not show scrollbar in settings
CSS Variable(s) targeted: `var(--flexcyon-settings-scrollbar-removed)`

Default: true (class toggle)

### Enabled alternate active item effect in settings
CSS Variable(s) targeted: `var(--flexcyon-enable-alt-active-item-effect)`

Default: true (class toggle)

### Style Settings
Configure the appearance for style settings

Accepted Formats: px

#### Indentation width between style settings headings
CSS Variable(s) targeted: `var(--flexcyon-style-settings-indent-width)`

Default: 4 (px)

#### Dim collapsed style settings headings
CSS Variable(s) targeted: `var(--flexcyon-style-settings-dim-collapsed-headings)`

Default: true

___
# Plugins Section
For configuration of officially supported plugins

Accepted formats: HEX, rem, x.y, %

## Alternate file tree

### Folders font size
CSS Variable(s) targeted: `var(--oz-fta-folder-font-size)`

Default: 0.925 (rem)

### Folders font color
CSS Variable(s) targeted: `var(--oz-fta-folder-pane-file-name-color)`

Default: #d3d5d3

### Active folder color
CSS Variables(s) targeted: `var(--oz-fta-all-panes-active-text-color)`

Default: #d3d5d3

### Files font size
CSS Variable(s) targeted: `var(--oz-fta-file-font-size)`

Default: 0.9 (rem)

### Files font color
CSS Variable(s) targeted: `var(--oz-fta-file-pane-file-name-color)`

Default: #6f768599

### Disable folder icons
CSS Variable(s) targeted: `var(--flexcyon-oz-folder-icons-disabled)`

Default: false (class toggle)

### Disable file tree header
CSS Variable(s) targeted: `var(--flexcyon-oz-file-tree-header-disabled)`

Default: false (class toggle)

### Enable Alternate folder count
CSS Variable(s) targeted: `var(--flexcyon-oz-alternate-folder-count)`

Default: false (class toggle)

### Enabled dimmed file extensions in file tree
CSS Variable(s) targeted: `var(--flexcyon-oz-dimmed-file-exts-enabled)`

Default: true (class toggle)

___
## Full Calendar

Accepted formats: x.y, %

### Opacity of dimmed full calendar items
CSS Variables(s) targeted: `var(--flexcyon-fc-dimmed-items-opacity)`

Default: 0.89

___
## Dataview

Accepted formats: px

### Horizontal padding of dataview error messages
CSS Variables(s) targeted: `var(--flexcyon-dataview-horizontal-padding)`

Default: 8 (px)

## Canvas
Defines styles for the core Canvas plugin.

Accepted formats: px, RGB

### Blur inactive Canvas nodes
CSS Variable(s) targeted: `var(--flexcyon-canvas-blur-inactive-nodes)`

Default: false (class toggle)

### Blur intensity for inactive nodes
Used with the previous setting to set the blur intensity of inactive canvas nodes and all arrows/edges.

CSS Variable(s) targeted: `var(--flexcyon-canvas-blur-intensity)`

Default: 1 (px)
<!-- 
### Canvas node color
CSS Variable(s) targeted: `var(--canvas-color)`

Default: 126, 126, 126 (RGB)

### Canvas color 1
CSS Variable(s) targeted `var(--canvas-color-1)`

Default: 192, 58, 71 (RGB)

### Canvas color 2
CSS Variable(s) targeted `var(--canvas-color-2)`

Default: 194, 158, 66 (RGB)

### Canvas color 3
CSS Variable(s) targeted `var(--canvas-color-3)`

Default: 161, 192, 92 (RGB)

### Canvas color 4
CSS Variable(s) targeted `var(--canvas-color-4)`

Default: 212, 88, 143 (RGB)

### Canvas color 5
CSS Variable(s) targeted `var(--canvas-color-5)`

Default: 60, 185, 194 (RGB)

### Canvas color 6
CSS Variable(s) targeted `var(--canvas-color-6)`

Default: 90, 143, 205 (RGB)
 -->

___
# Others Section
For configuring vim mode text, new tab apperance (ASCII art), sidedock icons, tooltip radius

Accepted formats: px, text

## Vim Mode Text
### Enable Vim Mode Text
CSS Variable(s) targeted: `var(--flexcyon-vim-mode-text-enable)`

Default: true (class toggle)

### Vim mode text left positioning
CSS Variable(s) targeted: `var(--flexcyon-vim-mode-left-positioning)`

Default: 6 (px)

### Vim mode text bottom positioning
CSS Variable(s) targeted: `var(--flexcyon-vim-mode-left-positioning)`

Default: -4 (px)

### Insert Mode Text
CSS Variable(s) targeted: `var(--flexcyon-vim-insert-text)`

Default: "INSERT"

### Normal Mode Text
CSS Variable(s) targeted: `var(--flexcyon-vim-normal-text)`

Default: "NORMAL"

### Command Mode Text
CSS Variable(s) targeted: `var(--flexcyon-vim-command-text)`

Default: "COMMAND"

___
## New Tab Appearance
Customize the apperance of new empty tabs

Accepted Formats: px

### Add before empty state title
CSS Variable(s) targeted: `var(--flexcyon-ascii-enable), var(--flexcyon-quote-enable)`
> Changing this may take an app reload/restart to take effect

Default: none (class select)
Options:
- ASCII Art
- Quote

### Background for add before empty state title
CSS Variable(s) targeted: `var(--flexcyon-new-tab-bg-wrapper)`

Default: `linear-gradient(to right, var(--text-accent), var(--color-blue), var(--color-cyan))`

### Quote
CSS Variable(s) targeted: `var(--flexcyon-quote-val)`
Default: ""

### Quote font size
CSS Variable(s) targeted: `var(--flexcyon-quote-font-size)`
Default: 24px

> Line breaks are escaped as `\a` and `\` is escaped as `\\`

### ASCII Art
CSS Variable(s) targeted: `var(--flexcyon-ascii-art)`

Default: " \a\
    _______________                                       \a\
    ___  ____/__  /________  ____________  ______________ \a\
    __  /_   __  /_  _ \\_  |/_/  ___/_  / / /  __ \\_  __ \\ \a\
    _  __/   _  / /  __/_>  < / /__ _  /_/ // /_/ /  / / / \a\
    /_/      /_/  \\___//_/|_| \\___/ _\\__, / \\____//_/ /_/ \a\
                                    /____/                \a\a\a "

> The ASCII art string needs to be escaped for CSS to render it, line breaks are escaped as `\a` and `\` is escaped as `\\`


### ASCII art font size limit
CSS Variable(s) targeted: `var(--flexcyon-ascii-max-font-size)`

Default: 14 (px)

### ASCII art line height
CSS Variable(s) targeted: `var(--flexcyon-ascii-line-height)`
> Changes line height for quote as welll

Default: 1

### Disable Empty State title
CSS Variable(s) targeted: `var(--flexcyon-empty-state-title-disable)`

Default: true (class toggle)

### Disable Empty State Actions
CSS Variable(s) targeted: `var(--flexcyon-empty-state-actions-disable)`

Default: false (class toggle)


___
## Side Dock Icons
Configure the side dock icons

### Enable side dock icon effects
> Rainbow effect on hover
CSS Variable(s) targeted: `var(--flexcyon-sidedock-icon-effects)`

Default: true (class toggle)

### Hide the side dock ribbon
CSS Variable(s) targeted: `var(--flexcyon-sidedock-ribbon-hidden)`

Default: false (class toggle)

___
## Tooltip radius
Configure the tooltip radius

### Small radius
CSS Variable(s) targeted: `var(--radius-s)`

Default: 2 (px)

### Medium radius
CSS Variable(s) targeted: `var(--radius-m)`

Default: 4 (px)

### Large radius
CSS Variable(s) targeted: `var(--radius-l)`

Default: 6 (px)

### Extra large radius
CSS Variable(s) targeted: `var(--radius-xl)`

Default: 8 (px)

___

## Sidebar Background 
Configure background images in the left and right sidebars.

Accepted Formats: px, %

### Select background in sidebar
CSS Variable(s) targeted: `var(--flexcyon-sidebar-bg-dots), var(--flexcyon-sidebar-bg-grid), var(--flexcyon-sidebar-bg-rhombus)`
> Overrides background image declaration below, configures in both left and right sidebar

Default: none (class select)
Options:
- Grid
- Dotted
- Rhombus

### Left sidebar background image url
CSS Variable(s) targeted: `var(--flexcyon-bg-image-sidebar-left-url)`

Default: url("")
> For urls to work, add your URL between the double quotes e.g. a value of:
`url("https://fake_domain/not_a_real_image.png")`

### Right sidebar background image url
CSS Variable(s) targeted: `var(--flexcyon-bg-image-sidebar-right-url)`

Default: url("")
> For urls to work, add your URL between the double quotes e.g. a value of:
`url("https://fake_domain/not_a_real_image.png")`

### Sidebar Background image blend mode
CSS Variable(s) targeted: `var(--flexcyon-bg-image-blend-mode)`

Default: darken

### Sidebar Background image repeat
CSS Variable(s) targeted: `var(--flexcyon-bg-image-repeat)`

Default: no-repeat

### Sidebar Background image blur
CSS Variable(s) targeted: `var(--flexcyon-bg-image-blur)`

Default: 1px

### Sidebar Background image brightness
CSS Variable(s) targeted: `var(--flexcyon-bg-image-brightness)`

Default: 55%

### Sidebar Background image size
CSS Variable(s) targeted: `var(--flexcyon-bg-image-size)`

Default: contain

### Sidebar Background image position
CSS Variable(s) targeted: `var(--flexcyon-bg-image-position)`

Default: center


___
## Modal Background
Configure background images in the background of settings menu, prompts etc

Accepted Formats: px, %


### Modal Background image url
CSS Variable(s) targeted: `var(--flexcyon-modal-bg-url)`

Default: url("")
> For urls to work, add your URL between the double quotes e.g. a value of:
`url("https://fake_domain/not_a_real_image.png")`


### Modal Background image blend mode
CSS Variable(s) targeted: `var(--flexcyon-modal-image-blend-mode)`

Default: lighten

### Modal Background image repeat
CSS Variable(s) targeted: `var(--flexcyon-modal-image-repeat)`

Default: no-repeat

### Modal Background image blur
CSS Variable(s) targeted: `var(--flexcyon-modal-image-blur)`

Default: 1px

### Modal Background image brightness
CSS Variable(s) targeted: `var(--flexcyon-bg-modal-brightness)`

Default: 55%

### Modal background image size
CSS Variable(s) targeted: `var(--flexcyon-modal-image-size)`

Default: cover

### Modal background image position
CSS Variable(s) targeted: `var(--flexcyon-modal-image-position)`

Default: center