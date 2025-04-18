---
title: Animations
icon: material/animation
---

Configure transition animations of prompts, modals and tab container.

Accepted Formats: s

## Navigation
```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
|   |-- Editor
|   |   |-- ...
|   |   |-- Workspace
|   |   |   |-- ...
|   |   |   |-- Animations
|   |   |   |-- ...
|   |   |-- ...
|   |-- ...
|-- ...
```

## Configuration Options

### Animation type
CSS Variable(s) targeted: `var(--flexcyon-anims-slide-rtl), var(--flexcyon-anims-slide-ltr), var(--flexcyon-anims-slide-tb), var(--flexcyon-anims-slide-bt), var(--flexcyon-anims-spin-bt), var(--flexcyon-anims-spin-rl)`
> Changes may need an app reload/restart to take effect

Default: none (class select)
Options: 
  - Slide in Left to Right
  - Slide in Right to Left
  - Slide in Top to Bottom
  - Rotate in Bottom to Top
  - Rotate in Right to Left 

### Animation duration
CSS Variable(s) targeted: `var(--flexcyon-anim-duration)`

Default: 0.5s

### Animation easing function
CSS Variable(s) targeted: `var(--flexcyon-anim-easing)`

Default: ease-in-out