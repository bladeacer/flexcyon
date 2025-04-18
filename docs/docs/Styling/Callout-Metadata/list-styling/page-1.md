---
title: Ordered List Styling
icon: material/format-list-numbered
---

> `ol-style_type`

```md
>[!info|ol-lower-greek] Your title as usual
> 1. The number 1 will render as the greek letter alpha in reading/live preview
> 2. The number 2 render as the greek letter beta in reading/live preview
> 3. The number 3 render as the greek letter gamma in reading/live preview
> ...
```

___
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