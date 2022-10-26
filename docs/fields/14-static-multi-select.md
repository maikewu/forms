---
title: StaticMultiSelect
category: 62ebf4654ae80e09e468624b
parentDoc: 62ec01bd561bab0aa775efe4
---


The StaticMultiSelect field allows to choose one or more options of the dropdown.

# Configuration Overview

| Property                                                                     | Description                      |
| :--------------------------------------------------------------------------- | :--------------------------------|
| [required](./24-general-properties/#required)                                | If this is set to `true`, the field is considered invalid as long as no value is entered. |
| [disabled](./24-general-properties/#disabled)                                | Setting this to `true` permanently disables the field in the UI. |
| [pdfHide](./24-general-properties/#pdfhide)                                  | Setting this to `true` hides the whole field in the PDF. |
| [pdfHideIfValueIsEmpty](./24-general-properties/#pdfhideifvalueisempty)      | Setting this to `true` hides the whole field in the PDF in case the field value is empty. |
| [pdfWidth](./24-general-properties/#pdfwidth)                                | Configuration of the width of the field. |
| [minAmountOfSelections](#minamountofselections)                              | Sets the minimum of selected options |
| [maxAmountOfSelections](#maxamountofselections)                              | Sets the maximum of selected options |
| [label](#label)                                                              | Configuration of the field label. |
| [value](#value)                                                              | Configuration of the field value. |
| [prefill](#prefill)                                                          | Configuration to prefill the field with a value upon creation of the form instance. |
| [onChange](#onchange)                                                        | Configuration to change the field with a certain value when pre defined event get executed |

``` JSON (complete)
{
    "id": "exampleStaticMultiSelect_1",
    "type": "staticMultiSelect",
    "config": {
        "disabled": false,
        "pdfHide": false,
        "pdfWidth": 1,
        "pdfHideIfValueIsEmpty": false,
        "minAmountOfSelections": 2,
        "maxAmountOfSelections": 3,        
        "label": {
            "text": {
                "en": "Static Multi Select 1",
                "de": "Static Multi Select 1 [DE]",
                "tr": "Static Multi Select 1 [TR]",
                "fr": "Static Multi Select 1 [FR]",
                "es": "Static Multi Select 1 [ES]",
                "it": "Static Multi Select 1 [IT]"
            },
            "pdfHide": false,
            "pdfTextColor": "#facc2e",
            "pdfTextSize": 14,
            "uiHide": false
        },
        "value": {
            "pdfHide": false,
            "pdfStartInNewLine": false,
            "pdfTextColor": "#facc2e",
            "pdfTextSize": 14,
            "pdfAddLineBreaks": true,
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
                },
                "exampleOptionThree": {
                    "en": "Example option 3",
                    "de": "Example option 3 [DE]",
                    "tr": "Example option 3 [TR]",
                    "fr": "Example option 3 [FR]",
                    "es": "Example option 3 [ES]",
                    "it": "Example option 3 [IT]"
                }
            },
        },
        "prefill": {
            "value": [{
                "input": "none",
                "steps": [[
                    "staticStringArray",
                    [
                    "exampleOptionOne",
                    "exampleOptionTwo"
                    ]
                ]]
            }]
        }
    }
},
```
``` JSON (minimal)
{
    "id": "exampleStaticMultiSelect_1",
    "type": "staticMultiSelect",
    "config": {        
        "label": {
            "text": {
                "en": "Static Multi Select 1",
                "de": "Static Multi Select 1 [DE]",
                "tr": "Static Multi Select 1 [TR]",
                "fr": "Static Multi Select 1 [FR]",
                "es": "Static Multi Select 1 [ES]",
                "it": "Static Multi Select 1 [IT]"
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
                },
                "exampleOptionThree": {
                    "en": "Example option 3",
                    "de": "Example option 3 [DE]",
                    "tr": "Example option 3 [TR]",
                    "fr": "Example option 3 [FR]",
                    "es": "Example option 3 [ES]",
                    "it": "Example option 3 [IT]"
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
| [pdfAddLineBreaks](./24-general-properties/#pdfaddlinebreaks)                   | Setting this to `true` will add a linebreak in the PDF. |
| [options](#options)                                                             | Defines options that will appear in the dropdown |


---
### `options`

| `options`       |                 |
| :-------------- | :-------------- |
| Possible Values | `MultiLanguageText`   |
| Required        | yes              |
| Default Value   | -             |

In `options` the content of the dropdown can be defined.

```JSON
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
    },
    "exampleOptionThree": {
        "en": "Example option 3",
        "de": "Example option 3 [DE]",
        "tr": "Example option 3 [TR]",
        "fr": "Example option 3 [FR]",
        "es": "Example option 3 [ES]",
        "it": "Example option 3 [IT]"
    }
},
```
---
## `minAmountOfSelections`

| `minAmountOfSelections`       |                 |
| :-------------- | :-------------- |
| Possible Values | Integer   |
| Required        | no              |
| Default Value   | -             |

By setting `minAmountOfSelections` the minimum number of values that must be selected get defined.

```JSON
"minAmountOfSelections": 2
```

---
## `maxAmountOfSelections`

| `maxAmountOfSelections`       |                 |
| :-------------- | :-------------- |
| Possible Values | Integer   |
| Required        | no              |
| Default Value   | -             |

By setting `maxAmountOfSelections` the maximum number of values that must be selected get defined.

```JSON
"maxAmountOfSelections": 2
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
            "staticStringArray",
            [
            "exampleOptionOne",
            "exampleOptionTwo"
            ]
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

