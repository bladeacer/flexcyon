---
title: Prompts
icon: material/text-box 
---

Configure prompts such as the command prompt, quick switcher etc.

Accepted Formats: px, vw, vh

## Navigation
```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
|   |-- Editor
|   |   |-- ...
|   |   |-- Workspace
|   |   |   |-- ...
|   |   |   |-- Prompts
|   |   |   |-- ...
|   |   |-- ...
|   |-- ...
|-- ...
```

## Configuration Prompts

### Prompt width
CSS Variable(s) targeted: `var(--prompt-width)`

Default: 700 (px)

### Prompt max width
CSS Variable(s) targeted: `var(--prompt-max-width)`

Default: 80 (vw)

### Prompt max height
CSS Variable(s) targeted: `var(--prompt-max-height)`

Default: 70 (vh)

### Prompt alignment
CSS Classe(s) targeted: `.flexcyon-prompt-align-bottom-left, .flexcyon-prompt-align-bottom-center, .flexcyon-prompt-align-center-left, .flexcyon-prompt-align-top-left, .flexcyon-prompt-align-top-center`

Default: none (class select)
Options:
  - Top left
  - Top center
  - Center left
  - Bottom left
  - Bottom center