---
title: GeneralProperty
category: 62ebf4654ae80e09e468624b
parentDoc: 62ec01bd561bab0aa775efe4
---

On this page you will find a list of repeating properties of various fields.

>🚧 
>
> In progress

---
# Configuration Parameters

| Property                                        | Description                      |
| :-----------------------------------------------| :--------------------------------|
| [required](#required)                           | If this is set to `true`, the field is considered invalid as long as no value is entered. |
| [disabled](#disabled)                           | Setting this to `true` permanently disables the field in the UI.                          |
| [pdfHide](#pdfhide)                             | Setting this to `true` hides the whole field in the PDF.                                  |
| [pdfHideIfValueIsEmpty](#pdfhideifvalueisempty) | Setting this to `true` hides the whole field in the PDF in case the field value is empty. |
| [pdfWidth](#pdfwidth)                           | Configuration of the width of the field.                                                  |
| [values](#values)                               | The values defines the kind of entries (expenses) that the user can select.               |

| [prefill](#prefill)                             | Configuration to prefill the field with a value upon creation of the form instance. |
| [onChange](#onchange)                           | ??? |

---
# `values`

| Property                                | Description                                                                               |
| :---------------------------------------| :---------------------------------------------------------------------------------------- |
| [options](#options)                     | Sets options that will appear in the dropdown. |
| [pdfHide](#pdfhide)                     | Setting this to `true` permanently disables the field in the UI.                          |
| [pdfTextSize](#pdftextsize)             | Setting this to `true` hides the whole field in the PDF.                                  |
| [pdfTextColor](#pdftextcolor)           | Setting this to `true` hides the whole field in the PDF.                                  |
| [pdfStartInNewLine](#pdfstartinnewline) | Setting this to `true` hides the whole field in the PDF.                                  |
| [validators](#validators)               | Setting this to `true` hides the whole field in the PDF.                                  |

 
In `values` it can be define what and how appears in the dropdown and in the pdf as well.

``` typescript
value: {
    options: {
        exampleOptionOne: {
            en: 'Example option 1',
            de: 'Example option 1 [DE]',
            tr: 'Example option 1 [TR]',
            fr: 'Example option 1 [FR]',
            es: 'Example option 1 [ES]',
            it: 'Example option 1 [IT]',
        },
        exampleOptionTwo: {
            en: 'Example option 2',
            de: 'Example option 2 [DE]',
            tr: 'Example option 2 [TR]',
            fr: 'Example option 2 [FR]',
            es: 'Example option 2 [ES]',
            it: 'Example option 2 [IT]',
        },
    },
    pdfHide: false,
    pdfStartInNewLine: false,
    pdfTextColor: '#facc2e',
    pdfTextSize: 14,
},

```

## `pdfHide`

| `pdfHide`      |                 |
| :-------------- | :-------------- |
| Possible Values | `true`, `false` |
| Required        | no              |
| Default Value   | `false`         |

If `pdfHide` is set to `true`, the field is not shown in the PDF at all. This takes precedence over `pdfHideIfValueIsEmpty`.

``` typescript
pdfHide: true
```


---
## `pdfHideIfValueIsEmpty`

| `pdfHideIfValueIsEmpty` |                 |
| :------------------------- | :-------------- |
| Possible Values            | `true`, `false` |
| Required                   | no              |
| Default Value              | `false`         |

If `pdfHideIfValueIsEmpty` is set to `true` and the field value is empty, the field is not shown in the PDF at all.
If the field value is not empty, the field will still be shown (unless `pdfHide` is not set to `true`). 

``` typescript
pdfHideIfValueIsEmpty: true
```

---
## `pdfWidth`

| `pdfWdith`                 |                      |
| :------------------------- | :------------------- |
| Possible Values            | `0.25, 0.3, 0.5, 1`  |
| Required                   | no                   |
| Default Value              | `1 (full wdith)`     |

The value of `pdfWidth` defines the width of a field in the pdf layout.
`1` represent the full row in the pdf, e.g. `0.5` represent the half row / 50 % of the row.

``` typescript
pdfWidth: 0.5
```

---
## `required`

| `required`      |                 |
| :-------------- | :-------------- |
| Possible Values | `true`, `false` |
| Required        | no              |
| Default Value   | `false`         |

If `required` is set to `true`, the field is considered invalid as long as no value is entered.

``` typescript
required: true
```

---
## `disabled`

| `disabled`      |                 |
| :-------------- | :-------------- |
| Possible Values | `true`, `false` |
| Required        | no              |
| Default Value   | `false`         |

If `disabled` is set to `true`, the field is permanently disabled in the UI. It can still be modified during initial prefilling or dynamic field actions but directly modifying the value in the UI is not possible.

``` typescript
disabled: true
```

