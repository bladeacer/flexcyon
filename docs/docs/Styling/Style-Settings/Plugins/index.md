---
title: Plugins
icon: material/hexagon-outline
---

For configuration of officially supported plugins

Accepted formats: HEX, rem, x.y, %

## Navigation
```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
|   |-- ...
|   |-- Plugins
|   |-- ...
```

## Configuration Options

### Alternate file tree

#### Folders font size
CSS Variable(s) targeted: `var(--oz-fta-folder-font-size)`

Default: 0.925 (rem)

#### Folders font color
CSS Variable(s) targeted: `var(--oz-fta-folder-pane-file-name-color)`

Default: #d3d5d3

#### Active folder color
CSS Variables(s) targeted: `var(--oz-fta-all-panes-active-text-color)`

Default: #d3d5d3

#### Files font size
CSS Variable(s) targeted: `var(--oz-fta-file-font-size)`

Default: 0.9 (rem)

#### Files font color
CSS Variable(s) targeted: `var(--oz-fta-file-pane-file-name-color)`

Default: #6f768599

#### Disable folder icons
CSS Variable(s) targeted: `var(--flexcyon-oz-folder-icons-disabled)`

Default: false (class toggle)

#### Disable file tree header
CSS Variable(s) targeted: `var(--flexcyon-oz-file-tree-header-disabled)`

Default: false (class toggle)

#### Enable Alternate folder count
CSS Variable(s) targeted: `var(--flexcyon-oz-alternate-folder-count)`

Default: false (class toggle)

#### Enabled dimmed file extensions in file tree
CSS Variable(s) targeted: `var(--flexcyon-oz-dimmed-file-exts-enabled)`

Default: true (class toggle)

___
### Full Calendar

Accepted formats: x.y, %

#### Opacity of dimmed full calendar items
CSS Variables(s) targeted: `var(--flexcyon-fc-dimmed-items-opacity)`

Default: 0.89

___
### Dataview

Accepted formats: px

#### Horizontal padding of dataview error messages
CSS Variables(s) targeted: `var(--flexcyon-dataview-horizontal-padding)`

Default: 8 (px)

___
### Canvas
Defines styles for the core Canvas plugin.

Accepted formats: px, RGB

#### Blur inactive Canvas nodes
CSS Variable(s) targeted: `var(--flexcyon-canvas-blur-inactive-nodes)`

Default: false (class toggle)

#### Blur intensity for inactive nodes
Used with the previous setting to set the blur intensity of inactive canvas nodes and all arrows/edges.

CSS Variable(s) targeted: `var(--flexcyon-canvas-blur-intensity)`

Default: 1 (px)