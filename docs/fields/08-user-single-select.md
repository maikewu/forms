---
title: UserSingleSelect
category: 635ce1e7775bc60045570ffb
parentDoc: 635ce486ae5fac003cef279e
---

The UserSingleSelect field allows to select a user from the own or from a customers organization.

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

```json (complete)
{
    "id": "exampleUserSingleSelect_1",
    "type": "userSingleSelect",
    "config": {
        "required": true,
        "disabled": false,
        "pdfHide": false,
        "pdfHideIfValueIsEmpty": false,
        "pdfWidth": 1,
        "label": {
            "text": {
                "en": "User Select 1",
                "de": "User Auswahl 1",
                "tr": "User Select 1 [TR]",
                "fr": "User Select 1 [FR]",
                "es": "User Select 1 [ES]",
                "it": "User Select 1 [IT]"
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
            "pdfPrintEmailAddress": true
        },
      "prefill": {
          "value": [{
                  "input": "currentUserId",
                  "steps": [],
              }]
      },
      "onChange": [{
            "target": { "id": "exampleSignatureSection", "propertyName": "name" },
            "steps": [ "userToFullNameString" ],
          },
          {
            "target": { "id": "examplePhoneNumberInput_1" },
            "steps": ["userInfoToUser", "userToPhoneNumberString", "phoneNumberStringToPhoneNumberObject"],
          }],
  },
},
```
```json (minimal)
{
    "id": "exampleUserSingleSelect_1",
    "type": "userSingleSelect",
    "config": {
        "label": {
            "text": {
                "en": "User Select 1",
                "de": "User Auswahl 1",
                "tr": "User Select 1 [TR]",
                "fr": "User Select 1 [FR]",
                "es": "User Select 1 [ES]",
                "it": "User Select 1 [IT]"
            },
        },
    },
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
| [printEmailAddress](#printemailaddress)                                         | Setting this to `true` prints the email address of the selected user in the PDF. |

---
### `printEmailAddress`

| `printEmailAddress`     |                 |
| :-------------- | :-------------- |
| Possible Values | `true`, `false`     |
| Required        | no              |
| Default Value   | `false`               |

By setting `printEmailAddress` to `true`, email address of the selected user will be printed in brackets next to the name in the PDF.

```json
value:{
"printEmailAddress": true
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
```json (current UserID)
"prefill": {
    "value": [
        {
            "input": "currentUserId",
            "steps": [],
        }
    ]
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
```json (Name to Signature Section)
"onChange": [
    {
        "target": { "id": "exampleSignatureSection", "propertyName": "name" },
        "steps": [ "userToFullNameString" ],
    }
],
```
```json (phone number)
"onChange": [
    {
        "target": {"id": "phone"},
        "steps": ["userInfoToUser", "userToPhoneNumberString", "phoneNumberStringToPhoneNumberObject"]
    }
],
```
