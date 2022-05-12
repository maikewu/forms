# MultiLineTextInput

The MultiLineTextInput field allows entering larger amounts of unformatted text. It respects line breaks and can be configured to limit the possible content length.

## Configuration Overview

| Property                                              | Description                      |
| :---------------------------------------------------- | :--------------------------------|
| [required](#required)                                 | If this is set to `true`, the field is considered invalid as long as no value is entered. |
| [disabled](#disabled)                                 | Setting this to `true` permanently disables the field in the UI. |
| [placeHolderText](#placeholdertext)                   | Localized placeholder text that is shown in the UI when the field is focused but does not have a value. |
| [pdfHideAll](#pdfhideall)                             | Setting this to `true` hides the whole field in the PDF. |
| [pdfHideAllIfValueIsEmpty](#pdfhideallifvalueisempty) | Setting this to `true` hides the whole field in the PDF in case the field value is empty. |
| [label](#label)                                       | Configuration of the field label. |
| [value](#value)                                       | Configuration of the field value. |
| [prefill](#prefill)                                   | Configuration to prefill the field with a value upon creation of the form instance. |

=== "Example (complete)"
    ``` typescript
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
            pdfHideAll: false,
            pdfHideAllIfValueIsEmpty: false,
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

=== "Example (minimal)"
    ``` typescript
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
## Configuration Parameters

### `required`

| `required`      |                 |
| :-------------- | :-------------- |
| Possible Values | `true`, `false` |
| Required        | no              |
| Default Value   | `false`         |

If `required` is set to `true`, the field is considered invalid as long as no value is entered.

=== "Example"
    ``` typescript
    required: true
    ```

---
### `disabled`

| `disabled`      |                 |
| :-------------- | :-------------- |
| Possible Values | `true`, `false` |
| Required        | no              |
| Default Value   | `false`         |

If `disabled` is set to `true`, the field is permanently disabled in the UI. It can still be modified during initial prefilling or dynamic field actions but directly modifying the value in the UI is not possible.

=== "Example"
    ``` typescript
    disabled: true
    ```

---
### `placeHolderText`

| `placeHolderText` |                            |
| :---------------- | :------------------------- |
| Possible Values   | [MultiLanguageText](#todo) |
| Required          | no                         |
| Default Value     | `undefined` in which case `label.text` is used as fallback |

Placeholder text that is shown in the UI when the field is focused but does not have a value. 

Important: If the field is not focused and does not have a value, `label.text` is shown instead.

=== "Example"
    ``` typescript
    placeHolderText: {
        en: 'Example Placeholder',
        de: 'Example Placeholder [DE]',
        tr: 'Example Placeholder [TR]',
        fr: 'Example Placeholder [FR]',
        es: 'Example Placeholder [ES]',
        it: 'Example Placeholder [IT]',
    }
    ```

---
### `pdfHideAll`

| `pdfHideAll`      |                 |
| :-------------- | :-------------- |
| Possible Values | `true`, `false` |
| Required        | no              |
| Default Value   | `false`         |

If `pdfHideAll` is set to `true`, the field is not shown in the PDF at all. This takes precedence over `pdfHideAllIfValueIsEmpty`.

=== "Example"
    ``` typescript
    pdfHideAll: true
    ```

---
### `pdfHideAllIfValueIsEmpty`

| `pdfHideAllIfValueIsEmpty` |                 |
| :------------------------- | :-------------- |
| Possible Values            | `true`, `false` |
| Required                   | no              |
| Default Value              | `false`         |

If `pdfHideAllIfValueIsEmpty` is set to `true` and the field value is empty, the field is not shown in the PDF at all.
If the field value is not empty, the field will still be shown (unless `pdfHideAll` is not set to `true`). 

=== "Example"
    ``` typescript
    pdfHideAllIfValueIsEmpty: true
    ```

---
### `label`

| Property                                              | Description                       |
| :---------------------------------------------------- | :-------------------------------- |
| [text](#labeltext)                                    | Localized label text of the field. Shown in the UI and the PDF. |
| [uiHide](#labeluihide)                                | Setting this to `true` hides the label in the UI. |
| [pdfHide](#labelpdfhide)                              | Setting this to `true` hides the label in the PDF. |
| [pdfTextColor](#labelpdftextcolor)                    | Text color of the label in the PDF. |
| [pdfTextSize](#labelpdftextsize)                      | Text size of the label in the PDF. |

---
#### `label.text`

| `text` |                                       |
| :---------------- | :------------------------- |
| Possible Values   | [MultiLanguageText](#todo) |
| Required          | yes                        |

Label text that is shown in the UI and the PDF to identify the field. 

=== "Example"
    ``` typescript
    text: {
        en: 'Example Placeholder',
        de: 'Example Placeholder [DE]',
        tr: 'Example Placeholder [TR]',
        fr: 'Example Placeholder [FR]',
        es: 'Example Placeholder [ES]',
        it: 'Example Placeholder [IT]',
    }
    ```

---
#### `label.uiHide`

| `uiHide`       |                 |
| :-------------- | :-------------- |
| Possible Values | `true`, `false` |
| Required        | no              |
| Default Value   | `false`         |

If `uiHide` is set to `true`, the label is not shown in the UI.

=== "Example"
    ``` typescript
    uiHide: true
    ```

---
#### `label.pdfHide`

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
#### `label.pdfTextColor`

| `pdfTextColor`  |                 |
| :-------------- | :-------------- |
| Possible Values | Hex-Color-Code  |
| Required        | no              |
| Default Value   | `#000000`       |

By setting `pdfTextColor`, the field label will show up in the PDF having the defined color.

=== "Example"
    ``` typescript
    pdfTextColor: true
    ```

---
#### `label.pdfTextSize`

| `pdfTextSize`   |                  |
| :-------------- | :-------------- |
| Possible Values | Integer > 0     |
| Required        | no              |
| Default Value   | 9               |

By setting `pdfTextSize`, the field label will show up in the PDF having the defined text size in pixels.

=== "Example"
    ``` typescript
    pdfTextSize: 20
    ```

---
### `value`

| Property                                              | Description                       |
| :---------------------------------------------------- | :-------------------------------- |
| [text](#valuetext)                                    | Localized value text of the field. Shown in the UI and the PDF. |
| [pdfStartInNewLine](#valuepdfstartinnewline)          | Setting this to `true` will show the field value in the PDF in a separate line below the label. |
| [pdfHide](#valuepdfhide)                              | Setting this to `true` hides the value in the PDF. |
| [pdfTextColor](#valuepdftextcolor)                    | Text color of the value in the PDF. |
| [pdfTextSize](#valuepdftextsize)                      | Text size of the value in the PDF. |
| [uiMaxRows](#valueuimaxrows)                          | Maximum number of lines that can be seen in the UI without scrolling. |
| [uiMinRows](#valueuiminrows)                          | Minimum number of lines that are shown in the UI. |
| [validators.maxCharacters](#valuevalidatorsmaxcharacters) | Maximum number of characters for the input value to be valid. |
| [validators.minCharacters](#valuevalidatorsmincharacters) | Minimum number of characters for the input value to be valid. |

---
#### `value.pdfStartInNewLine`

| `pdfStartInNewLine`       |                 |
| :-------------- | :-------------- |
| Possible Values | `true`, `false` |
| Required        | no              |
| Default Value   | `false`         |

If `pdfStartInNewLine` is set to `true`, the value of the field will be shown in the PDF on a new line below the label. If the value is `false`, the value is shown on the same line as the label.

=== "Example"
    ``` typescript
    pdfStartInNewLine: true
    ```

---
#### `value.pdfHide`

| `pdfHide`       |                 |
| :-------------- | :-------------- |
| Possible Values | `true`, `false` |
| Required        | no              |
| Default Value   | `false`         |

If `pdfHide` is set to `true`, the value is not shown in the PDF.

=== "Example"
    ``` typescript
    pdfHide: true
    ```

---
#### `value.pdfTextColor`

| `pdfTextColor`  |                 |
| :-------------- | :-------------- |
| Possible Values | Hex-Color-Code  |
| Required        | no              |
| Default Value   | `#000000`       |

By setting `pdfTextColor`, the field value will show up in the PDF having the defined color.

=== "Example"
    ``` typescript
    pdfTextColor: true
    ```

---
#### `value.pdfTextSize`

| `pdfTextSize`   |                  |
| :-------------- | :-------------- |
| Possible Values | Integer > 0     |
| Required        | no              |
| Default Value   | 9               |

By setting `pdfTextSize`, the field value will show up in the PDF having the defined text size in pixels.

=== "Example"
    ``` typescript
    pdfTextSize: 20
    ```

---
#### `value.uiMaxRows`

| `uiMaxRows`     |                 |
| :-------------- | :-------------- |
| Possible Values | Integer > 1     |
| Required        | no              |
| Default Value   | 10              |

By setting `uiMaxRows`, the text input in he UI will not grow further than the specified amount of lines.
If the content spans more lines than that maximum, there will be a scrollbar to access the additional lines.

=== "Example"
    ``` typescript
    uiMaxRows: 15
    ```

---
#### `value.uiMinRows`

| `uiMinRows`     |                 |
| :-------------- | :-------------- |
| Possible Values | Integer > 1     |
| Required        | no              |
| Default Value   | 1               |

By setting `uiMinRows`, the text input in he UI will always span at the least the configured amount of lines.
If the content spans less lines, the size of the text input will not shrink further.

=== "Example"
    ``` typescript
    uiMinRows: 5
    ```

---
#### `value.validators.maxCharacters`

| `uiMinRows`     |                 |
| :-------------- | :-------------- |
| Possible Values | Integer > 1     |
| Required        | no              |
| Default Value   | -               |

By setting `validators.maxCharacters`, the field will be marked as invalid if the value contains more characters than the specified number.

=== "Example"
    ``` typescript
    validators: {
        maxCharacters: 100
    }
    ```

---
#### `value.validators.minCharacters`

| `uiMinRows`     |                 |
| :-------------- | :-------------- |
| Possible Values | Integer > 1     |
| Required        | no              |
| Default Value   | -               |

By setting `validators.minCharacters`, the field will be marked as invalid if the value contains less characters than the specified number.

=== "Example"
    ``` typescript
    validators: {
        minCharacters: 10
    }
    ```

---
### `prefill`

| `prefill`                  |                                                                     |
| :------------------------- | :--------------                                                     |
| Possible Values            | Array of [PrefillRules](#todo) that output a value of type `string` |
| Required                   | no                                                                  |
| Default Value              | -                                                                   |

This configuration follows the [general syntax for prefilling rules](#todo).
The provided PrefillRules need to have an output value of type string.

=== "Example (static string)"
    ``` typescript
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

=== "Example (asset type name)"
    ``` typescript
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
