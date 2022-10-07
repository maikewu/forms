---
title: AssetSingleSelect
category: 62ebf4654ae80e09e468624b
parentDoc: 62ec01bd561bab0aa775efe4
---

The AssetSingleSelect field allows to select an asset from the account or a certain costumer.

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

``` typescript (complete)
{
    id: 'exampleAssetSingleSelect_1',
    type: FormFieldTypesEnum.ASSET_SINGLE_SELECT,
    config: {
        required: true,
        disabled: false,
        pdfHide: false,
        pdfHideIfValueIsEmpty: false,
        uiHideInRepeaterCardDisplay: false,
        label: {
            text: {
                en: 'Asset Select 1',
                de: 'Asset Auswahl 1',
                tr: 'Asset Select 1 [TR]',
                fr: 'Asset Select 1 [FR]',
                es: 'Asset Select 1 [ES]',
                it: 'Asset Select 1 [IT]',
            },
            pdfHide: false,
            pdfTextColor: '#facc2e',
            pdfTextSize: 14,
            uiHide: false,
        },
        value: {
            disableAssetFormInstanceRelationship: false,
            disableCreation: false,
            pdfHide: false,
            pdfStartInNewLine: false,
            pdfTextColor: '#facc2e',
            pdfTextSize: 14,
        },
        prefill: {
            selectedAsset: [
                {
                    input: 'assetId',
                    steps: [],
                },
            ],
        },
        onChange: [
            {
                steps: [
                    'assetInfoToAsset',
                    [ 'assetToCustomPropertyValue', 5 ], // 5 - propertyId of the customer property that exists in your system
                ],
                target: { id: 'exampleMultiLineTextInput_1' },
            },
            {
                steps: [
                    'assetInfoToCustomerId',
                    'accountIdToAccount',
                    'accountToAccountInfo',
                ],
                target: { id: 'exampleCompanySingleSelect_1' },
            },
        ],
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

---
## `prefill`

| `prefill`                  |                                                                     |
| :------------------------- | :--------------                                                     |
| Possible Values            | Array of [PrefillRules](.25-prefill-rules)            |
| Required                   | no                                                                  |
| Default Value              | -                                                                   |

This configuration follows the [general syntax for prefilling rules](.25-prefill-rules).
``` typescript (assetID)
prefill: {
    selectedAsset: [
        {
            input: 'assetId',
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
``` typescript
onChange: [
    {
        steps: [
            'assetInfoToAsset',
            [ 'assetToCustomPropertyValue', 5 ], // 5 - propertyId of the customer property that exists in your system
        ],
        target: { id: 'exampleMultiLineTextInput_1' },
    },
    {
        steps: [
            'assetInfoToCustomerId',
            'accountIdToAccount',
            'accountToAccountInfo',
        ],
        target: { id: 'exampleCompanySingleSelect_1' },
    },
],
```
