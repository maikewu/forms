---
title: Repeating fields
category: 635ce1e7775bc60045570ffb
parentDoc: 635ce486ae5fac003cef279e
---

On this page you will find a list of repeating fields.


---
# Configuration Overview

| Property                                           | Description                                                                                             |
| :--------------------------------------------------| :-------------------------------------------------------------------------------------------------------|
| [required](#required)                              | If this is set to `true`, the field is considered invalid as long as no value is entered.               |
| [disabled](#disabled)                              | Setting this to `true` permanently disables the field in the UI.                                        |
| [pdfHide](#pdfhide)                                | Setting this to `true` hides the whole field in the PDF.                                                |
| [pdfHideIfValueIsEmpty](#pdfhideifvalueisempty)    | Setting this to `true` hides the whole field in the PDF in case the field value is empty.               |
| [pdfWidth](#pdfwidth)                              | Configuration of the width of the field.                                                                |
| [placeHolderText](#placeholdertext)                | Localized placeholder text that is shown in the UI when the field is focused but does not have a value. |
| [pdfTextSize](#pdftextsize)                        | Text size of a certain field in the PDF.                                                                |
| [pdfTextColor](#pdftextcolor)                      | Text color of a certain field in the PDF.                                                               |
| [text](#text)                                      | Localized text of the field. Shown in the UI and the PDF.                                               |
| [uiHide](#uihide)                                  | Setting this to `true` hides the field in the UI.                                                       |
| [requiredAmountOfEntries](#requiredamountofentries)| Specify how many repeating entries are required to fill the form.                  |                                                                             |
| [label](#lable)                                    | Several configurations for the label.                                                                 |
| [values](#value)                                  | Several configurations for the values.                                                                 |
| [prefill](#prefill)                                | Configuration to prefill the field with a value upon creation of the form instance.                     |
| [onChange](#onchange)                                                        | Configuration to change the field with a certain value when pre defined event get executed |
| [fields](#fields)                                  | Components of the field |


---
# Configuration Parameters

## `required`

| `required`      |                                         |
| :-------------- | :-------------------------------------- |
| Possible Values | `true`, `false`                         |
| Required        | no                                      |
| Default Value   | `false`                                 |

If `required` is set to `true`, the field is considered invalid as long as no value is entered.

```json
"required": true
```

---
## `disabled`

| `disabled`      |                 |
| :-------------- | :-------------- |
| Possible Values | `true`, `false` |
| Required        | no              |
| Default Value   | `false`         |

If `disabled` is set to `true`, the field is permanently disabled in the UI. It can still be modified during initial prefilling or dynamic field actions but directly modifying the value in the UI is not possible.

```json
"disabled": true
```

---
## `pdfHide`

| `pdfHide`      |                 |
| :-------------- | :-------------- |
| Possible Values | `true`, `false` |
| Required        | no              |
| Default Value   | `false`         |

If `pdfHide` is set to `true`, the field is not shown in the PDF at all. This takes precedence over `pdfHideIfValueIsEmpty`.

```json
"pdfHide": true
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

```json
pdfHideIfValueIsEmpty: true
```

---
## `pdfWidth`

| `pdfWidth`                 |                           |
| :------------------------- | :-------------------------|
| Possible Values            | Values between `0` - `1`  |
| Required                   | no                        |
| Default Value              | `1 (full width)`          |

The value of `pdfWidth` defines the width of a field in the pdf layout.
`1` represent the full row in the pdf, e.g. `0.5` represent the half row / 50 % of the row.

```json
"pdfWidth": 0.5
```

---
## `placeHolderText`

| `placeHolderText` |                            |
| :---------------- | :------------------------- |
| Possible Values   | [MultiLanguageText](#multilanguagetext) |
| Required          | no                         |
| Default Value     | `undefined` in which case `label.text` is used as fallback |

Placeholder text that is shown in the UI when the field is focused but does not have a value. 

Important: If the field is not focused and does not have a value, `label.text` is shown instead.

```json
"placeHolderText": {
    "en": "Example Placeholder",
    "de": "Platzhalter",
    "tr": "Example Placeholder [TR]",
    "fr": "Example Placeholder [FR]",
    "es": "Example Placeholder [ES]",
    "it": "Example Placeholder [IT]",
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

```json
"pdfTextSize": 20
```

---
## `pdfTextColor`

| `pdfTextColor`  |                 |
| :-------------- | :-------------- |
| Possible Values | Hex-Color-Code  |
| Required        | no              |
| Default Value   | `#000000`       |

By setting `pdfTextColor`, the field label in the PDF will have the defined color.

```json
"pdfTextColor": "#F1F8F1"
```

---
## `text`

| `text` |                                       |
| :---------------- | :------------------------- |
| Possible Values   | [MultiLanguageText](#multilanguagetext) |
| Required          | yes                        |

Label text that is shown in the UI and the PDF to identify the field. 

```json
"text": {
    "en": "Example Text",
    "de": "Platzhalter",
    "tr": "Example Text [TR]",
    "fr": "Example Text [FR]",
    "es": "Example Text [ES]",
    "it": "Example Text [IT]",
}
```

## `uiHide`

| `uiHide`       |                 |
| :-------------- | :-------------- |
| Possible Values | `true`, `false` |
| Required        | no              |
| Default Value   | `false`         |

If `uiHide` is set to `true`, the label is not shown in the UI.

```json
"uiHide": true
```

---

## `requiredAmountOfEntries`


| `requiredAmountOfEntries`  |                 |
| :--------------------------| :-------------- |
| Possible Values            | Integer >= `0`  |
| Required                   | no              |
| Default Value              | `0`             |

By setting `requiredAmountOfEntries`, it specify how many repeating entries are required to fill the form.

```json
"requiredAmountOfEntries": 3,
```

---
## `MultiLanguageText`

| `MultiLanguageText` |                        |
| :------------------ | :--------------------- |
| Possible Values     | en, de, tr, fr, es, it |
| Required            | no                     |

 Allows to display text in the pdf in different languages.

```json
{
 "en": "Example MultiLanguageText",
 "de": "Beispiel Mehrfachsprachen Text",
 "tr": "Example MultiLanguageText [TR]",
 "fr": "Example MultiLanguageText [FR]",
 "es": "Example MultiLanguageText [ES]",
 "it": "Example MultiLanguageText [IT]",
}
```

---
## `label`

| Property                                         | Description                       |
| :------------------------------------------------| :-------------------------------- |
| [text](#text)                                    | Localized label text of the field. Shown in the UI and the PDF. |
| [uiHide](#uihide)                                | Setting this to `true` hides the label in the UI. |
| [pdfHide](#pdfhide)                              | Setting this to `true` hides the label in the PDF. |
| [pdfTextSize](#pdftextsize)                      | Text size of the label in the PDF. |
| [pdfTextColor](#pdftextcolor)                    | Text color of the label in the PDF. |

---
## `value`

| Property                                                  | Description                                                                                     |
| :-------------------------------------------------------- | :---------------------------------------------------------------------------------------------- |
| [pdfHide](#pdfhide)                                       | Setting this to `true` hides the label in the PDF. |
| [pdfTextSize](#pdftextsize)                               | Text size of the label in the PDF. |
| [pdfTextColor](#pdftextcolor)                             | Text color of the label in the PDF. |
| [pdfStartInNewLine](#pdfstartinnewline)                   | Setting this to `true` will show the field value in the PDF in a separate line below the label. |
| [pdfAddLineBreak](#pdfaddlinebreak)                       | Setting this to `true` will add a linebreak in the PDF. |
| [validators.maxCharacters](#validatorsmaxcharacters)      | Maximum number of characters for the input value to be valid. |
| [validators.minCharacters](#validatorsmincharacters)      | Minimum number of characters for the input value to be valid. |
| [validators.regex](#validatorsregex)                      | Allowing only specific characters as inputs. |
| [disableCreation](#disablecreation)                       | Hides the create button, so that no new companies can be created. |
| [disableAssetFormInstanceRelationship](#disableAssetFormInstanceRelationship) | Setting this to `true` will unlink the form from the asset detail pages |

---
### `pdfStartInNewLine`

| `pdfStartInNewLine` |                 |
| :------------------------- | :-------------- |
| Possible Values            | `true`, `false` |
| Required                   | no              |
| Default Value              | ``               |

If `pdfStartInNewLine` is set to `true`, the field value starts below the field label in the PDF.

```json
"pdfStartInNewLine": true,
```

---
### `pdfAddLineBreaks`

| `pdfAddLineBreaks` |                 |
| :------------------------- | :-------------- |
| Possible Values            | `true`, `false` |
| Required                   | no              |
| Default Value              | -               |

If `pdfAddLineBreaks` is set to `true`, a linebreak is set after every value of the field in the PDF.

```json
"pdfAddLineBreaks": true,
```

---
### `validators.minCharacters`

| `validators.minCharacters`     |                 |
| :-------------- | :-------------- |
| Possible Values | Integer > 1     |
| Required        | no              |
| Default Value   | -               |

By setting `validators.minCharacters`, the field will be marked as invalid if the value contains less characters than the specified number.

```json
"validators": {
    "minCharacters": 10
}
```

---
### `validators.maxCharacters`

| `validators.maxCharacters`     |                 |
| :-------------- | :-------------- |
| Possible Values | Integer > 1     |
| Required        | no              |
| Default Value   | -               |

By setting `validators.maxCharacters`, the field will be marked as invalid if the value contains more characters than the specified number.

```json
"validators": {
    "maxCharacters": 100
}
```

---
### `validators.regex`

| `validators.regex`     |                 |
| :-------------- | :-------------- |
| Possible Values | regex pattern   |
| Required        | no              |
| Default Value   | -               |

By setting `validators.regex`, the field will be marked as invalid if the value contains other characters than allowed.

| Regex patterns    |                                    |
| :---------------- | :--------------------------------- |
| `^[A-Z]*$ `         | Only upper case letters            |
| `^[0-9]+$`         | Only numbers incl. 0          |
| `^[A-Za-z]*$`       | Only upper and lower case letters  |
| `^[-,0-9]+$`     | Only numbers and comma |
| `^[-,0-9]+[.]([-,0-9]{1,2})?$` | Only numbers and dot, limit to 2 digit after dot - Use for e.g. currency entries |

[Cheat Sheet](https://cheatography.com/davechild/cheat-sheets/regular-expressions/)

```json
"validators": {
    "regex": {
        "pattern": "^[A-Z]*$",
        "errorText": {
            "de": " ",
            "en": " "
        }
  }
}
```
---
## `fields`

| Property                                         | Description                       |
| :------------------------------------------------| :-------------------------------- |
| [commentMultiLineTextInput](#commenmultilinetextinput)        | Defines a comment section as multiLineTextInput  |


---
### `commentMultiLineTextInput`

| Property               | Description                                                                               |
| :----------------------| :---------------------------------------------------------------------------------------- |
| [required](./24-general-properties/#required)                                | If this is set to `true`, the field is considered invalid as long as no value is entered. |
| [disabled](./24-general-properties/#disabled)                                | Setting this to `true` permanently disables the field in the UI. |
| [pdfHide](./24-general-properties/#pdfhide)                                  | Setting this to `true` hides the label in the PDF. |

---

#### `enable`

| `enable` |                 |
| :------------------------- | :-------------- |
| Possible Values            | `true`, `false` |
| Required                   | yes              |
| Default Value              | -               |

If `enable` is set to `true`, the sub-property appears in the UI. 

```json
 "enable": true

```
---
### `disableCreation`

| `disableCreation` |                 |
| :---------------- | :-------------- |
| Possible Values   | `true`, `false` |
| Required          | no              |
| Default Value     | `false`         |

If `disableCreation` is set to `true`, the create button is hidden, so that no new companies can be created while working in forms.

```json
"disableCreation": true
```
---
### `disableAssetFormInstanceRelationship`

| `disableAssetFormInstanceRelationship` |                 |
| :---------------- | :-------------- |
| Possible Values   | `true`, `false` |
| Required          | no              |
| Default Value     | `false`         |

If `disableAssetFormInstanceRelationship` is set to `true`, the form will not be linked to the asset(s) and therefore not be shown in the asset detail page(s).

```json
"disableAssetFormInstanceRelationship": true
```

---
## `prefill`

| `prefill`                  |                                                                     |
| :------------------------- | :--------------                                                     |
| Possible Values            | Array of [PrefillRules](./25-prefill-rules)            |
| Required                   | no                                                                  |
| Default Value              | -                                                                   |

This configuration follows the [general syntax for prefilling rules](./25-prefill-rules).

---
## `onChange`

| `onChange`                 |                                                                        |
| :------------------------- | :--------------                                                        |
| Possible Values            | Array of [DynamicFieldActions](./26-on-change-rules) |
| Required                   | no                                                                     |
| Default Value              | -                                                                      |


This configuration follows the [general syntax for dynamic field actions](./26-on-change-rules).
