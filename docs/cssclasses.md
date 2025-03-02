[Back to documentation welcome page](https://github.com/bladeacer/flexcyon/tree/master/docs/docs.md)

## CSS Classes
### Table of Contents
- [Callouts](#callouts)
    - [Callout metadata](#callout-metadata)
        - [No Icon](#no-icon)
        - [No Title](#no-title)
        - [Empty](#empty)
        - [Transparent Background](#transparent-background)
        - [RTL Title](#rtl-title)
        - [RTL Content](#rtl-content)
        - [RTL All](#rtl-all)
        - [LTR Title](#ltr-title)
        - [LTR Content](#ltr-content)
        - [LTR All](#ltr-all)
        - [Center Title](#center-title)
        - [Center Content](#center-content)
        - [Center All](#center-all)
        - [Uppercase Title](#uppercase-title)
        - [Uppercase Content](#uppercase-content)
        - [Uppercase All](#uppercase-all)
        - [Lowercase Title](#lowercase-title)
        - [Lowercase Content](#lowercase-content)
        - [Lowercase All](#lowercase-all)
        - [Capitalize Title](#capitalize-title)
        - [Capitalize Content](#capitalize-content)
        - [Capitalize All](#capitalize-all)
        - [Combined usage](#combined-usage)
- [Tategaki](#tategaki)
    - [Tategaki in callouts](#tategaki-in-callouts)
- [Vertical LTR](#vertical-ltr)
    - [Vertical LTR in callouts](#vertical-ltr-in-callouts)


## Callouts
Defines utilities for callouts.

### Callout metadata
> Note: you need at least `>[!|] your title` for Obsidian to render your callout. In this case where the callout type is not specified, it will render as if you typed `>[!note] your title`

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
Callout metadata: "transparent-bg"

Usage: 
```md
> [!warning|transparent-bg] The background color will be transparent
> Content and title is shown as usual
```
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