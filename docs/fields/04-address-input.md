---
title: AddressInput
category: 635ce1e7775bc60045570ffb
parentDoc: 635ce486ae5fac003cef279e
---

The AddressInput contains various fields for every information of an address.
# Configuration Overview

| Property                                                                     | Description                      |
| :--------------------------------------------------------------------------- | :--------------------------------|
| [required](#required)                                                        | Contains various sub-fields the can be set as mandatory fields. |
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
    "id": "exampleAddressInput_1",
    "type": "addressInput",
    "config": {
      "required": {
        "street": false,
        "streetNumber": false,
        "company": false,
        "supplement": false,
        "zipPostCode": false,
        "city": false,
        "state": false,
        "country": false
      },
      "disabled": false,
      "pdfHide": false,
      "pdfHideIfValueIsEmpty": false,
      "pdfWidth": 1,
      "label": {
        "text": { 
          "en": "Address Input 1",
          "de": "Anschrift Input 1",
          "tr": "Address Input 1 [TR]",
          "fr": "Address Input 1 [FR]",
          "es": "Address Input 1 [ES]",
          "it": "Address Input 1 [IT]"
        },
        "pdfHide": false,
        "pdfTextColor": "#facc2e",
        "pdfTextSize": 14
      },
      "value": {
        "pdfHide": false,
        "pdfStartInNewLine": false,
        "pdfAddLineBreaks": false,
        "pdfTextColor": "#facc2e",
        "pdfTextSize": 14
      },
      "prefill": {
        "value": [
          {
            "input": "none",
            "steps": [
              [
                "staticAddress",
                {
                  "city": "Default City",
                  "street": "Default Street",
                  "streetNumber": "1",
                  "country": "Default Country",
                  "other": "Default supplement",
                  "countryProvince": "Default state",
                  "company": "Default Company"
                }
              ]
            ]
          }
        ]
      },
      "onChange": [{
          "target": { "id": "exampleSignatureSection", "propertyName": "location" },    
          "steps": ["addressToCityString"]
      }]
    }
},
```
```json (minimal)
{
    "id": "exampleAddressInput_2",
    "type": "addressInput",
    "config": {
        "required": {
        },
         "label": {
              "text": {
                "en": "Address Input 1",
                "de": "Anschrift Input 1",
                "tr": "Address Input 1 [TR]",
                "fr": "Address Input 1 [FR]",
                "es": "Address Input 1 [ES]",
                "it": "Address Input 1 [IT]"
              },
        },
        "value": {
        },
    },
},
```

---
# Configuration Parameters

## `required`

| Property                                                    | Description                       |
| :---------------------------------------------------------- | :-------------------------------- |
| `street`                                                    | Setting this to `true` makes this field required  |
| `streetNumber`                                              | Setting this to `true` makes this field required  |
| `supplement`                                                | Setting this to `true` makes this field required  |
| `company`                                                   | Setting this to `true` makes this field required  |
| `zipPostCode`                                               | Setting this to `true` makes this field required  |
| `city`                                                      | Setting this to `true` makes this field required  |
| `state`                                                     | Setting this to `true` makes this field required  |
| `country`                                                   | Setting this to `true` makes this field required  |

The Address Input field has several different fields that can be individually set as mandatory fields.

```json
"required": {
    "street": false,
    "streetNumber": false,
    "company": false,
    "supplement": false,
    "zipPostCode": false,
    "city": false,
    "state": false,
    "country": false
},
```

---
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


---
## `prefill`

| `prefill`                  |                                                                     |
| :------------------------- | :--------------                                                     |
| Possible Values            | Array of [PrefillRules](./25-prefill-rules)            |
| Required                   | no                                                                  |
| Default Value              | -                                                                   |

This configuration follows the [general syntax for prefilling rules](./25-prefill-rules).
```json
"prefill": {
    "value": [
    {
        "input": "none",
        "steps": [
        [
            "staticAddress",
            {
            "street": "Default Street",
            "streetNumber": "1",
            "company": "remberg GmbH",
            "supplement": "Default Supplement",
            "zipPostCode": "Default Zip-code",
            "city": "Default City",
            "state": "Default State",
            "country": "Default Country",
            "city": "Default City",
            }
        ]
        ]
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
```json
"onChange": [{
    "target": { "id": "exampleSignatureSection", "propertyName": "location" },    
    "steps": ["addressToCityString"]
}]
```

