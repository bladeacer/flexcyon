## WIP, to implement later
[Back to documentation welcome page](https://github.com/bladeacer/flexcyon/tree/master/docs/docs.md)

## CSS Classes

## Callouts
Defines utilities for callouts.

### Callout metadata
> Note: you need at least `>[!|] your title` for Obsidian to render your callout. In this case where the callout type is not specified, it will render as if you typed `>[!note] your title`

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

Callout metadata: "no-title"

Usage: 

```md
> [!info|no-title] This title will not show
> Content wil show as usual
```
___
Callout metadata: "empty"

Usage: 
```md
> [!|empty] Neither the title and callout icon will show
> Content is shown as usual
```
___
Callout metadata: "transparent-bg"

Usage: 
```md
> [!warning|transparent-bg] The background color will be transparent
> Content and title is shown as usual
```
___
Callout metadata: "rtl-title"

Usage:
```md
> [!info|rtl-title] The title will be displayed as rtl
> Content and title is shown as usual
```

Callout metadata: "rtl-content"

Usage: 
```md
> [!info|rtl-content] The title will be displayed as usual
> The content will be dispalyed as rtl
```

Callout metadata: "rtl-all"

Usage: 
```md
> [!info|rtl-all] The title will be displayed as rtl
> The content will be dispalyed as rtl
```
___
Callout metadata: "ltr-title"

Usage:
```md
> [!info|ltr-title] The title will be displayed as ltr
> Content and title is shown as usual
```

Callout metadata: "ltr-content"

Usage: 
```md
> [!info|ltr-content] The title will be displayed as usual
> The content will be dispalyed as ltr
```

Callout metadata: "ltr-all"

Usage:
```md
> [!info|ltr-all] The title will be displayed as ltr
> The content will be dispalyed as ltr
```

___

Callout metadata: "center-title"

Usage:
```md
> [!info|center-title] The title will be centered
> The content will display as usual
```


Callout metadata: "center-content"
> Note: this will not center text in codeblocks

Usage:
```md
> [!info|center-content] The title will display as usual
> The content will be centered
```

Callout metadata: "center-all"
> Note: this will not center text in codeblocks

Usage:
```md
> [!info|center-all] The title will be centered
> The content will be centered
```

___
### Combined usage
```md
> [!info|ltr-content rtl-title transparent-bg center-content] RTL Title
> LTR and centered content, transparent background
```

The `ltr-*` variants will override the `rtl-*` variants if your language is left-to-right by default.