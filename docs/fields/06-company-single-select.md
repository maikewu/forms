---
title: CompanySingleSelect
category: 635ce1e7775bc60045570ffb
parentDoc: 635ce486ae5fac003cef279e
---

The CompanySingleSelect field allows the user to choose one of the customer companies.

# Configuration Overview

| Property                                        | Description                                                                               |
| :---------------------------------------------- | :---------------------------------------------------------------------------------------- |
| [required](./24-general-properties/#required)                                | If this is set to `true`, the field is considered invalid as long as no value is entered. |
| [disabled](./24-general-properties/#disabled)                                | Setting this to `true` permanently disables the field in the UI. |
| [pdfHide](./24-general-properties/#pdfhide)                                  | Setting this to `true` hides the whole field in the PDF. |
| [pdfHideIfValueIsEmpty](./24-general-properties/#pdfhideifvalueisempty)      | Setting this to `true` hides the whole field in the PDF in case the field value is empty. |
| [pdfWidth](./24-general-properties/#pdfwidth)                                | Configuration of the width of the field. |
| [label](#label)                                 | Configuration of the field label.                                                         |
| [value](#value)                                 | Configuration of the field value.                                                         |
| [useAsFilterForFields](#useasfilterforfields)   | Set `CompanySingleSelect` as filter for asset or user or both                                                         |
| [prefill](#prefill)                             | Configuration to prefill the field with a value upon creation of the form instance. |
| [onChange](#onchange)                                                        | Configuration to change the field with a certain value when pre defined event get executed |

```json (complete)
{
    "id": "exampleCompanySingleSelect_1",
    "type": "companySingleSelect",
    "config": {
        "required": false,
        "disabled": false,
        "pdfHide": false,
        "pdfHideIfValueIsEmpty": false,
        "pdfWidth": 1,
        "label": {
            "text": {
                "en": "Company Single Select 1",
                "de": "Einfache Unternehmensauswahl",
                "tr": "Company Single Select 1 [TR]",
                "fr": "Company Single Select 1 [FR]",
                "es": "Company Single Select 1 [ES]",
                "it": "Company Single Select 1 [IT]"
            },
            "pdfHide": false,
            "pdfTextColor": "#facc2e",
            "pdfTextSize": 14,
            "uiHide": false
        },
        "useAsFilterForFields": [
            "exampleAssetSingleSelect_1"
        ],
        "value": {
            "disableCreation": false,
            "pdfPrintCompanyNumber": false,
            "pdfHide": false,
            "pdfStartInNewLine": false,
            "pdfTextColor": "#facc2e",
            "pdfTextSize": 14
        },
        "prefill": {
            [ "selectedCompany" ]: [
                {
                    "input": "organizationId",
                    "steps": []
                }
            ]
        },
        "onChange": [
            {
                "target": { "id": "disabledSingleLineInput_1" },
                "steps": ["accountInfoToCompanyName"]
            },
            {
                "target": { "id": "exampleAddressInput_1" },
                "steps": [ "accountInfoToAccount", "accountToBillingAddressAddress"]
            },
            {
                "target": { "id": "exampleSignatureSection", "propertyName": "location" },
                "steps": [ "accountInfoToAccount", "accountToBillingAddressAddress", "addressToCityString"]
            },
            {
                "target": { "id": "exampleSingleLineInput_2" },
                "steps": ["accountInfoToAccount", "accountToPhoneNumberString" ]
            },
            {
                "target": { "id": "examplePhoneNumberInput_1" },
                "steps": [ "accountInfoToAccount", "accountToPhoneNumberString", "phoneNumberStringToPhoneNumberObject" ]
            }
        ]
    }
}
```

```json (minimal)
{
    "id": "exampleCompanySingleSelect_1",
    "type": "companySingleSelect",
    "config": {
        "label": {
            "text": {
                "en": "Company Single Select 1",
                "de": "Einfache Unternehmensauswahl",
                "tr": "Company Single Select 1 [TR]",
                "fr": "Company Single Select 1 [FR]",
                "es": "Company Single Select 1 [ES]",
                "it": "Company Single Select 1 [IT]"
            }
        }
    }
}
```
---
# Configuration Parameters

## `label`

Property                                                    | Description                       |
| :---------------------------------------------------------- | :-------------------------------- |
| [text](./24-general-properties/#text)                       | Localized label text of the field. Shown in the UI and the PDF. |
| [uiHide](./24-general-properties/#uihide)                   | Setting this to `true` hides the label in the UI. |
| [pdfHide](./24-general-properties/#pdfhide)                 | Setting this to `true` hides the label in the PDF. |
| [pdfTextSize](./24-general-properties/#pdftextsize)         | Text size of the label in the PDF. |
| [pdfTextColor](./24-general-properties/#pdftextcolor)       | Text color of the label in the PDF. |

---
## `value`

| Property                                        | Description                                                                                     |
| :---------------------------------------------- | :---------------------------------------------------------------------------------------------- |
| [pdfHide](./24-general-properties/#pdfhide)                                     | Setting this to `true` hides the label in the PDF. |
| [pdfTextSize](./24-general-properties/#pdftextsize)                             | Text size of the label in the PDF. |
| [pdfTextColor](./24-general-properties/#pdftextcolor)                           | Text color of the label in the PDF. |
| [pdfStartInNewLine](./24-general-properties/#pdfstartinnewline)                 | Setting this to `true` will show the field value in the PDF in a separate line below the label. |
| [disableCreation](#disablecreation)             | Hides the create button, so that no new companies can be created.                                                                                            |
| [pdfPrintCompanyNumber](#pdfprintcompanynumber) | Setting this to `true` prints the company number in the PDF.                                                                                             |

---
### `value.disableCreation`

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
### `value.pdfPrintCompanyNumber`

| `pdfPrintCompanyNumber` |                 |
| :---------------------- | :-------------- |
| Possible Values         | `true`, `false` |
| Required                | no              |
| Default Value           | `false`         |

If `pdfPrintCompanyNumber` is set to `true`, the company number will be printed in the PDF in brackets behind the company name.

```json
"pdfPrintCompanyNumber": true
```

## `useAsFilterForFields`


| `useAsFilterForFields` |      |
| :--------------------- | :--- |
| Possible Values        | Field IDs of `assetSingleSelect` or `userSingleSelect`  |
| Required               | no   |
| Default Value          | -  |

The `useAsFilterForFields` property can be used to filter the asset and user select field by entering the field id.

```json
"useAsFilterForFields": [ "exampleAssetSingleSelect_1" ]
```
---



## `prefill`

| `prefill`                  |                                                                     |
| :------------------------- | :--------------                                                     |
| Possible Values            | Array of [PrefillRules](./25-prefill-rules)            |
| Required                   | no                                                                  |
| Default Value              | -                                                                   |

This configuration follows the [general syntax for prefilling rules](./25-prefill-rules).
```json (currentAccountId)
"prefill": {
    "selectedCompany": [
        {
            "input": "currentAccountId",
            "steps": []
        }
    ]
}
```
```json (organizationId)
"prefill": {
    "selectedCompany": [
        {
            "input": "organizationId",
            "steps": []
        }
    ]
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
```json
"onChange": [
    {
        "steps": ["accountInfoToCompanyName"],
        "target": { "id": "disabledSingleLineInput_1" }
    },
    {
        "steps": [ "accountInfoToAccount", "accountToBillingAddressAddress"],
        "target": { "id": "exampleAddressInput_1" }
    },
    {
        "steps": [ "accountInfoToAccount", "accountToBillingAddressAddress", "addressToCityString"],
        "target": { "id": "exampleSignatureSection", "propertyName": "location" }
    },
    {
        "steps": ["accountInfoToAccount", "accountToPhoneNumberString" ],
        "target": { "id": "exampleSingleLineInput_2" }
    },
    {
        "steps": [ "accountInfoToAccount", "accountToPhoneNumberString", "phoneNumberStringToPhoneNumberObject" ],
        "target": { "id": "examplePhoneNumberInput_1" }
    }
]
```
