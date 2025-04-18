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
    - [Easter Egg Mode](#easter-egg-mode)

## Markdown Navigation tree for Flexcyon's Style Settings
```md
Style Settings
|--...
|-- Flexcyon Style Settings
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

If you are seeing this the missing stuff has been moved to the new documentation site.

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

___
## Easter egg mode
Toggles Easter egg mode

### Enable Easter Egg Mode
CSS Variable(s) targeted: `var(--flexcyon-easter-egg-mode)`
> If you are searching for answers, I am not giving hints here '_'

Default: false (class toggle)