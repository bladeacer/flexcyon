---
title: Editor Background
icon: material/layers-edit
---

Configure the background in the editor
Accepted formats: px, deg

## Navigation
```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
|   |-- Editor
|   |   |-- ...
|   |   |-- Workspace
|   |   |   |-- ...
|   |   |   |-- Editor Background
|   |   |   |-- ...
|   |   |-- ...
|   |-- ...
|-- ...
```

## Configuration Options

### Select Background Type
CSS Classe(s) targeted: `.flexcyon-editor-grid, .flexcyon-editor-dots, .flexcyon-editor-rhombus`

Default: none (class select)
Options:
- Grid Background
- Dotted Background
- Rhombus Background

### Rotation value for grid and rhombus background
CSS Variable(s) targeted: `var(--flexcyon-editor-bg-rotation)`

Default: 0 (deg)

### Width between each dot/line for grid/dotted background
CSS Variable(s) targeted: `var(--flexcyon-editor-bg-width)`

Default: 15 (px)

### Size of dots for dotted background
CSS Variable(s) targeted: `var(--flexcyon-editor-dot-size)`

Default: 2 (px)