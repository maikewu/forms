---
title: PhoneNumberInput
category: 635ce1e7775bc60045570ffb
parentDoc: 635ce3a98eac79008251739a
---

The PhoneNumberInput field allows to input telephone numbers in the common format.
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
    "id": "examplePhoneNumberInput_1",
    "type": "phoneNumberInput",
    "config": {
        "disabled": false,
        "required": true,
        "pdfHide": false,
        "pdfHideIfValueIsEmpty": false,
        "pdfWidth": 1,
        "label": {
            "pdfHide": false,
            "pdfTextColor": "#facc2e",
            "pdfTextSize": 14,
            "text": {
                "en": "Phone number input required",
                "de": "Phone number input required [DE]",
                "tr": "Phone number input required [TR]",
                "fr": "Phone number input required [FR]",
                "es": "Phone number input required [ES]",
                "it": "Phone number input required [IT]"
            },
        }, 
       "placeHolderText": {
            "en": "Phone number input placeholder",
            "de": "Phone number input placeholder [DE]",
            "tr": "Phone number input placeholder [TR]",
            "fr": "Phone number input placeholder [FR]",
            "es": "Phone number input placeholder [ES]",
            "it": "Phone number input placeholder [IT]"
        },
        "value": {
            "pdfHide": false,
            "pdfStartInNewLine": false,
            "pdfTextColor": "#facc2e",
            "pdfTextSize": 14,
            "validators": {
                "minCharacters": 6,
                "maxCharacters": 10,
                "supportedNonNumericsCharacters": ["A", "I", "*"]   
            }
        },
        "prefill": {
            "value": [{
                "input": "none",
                "steps": [[
                    "staticPhoneNumber",
                    {
                    "countryPrefix": "49",
                    "number": "1753463937"
                    }
                ]]
            }]
        },
    }
}
```
``` JSON (minimal)
{
    "id": "examplePhoneNumberInput_1",
    "type": "phoneNumberInput",
    "config": {
        "label": {
            "text": {
                "en": "Phone number input required",
                "de": "Phone number input required [DE]",
                "tr": "Phone number input required [TR]",
                "fr": "Phone number input required [FR]",
                "es": "Phone number input required [ES]",
                "it": "Phone number input required [IT]"
            },
        }, 
        "value": {
        },
    }
}
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
## `value`

| Property                                                                        | Description                                                                                     |
| :------------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------- |
| [pdfHide](./24-general-properties/#pdfhide)                                     | Setting this to `true` hides the label in the PDF. |
| [pdfTextSize](./24-general-properties/#pdftextsize)                             | Text size of the label in the PDF. |
| [pdfTextColor](./24-general-properties/#pdftextcolor)                           | Text color of the label in the PDF. |
| [pdfStartInNewLine](./24-general-properties/#pdfstartinnewline)                 | Setting this to `true` will show the field value in the PDF in a separate line below the label. |
| [validators.minCharacters](./24-general-properties/#validatorsmincharacters)    | Minimum number of characters for the input value to be valid.                                   |
| [validators.maxCharacters](./24-general-properties/#validatorsmaxcharacters)    | Maximum number of characters for the input value to be valid.                                   |
| [validators.supportedNonNumericCharacters](#supportedNonNumericCharacters)      | By setting this, the field will support a list of non numeric characters.                                             |

---
### `supportedNonNumericCharacters`

| `supportedNonNumericCharacters`     |                 |
| :-------------- | :-------------- |
| Possible Values | `String [Array]     |
| Required        | no              |
| Default Value   | empty [Array]               |

By setting `supportedNonNumericCharacters`, the field will support a list of non numeric characters. The characters are case sensitive.

``` JSON (validators)
"validators":{
"supportedNonNumericsCharacters": ["A", "I", "*"]
}
```

---
## `prefill`

| `prefill`                  |                                                                     |
| :------------------------- | :--------------                                                     |
| Possible Values            | Array of [PrefillRules](./25-prefill-rules)            |
| Required                   | no                                                                  |
| Default Value              | -                                                                   |

This configuration follows the [general syntax for prefilling rules](./25-prefill-rules).

``` JSON (static phone number)
"prefill": {
    "value": [{
        "input": "none",
        "steps": [[
            "staticPhoneNumber",
            {
            "countryPrefix": "49",
            "number": "1753463937"
            }
        ]]
    }]
},
```
---
## `onChange`

| `onChange`                 |                                                                        |
| :------------------------- | :--------------                                                        |
| Possible Values            | Array of [DynamicFieldActions](./26-on-change-rules) |
| Required                   | no                                                                     |
| Default Value              | -                                                                      |


This configuration follows the [general syntax for dynamic field actions](./26-on-change-rules).
