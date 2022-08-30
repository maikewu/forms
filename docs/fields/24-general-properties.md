---
title: GeneralProperties
category: 62ebf4654ae80e09e468624b
parentDoc: 62ec01bd561bab0aa775efe4
---

On this page you will find a list of repeating properties of various fields.

>🚧 
>
> In progress

---
# Configuration Overview

| Property                                        | Description                                                                                             |
| :-----------------------------------------------| :-------------------------------------------------------------------------------------------------------|
| [required](#required)                           | If this is set to `true`, the field is considered invalid as long as no value is entered.               |
| [disabled](#disabled)                           | Setting this to `true` permanently disables the field in the UI.                                        |
| [pdfHide](#pdfhide)                             | Setting this to `true` hides the whole field in the PDF.                                                |
| [pdfHideIfValueIsEmpty](#pdfhideifvalueisempty) | Setting this to `true` hides the whole field in the PDF in case the field value is empty.               |
| [pdfWidth](#pdfwidth)                           | Configuration of the width of the field.                                                                |
| [placeHolderText](#placeholdertext)             | Localized placeholder text that is shown in the UI when the field is focused but does not have a value. |
| [pdfTextSize](#pdftextsize)                     | Text size of a certain field in the PDF.                                                                |
| [pdfTextColor](#pdftextcolor)                   | Text color of a certain field in the PDF.                                                               |
| [text](#labeltext)                              | Localized text of the field. Shown in the UI and the PDF.                                               |
| [uiHide](#labeluihide)                          | Setting this to `true` hides the field in the UI.                                                       |
| [uiTextColor](#uitextcolor)                     | Text color of a certain field in the UI.                                                                |
| [requiredAmountOfEntries](#)                    | ???                                                                                                     |
| [lable](#lable)                                 | Property with different sub properties.                                                                 |
| [values](#values)                               | Property with different sub properties.                                                                 |
| [fields](#fields)                               | Property with different sub properties.                                                                 |
| [prefill](#prefill)                             | Configuration to prefill the field with a value upon creation of the form instance.                     |
| [onChange](#onchange)                           | ??? |

---
# Configuration Parameters

## `required`

| `required`      |                                         |
| :-------------- | :-------------------------------------- |
| Possible Values | `true`, `false`                         |
| Required        | no                                      |
| Default Value   | `false`                                 |

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

---
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

| `pdfWdith`                 |                           |
| :------------------------- | :-------------------------|
| Possible Values            | Values between `0` - `1`  |
| Required                   | no                        |
| Default Value              | `1 (full wdith)`          |

The value of `pdfWidth` defines the width of a field in the pdf layout.
`1` represent the full row in the pdf, e.g. `0.5` represent the half row / 50 % of the row.

``` typescript
pdfWidth: 0.5
```

---
## `placeHolderText`

| `placeHolderText` |                            |
| :---------------- | :------------------------- |
| Possible Values   | [MultiLanguageText](#todo) |
| Required          | no                         |
| Default Value     | `undefined` in which case `label.text` is used as fallback |

Placeholder text that is shown in the UI when the field is focused but does not have a value. 

Important: If the field is not focused and does not have a value, `label.text` is shown instead.

``` typescript
placeHolderText: {
    en: 'Example Placeholder',
    de: 'Platzhalter',
    tr: 'Example Placeholder [TR]',
    fr: 'Example Placeholder [FR]',
    es: 'Example Placeholder [ES]',
    it: 'Example Placeholder [IT]',
}
```

---
## `pdfTextSize`

| `pdfTextSize`   |                  |
| :-------------- | :-------------- |
| Possible Values | Integer > 0     |
| Required        | no              |
| Default Value   | 9               |

By setting `pdfTextSize`, the field label will show up in the PDF having the defined text size in pixels.

``` typescript
pdfTextSize: 20
```

---
## `pdfTextColor`

| `pdfTextColor`  |                 |
| :-------------- | :-------------- |
| Possible Values | Hex-Color-Code  |
| Required        | no              |
| Default Value   | `#000000`       |

By setting `pdfTextColor`, the field label in the PDF will have the defined color.

``` typescript
pdfTextColor: #F1F8F1
```

---
## `text`

| `text` |                                       |
| :---------------- | :------------------------- |
| Possible Values   | [MultiLanguageText](./01-single-line-text-input.md) |
| Required          | yes                        |

Label text that is shown in the UI and the PDF to identify the field. 

``` typescript
text: {
    en: 'Example Placeholder',
    de: 'Platzhalter',
    tr: 'Example Placeholder [TR]',
    fr: 'Example Placeholder [FR]',
    es: 'Example Placeholder [ES]',
    it: 'Example Placeholder [IT]',
}
```

## `uiHide`

| `uiHide`       |                 |
| :-------------- | :-------------- |
| Possible Values | `true`, `false` |
| Required        | no              |
| Default Value   | `false`         |

If `uiHide` is set to `true`, the label is not shown in the UI.

``` typescript
uiHide: true
```

---

## `uiTextColor`

| `pdfTextColor`  |                 |
| :-------------- | :-------------- |
| Possible Values | Hex-Color-Code  |
| Required        | no              |
| Default Value   | `#000000`       |

By setting `uiTextColor`, the field label in the UI will have the defined color.

``` typescript
uiTextColor: #F1F8F1
```

---

## `value`

| Property                                                  | Description                                                                                     |
| :-------------------------------------------------------- | :---------------------------------------------------------------------------------------------- |
| [uiMinRows](#valueuiminrows)                              | Minimum number of lines that are shown in the UI.                                               |
| [uiMaxRows](#valueuimaxrows)                              | Maximum number of lines that can be seen in the UI without scrolling.                           |
| [pdfHide](#valuepdfhide)                                  | Setting this to `true` hides the value in the PDF.                                              |
| [pdfTextSize](#valuepdftextsize)                          | Text size of the value in the PDF.                                                              |
| [pdfTextColor](#valuepdftextcolor)                        | Text color of the value in the PDF.                                                             |
| [pdfStartInNewLine](#valuepdfstartinnewline)              | Setting this to `true` will show the field value in the PDF in a separate line below the label. |
| [validators.maxCharacters](#valuevalidatorsmaxcharacters) | Maximum number of characters for the input value to be valid.                                   |
| [validators.minCharacters](#valuevalidatorsmincharacters) | Minimum number

<details>
<summary>Click to toggle contents of `code`</summary>
```
CODE!
```
</details>

---
## `prefill`

| `prefill`                  |                                                                     |
| :------------------------- | :--------------                                                     |
| Possible Values            | Array of [PrefillRules](#todo) that output a value of type `string` |
| Required                   | no                                                                  |
| Default Value              | -                                                                   |

This configuration follows the [general syntax for prefilling rules](#todo).
The provided PrefillRules need to have an output value of type string.

``` typescript (static string)
prefill: {
        value: [
            {
                input: 'none',
                steps: [
                    [ 'staticString', 'Default \n Multi \n Line \n Text' ],
                ],
            },
        ],
    },
```
``` typescript (asset type name)
prefill: {
        value: [
            {
                input: 'assetId',
                steps: [
                    'assetIdToAsset',
                    'assetToAssetTypeNameString',
                ],
            },
        ],
    },
```

---
## `onChange`

| `onChange`                 |                   |
| :------------------------- | ------------------|
| Possible Values            | Array of Fuctions |
| Required                   | no                |
| Default Value              | -     

*???Description???*