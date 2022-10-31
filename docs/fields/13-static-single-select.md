---
title: StaticSingleSelect
category: 635ce1e7775bc60045570ffb
parentDoc: 635ce486ae5fac003cef279e
---


The StaticSingleSelect field allows to choose one option of the dropdown.

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
    "id": "exampleStaticSingleSelect_1",
    "type": "staticSingleSelect",
    "config": {
        "required": true,
        "disabled": false,
        "pdfHide": false,
        "pdfHideIfValueIsEmpty": false,
        "pdfWidth": 1,
        "label": {
            "text": {
                "en": "Static Single Select 1",
                "de": "Static Single Select 1 [DE]",
                "tr": "Static Single Select 1 [TR]",
                "fr": "Static Single Select 1 [FR]",
                "es": "Static Single Select 1 [ES]",
                "it": "Static Single Select 1 [IT]"
            },
            "pdfHide": false,
            "pdfTextColor": "#facc2e",
            "pdfTextSize": 14,
            "uiHide": false
        },
        "value": {
            "options": {
                "exampleOptionOne": {
                    "en": "Example option 1",
                    "de": "Example option 1 [DE]",
                    "tr": "Example option 1 [TR]",
                    "fr": "Example option 1 [FR]",
                    "es": "Example option 1 [ES]",
                    "it": "Example option 1 [IT]"
                },
                "exampleOptionTwo": {
                    "en": "Example option 2",
                    "de": "Example option 2 [DE]",
                    "tr": "Example option 2 [TR]",
                    "fr": "Example option 2 [FR]",
                    "es": "Example option 2 [ES]",
                    "it": "Example option 2 [IT]"
                }
            },
            "pdfHide": false,
            "pdfStartInNewLine": false,
            "pdfTextColor": "#facc2e",
            "pdfTextSize": 14
        },
        "prefill": {
            "value": [{
                "input": "none",
                "steps": [[
                    "staticString",
                    "exampleOptionOne"
                ]]
            }]
        }
    }
},
```
```json (minimal)
 {
    "id": "exampleStaticSingleSelect_1",
    "type": "staticSingleSelect",
    "config": {
        "label": {
            "text": {
                "en": "Static Single Select 1",
                "de": "Static Single Select 1 [DE]",
                "tr": "Static Single Select 1 [TR]",
                "fr": "Static Single Select 1 [FR]",
                "es": "Static Single Select 1 [ES]",
                "it": "Static Single Select 1 [IT]"
            },
        },
        "value": {
            "options": {
                "exampleOptionOne": {
                    "en": "Example option 1",
                    "de": "Example option 1 [DE]",
                    "tr": "Example option 1 [TR]",
                    "fr": "Example option 1 [FR]",
                    "es": "Example option 1 [ES]",
                    "it": "Example option 1 [IT]"
                },
                "exampleOptionTwo": {
                    "en": "Example option 2",
                    "de": "Example option 2 [DE]",
                    "tr": "Example option 2 [TR]",
                    "fr": "Example option 2 [FR]",
                    "es": "Example option 2 [ES]",
                    "it": "Example option 2 [IT]"
                }
            },
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
| [options](#options)                                                             | Defines options that will appear in the dropdown |


---
### `options`

| `options`       |                 |
| :-------------- | :-------------- |
| Possible Values | MultiLanguageText   |
| Required        | yes              |
| Default Value   | -             |

In `options` the content of the dropdown can be defined.

```json
"options": {
    "exampleOptionOne": {
        "en": "Example option 1",
        "de": "Example option 1 [DE]",
        "tr": "Example option 1 [TR]",
        "fr": "Example option 1 [FR]",
        "es": "Example option 1 [ES]",
        "it": "Example option 1 [IT]"
    },
    "exampleOptionTwo": {
        "en": "Example option 2",
        "de": "Example option 2 [DE]",
        "tr": "Example option 2 [TR]",
        "fr": "Example option 2 [FR]",
        "es": "Example option 2 [ES]",
        "it": "Example option 2 [IT]"
    }
},
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
            "staticString",
            "exampleOptionOne"
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

