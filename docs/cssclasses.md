[Back to documentation welcome page](https://github.com/bladeacer/flexcyon/tree/master/docs/docs.md)

## CSS Classes
### Table of Contents
- [Callouts](#callouts)
    - [Callout metadata](#callout-metadata)
        - [Callout Lists](#callout-lists)
        - ---------------------------------------------------
        - [Flashcard Callout](#flashcard-callout)
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
        - [Tilt Title](#tilt-title)
        - [Tilt Content](#tilt-content)
        - [Tilt All](#tilt-all)

        - [Italic Title](#italic-title)
        - [Italic Content](#italic-content)
        - [Italic All](#italic-all)

        - [Oblique Title](#oblique-title)
        - [Oblique Content](#oblique-content)
        - [Oblique All](#oblique-all)

        - [Dashed Title](#dashed-title)
        - [Dashed Content](#dashed-content)
        - [Dashed All](#dashed-all)

        - [Overline Title](#overline-title)
        - [Overline Content](#overline-content)
        - [Overline All](#overline-all)

        - [Underline Title](#underline-title)
        - [Underline Content](#underline-content)
        - [Underline All](#underline-all)

        - [Strikethrough Title](#strikethrough-title)
        - [Strikethrough Content](#strikethrough-content)
        - [Strikethrough All](#strikethrough-all)

        - ---------------------------------------------------
        - [Font Weight Title](#font-weight-title)
        - [Font Weight Content](#font-weight-content)
        - [Font Weight All](#font-weight-all)

        - ---------------------------------------------------
        - [Heading 1 Title](#heading-1-title)
        - [Heading 2 Title](#heading-2-title)
        - [Heading 3 Title](#heading-3-title)
        - [Heading 4 Title](#heading-4-title)
        - [Heading 5 Title](#heading-5-title)
        - [Heading 6 Title](#heading-6-title)

        - ---------------------------------------------------
        - [Combined usage](#combined-usage)
        
- [Tategaki](#tategaki)
    - [Tategaki in callouts](#tategaki-in-callouts)
- [Vertical LTR](#vertical-ltr)
    - [Vertical LTR in callouts](#vertical-ltr-in-callouts)
- [Dotted background](#dotted-background)
- [Grid background](#grid-background)
- [Rhombus background](#rhombus-background)
- [Heading indicators](#heading-indicators)
- [Writing Mode](#writing-mode)

## Callouts
Defines utilities for callouts.

### Callout metadata
> Note: you need at least `>[!|] your title` for Obsidian to render your callout. In this case where the callout type is not specified, it will render as if you typed `>[!note] your title`

#### Callout Lists
These are some utilities for styling ordered and unordered lists in Obsidian.

Accepted values for `style_type`: The [values that are defined in the MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/list-style-type#Values)
> Why are the `style_type` names so long? Well they are standardised style types available in major browsers

###### Note
To write an ordered list in Obsidian, use:
```md
1. Never
2. Gonna
3. Give
4. ...
```

To write an unordered list in Obsidian. use:
```md
- Never
- Gonna
- Give
- ...
```

Accepted values for `style_type`: The [values that are defined in the MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/list-style-type#Values)
- yes there are quite a bit of them

##### Callout Lists: Ordered Lists
> `ol-style_type`

Usage:
```md
>[!info|ol-lower-greek] Your title as usual
> 1. The number 1 will render as the greek letter alpha in reading/live preview
> 2. The number 2 render as the greek letter beta in reading/live preview
> 3. The number 3 render as the greek letter gamma in reading/live preview
> ...
```

> `ol-style_type-ins`

Usage:
```md
>[!info|ol-lower-greek-ins] Your title as usual
> 1. The number 1 render as the greek letter alpha in reading/live preview, inside the list item along with the text.
> 2. The number 2 will render as the greek letter beta in reading/live preview, inside the list item along with the text.
> 3. The number 3 will render as the greek letter gamma in reading/live preview, inside the list item along with the text.
> ...
```

- There is no standard implementation for upper Greek

What does "inside the list item along with the text mean"?
> Effectively, the list item number/letter/whatever will inherit the indentation of the list item. Think of writing:
```md
  1. Never
  2. Gonna
  3. Give
```

instead of 
```
1. Never
2. Gonna
3. Give
```

##### Callout Lists: Unordered Lists
> `ul-style_type`

Usage:
```md
>[!info|ul-lower-roman] Your title as usual
> 1. The bullet point will render as the roman numeral i in reading/live preview
> 2. The bullet point render as the roman numeral ii in reading/live preview
> 3. The bullet point render as the roman numeral iii in reading/live preview
> ...
```

> `ul-style_type-ins`

Usage:
```md
>[!info|ul-lower-roman-ins] Your title as usual
> - The bullet point will render as the roman numeral i in reading/live preview, inside the list item along with the text.
> - The bullet point will render as the roman numeral ii in reading/live preview, inside the list item along with the text.
> - The bullet point will render as the roman numeral iii in reading/live preview, inside the list item along with the text.
> ...
```

##### Callout Lists: Ordered + Unordered Lists
Accepted values for `style_type`: The [values that are defined in the MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/list-style-type#Values)

Use when you want to apply the same style to both ordered and unordered lists 
> `li-style_type`

Usage:
```md
>[!info|li-upper-roman] Your title as usual
> 1. The number 1 will render as the roman numeral I in reading/live preview
> 2. The number 2 render as the roman numeral II in reading/live preview
> 3. The number 3 render as the roman numeral III in reading/live preview
> 
> - The bullet point will render as the roman numeral I in reading/live preview
> - The bullet point will render as the roman numeral II in reading/live preview
> ...
```

> `li-style_type-ins`

Usage:
```md
>[!info|li-upper-roman-ins] Your title as usual
> 1. The number 1 render as the roman numeral I in reading/live preview, inside the list item along with the text.
> 2. The number 2 will render as the roman numeral II in reading/live preview, inside the list item along with the text.
> 3. The number 3 will render as the roman numeral III in reading/live preview, inside the list item along with the text.
>
> - The bullet point will render as the roman numeral I in reading/live preview, inside the list item along with the text.
> - The bullet point will render as the roman numeral II in reading/live preview, inside the list item along with the text.
> ...
```

#### Flashcard callout
Callout metadata: "flashcard"

Usage:
```md
> [!info|flashcard] The title and the callout will styled nicely to resemble a card
> The contents will be flipped in reading mode or live preview, which will show on hover
```

#### Popup callout
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

__
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
Usage:
```md
> [!tip|all-red-blue] Title will display as usual
> The background color will be the color mix of red and blue colors of this theme
```

> `title-color1-color2-`
Usage: 
```md
> [!tip|title-red-blue] Title will be the color mix of red and blue colors of this theme
> The background color will be as usual
```

> `all-color1-color2-`
Usage: 
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
> Content is shown as usual
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
> Content is shown as usual
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
> [!info|uppercase-title] I will be uppercase in live preview and reading mode/reading mode
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
> [!info|lowercase-title] I will be lowercase in live preview and reading mode/reading mode
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
> [!info|caps-title] I will be capitalized in live preview and reading mode/reading mode
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
#### Tilt title
Callout metadata: "tilt-title"

Usage: 
```md
> [!info|tilt-title] I will be tilted in live preview and reading mode/reading mode
> Content is shown as usual
```

#### Tilt content
Callout metadata: "tilt-content"

Usage: 
```md
> [!info|tilt-content] I will be display as usual
> Content will be titlted
```

#### Tilt all
Callout metadata: "tilt-all"

Usage:
```md
> [!info|tilted-all] I will be tilted
> Content will be tilted
```

___
#### Italic title
Callout metadata: "italic-title"

Usage: 
```md
> [!info|italic-title] I will be italic in live preview and reading mode/reading mode
> Content is shown as usual
```

#### Italic content
Callout metadata: "italic-content"

Usage: 
```md
> [!info|italic-content] I will be display as usual
> Content will be italic
```

#### Italic all
Callout metadata: "italic-all"

Usage:
```md
> [!info|italic-all] I will be italic
> Content will be italic
```

___
#### Oblique title
Callout metadata: "oblique-title"

Usage: 
```md
> [!info|oblique-title] I will be oblique in live preview and reading mode/reading mode
> Content is shown as usual
```

#### Oblique content
Callout metadata: "oblique-content"

Usage: 
```md
> [!info|oblique-content] I will be display as usual
> Content will be oblique
```

#### Oblique all
Callout metadata: "oblique-all"

Usage:
```md
> [!info|oblique-all] I will be oblique
> Content will be oblique
```

___
#### Dashed title
Callout metadata: "dashed-title"

Usage: 
```md
> [!info|dashed-title] I will be dashed in live preview and reading mode/reading mode
> Content is shown as usual
```

#### Dashed content
Callout metadata: "dashed-content"

Usage: 
```md
> [!info|dashed-content] I will be display as usual
> Content will be dashed
```

#### Dashed all
Callout metadata: "dashed-all"

Usage:
```md
> [!info|dashed-all] I will be dashed
> Content will be dashed
```

___
#### Overline title
Callout metadata: "overline-title"

Usage: 
```md
> [!info|overline-title] I will be overline in live preview and reading mode/reading mode
> Content is shown as usual
```

#### Overline content
Callout metadata: "overline-content"

Usage: 
```md
> [!info|overline-content] I will be display as usual
> Content will be overline
```

#### Overline all
Callout metadata: "overline-all"

Usage:
```md
> [!info|overline-all] I will be overline
> Content will be overline
```

___
#### Underline title
Callout metadata: "underline-title"

Usage: 
```md
> [!info|underline-title] I will be underline in live preview and reading mode/reading mode
> Content is shown as usual
```

#### Underline content
Callout metadata: "underline-content"

Usage: 
```md
> [!info|underline-content] I will be display as usual
> Content will be underline
```

#### Underline all
Callout metadata: "underline-all"

Usage:
```md
> [!info|underline-all] I will be underline
> Content will be underline
```

___
#### Strikethrough title
Callout metadata: "line-through-title"

Usage: 
```md
> [!info|line-through-title] I will be strikethrough in live preview and reading mode/reading mode
> Content is shown as usual
```

#### Strikethrough content
Callout metadata: "line-through-content"

Usage: 
```md
> [!info|line-through-content] I will be display as usual
> Content will be strikethrough
```

#### Strikethrough all
Callout metadata: "line-through-all"

Usage:
```md
> [!info|line-through-all] I will be strikethrough
> Content will be strikethrough
```

___
#### Font weight title
Callout metadata: "w-`value`-title"

Accepted values for `value`:
- 100 to 900 (in increments of 100)
- bold
- bolder
- lighter

Usage: 
```md
> [!info|w-900-title] I will have a font weight of 900 in live preview and reading mode/reading mode
> Content is shown as usual
```

#### Font weight content
Callout metadata: "w-`value`-content"

Accepted values for `value`:
- 100 to 900 (in increments of 100)
- bold
- bolder
- lighter

Usage: 
```md
> [!info|w-bold-content] I will be display as usual
> Content will have a bold font weight
```

#### Font weight all
Callout metadata: "w-`value`-content"

Accepted values for `value`:
- 100 to 900 (in increments of 100)
- bold
- bolder
- lighter

Usage:
```md
> [!info|w-lighter-all] I will have a lighter font weight 
> Content will have a lighter font weight
```
___
#### Heading 1 Title
Callout metadata: "h1-title"

Usage:
```md
> [!info|h1-title] I will display inheriting the style of Heading 1s in this theme
> Content will display as usual
```

#### Heading 2 Title
Callout metadata: "h2-title"

Usage:
```md
> [!info|h2-title] I will display inheriting the style of Heading 2s in this theme
> Content will display as usual
```

#### Heading 3 Title
Callout metadata: "h3-title"

Usage:
```md
> [!info|h3-title] I will display inheriting the style of Heading 3s in this theme
> Content will display as usual
```

#### Heading 4 Title
Callout metadata: "h4-title"

Usage:
```md
> [!info|h4-title] I will display inheriting the style of Heading 4s in this theme
> Content will display as usual
```

#### Heading 5 Title
Callout metadata: "h5-title"

Usage:
```md
> [!info|h5-title] I will display inheriting the style of Heading 5s in this theme
> Content will display as usual
```

#### Heading 6 Title
Callout metadata: "h6-title"

Usage:
```md
> [!info|h6-title] I will display inheriting the style of Heading 6s in this theme
> Content will display as usual
```

___
### Combined usage
E.g. 
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
There is also a callout metadata provider for tategaki (which works in live preview and reading mode)

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

### Dotted background
Adds repeating dots to your editor background. Size can be adjusted in style settings.

Usage:
```md
cssclasses:
    - editor-dots
---

Your content will render as usual
```

### Dotted background in callouts
There is also a callout metadata provider for dotted background (which works in live preview and reading mode)

```md
>[!note|bg-grid] I will display as usual
> I will have a dotted background
```

### Grid background
Adds a grid to your editor background. Size can be adjusted in style settings.

Usage:
```md
cssclasses:
    - editor-grid
---

Your content will render as usual
```

### Grid background in callouts
There is also a callout metadata provider for grid background (which works in live preview and reading mode)

```md
>[!note|bg-grid] I will display as usual
> I will have a grid background
```

### Rhombus background
Adds a repeating pattern of rhombi to your editor background. Rotation can be adjusted.

Usage:
```md
cssclasses:
    - editor-rhombus
---

Your content will render as usual
```

### Rhombus background in callouts
There is also a callout metadata provider for rhombus background (which works in live preview and reading mode)

```md
>[!note|bg-rhombus] I will display as usual
> I will have a rhombus background
```

___
## Heading indicators
Add a heading indicator for all headings. Will appear in reading, editing and source mode.

Usage:
```md
cssclasses:
    - headings-indicator-all
---

# I will have an indicator before me
## I will have an indicator before me
### I will have an indicator before me
#### I will have an indicator before me
##### I will have an indicator before me
###### I will have an indicator before me
```

### Heading indicators - h1
Add a heading indicator for heading 1s. Will appear in reading, editing and source mode.

Usage:
```md
cssclasses:
    - headings-indicator-h1
---

# I will have an indicator before me
Others headings display as usual
```


### Heading indicators - h2
Add a heading indicator for heading 2s. Will appear in reading, editing and source mode.

Usage:
```md
cssclasses:
    - headings-indicator-h2
---

## I will have an indicator before me
Others headings display as usual
```


### Heading indicators - h3
Add a heading indicator for heading 3s. Will appear in reading, editing and source mode.

Usage:
```md
cssclasses:
    - headings-indicator-h3
---

### I will have an indicator before me
Others headings display as usual
```


### Heading indicators - h4
Add a heading indicator for heading 4s. Will appear in reading, editing and source mode.

Usage:
```md
cssclasses:
    - headings-indicator-h4
---

#### I will have an indicator before me
Others headings display as usual
```


### Heading indicators - h5
Add a heading indicator for heading 5s. Will appear in reading, editing and source mode.

Usage:
```md
cssclasses:
    - headings-indicator-h5
---

##### I will have an indicator before me
Others headings display as usual
```

### Heading indicators - h6
Add a heading indicator for heading 6s. Will appear in reading, editing and source mode.

Usage:
```md
cssclasses:
    - headings-indicator-h6
---

###### I will have an indicator before me
Others headings display as usual
```
-

## Writing mode 
Adds text indent and increased paragraph spacing to your editor. Size can be adjusted in style settings.

Usage:
```md
cssclasses:
    - editor-writing
---

Your content will have increased text indent and paragraph spacing 
```

### Writing mode in callouts
There is also a callout metadata provider for writing (which works in live preview and reading mode)

```md
>[!note|writing] I will display as usual
> I will have increased text indent and paragraph spacing 
```