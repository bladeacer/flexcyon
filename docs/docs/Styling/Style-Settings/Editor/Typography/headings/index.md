---
title: Headings
icon: material/format-header-pound
---

Defines CSS variables for styling related to headings like font weight.

Accepted Formats: px, number, rem

## Navigation
```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
|   |-- Editor
|   |   |-- ...
|   |   |-- Typography
|   |   |   |-- Headings
|   |   |   |-- ...
|   |   |-- ...
|   |-- ...
|-- ...
```

## Configuration Options

### Enable coloured headings
CSS Variable(s) targeted: `var(--flexcyon-headings-coloured-enabled)`

Default: true (class toggle)

> Inherits from accent colors like `--color-blue`, `--color-red` etc

### Enable soft glow for headings
CSS Variable(s) targeted: `var(--flexcyon-headings-glow-enabled)`

Default: false (class toggle)

### Enable heading indicators globally
Customise which headings have heading indicators before them globally. If you are looking to apply them on a per-note basis, [click here](../../../../CSS-Classes/heading-indicators/index.md)

#### For Heading 1
CSS Variable(s) targeted: `var(--flexcyon-headings-indicator-h1)`

Default: false (class toggle)

> The CSS Class equivalent can be [found here](../../../../CSS-Classes/heading-indicators/page-1.md)

#### For Heading 2
CSS Variable(s) targeted: `var(--flexcyon-headings-indicator-h2)`

Default: false (class toggle)

> The CSS Class equivalent can be [found here](../../../../CSS-Classes/heading-indicators/page-2.md)

#### For Heading 3
CSS Variable(s) targeted: `var(--flexcyon-headings-indicator-h3)`

Default: false (class toggle)

> The CSS Class equivalent can be [found here](../../../../CSS-Classes/heading-indicators/page-3.md)

#### For Heading 4
CSS Variable(s) targeted: `var(--flexcyon-headings-indicator-h4)`

Default: false (class toggle)

> The CSS Class equivalent can be [found here](../../../../CSS-Classes/heading-indicators/page-4.md)

#### For Heading 5
CSS Variable(s) targeted: `var(--flexcyon-headings-indicator-h5)`

Default: false (class toggle)

> The CSS Class equivalent can be [found here](../../../../CSS-Classes/heading-indicators/page-5.md)

#### For Heading 6
CSS Variable(s) targeted: `var(--flexcyon-headings-indicator-h6)`

Default: false (class toggle)

> The CSS Class equivalent can be [found here](../../../../CSS-Classes/heading-indicators/page-6.md)

___
### Font size
#### Heading 1 font size
CSS Variable(s) targeted: `var(--h1-size)`

Default: 1.802 (em)

<h1 style="font-weight: 700; font-size: 1.802em;">Sample h1</h1>

#### Heading 2 font size
CSS Variable(s) targeted: `var(--h2-size)`

Default: 1.602 (em)

<h2 style="font-weight: 675; font-size: 1.602em;">Sample h2</h2>

#### Heading 3 font size
CSS Variable(s) targeted: `var(--h3-size)`

Default: 1.424 (em)

<h3 style="font-weight: 650; font-size: 1.424em;">Sample h3</h3>

#### Heading 4 font size
CSS Variable(s) targeted: `var(--h4-size)`

Default: 1.266 (em)

<h4 style="font-weight: 625; font-size: 1.266;">Sample h4</h4>

#### Heading 5 font size
CSS Variable(s) targeted: `var(--h5-size)`

Default: 1.125 (em)

<h5 style="font-weight: 600; font-size: 1.125em;">Sample h5</h5>

#### Heading 6 font size
CSS Variable(s) targeted: `var(--h6-size)`

Default: 1 (em)

<h6 style="font-weight: 575; font-size: 1em;">Sample h6</h6>

___
### Font weight

#### Heading 1 font weight
CSS Variable(s) targeted: `var(--h1-weight)`

Default: 700

<h1 style="font-weight: 700; font-size: 1.802em;">Sample h1</h1>

#### Heading 2 font weight
CSS Variable(s) targeted: `var(--h2-weight)`

Default: 675

<h2 style="font-weight: 675; font-size: 1.602em;">Sample h2</h2>

#### Heading 3 font weight
CSS Variable(s) targeted: `var(--h3-weight)`

Default: 650

<h3 style="font-weight: 650; font-size: 1.424em;">Sample h3</h3>

#### Heading 4 font weight
CSS Variable(s) targeted: `var(--h4-weight)`

Default: 625

<h4 style="font-weight: 625; font-size: 1.266;">Sample h4</h4>

#### Heading 5 font weight
CSS Variable(s) targeted: `var(--h5-weight)`

Default: 600

<h5 style="font-weight: 600; font-size: 1.125em;">Sample h5</h5>

#### Heading 6 font weight
CSS Variable(s) targeted: `var(--h6-weight)`

Default: 575

<h6 style="font-weight: 575; font-size: 1em;">Sample h6</h6>

___
### Line Height

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

___
### Underline

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