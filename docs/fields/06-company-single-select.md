---
title: CompanySingleSelect
category: 62ebf4654ae80e09e468624b
parentDoc: 62ec01bd561bab0aa775efe4
---


>🚧 
>
> In progress

The CompanySingleSelect field allows the user to choose one of the customer companys.

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
| [useAsFilterForFields](#useasfilterforfields)   | ???                                                         |
| [prefill](#prefill)                             | Configuration to prefill the field with a value upon creation of the form instance. |
| [onChange](#onchange)                                                        | Configuration to change the field with a certain value when pre defined event get executed |

``` typescript (complete)
{
    id: 'exampleCompanySingleSelect_1',
    type: FormFieldTypesEnum.COMPANY_SINGLE_SELECT,
    config: {
        disabled: false,
        pdfHide: false,
        pdfHideIfValueIsEmpty: false,
        uiHideInRepeaterCardDisplay: false,
        label: {
            text: {
                en: 'Company Single Select 1',
                de: 'Einfache Unternehmensauswahl',
                tr: 'Company Single Select 1 [TR]',
                fr: 'Company Single Select 1 [FR]',
                es: 'Company Single Select 1 [ES]',
                it: 'Company Single Select 1 [IT]',
            },
            pdfHide: false,
            pdfTextColor: '#facc2e',
            pdfTextSize: 14,
            uiHide: false,
        },
        value: {
            disableCreation: false,
            pdfPrintCompanyNumber: false,
            pdfHide: false,
            pdfStartInNewLine: false,
            pdfTextColor: '#facc2e',
            pdfTextSize: 14,
        },
        prefill: {
            [CompanySingleSelectPrefillTargetsEnum.SELECTED_COMPANY]: [
                {
                    input: 'currentAccountId',
                    steps: [],
                },
            ],
        },
        onChange: [
            {
                steps: ['accountInfoToCompanyName'],
                target: { id: 'disabledSingleLineInput_1' },
            },
            {
                steps: ['accountInfoToAccount', 'accountToBillingAddressAddress'],
                target: { id: 'exampleAddressInput_1' },
            },
            {
                steps: ['accountInfoToAccount', 'accountToBillingAddressAddress', 'addressToCityString'],
                target: { id: 'exampleSignatureSection', propertyName: 'location' },
            },
            {
                steps: ['accountInfoToAccount', 'accountToPhoneNumberString' ],
                target: { id: 'exampleSingleLineInput_2' },
            },
            {
                steps: ['accountInfoToAccount', 'accountToPhoneNumberString', 'phoneNumberStringToPhoneNumberObject'],
                target: { id: 'examplePhoneNumberInput_1' },
            },
        ],
    },
},

```

``` typescript (minimal)
{
    id: 'exampleCompanySingleSelect_1',
    type: FormFieldTypesEnum.COMPANY_SINGLE_SELECT,
    config: {
        label: {
             text: {
                 en: 'Company Single Select 1',
                 de: 'Einfache Unternehmensauswahl',
                 tr: 'Company Single Select 1 [TR]',
                 fr: 'Company Single Select 1 [FR]',
                 es: 'Company Single Select 1 [ES]',
                 it: 'Company Single Select 1 [IT]',
             },
        },
    },
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
| [disableCreation](#disablecreation)             | Hides the creat button, so that no new companies can be created.                                                                                            |
| [pdfPrintCompanyNumber](#pdfprintcompanynumber) | Setting this to `true` printes the company number in the PDF.                                                                                             |

---
### `value.disableCreation`

| `disableCreation` |                 |
| :---------------- | :-------------- |
| Possible Values   | `true`, `false` |
| Required          | no              |
| Default Value     | `false`         |

If `disableCreation` is set to `true`, the creat button is hidden, so that no new companies can be created while working in forms.

``` typescript
disableCreation: true
```

---
### `value.pdfPrintCompanyNumber`

| `pdfPrintCompanyNumber` |                 |
| :---------------------- | :-------------- |
| Possible Values         | `true`, `false` |
| Required                | no              |
| Default Value           | `false`         |

If `pdfPrintCompanyNumber` is set to `true`, the company number will be printed in the PDF in brackets behinde the company name.

``` typescript
pdfPrintCompanyNumber: true
```

## `useAsFilterForFields`


| `useAsFilterForFields` |      |
| :--------------------- | :--- |
| Possible Values        | Field IDs of `assetSingleSelect` or `userSingleSelect`  |
| Required               | no   |
| Default Value          | -  |

The `useAsFilterForFields` property can be used to filter the asset and user select field.

``` typescript
useAsFilterForFields: [ 'exampleAssetSingleSelect_1' ]
```
---



## `prefill`

| `prefill`                  |                                                                     |
| :------------------------- | :--------------                                                     |
| Possible Values            | Array of [PrefillRules](.25-prefill-rules)            |
| Required                   | no                                                                  |
| Default Value              | -                                                                   |

This configuration follows the [general syntax for prefilling rules](.25-prefill-rules).
``` typescript (currentAccountId)
prefill: {
    [CompanySingleSelectPrefillTargetsEnum.SELECTED_COMPANY]: [
        {
            input: 'currentAccountId',
            steps: [],
        },
    ],
},
```
---
## `onChange`

| `onChange`                 |                                                                        |
| :------------------------- | :--------------                                                        |
| Possible Values            | Array of [DynamicFieldActions](.26-on-change-rules) |
| Required                   | no                                                                     |
| Default Value              | -                                                                      |


This configuration follows the [general syntax for dynamic field actions](.26-on-change-rules).
```typescript
onChange: [
    {
        steps: ['accountInfoToCompanyName'],
        target: { id: 'disabledSingleLineInput_1' },
    },
    {
        steps: ['accountInfoToAccount', 'accountToBillingAddressAddress'],
        target: { id: 'exampleAddressInput_1' },
    },
    {
        steps: ['accountInfoToAccount', 'accountToBillingAddressAddress', 'addressToCityString'],
        target: { id: 'exampleSignatureSection', propertyName: 'location' },
    },
    {
        steps: ['accountInfoToAccount', 'accountToPhoneNumberString' ],
        target: { id: 'exampleSingleLineInput_2' },
    },
    {
        steps: ['accountInfoToAccount', 'accountToPhoneNumberString', 'phoneNumberStringToPhoneNumberObject'],
        target: { id: 'examplePhoneNumberInput_1' },
    },
],
```
