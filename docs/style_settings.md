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
|   |   |-- Workspace
|   |   |   |--  File line width
|   |   |   |--  Opacity of dimmed UI elements
|   |   |   |--  Upscale percentage of icons 1
|   |   |   |--  Upscale percentage of icons 2
|   |   |   |--  Top Actions Alignment
|   |   |   |--  Prompt width
|   |   |   |--  Prompt max width
|   |   |   |--  Prompt max height
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
|   |   |   |-- Display status bar on mobile
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
|   |   |   |-- ASCII art font size limit
|   |   |-- Side Dock Icons
|   |   |   |-- Enable side dock icon effects
|   |   |   |-- Hide the side dock ribbon
|   |   |-- Tooltip radius
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

Default: #6f768555

### Width of table in reading mode
CSS Variable(s) targeted: `var(--flexcyon-table-reading-mode-width)`

Default: 100%

___
## Files

### Enable dimmed file extensions in file explorer
CSS Variable(s) targeted: `var(--flexcyon-file-exp-dimmed-file-exts-enabled)`

Default: true (class toggle)

___
## Workspace
Defines file line width when readable line length is enabled, opacity of dimmed UI elements, upscale percentage of icons used in effects

Accepted Formats: %, x.y, px, vw, vh

### File line width
CSS Variable(s) targeted: `var(--file-line-width)`

Default: true (class toggle)

### Opacity of dimmed elements
CSS Variable(s) targeted: `var(--dimmed)`

Default: 0.55

### Upscale percentage of icons 1
CSS Variable(s) targeted: `var(--upsize)`

Default: 103%

### Upscale percentage of icons 2
CSS Variable(s) targeted: `var(--expand)`

Default: 110%

### Top Actions alignment
CSS Variable(s) targeted: `var(--flexcyon-file-exp-top-actions-alignment)`

Default: center

### Prompt width
CSS Variable(s) targeted: `var(--prompt-width)`

Default: 700 (px)

### Prompt max width
CSS Variable(s) targeted: `var(--prompt-max-width)`

Default: 80 (vw)

### Prompt max height
CSS Variable(s) targeted: `var(--prompt-max-height)`

Default: 70 (vh)

___
## Callouts
Configure styling of callouts 

Accepted Formats: px, rem

### Callout Icon Right padding
CSS Variable(s) targeted: `var(--flexcyon-callout-icon-right-padding)`

Default: 4 (px)

### First Codeblock Margin Top
CSS Variable(s) targeted: `var(--flexcyon-callout-first-codeblock-margin-top)`

Default: 1.25 (rem)

___
## Status Bar
Defines CSS variables to configure the status bar

Accepted Formats: s, text

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

___
## Title Bar
For configuration of the titlebar, enable hover effects on titlebar buttons

### Titlebar Button Effects
CSS Variable(s) targeted: `var(--flexcyon-titlebar-button-effects)`

Default: true (class toggle)

___
# Settings Section
Customise the appearance of settings

Accepted Formats: %, x.y, rem

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

### FIles font color
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
# Others Section
For configuring vim mode text, new tab apperance (ASCII art), sidedock icons, tooltip radius

Accepted formats: px, text

## Vim Mode Text
### Enable Vim Mode Text
CSS Variable(s) targeted: `var(--flexcyon-vim-mode-text-enable)`

Default: true (class toggle)

### Vim mode text left positioning
CSS Variable(s) targeted: `var(--flexcyon-vim-mode-left-positioning)`

Default: 12 (px)

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

### Enable ASCII Art
CSS Variable(s) targeted: `var(--flexcyon-ascii-enable)`

Default: true (class toggle)

### ASCII Art
CSS Variable(s) targeted: `var(--flexcyon-ascii-art)`

Default: " \a\
    _______________                                       \a\
    ___  ____/__  /________  ____________  ______________ \a\
    __  /_   __  /_  _ \\_  |/_/  ___/_  / / /  __ \\_  __ \\ \a\
    _  __/   _  / /  __/_>  < / /__ _  /_/ // /_/ /  / / / \a\
    /_/      /_/  \\___//_/|_| \\___/ _\\__, / \\____//_/ /_/ \a\
                                    /____/                \a\a\a "

> The ASCII art string needs to be escaped for CSS to render it, line breaks are escaped as \a and \ is escaped as \\

### Disable Empty State title
CSS Variable(s) targeted: `var(--flexcyon-empty-state-title-disable)`

Default: true (class toggle)

### Disable Empty State Actions
CSS Variable(s) targeted: `var(--flexcyon-empty-state-actions-disable)`

Default: false (class toggle)

### ASCII art font size limit
CSS Variable(s) targeted: `var(--flexcyon-ascii-max-font-size)`

Default: 14 (px)

___
## Side Dock Icons
Configure the side dock icons

### Enable side dock icon effects
CSS Variable(s) targeted: `var(--flexcyon-sidedock-icon-effects)`

Default: true (class toggle)

### Hide the side dock ribbon
CSS Variable(s) targeted: `var(--flexcyon-sidedock-ribbon-hidden)`

Default: false (class toggle)

___
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
