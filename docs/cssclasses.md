[Back to documentation welcome page](https://github.com/bladeacer/flexcyon/tree/master/docs/docs.md)

## CSS Classes
### Table of Contents
- [Callouts](#callouts)
    - [Callout metadata](#callout-metadata)
        - [Popup Callout](#popup-callout)
        - ---------------------------------------------------
        - [No Icon](#no-icon)
        - [No Title](#no-title)
        - [Empty](#empty)
        - ---------------------------------------------------
        - [Transparent Background](#transparent-background)
        - [Blue Background](#blue-background)
        - [Blue Title](#blue-title)
        - [All Blue](#all-blue)
        - [Red Background](#red-background)
        - [Red Title](#red-title)
        - [All Red](#all-red)
        - [Purple Background](#purple-background)
        - [Purple Title](#purple-title)
        - [All Purple](#all-purple)
        - [Cyan Background](#cyan-background)
        - [Cyan Title](#cyan-title)
        - [All Cyan](#all-cyan)
        - [Pink Background](#pink-background)
        - [Pink Title](#pink-title)
        - [All Pink](#all-pink)
        - [Green Background](#green-background)
        - [Green Title](#green-title)
        - [All Green](#all-green)
        - [Orange Background](#orange-background)
        - [Orange Title](#orange-title)
        - [All Orange](#all-orange)
        - [Yellow Background](#yellow-background)
        - [Yellow Title](#yellow-title)
        - [All Yellow](#all-yellow)     
        - [Extened Color Palette](#extended-color-palette)
        - ---------------------------------------------------
        - [RTL Title](#rtl-title)
        - [RTL Content](#rtl-content)
        - [RTL All](#rtl-all)

        - [LTR Title](#ltr-title)
        - [LTR Content](#ltr-content)
        - [LTR All](#ltr-all)

        - [Center Title](#center-title)
        - [Center Content](#center-content)
        - [Center All](#center-all)
        - ---------------------------------------------------
        - [Uppercase Title](#uppercase-title)
        - [Uppercase Content](#uppercase-content)
        - [Uppercase All](#uppercase-all)

        - [Lowercase Title](#lowercase-title)
        - [Lowercase Content](#lowercase-content)
        - [Lowercase All](#lowercase-all)

        - [Capitalize Title](#capitalize-title)
        - [Capitalize Content](#capitalize-content)
        - [Capitalize All](#capitalize-all)
        - ---------------------------------------------------
        - [Combined usage](#combined-usage)
        
- [Tategaki](#tategaki)
    - [Tategaki in callouts](#tategaki-in-callouts)
- [Vertical LTR](#vertical-ltr)
    - [Vertical LTR in callouts](#vertical-ltr-in-callouts)
- [Dotted editor background](#dotted-editor-background)
- [Grid editor background](#grid-editor-background)

## Callouts
Defines utilities for callouts.

### Callout metadata
> Note: you need at least `>[!|] your title` for Obsidian to render your callout. In this case where the callout type is not specified, it will render as if you typed `>[!note] your title`

### Popup callout
Callout metadata: "$pop"

Usage:
```md
> [!info|$pop] The callout will be shown as normal in editing mode
> The callout will be rendered as a popup ">" on the left side of the editor in reading mode, which will show its contents on hover
```

___
#### No Icon
Callout metadata: "no-icon"

Usage:
```md
> [!info|no-icon] The callout will have no icon
> Content
```

```md
> [!|no-icon] The callout will have no icon
> Content
```

#### No Title
Callout metadata: "no-title"

Usage: 

```md
> [!info|no-title] This title will not show
> Content wil show as usual
```
#### Empty
Callout metadata: "empty"

Usage: 
```md
> [!|empty] Neither the title and callout icon will show
> Content is shown as usual
```

Alternatively, you can use:
```md
> [!empty] Neither the title and callout icon will show
> Content is shown as usual
```

___
#### Transparent Background
Callout metadata: "transparent-bg" or "bg-transparent"

Usage: 
```md
> [!warning|transparent-bg] The background color will be transparent
> Content and title is shown as usual
```
or 
```md
> [!warning|bg-transparent] The background color will be transparent
> Content and title is shown as usual
```

#### Blue Background
Callout metadata: "bg-blue"

```md
> [!info|bg-blue] Title will display as usual
> The background color will be blue
```

#### Blue Title
Callout metadata: "title-blue"

```md
> [!info|title-blue] Title will be blue
> The background color will display as usual
```

#### All Blue
> Shorthand for both `bg-blue` and `title-blue`

Callout metadata: "all-blue"

```md
> [!tip|all-blue] Title will be blue
> The background color will be blue
```

#### Red Background
Callout metadata: "bg-red"

```md
> [!info|bg-red] Title will display as usual
> The background color will be red
```

#### Red Title
Callout metadata: "title-red"

```md
> [!info|title-red] Title will be red
> The background color will display as usual
```

#### All Red
> Shorthand for both `bg-red` and `title-red`

Callout metadata: "all-red"

```md
> [!tip|all-red] Title will be red
> The background color will be red
```

#### Purple Background
Callout metadata: "bg-purple"

```md
> [!info|bg-purple] Title will display as usual
> The background color will be purple
```

#### Purple Title
Callout metadata: "title-purple"

```md
> [!info|title-purple] Title will be purple
> The background color will display as usual
```

#### All Purple
> Shorthand for both `bg-purple` and `title-purple`

Callout metadata: "all-purple"

```md
> [!tip|all-purple] Title will be purple
> The background color will be purple
```

#### Cyan Background
Callout metadata: "bg-cyan"

```md
> [!info|bg-cyan] Title will display as usual
> The background color will be cyan
```

#### Cyan Title
Callout metadata: "title-cyan"

```md
> [!info|title-cyan] Title will be cyan
> The background color will display as usual
```

#### All Cyan
> Shorthand for both `bg-cyan` and `title-cyan`

Callout metadata: "all-cyan"

```md
> [!tip|all-cyan] Title will be cyan
> The background color will be cyan
```

#### Pink Background
Callout metadata: "bg-pink"

```md
> [!info|bg-pink] Title will display as usual
> The background color will be pink
```

#### Pink Title
Callout metadata: "title-pink"

```md
> [!info|title-pink] Title will be pink
> The background color will display as usual
```

#### All Pink
> Shorthand for both `bg-pink` and `title-pink`

Callout metadata: "all-pink"

```md
> [!tip|all-pink] Title will be pink
> The background color will be pink
```

#### Green Background
Callout metadata: "bg-green"

```md
> [!info|bg-green] Title will display as usual
> The background color will be green
```

#### Green Title
Callout metadata: "title-green"

```md
> [!info|title-green] Title will be green
> The background color will display as usual
```

#### All Green
> Shorthand for both `bg-green` and `title-green`

Callout metadata: "all-green"

```md
> [!tip|all-green] Title will be green
> The background color will be green
```

#### Orange Background
Callout metadata: "bg-orange"

```md
> [!info|bg-orange] Title will display as usual
> The background color will be orange
```

#### Orange Title
Callout metadata: "title-orange"

```md
> [!info|title-orange] Title will be orange
> The background color will display as usual
```

#### All Orange
> Shorthand for both `bg-orange` and `title-orange`

Callout metadata: "all-orange"

```md
> [!tip|all-orange] Title will be orange
> The background color will be orange
```

#### Yellow Background
Callout metadata: "bg-yellow"

```md
> [!info|bg-yellow] Title will display as usual
> The background color will be yellow
```

#### Yellow Title
Callout metadata: "title-yellow"

```md
> [!info|title-yellow] Title will be yellow
> The background color will display as usual
```

#### All Yellow
> Shorthand for both `bg-yellow` and `title-yellow`

Callout metadata: "all-yellow"

```md
> [!tip|all-yellow] Title will be yellow
> The background color will be yellow
```

#### Extended Color Palette
> `bg-color1-color2-`
Example Usage:
```md
> [!tip|all-red-blue] Title will display as usual
> The background color will be the color mix of red and blue colors of this theme
```

> `title-color1-color2-`
Example Usage: 
```md
> [!tip|title-red-blue] Title will be the color mix of red and blue colors of this theme
> The background color will be as usual
```

> `all-color1-color2-`
Example Usage: 
```md
> [!tip|all-red-blue] Title will be the color mix of red and blue colors of this theme
> The background color will be the color mix of red and blue colors of this theme
```

> You can also use this colors in your own css snippets, they take the form of:
> - `var(--color-color1-color2-mix)`: E.g. `var(--color-red-blue-mix)`
> - `var(--color-color1-color2-mix-bg)`: E.g. `var(--color-red-blue-mix-bg)`


___
#### RTL Title
Callout metadata: "rtl-title"

Usage:
```md
> [!info|rtl-title] The title will be displayed as rtl
> Content and title is shown as usual
```

#### RTL Content
Callout metadata: "rtl-content"

Usage: 
```md
> [!info|rtl-content] The title will be displayed as usual
> The content will be dispalyed as rtl
```

#### RTL All
Callout metadata: "rtl-all"

Usage: 
```md
> [!info|rtl-all] The title will be displayed as rtl
> The content will be dispalyed as rtl
```
___
#### LTR Title
Callout metadata: "ltr-title"

Usage:
```md
> [!info|ltr-title] The title will be displayed as ltr
> Content and title is shown as usual
```

#### LTR Content
Callout metadata: "ltr-content"

Usage: 
```md
> [!info|ltr-content] The title will be displayed as usual
> The content will be dispalyed as ltr
```

#### LTR All
Callout metadata: "ltr-all"

Usage:
```md
> [!info|ltr-all] The title will be displayed as ltr
> The content will be dispalyed as ltr
```

___
#### Center Title
Callout metadata: "center-title"

Usage:
```md
> [!info|center-title] The title will be centered
> The content will display as usual
```

#### Center Content
Callout metadata: "center-content"
> Note: this will not center text in codeblocks

Usage:
```md
> [!info|center-content] The title will display as usual
> The content will be centered
```

#### Center All
Callout metadata: "center-all"
> Note: this will not center text in codeblocks

Usage:
```md
> [!info|center-all] The title will be centered
> The content will be centered
```
___
#### Uppercase title
Callout metadata: "uppercase-title"

Usage: 
```md
> [!info|uppercase-title] I will be uppercase in live preview/reading mode
> Content is shown as usual
```

#### Uppercase content
Callout metadata: "uppercase-content"

Usage: 
```md
> [!info|uppercase-content] I will be display as usual
> Content will be uppercase
```

#### Uppercase all
Callout metadata: "uppercase-all"

Usage:
```md
> [!info|uppercase-all] I will be uppercase
> Content will be uppercase
```

#### Lowercase title
Callout metadata: "lowercase-title"

Usage: 
```md
> [!info|lowercase-title] I will be lowercase in live preview/reading mode
> Content is shown as usual
```

#### Lowercase content
Callout metadata: "lowercase-content"

Usage: 
```md
> [!info|lowercase-content] I will be display as usual
> Content will be lowercase
```

#### Lowercase all
Callout metadata: "lowercase-all"

Usage:
```md
> [!info|lowercase-all] I will be lowercase
> Content will be lowercase
```

#### Capitalize title
Callout metadata: "caps-title"

Usage: 
```md
> [!info|caps-title] I will be capitalized in live preview/reading mode
> Content is shown as usual
```

#### Capitalize content
Callout metadata: "caps-content"

Usage: 
```md
> [!info|caps-content] I will be display as usual
> Content will be capitalized
```

#### Capitalize all
Callout metadata: "caps-all"

Usage:
```md
> [!info|caps-all] I will be capitalized
> Content will be capitalized
```


___
### Combined usage
```md
> [!info|ltr-content rtl-title transparent-bg center-content] RTL Title
> LTR and centered content, transparent background
```

The `ltr-*` variants will override the `rtl-*` variants if your language is left-to-right by default.

___
## Tategaki
Vertical RTLs your notes in reading mode.

Usage:
```md
---
cssclasses:
    - tategaki
---

Your content will render as vertical rtl  (text goes from top right to bottom right and towards the left)
```

### Tategaki in callouts
There is also a callout metadata provider for tategaki (which works in live preview)

Usage:
```md
>[!info|tategaki] The title will not display
> The contents will be displayed as vertical rtl
```

## Vertical LTR
Vertical LTRs your notes in reading mode

Usage:
```md
cssclasses:
    - vertical-ltr
---

Your content will render as vertical ltr  (text goes from top left to bottom left and towards the right)
```

### Vertical LTR in callouts
There is also a callout metadata provider for Vertical LTR

Usage:
```md
>[!info|vertical-ltr] The title will not display
> The contents will be displayed as vertical ltr
```

### Dotted editor background
Adds repeating dots to your editor background. Size can be adjusted in style settings.

Usage:
```md
cssclasses:
    - editor-dots
---

Your content will render as usual
```

### Grid editor background
Adds a grid to your editor background. Size can be adjusted in style settings.

Usage:
```md
cssclasses:
    - editor-grid
---

Your content will render as usual
```