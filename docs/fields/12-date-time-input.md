---
title: DateTimeInput
category: 635ce1e7775bc60045570ffb
parentDoc: 635ce486ae5fac003cef279e
---


The dateTimeInput field allows to enter a datetime.

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

```json (complete)
{
    "id": "exampleDateTimeInput_1",
    "type": "dateTimeInput",
    "config": {
        "pdfHide": false,
        "disabled": false,
        "required": false,
        "pdfWidth": 1,
        "pdfHideIfValueIsEmpty": false,
        "label": {
            "text": {
                "en": "Date time input 1",
                "de": "Date time input 1 [DE]",
                "tr": "Date time input 1 [TR]",
                "fr": "Date time input 1 [FR]",
                "es": "Date time input 1 [ES]",
                "it": "Date time input 1 [IT]"
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
            "pdfStartInNewLine": false,
            "autofill": ""
        },
        "prefill": {
            "value": [{
                "input": "none",
                "steps": [[
                    "staticDateTime",
                    "2022-02-22T22:22:00.000Z_Europe/Berlin"
                ]]
            }]
        }
    }
},
```

```json (minimal)
{
    "id": "exampleDateTimeInput_1",
    "type": "dateTimeInput",
    "config": {
        "label": {
            "text": {
                "en": "Date time input 1",
                "de": "Date time input 1 [DE]",
                "tr": "Date time input 1 [TR]",
                "fr": "Date time input 1 [FR]",
                "es": "Date time input 1 [ES]",
                "it": "Date time input 1 [IT]"
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
| autofill | Setting this to `always` will update the field with the current date and time every time the form is opened, regardless of the field being changed previously. Setting this to `only-empty` will autofill the current date and time only if field is empty |

---
### `dropDownInterval`

| `dropDownInterval`     |                 |
| :-------------- | :-------------- |
| Possible Values | `1`,`5`,`6`,`15`,`30`,`60`     |
| Required        | no              |
| Default Value   | `1`               |

`dropDownInterval` defines an interval between dropdown values in minutes.

```json
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
```json (static time)
"prefill": {
    "value": [{
        "input": "none",
        "steps": [[
            "staticDateTime",
            "2022-02-22T22:22:00.000Z_Europe/Berlin"
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

