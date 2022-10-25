---
title: TimeInput
category: 62ebf4654ae80e09e468624b
parentDoc: 62ec01bd561bab0aa775efe4
---


The TimeInput field allows to enter a time.

# Configuration Overview

| Property                                                                     | Description                      |
| :--------------------------------------------------------------------------- | :--------------------------------|
| [required](./24-general-properties/#required)                                | If this is set to `true`, the field is considered invalid as long as no value is entered. |
| [disabled](./24-general-properties/#disabled)                                | Setting this to `true` permanently disables the field in the UI. |
| [pdfHide](./24-general-properties/#pdfhide)                                  | Setting this to `true` hides the whole field in the PDF. |
| [pdfHideIfValueIsEmpty](./24-general-properties/#pdfhideifvalueisempty)      | Setting this to `true` hides the whole field in the PDF in case the field value is empty. |
| [pdfWidth](./24-general-properties/#pdfwidth)                                | Configuration of the width of the field. |
| [label](#label)                                                              | Configuration of the field label. |
| [value](#value)                                                              | Configuration of the field value. |
| [prefill](#prefill)                                                          | Configuration to prefill the field with a value upon creation of the form instance. |
| [onChange](#onchange)                                                        | Configuration to change the field with a certain value when pre defined event get executed |

``` JSON (complete)
{
    "id": "exampleTimeInput_1",
    "type": "timeInput",
    "config": {
        "pdfHide": false,
        "disabled": false,
        "required": false,
        "pdfWidth": 1,
        "pdfHideIfValueIsEmpty": false,
        "label": {
            "text": {
                "en": "Time input 1",
                "de": "Time input 1 [DE]",
                "tr": "Time input 1 [TR]",
                "fr": "Time input 1 [FR]",
                "es": "Time input 1 [ES]",
                "it": "Time input 1 [IT]"
            },
            "uiHide": false,
            "pdfHide": false,
            "pdfTextSize": 14,
            "pdfTextColor": "#facc2e"
        },
        "value": {
            "dropdownInterval": 30,
            "pdfHide": false,
            "pdfTextSize": 14,
            "pdfTextColor": "#facc2e",
            "pdfStartInNewLine": false
        },
        "prefill": {
            "value": [{
                "input": "none",
                "steps": [[
                    "staticTime",
                    "22:22"
                ]]
            }]
        }
    }
},
```

``` JSON (minimal)
{
    "id": "exampleTimeInput_1",
    "type": "timeInput",
    "config": {
        "label": {
            "text": {
                "en": "Time input 1",
                "de": "Time input 1 [DE]",
                "tr": "Time input 1 [TR]",
                "fr": "Time input 1 [FR]",
                "es": "Time input 1 [ES]",
                "it": "Time input 1 [IT]"
            },
        },
        "value": {
        },
    }
},
```

---
# Configuration Parameters

## `label`

| Property                                                    | Description                       |
| :---------------------------------------------------------- | :-------------------------------- |
| [text](./24-general-properties/#text)                       | Localized label text of the field. Shown in the UI and the PDF. |
| [uiHide](./24-general-properties/#uihide)                   | Setting this to `true` hides the label in the UI. |
| [pdfHide](./24-general-properties/#pdfhide)                 | Setting this to `true` hides the label in the PDF. |
| [pdfTextSize](./24-general-properties/#pdftextsize)         | Text size of the label in the PDF. |
| [pdfTextColor](./24-general-properties/#pdftextcolor)       | Text color of the label in the PDF. |

---
## `value`

| Property                                                                        | Description                                                                                     |
| :------------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------- |
| [pdfHide](./24-general-properties/#pdfhide)                                     | Setting this to `true` hides the label in the PDF. |
| [pdfTextSize](./24-general-properties/#pdftextsize)                             | Text size of the label in the PDF. |
| [pdfTextColor](./24-general-properties/#pdftextcolor)                           | Text color of the label in the PDF. |
| [pdfStartInNewLine](./24-general-properties/#pdfstartinnewline)                 | Setting this to `true` will show the field value in the PDF in a separate line below the label. |
| [dropdownInterval](#dropdowninterval)                                           | Defines interval between dropdown values in minutes. |

---
### `dropDownInterval`

| `dropDownInterval`     |                 |
| :-------------- | :-------------- |
| Possible Values | `1`,`5`,`6`,`15`,`30`,`60`     |
| Required        | no              |
| Default Value   | `1`               |

`dropDownInterval` defines an interval between dropdown values in minutes.

```JSON
"dropDownInterval": 6
```
---
## `prefill`

| `prefill`                  |                                                                     |
| :------------------------- | :--------------                                                     |
| Possible Values            | Array of [PrefillRules](./25-prefill-rules)            |
| Required                   | no                                                                  |
| Default Value              | -                                                                   |

This configuration follows the [general syntax for prefilling rules](./25-prefill-rules).
``` JSON (static time)
"prefill": {
    "value": [{
        "input": "none",
        "steps": [[
            "staticTime",
            "22:22"
        ]]
    }]
}
```
---
## `onChange`

| `onChange`                 |                                                                        |
| :------------------------- | :--------------                                                        |
| Possible Values            | Array of [DynamicFieldActions](./26-on-change-rules) |
| Required                   | no                                                                     |
| Default Value              | -                                                                      |


This configuration follows the [general syntax for dynamic field actions](./26-on-change-rules).

