---
title: BooleanInput
category: 635ce1e7775bc60045570ffb
parentDoc: 635ce486ae5fac003cef279e
---

The booleanInput allows the user to mark a checkbox true or false.
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
    "id": "exampleBooleanInput_1",
    "type": "booleanInput",
    "config": {
        "required": true,
        "disabled": false,
        "pdfHide": false,
        "pdfHideIfValueIsEmpty": false,
        "pdfWidth": 1,
        "label": {
            "pdfHide": false,
            "pdfTextColor": "#facc2e",
            "pdfTextSize": 14,
            "text": {
                "en": "Boolean input 1",
                "de": "Boolean input 1 [DE]",
                "tr": "Boolean input 1 [TR]",
                "fr": "Boolean input 1 [FR]",
                "es": "Boolean input 1 [ES]",
                "it": "Boolean input 1 [IT]"
            }
        },
        "prefill": {
            "value": [{
                "input": "none",
                "steps": [[
                    "staticBoolean",
                    true
                ]]
            }]
        }
    }
},
```
```json (minimal)
{
    "id": "exampleBooleanInput_1",
    "type": "booleanInput",
    "config": {
        "label": {
            "text": {
                "en": "Boolean input 1",
                "de": "Boolean input 1 [DE]",
                "tr": "Boolean input 1 [TR]",
                "fr": "Boolean input 1 [FR]",
                "es": "Boolean input 1 [ES]",
                "it": "Boolean input 1 [IT]"
            }
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
| [pdfHide](./24-general-properties/#pdfhide)                 | Setting this to `true` hides the label in the PDF. |
| [pdfTextSize](./24-general-properties/#pdftextsize)         | Text size of the label in the PDF. |
| [pdfTextColor](./24-general-properties/#pdftextcolor)       | Text color of the label in the PDF. |

---

## `prefill`

| `prefill`                  |                                                                     |
| :------------------------- | :--------------                                                     |
| Possible Values            | Array of [PrefillRules](./25-prefill-rules)            |
| Required                   | no                                                                  |
| Default Value              | -                                                                   |

This configuration follows the [general syntax for prefilling rules](./25-prefill-rules).
```json (static boolean)
"prefill": {
    "value": [{
        "input": "none",
        "steps": [[
            "staticBoolean",
            true
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

