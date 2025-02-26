# Documentation for Flexcyon Style Settings
[Back to documentation welcome page](https://github.com/bladeacer/flexcyon/tree/master/docs/docs.md)

## Map of Contents
-  [Documentation for Flexcyon Style Settings](#documentation-for-flexcyon-style-settings)
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
    - [Status Bar](#status-bar)
    - [Title Bar](#title-bar)
- [Settings Section](#settings-section)
- [Plugins Section](#plugins-section)
    - [Alternate file tree](#alternate-file-tree)
    - [Full Calendar](#full-calendar)
- [Others Sections](#others-section)
    - [Vim Mode Text](#vim-mode-text)
    - [New Tab Apperance](#new-tab-appearance)
    - [Side Dock Icons](#side-dock-icons)
    - [Tooltip radius](#tooltip-radius)
        

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
|   |   |   |   |--  Enabled coloured headings
|   |   |   |   |--  Heading 1 font weight
|   |   |   |   |--  Heading 2 font weight
|   |   |   |   |--  Heading 3 font weight
|   |   |   |   |--  Heading 4 font weight
|   |   |   |   |--  Heading 5 font weight
|   |   |   |   |--  Heading 6 font weight
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
|   |   |-- Workspace
|   |   |   |--  File line width
|   |   |   |--  Opacity of dimmed UI elements
|   |   |   |--  Upscale percentage of icons 1
|   |   |   |--  Upscale percentage of icons 2
|   |   |-- Callouts
|   |   |   |-- Callout Icon Right padding
|   |   |   |-- First Codeblock Margin Top
|   |   |-- Status Bar
|   |   |   |-- Hide until hover
|   |   |   |-- Text to show when hide until hover is enabled
|   |   |   |-- Transition duration for showing status bar on hover
|   |   |   |-- Transition timing function for showing status bar on hover
|   |   |   |-- Use text instead of icons for mode status
|   |   |   |-- Reading Mode Text
|   |   |   |-- Source Mode Text
|   |   |   |-- Live Preview Mode Text
|   |   |-- Title Bar
|   |   |   |-- Titlebar Button Effects
|   |-- **Settings**
|   |   |-- Smiley Toggle Icons in Settings
|   |   |-- Coloured Icons in Settings
|   |   |-- Enable community item effects
|   |   |-- Opacity of community items (unselected)
|   |   |-- Installed tooltip left margin
|   |   |-- Do not show scrollbar in settings
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
|   |-- **Others**
|   |   |-- Vim Mode Text
|   |   |   |-- Enable Vim Mode Text
|   |   |   |-- Vim mode text left positioning
|   |   |   |-- Vim mode text bottom positioning
|   |   |   |-- Insert Mode Text
|   |   |   |-- Normal Mode Text
|   |   |   |-- Command Mode Text
|   |   |-- New Tab Apperance
|   |   |   |-- Enable ASCII Art
|   |   |   |-- ASCII Art
|   |   |   |-- Disable Empty State title
|   |   |   |-- Disable Empty State actions
|   |   |-- Side Dock Icons
|   |   |   |-- Enable side dock icon effects
|   |   |   |-- Tooltip radius
|   |   |   |-- Small radius
|   |   |   |-- Medium radius
|   |   |   |-- Large radius
|   |   |   |-- Extra large radius
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

Default value: #3cb9c2

### Green Color
CSS Variable(s) targeted: `var(--flexcyon-lime-green)`, `var(--color-green-rgb)`

Default value: #a1c05c

### Orange Color
CSS Variable(s) targeted: `var(--flexcyon-orange)`, `var(--color-orange-rgb)`

Default value: #cc8449

### Yellow Color
CSS Variable(s) targeted: `var(--flexcyon-yellow)`, `var(--color-yellow-rgb)`

Default value: #c29e42

### Purple Color
CSS Variable(s) targeted: `var(--flexcyon-purple-lilac)`, `var(--color-purple-rgb)`

Default value: #a461c8

### Red Color
CSS Variable(s) targeted: `var(--flexcyon-red-salmon)`, `var(--color-red-rgb)`

Default value: #c03a47

### Blue Color
CSS Variable(s) targeted: `var(--flexcyon-blue)`, `var(--color-blue-rgb)`

Default value: #5a8fcd

### Pink Color
CSS Variable(s) targeted: `var(--flexcyon-pink)`, `var(--color-pink-rgb)`

Default value: #d458a3

### Accent Color
CSS Variable(s) targeted: `var(--flexcyon-accent)`

Default value: #92a871

___
## Base Colors
Defined colors overrides theme defaults for base colors used in the background and other UI elements.

Accepted Formats: HEX
### Base Color 01
CSS Variable(s) targeted: `var(--flexcyon-base-blue-01)`

Default value: #14161c

### Base Color 02
CSS Variable(s) targeted: `var(--flexcyon-base-blue-02)`

Default value: #191d28

### Base Color 03
CSS Variable(s) targeted: `var(--flexcyon-base-blue-03)`

Default value: #24262c

### Base Color 04
CSS Variable(s) targeted: `var(--flexcyon-base-blue-04)`

Default value: #4d566b

### Base Color 05
CSS Variable(s) targeted: `var(--flexcyon-base-blue-05)`

Default value: #6f7685

### Base dark grey
CSS Variable(s) targeted: `var(--flexcyon-base-grey-dark)`

Default value: #898c93

### Base light grey
CSS Variable(s) targeted: `var(--flexcyon-base-grey-light)`

Default value: #d3d5d3

### Base grey tab
CSS Variable(s) targeted: `var(--flexcyon-base-grey-token)`

Default value: #586582

### Base grey scroll 
CSS Variable(s) targeted: `var(--flexcyon-base-grey-scroll)`

Default value: #3f495e

### Base grey scroll hover
CSS Variable(s) targeted: `var(--flexcyon-base-grey-scroll-hover)`

Default value: #5d6782

___

## Typography
Defined colors for muted text color, styling for headings, and controlling UI font sizes.

Accepted Formats: HEX, px

### Muted text color
CSS Variable(s) targeted: `var(--flexcyon-text-muted)`

Default value: #6f768599

___

### Headings
#### Enable coloured headings
CSS Variable(s) targeted: `var(--flexcyon-headings-coloured-enabled)`

Default value: true (class toggle)

#### Heading 1 font weight
CSS Variable(s) targeted: `var(--h1-weight)`

Default value: 700

#### Heading 2 font weight
CSS Variable(s) targeted: `var(--h2-weight)`

Default value: 675

#### Heading 3 font weight
CSS Variable(s) targeted: `var(--h3-weight)`

Default value: 650

#### Heading 4 font weight
CSS Variable(s) targeted: `var(--h4-weight)`

Default value: 625

#### Heading 5 font weight
CSS Variable(s) targeted: `var(--h5-weight)`

Default value: 600

#### Heading 6 font weight
CSS Variable(s) targeted: `var(--h6-weight)`

Default value: 575

___

### UI Font sizes
Overrides default font sizes used in the interface.

#### Smaller UI Font size
CSS Variable(s) targeted: `var(--font-ui-smaller)`

Default value: 12 (px)

#### Small UI Font size
CSS Variable(s) targeted: `var(--font-ui-small)`

Default value: 13 (px)

#### Medium UI Font size
CSS Variable(s) targeted: `var(--font-ui-medium)`

Default value: 15 (px)

#### Large UI Font size
CSS Variable(s) targeted: `var(--font-ui-large)`

Default value: 20 (px)
___
## Table
Define color for table borders, and the width of tables in reading mode.

Accepted formats: HEX, %, x.y

### Table border color
CSS Variable(s) targeted: `var(--table-border-color)`

Default value: #6f768555

### Width of table in reading mode
CSS Variable(s) targeted: `var(--flexcyon-table-reading-mode-width)`

Default value: 100%

___
## Files

### Enable dimmed file extensions in file explorer
CSS Variable(s) targeted: `var(--flexcyon-file-exp-dimmed-file-exts-enabled)`

Default value: true (class toggle)

___
## Workspace
Defines file line width when readable line length is enabled, opacity of dimmed UI elements, upscale percentage of icons used in effects

Accepted formats: %, x.y

### File line width
CSS Variable(s) targeted: `var(--file-line-width)`

Default value: true (class toggle)

### Opacity of dimmed elements
CSS Variable(s) targeted: `var(--dimmed)`

Default value: 0.55

### Upscale percentage of icons 1
CSS Variable(s) targeted: `var(--upsize)`

Default value: 103%

### Upscale percentage of icons 2
CSS Variable(s) targeted: `var(--expand)`

Default value: 110%

___
## Callouts

___
## Status Bar

___
## Title Bar

___
# Settings Section

___
# Plugins Section

## Alternate file tree

___
## Full Calendar

___
# Others Section

## Vim Mode Text

___
## New Tab Appearance

___
## Side Dock Icons

___
## Tooltip radius
