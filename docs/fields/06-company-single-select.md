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
| [required](#required)                           | If this is set to `true`, the field is considered invalid as long as no value is entered. |
| [disabled](#disabled)                           | Setting this to `true` permanently disables the field in the UI.                          |
| [pdfHide](#pdfhide)                             | Setting this to `true` hides the whole field in the PDF.                                  |
| [pdfHideIfValueIsEmpty](#pdfhideifvalueisempty) | Setting this to `true` hides the whole field in the PDF in case the field value is empty. |
| [pdfWidth](#pdfwidth)                           | Configuration of the width of the field.                                                  |
| [label](#label)                                 | Configuration of the field label.                                                         |
| [value](#value)                                 | Configuration of the field value.                                                         |
| [useAsFilterForFields](#useasfilterforfields)   | ???                                                         |
| [prefill](#prefill)                             | Configuration to prefill the field with a value upon creation of the form instance. |
| [onChange](#onchange)                           | ??? |

``` typescript (complete)
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
                            pdfHide: false,
                            pdfTextColor: '#facc2e',
                            pdfTextSize: 14,
                            uiHide: false,
                        },
                        disabled: false,
                        pdfHide: false,
                        pdfHideIfValueIsEmpty: false,
                        uiHideInRepeaterCardDisplay: false,
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

## `required`

| `required`      |                 |
| :-------------- | :-------------- |
| Possible Values | `true`, `false` |
| Required        | no              |
| Default Value   | `false`         |

If `required` is set to `true`, the field is considered invalid as long as no value is entered.

``` typescript
required: true
```

---
## `disabled`

| `disabled`      |                 |
| :-------------- | :-------------- |
| Possible Values | `true`, `false` |
| Required        | no              |
| Default Value   | `false`         |

If `disabled` is set to `true`, the field is permanently disabled in the UI. It can still be modified during initial prefilling or dynamic field actions but directly modifying the value in the UI is not possible.

``` typescript
disabled: true
```

---
## `pdfHide`

| `pdfHide`       |                 |
| :-------------- | :-------------- |
| Possible Values | `true`, `false` |
| Required        | no              |
| Default Value   | `false`         |

If `pdfHide` is set to `true`, the field is not shown in the PDF at all. This takes precedence over `pdfHideIfValueIsEmpty`.

``` typescript
pdfHide: true
```

---
## `pdfHideIfValueIsEmpty`

| `pdfHideIfValueIsEmpty` |                 |
| :---------------------- | :-------------- |
| Possible Values         | `true`, `false` |
| Required                | no              |
| Default Value           | `false`         |

If `pdfHideIfValueIsEmpty` is set to `true` and the field value is empty, the field is not shown in the PDF at all.
If the field value is not empty, the field will still be shown (unless `pdfHide` is not set to `true`). 

``` typescript
pdfHideIfValueIsEmpty: true
```

---
## `pdfWidth`

| `pdfWdith`      |                     |
| :-------------- | :------------------ |
| Possible Values | `0.25, 0.3, 0.5, 1` |
| Required        | no                  |
| Default Value   | `1 (full wdith)`    |

*???Description???*

``` typescript
pdfWidth: 0.5
```

---
## `label`

| Property                           | Description                                                     |
| :--------------------------------- | :-------------------------------------------------------------- |
| [text](#labeltext)                 | Localized label text of the field. Shown in the UI and the PDF. |
| [uiHide](#labeluihide)             | Setting this to `true` hides the label in the UI.               |
| [pdfHide](#labelpdfhide)           | Setting this to `true` hides the label in the PDF.              |
| [pdfTextSize](#labelpdftextsize)   | Text size of the label in the PDF.                              |
| [pdfTextColor](#labelpdftextcolor) | Text color of the label in the PDF.                             |

---
### `label.text`

| `text`          |                            |
| :-------------- | :------------------------- |
| Possible Values | [MultiLanguageText](#todo) |
| Required        | yes                        |

Label text that is shown in the UI and the PDF to identify the field. 

``` typescript
text: {
    en: 'Example Placeholder',
    de: 'Platzhalter',
    tr: 'Example Placeholder [TR]',
    fr: 'Example Placeholder [FR]',
    es: 'Example Placeholder [ES]',
    it: 'Example Placeholder [IT]',
}
```

---
### `label.uiHide`

| `uiHide`        |                 |
| :-------------- | :-------------- |
| Possible Values | `true`, `false` |
| Required        | no              |
| Default Value   | `false`         |

If `uiHide` is set to `true`, the label is not shown in the UI.

``` typescript
uiHide: true
```

---
### `label.pdfHide`

| `pdfHide`       |                 |
| :-------------- | :-------------- |
| Possible Values | `true`, `false` |
| Required        | no              |
| Default Value   | `false`         |

If `pdfHide` is set to `true`, the label is not shown in the PDF.

=== "Example"
    ``` typescript
    pdfHide: true
    ```

---
### `label.pdfTextSize`

| `pdfTextSize`   |             |
| :-------------- | :---------- |
| Possible Values | Integer > 0 |
| Required        | no          |
| Default Value   | 9           |

By setting `pdfTextSize`, the field label will show up in the PDF having the defined text size in pixels.

``` typescript
pdfTextSize: 20
```

---
### `label.pdfTextColor`

| `pdfTextColor`  |                |
| :-------------- | :------------- |
| Possible Values | Hex-Color-Code |
| Required        | no             |
| Default Value   | `#000000`      |

By setting `pdfTextColor`, the field label will show up in the PDF having the defined color.

``` typescript
pdfTextColor: #F7F1F4
```

---
## `value`

| Property                                        | Description                                                                                     |
| :---------------------------------------------- | :---------------------------------------------------------------------------------------------- |
| [disableCreation](#disablecreation)             | ???                                                                                             |
| [pdfPrintCompanyNumber](#pdfprintcompanynumber) | ???                                                                                             |
| [pdfHide](#valuepdfhide)                        | Setting this to `true` hides the value in the PDF.                                              |
| [pdfTextSize](#valuepdftextsize)                | Text size of the value in the PDF.                                                              |
| [pdfTextColor](#valuepdftextcolor)              | Text color of the value in the PDF.                                                             |
| [pdfStartInNewLine](#valuepdfstartinnewline)    | Setting this to `true` will show the field value in the PDF in a separate line below the label. |

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

---
### `value.pdfHide`

| `pdfHide`       |                 |
| :-------------- | :-------------- |
| Possible Values | `true`, `false` |
| Required        | no              |
| Default Value   | `false`         |

If `pdfHide` is set to `true`, the value is not shown in the PDF.

``` typescript
pdfHide: true
```

---
### `value.pdfTextSize`

| `pdfTextSize`   |             |
| :-------------- | :---------- |
| Possible Values | Integer > 0 |
| Required        | no          |
| Default Value   | 9           |

By setting `pdfTextSize`, the field value will show up in the PDF having the defined text size in pixels.

``` typescript
pdfTextSize: 20
```

---
### `value.pdfTextColor`

| `pdfTextColor`  |                |
| :-------------- | :------------- |
| Possible Values | Hex-Color-Code |
| Required        | no             |
| Default Value   | `#000000`      |

By setting `pdfTextColor`, the field value will show up in the PDF having the defined color.

``` typescript
pdfTextColor: true
```

---
### `value.pdfStartInNewLine`

| `pdfStartInNewLine` |                 |
| :------------------ | :-------------- |
| Possible Values     | `true`, `false` |
| Required            | no              |
| Default Value       | `false`         |

If `pdfStartInNewLine` is set to `true`, the value of the field will be shown in the PDF on a new line below the label. If the value is `false`, the value is shown on the same line as the label.

``` typescript
pdfStartInNewLine: true
```

---
## `useAsFilterForFields ???`

***not described in FIGMA***

| `useAsFilterForFields` |      |
| :--------------------- | :--- |
| Possible Values        | ???  |
| Required               | no   |
| Default Value          | ???  |

***Description???***

``` typescript
useAsFilterForFields: ???
```
---
## `prefill ???`

| `prefill`       |                                                                     |
| :-------------- | :------------------------------------------------------------------ |
| Possible Values | Array of [PrefillRules](#todo) that output a value of type `string` |
| Required        | no                                                                  |
| Default Value   | -                                                                   |

This configuration follows the [general syntax for prefilling rules](#todo).
The provided PrefillRules need to have an output value of type string.

``` typescript (static string)
prefill: {
        value: [
            {
                input: 'none',
                steps: [
                    [ 'staticString', 'Default \n Multi \n Line \n Text' ],
                ],
            },
        ],
    },
```
``` typescript (asset type name)
prefill: {
        value: [
            {
                input: 'assetId',
                steps: [
                    'assetIdToAsset',
                    'assetToAssetTypeNameString',
                ],
            },
        ],
    },
```

---
## `onChange ???`

| `onChange`      |     |
| :-------------- | --- |
| Possible Values | ??? |
| Required        | no  |
| Default Value   | -   |

***Description???***