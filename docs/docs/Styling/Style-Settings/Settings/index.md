---
title: Settings
icon: material/cogs
---

For customising the appearance of various UI aspects of settings.

Accepted Formats: x.y, rem, px

## Navigation
```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
|   |-- ...
|   |-- Settings
|   |-- ...
|-- ...
```

## Configuration Options

### Smiley Toggle Icons in Settings
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

<span style="opacity: 0.89">Sample opacity of community items (unselected)</span>

### Installed tooltip left margin
CSS Variable(s) targeted: `var(--flexcyon-settings-installed-tooltip-left-margin)`

Default: 1 (rem)

### Do not show scrollbar in settings
CSS Variable(s) targeted: `var(--flexcyon-settings-scrollbar-removed)`

Default: true (class toggle)

### Enabled alternate active item effect in settings
CSS Variable(s) targeted: `var(--flexcyon-enable-alt-active-item-effect)`

Default: true (class toggle)

___

### Style Settings
Configure the appearance for style settings

Accepted Formats: px

#### Indentation width between style settings headings
CSS Variable(s) targeted: `var(--flexcyon-style-settings-indent-width)`

Default: 4 (px)

#### Dim collapsed style settings headings
CSS Variable(s) targeted: `var(--flexcyon-style-settings-dim-collapsed-headings)`

Default: true