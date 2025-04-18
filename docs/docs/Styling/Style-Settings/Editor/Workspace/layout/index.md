---
title: Layout
icon: material/page-layout-sidebar-left
---

Configure the workspace layout.

## Navigation
```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
|   |-- Editor
|   |   |-- ...
|   |   |-- Workspace
|   |   |   |-- ...
|   |   |   |-- Layout
|   |   |-- ...
|   |-- ...
|-- ...
```

## Configuration Options

### Select workspace layout
CSS Variable(s) targeted: `var(--flexcyon-workspace-card-layout), var(--flexcyon-workspace-angled-layout), var(--flexcyon-workspace-pl10k-layout)`

Default: none (class select)

Options:
- Cards Layout
- Angled Layout
- Powerlevel10k Layout

> Workspace layout changes may need app reload or restart to take effect

### Enable TUI add-on for cards layout
CSS Variable(s) targeted: `var(--flexcyon-workspace-cards-tui-ext)`

Default: true (class toggle)