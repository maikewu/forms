---
title: Signature Section
category: 62ebf4654ae80e09e468624b
parentDoc: 62ec01bd8854e3076580c823
---

The SignatureSection contains all sigatures to finish the form.
# Configuration Overview

| Property                                                                     | Description                      |
| :--------------------------------------------------------------------------- | :--------------------------------|
| [required](./24-general-properties/#required) (Required!)                               | If this is set to `true`, the field is considered invalid as long as no value is entered. |
| [headlineText](./24-general-properties/#mulitlanguagetext) (Required!)            | Configurate the displayed field lable |
| [helpTextHtmlAbove](#helptexthtmlabove)                                      | HTML help text above the section|
| [helpTextHtmlBelow](#helptexthtmlbelow)                                      | HTML help text below the section|
| [pdfHide](./24-general-properties/#pdfhide) (Required!)                                 | Setting this to `true` hides the whole field in the PDF. |
| [pdfHideIfValueIsEmpty](./24-general-properties/#pdfhideifvalueisempty) (Required!)    | Setting this to `true` hides the whole field in the PDF in case the field value is empty. |
| [hidePreviewPdfButton](#hidepreviewpdfbutton)                             | Setting this to `true` hides the preview PDF button in the UI |
| [hideDownloadPdfButton](#hidedownloadpdfbutton)                          |  Setting this to `true` hides the download PDF button in the UI|
| [fields](#fields) (Required!)                                                    | Field properties of a form. |
| [prefill](#prefill)                                                          | Configuration to prefill the field with a value upon creation of the form instance. |

```typescript

{
    id: 'exampleSignatureSection',
    type: FormSectionTypesEnum.SIGNATURE_SECTION,
    config: {
        required: true,
        headlineText: {
            en: 'Example Signature Section',
            de: 'Beispiel Signatur Sektion',
            tr: 'Example Signature Section [TR]',
            fr: 'Example Signature Section [FR]',
            es: 'Example Signature Section [ES]',
            it: 'Example Signature Section [IT]',
        },
        helpTextHtmlAbove: {
            en: '<b>Example HTML helptext before</b>',
            de: '<b>Beispiel HTML Hilfstext davor</b>',
            tr: '<b>Example HTML helptext before [TR]</b>',
            fr: '<b>Example HTML helptext before [FR]</b>',
            es: '<b>Example HTML helptext before [ES]</b>',
            it: '<b>Example HTML helptext before [IT]</b>',
        },
        helpTextHtmlBelow: {
            en: '<b>Example HTML helptext below</b>',
            de: '<b>Beispiel HTML Hilfstext derunter</b>',
            tr: '<b>Example HTML helptext below [TR]</b>',
            fr: '<b>Example HTML helptext below [FR]</b>',
            es: '<b>Example HTML helptext below [ES]</b>',
            it: '<b>Example HTML helptext below [IT]</b>',
        },
        pdfHide: false,
        pdfHideIfValueIsEmpty: false,    
        hideDownloadPdfButton: false,
        hidePreviewPdfButton: false,
        fields: {
            dateInput: {
                disable: false,
                pdfHide: false,
                required: false,
            },
            locationSingleLineTextInput: {
                disable: false,
                pdfHide: false,
                required: false,
            },
            nameSingleLineTextInput: {
                disable: false,
                pdfHide: false,
                capitalizeFirstLetterOfEveryWord: false,
                required: false,
            },
        },
        prefill: {
            name: [
                {
                    input: 'currentUser',
                    steps: [
                        'userToFullNameString',
                    ],
                },
            ],
            location: [
                {
                    input: 'assetId',
                    steps: [
                        'assetIdToAsset',
                        'assetToLocationAddress',
                        'addressToCityString',
                    ],
                },
                {
                    input: 'assetId',
                    steps: [
                        'assetIdToAsset',
                        'assetToCustomerAccountId',
                        'accountIdToAccount',
                        'accountToBillingAddressAddress',
                        'addressToCityString',
                    ],
                },
                {
                    input: 'organizationId',
                    steps: [
                        'accountIdToAccount',
                        'accountToBillingAddressAddress',
                        'addressToCityString',
                    ],
                },
                {
                    input: 'none',
                    steps: [
                        [
                            'staticString',
                            'Default Location',
                        ],
                    ],
                },
            ],
            date: [
                {
                    input: 'creationDateTime',
                    steps: ['dateTimeToDate'],
                },
            ],
        },
    },
},
```
---

# Configuration Parameters

## `helpTextHtmlAbove`

| `helpTextHtmlAbove` |                 |
| :---------------- | :------------------------- |
| Possible Values   | [MultiLanguageText](#multilanguagetext) |
| Required          | no           
| Default Value     | -       |

`helpTextHtmlAbove` can be used with HTML to place a helptext above the section properties in the PDF.

 ```typescript 
helpTextHtmlAbove: {
    en: '<b>Example HTML helptext before</b>',
    de: '<b>Beispiel HTML Hilfstext davor</b>',
    tr: '<b>Example HTML helptext before [TR]</b>',
    fr: '<b>Example HTML helptext before [FR]</b>',
    es: '<b>Example HTML helptext before [ES]</b>',
    it: '<b>Example HTML helptext before [IT]</b>',
},
```
---
## `helpTextHtmlBelow`

| `helpTextHtmlBelow` |                 |
| :---------------- | :------------------------- |
| Possible Values   | [MultiLanguageText](#multilanguagetext) |
| Required          | no           
| Default Value     | -       |

`helpTextHtmlBelow` can be used with HTML to place a helptext below the section properties in the PDF.

 ```typescript 
helpTextHtmlBelow: {
    en: '<b>Example HTML helptext below</b>',
    de: '<b>Beispiel HTML Hilfstext derunter</b>',
    tr: '<b>Example HTML helptext below [TR]</b>',
    fr: '<b>Example HTML helptext below [FR]</b>',
    es: '<b>Example HTML helptext below [ES]</b>',
    it: '<b>Example HTML helptext below [IT]</b>',
},
```
---
## `hidePreviewPdfButton`

| `hidePreviewPdfButton` |                 |
| :------------------------- | :-------------- |
| Possible Values            | `true`, `false` |
| Required                   | yes              |
| Default Value              | -       |

 Setting `hidePreviewPdfButton` to `true` hides the preview button in the UI.

 ```typescript 
hidePreviewPdfButton: true,
```
---
## `hideDownloadPdfButton`

| `hideDownloadPdfButton` |                 |
| :------------------------- | :-------------- |
| Possible Values            | `true`, `false` |
| Required                   | yes              |
| Default Value              | -       |

 Setting `hideDownloadPdfButton` to `true` hides the download button in the UI

 ```typescript 
hideDownloadPdfButton: true,
```
--
## `fields`

| Property                                                      | Description                       |
| :------------------------------------------------------------ | :-------------------------------- |
| [dateInput](#dateInput)    (Required!)                                         | Property to enter a date|
| [locationSingleLineTextInput](#locationsinglelinetextinput)     (Required!)    | An input field to enter the location|
| [nameSingleLineTextInput](#namesinglelinetextinput)     (Required!)            | An input field to enter the name of the signatory |


---
### `dateInput`

| Property                                                      | Description                       |
| :------------------------------------------------------------ | :-------------------------------- |
| [required](./24-general-properties/#required)  (Required!)               | If this is set to `true`, the field is considered invalid as long as no value is entered. |
| [disabled](./24-general-properties/#disabled)  (Required!)               | Setting this to `true` permanently disables the field in the UI. |
| [pdfHide](./24-general-properties/#pdfhide)    (Required!)               | Setting this to `true` hides the label in the PDF. |
| [onChange](./26-on-change-rules)                                                        | Configuration to change the field with a certain value when pre defined event get executed |

---
### `locationSingleLineTextInput`

| Property                                                      | Description                       |
| :------------------------------------------------------------ | :-------------------------------- |
| [required](./24-general-properties/#required)  (Required!)               | If this is set to `true`, the field is considered invalid as long as no value is entered. |
| [disabled](./24-general-properties/#disabled)  (Required!)               | Setting this to `true` permanently disables the field in the UI. |
| [pdfHide](./24-general-properties/#pdfhide)    (Required!)               | Setting this to `true` hides the label in the PDF. |
| [onChange](./26-on-change-rules)                                                        | Configuration to change the field with a certain value when pre defined event get executed |

---
### `nameSingleLineTextInput`

| Property                                                      | Description                       |
| :------------------------------------------------------------ | :-------------------------------- |
| [required](./24-general-properties/#required)  (Required!)               | If this is set to `true`, the field is considered invalid as long as no value is entered. |
| [disabled](./24-general-properties/#disabled)   (Required!)              | Setting this to `true` permanently disables the field in the UI. |
| [pdfHide](./24-general-properties/#pdfhide)     (Required!)              | Setting this to `true` hides the label in the PDF. |
| [capitalizeFirstLetterOfEveryWord](#capitalizefirstletterofeveryword)                   | Setting this to `true` capitalize every first letter of every word in the PDF |
| [onChange](./26-on-change-rules)                                                        | Configuration to change the field with a certain value when pre defined event get executed |

---

#### `capitalizeFirstLetterOfEveryWord`

| `capitalizeFirstLetterOfEveryWord` |                 |
| :------------------------- | :-------------- |
| Possible Values            | `true`, `false` |
| Required                   | yes              |
| Default Value              | -       |

 Setting `capitalizeFirstLetterOfEveryWord` to `true`capitalize every first letter of every word in the PDF.

 ```typescript 
capitalizeFirstLetterOfEveryWord: true,
```
---

## `prefill`

| `prefill`                  |                                                                     |
| :------------------------- | :--------------                                                     |
| Possible Values            | Array of [PrefillRules](./25-prefill-rules)            |
| Required                   | no                                                                  |
| Default Value              | -                                                                   |

This configuration follows the [general syntax for prefilling rules](./25-prefill-rules).

``` typescript (static string)
prefill: {
    name: [
        {
            input: 'currentUser',
            steps: [
                'userToFullNameString',
            ],
        },
    ],
    location: [
        {
            input: 'assetId',
            steps: [
                'assetIdToAsset',
                'assetToLocationAddress',
                'addressToCityString',
            ],
        },
        {
            input: 'assetId',
            steps: [
                'assetIdToAsset',
                'assetToCustomerAccountId',
                'accountIdToAccount',
                'accountToBillingAddressAddress',
                'addressToCityString',
            ],
        },
        {
            input: 'organizationId',
            steps: [
                'accountIdToAccount',
                'accountToBillingAddressAddress',
                'addressToCityString',
            ],
        },
        {
            input: 'none',
            steps: [
                [
                    'staticString',
                    'Default Location',
                ],
            ],
        },
    ],
    date: [
        {
            input: 'creationDateTime',
            steps: ['dateTimeToDate'],
        },
    ],
},
```