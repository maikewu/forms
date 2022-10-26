---
title: RichTextInput
category: 62ebf4654ae80e09e468624b
parentDoc: 62ec01bd561bab0aa775efe4
---

The RichTextInput is a text field that allows text formatting.
# Configuration Overview

| Property                                                                     | Description                      |
| :--------------------------------------------------------------------------- | :--------------------------------|
| [required](./24-general-properties/#required)                                | If this is set to `true`, the field is considered invalid as long as no value is entered. |
| [disabled](./24-general-properties/#disabled)                                | Setting this to `true` permanently disables the field in the UI. |
| [pdfHide](./24-general-properties/#pdfhide)                                  | Setting this to `true` hides the whole field in the PDF. |
| [pdfHideIfValueIsEmpty](./24-general-properties/#pdfhideifvalueisempty)      | Setting this to `true` hides the whole field in the PDF in case the field value is empty. |
| [pdfWidth](./24-general-properties/#pdfwidth)                                | Configuration of the width of the field. |
| [placeHolderText](./24-general-properties/#placeholdertext)                  | Localized placeholder text that is shown in the UI when the field is focused but does not have a value. |
| [label](#label)                                                              | Configuration of the field label. |
| [value](#value)                                                              | Configuration of the field value. |
| [prefill](#prefill)                                                          | Configuration to prefill the field with a value upon creation of the form instance. |
| [onChange](#onchange)                                                        | Configuration to change the field with a certain value when pre defined event get executed |

``` JSON (complete)
{
    "id": "richTextInput_1",
    "type": "richTextInput",
    "config": {
        "disabled": false,
        "required": true,
        "pdfHide": false,
        "pdfHideIfValueIsEmpty": false,
        "pdfWidth": 1,
        "placeHolderText": "<h1>Write some rich text</h1>",
        "label": {
            "pdfHide": false,
            "pdfTextColor": "#facc2e",
            "pdfTextSize": 14,
            "uiHide": false,
            "text": {
                "en": "Rich Text Input 1",
                "de": "Rich Text Eingabe 1",
                "tr": "Rich Text Input 1 [TR]",
                "fr": "Rich Text Input 1 [FR]",
                "es": "Rich Text Input 1 [ES]",
                "it": "Rich Text Input 1 [IT]"
            }
        },
        "value": {
            "pdfHide": false,
            "validators": {
                "minCharacters": 10,
                "maxCharacters": 200
            }
        },
        "prefill": {
            "value": [{
                "input": "none",
                "steps": [[ "staticString", "<h1>Default rich text content</h1>"]]
            }]
        }
    }
},
```
``` JSON (minimal)
{
    "id": "richTextInput_1",
    "type": "richTextInput",
    "config": {
        "label": {
            "text": {
                "en": "Rich Text Input 1",
                "de": "Rich Text Eingabe 1",
                "tr": "Rich Text Input 1 [TR]",
                "fr": "Rich Text Input 1 [FR]",
                "es": "Rich Text Input 1 [ES]",
                "it": "Rich Text Input 1 [IT]"
            }
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
| [validators.minCharacters](./24-general-properties/#validatorsmincharacters)    | Minimum number of characters for the input value to be valid.                                   |
| [validators.maxCharacters](./24-general-properties/#validatorsmaxcharacters)    | Maximum number of characters for the input value to be valid.                                   |

---
## `prefill`

| `prefill`                  |                                                                     |
| :------------------------- | :--------------                                                     |
| Possible Values            | Array of [PrefillRules](./25-prefill-rules)            |
| Required                   | no                                                                  |
| Default Value              | -                                                                   |

This configuration follows the [general syntax for prefilling rules](./25-prefill-rules).

``` JSON 
"prefill": {
    "value": [{
        "input": "none",
        "steps": [[ "staticString", "<h1>Default rich text content</h1>"
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
