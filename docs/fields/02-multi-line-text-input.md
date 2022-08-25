---
title: MultiLineTextInput
category: 62ebf4654ae80e09e468624b
parentDoc: 62ec01bd561bab0aa775efe4
---

>🚧 
>
> In progress

The MultiLineTextInput field allows entering larger amounts of unformatted text. It respects line breaks and can be configured to limit the possible content length.

# Configuration Overview

| Property                                              | Description                      |
| :---------------------------------------------------- | :--------------------------------|
| [required](#required)                                 | If this is set to `true`, the field is considered invalid as long as no value is entered. |
| [disabled](#disabled)                                 | Setting this to `true` permanently disables the field in the UI. |
| [placeHolderText](#placeholdertext)                   | Localized placeholder text that is shown in the UI when the field is focused but does not have a value. |
| [pdfHide](#pdfhide)                                   | Setting this to `true` hides the whole field in the PDF. |
| [pdfHideIfValueIsEmpty](#pdfhideifvalueisempty)       | Setting this to `true` hides the whole field in the PDF in case the field value is empty. |
| [pdfWidth](#pdfwidth)                                 | Configuration of the width of the field. |
| [label](#label)                                       | Configuration of the field label. |
| [value](#value)                                       | Configuration of the field value. |
| [prefill](#prefill)                                   | Configuration to prefill the field with a value upon creation of the form instance. |
| [onChange](#onchange)                                 | ??? |

``` typescript (complete)
{
    id: 'exampleMultiLineTextInput_1',
    type: FormFieldTypesEnum.MULTI_LINE_TEXT_INPUT,
    config: {
        required: true,
        label: {
            text: {
                en: 'MultiLine Input 1',
                de: 'Mehrzeiliger Input 1',
                tr: 'MultiLine Input 1 [TR]',
                fr: 'MultiLine Input 1 [FR]',
                es: 'MultiLine Input 1 [ES]',
                it: 'MultiLine Input 1 [IT]',
            },
            pdfHide: false,
            pdfTextColor: '#facc2e',
            pdfTextSize: 14,
            uiHide: false,
        },
        placeHolderText: {
            en: 'Example Placeholder',
            de: 'Platzhalter',
            tr: 'Example Placeholder [TR]',
            fr: 'Example Placeholder [FR]',
            es: 'Example Placeholder [ES]',
            it: 'Example Placeholder [IT]',
        },
        disabled: false,
        pdfHide: false,
        pdfHideIfValueIsEmpty: false,
        uiHideInRepeaterCardDisplay: false,
        value: {
            pdfHide: false,
            pdfStartInNewLine: false,
            pdfTextColor: '#facc2e',
            pdfTextSize: 14,
            validators: {
                maxCharacters: 1000,
                minCharacters: 3,
            },
            uiMaxRows: 5,
            uiMinRows: 2,
        },
        prefill: {
            value: [
                {
                    input: 'none',
                    steps: [
                        [
                            'staticString',
                            'Default \n Multi \n Line \n Text',
                        ],
                    ],
                },
            ],
        },
    },
}
```
``` typescript (minimal)
{
    id: 'exampleMultiLineTextInput_1',
    type: FormFieldTypesEnum.MULTI_LINE_TEXT_INPUT,
    config: {
        label: {
            text: {
                en: 'MultiLine Input 1',
                de: 'Mehrzeiliger Input 1',
                tr: 'MultiLine Input 1 [TR]',
                fr: 'MultiLine Input 1 [FR]',
                es: 'MultiLine Input 1 [ES]',
                it: 'MultiLine Input 1 [IT]',
            },
        },
    },
}
```

---
# Configuration Parameters

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
## `label`

| Property                                              | Description                       |
| :---------------------------------------------------- | :-------------------------------- |
| [text](#labeltext)                                    | Localized label text of the field. Shown in the UI and the PDF. |
| [uiHide](#labeluihide)                                | Setting this to `true` hides the label in the UI. |
| [pdfHide](#labelpdfhide)                              | Setting this to `true` hides the label in the PDF. |
| [pdfTextSize](#labelpdftextsize)                      | Text size of the label in the PDF. |
| [pdfTextColor](#labelpdftextcolor)                    | Text color of the label in the PDF. |

---
### `label.text`

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

---
### `label.uiHide`

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
### `label.pdfHide`

| `pdfHide`       |                 |
| :-------------- | :-------------- |
| Possible Values | `true`, `false` |
| Required        | no              |
| Default Value   | `false`         |

If `pdfHide` is set to `true`, the label is not shown in the PDF.

=== "Example"
    ``` typescript
    pdfHide: true
    ```

---
### `label.pdfTextSize`

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
### `label.pdfTextColor`

| `pdfTextColor`  |                 |
| :-------------- | :-------------- |
| Possible Values | Hex-Color-Code  |
| Required        | no              |
| Default Value   | `#000000`       |

By setting `pdfTextColor`, the field label will show up in the PDF having the defined color.

``` typescript
pdfTextColor: #F1F8F1
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
| [validators.minCharacters](#valuevalidatorsmincharacters) | Minimum number of characters for the input value to be valid.                                   |

---
### `value.uiMinRows`

| `uiMinRows`     |                 |
| :-------------- | :-------------- |
| Possible Values | Integer > 1     |
| Required        | no              |
| Default Value   | 1               |

By setting `uiMinRows`, the text input in he UI will always span at the least the configured amount of lines.
If the content spans less lines, the size of the text input will not shrink further.

``` typescript
uiMinRows: 5
```

---
### `value.uiMaxRows`

| `uiMaxRows`     |                 |
| :-------------- | :-------------- |
| Possible Values | Integer > 1     |
| Required        | no              |
| Default Value   | 10              |

By setting `uiMaxRows`, the text input in he UI will not grow further than the specified amount of lines.
If the content spans more lines than that maximum, there will be a scrollbar to access the additional lines.

``` typescript
uiMaxRows: 15
```

---
### `value.pdfHide`

| `pdfHide`       |                 |
| :-------------- | :-------------- |
| Possible Values | `true`, `false` |
| Required        | no              |
| Default Value   | `false`         |

If `pdfHide` is set to `true`, the value is not shown in the PDF.

``` typescript
pdfHide: true
```

---
### `value.pdfTextSize`

| `pdfTextSize`   |                  |
| :-------------- | :-------------- |
| Possible Values | Integer > 0     |
| Required        | no              |
| Default Value   | 9               |

By setting `pdfTextSize`, the field value will show up in the PDF having the defined text size in pixels.

``` typescript
pdfTextSize: 20
```

---
### `value.pdfTextColor`

| `pdfTextColor`  |                 |
| :-------------- | :-------------- |
| Possible Values | Hex-Color-Code  |
| Required        | no              |
| Default Value   | `#000000`       |

By setting `pdfTextColor`, the field value will show up in the PDF having the defined color.

``` typescript
pdfTextColor: true
```

---
### `value.pdfStartInNewLine`

| `pdfStartInNewLine`       |                 |
| :-------------- | :-------------- |
| Possible Values | `true`, `false` |
| Required        | no              |
| Default Value   | `false`         |

If `pdfStartInNewLine` is set to `true`, the value of the field will be shown in the PDF on a new line below the label. If the value is `false`, the value is shown on the same line as the label.

``` typescript
pdfStartInNewLine: true
```

---
### `value.validators.maxCharacters`

| `uiMinRows`     |                 |
| :-------------- | :-------------- |
| Possible Values | Integer > 1     |
| Required        | no              |
| Default Value   | -               |

By setting `validators.maxCharacters`, the field will be marked as invalid if the value contains more characters than the specified number.

``` typescript
validators: {
    maxCharacters: 100
}
```

---
### `value.validators.minCharacters`

| `uiMinRows`     |                 |
| :-------------- | :-------------- |
| Possible Values | Integer > 1     |
| Required        | no              |
| Default Value   | -               |

By setting `validators.minCharacters`, the field will be marked as invalid if the value contains less characters than the specified number.

``` typescript
validators: {
    minCharacters: 10
}
```

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