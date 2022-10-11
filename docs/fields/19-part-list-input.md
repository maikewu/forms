---
title: PartListInput
category: 62ebf4654ae80e09e468624b
parentDoc: 62ec01bd561bab0aa775efe4
---

With the PartListInput, the user can add parts to an form.
# Configuration Overview

| Property                                                                     | Description                      |
| :--------------------------------------------------------------------------- | :--------------------------------|
| [pdfHide](./24-general-properties/#pdfhide)                                  | Setting this to `true` hides the whole field in the PDF. |
| [pdfHideIfValueIsEmpty](./24-general-properties/#pdfhideifvalueisempty)      | Setting this to `true` hides the whole field in the PDF in case the field value is empty. |
| [pdfWidth](./24-general-properties/#pdfwidth)                                | Configuration of the width of the field. |
| [requiredAmountOfEntries](./24-general-properties/#requiredamountofentries)  | Specify how many repeating entries are requried to fill the form.                                                                                        |
| [label](#label)                                                              | Configuration of the field label. |
| [fields](#fields)                                                            | Components of the field |


```typescript (complete)
{
    id: 'exampleSparePartsList_1',
    type: FormFieldTypesEnum.PART_LIST_INPUT,
    config: {
        pdfHide: false,
        pdfHideIfValueIsEmpty: false,
        pdfWidth: 1,
        requiredAmountOfEntries: 3,
        label: {
            text: {
                en: 'Part List 1',
                de: 'Ersatzteilliste 1',
                tr: 'Part List 1 [TR]',
                fr: 'Part List 1 [FR]',
                es: 'Part List 1 [ES]',
                it: 'Part List 1 [IT]',
            },
            pdfHide: false,
            pdfTextColor: '#facc2e',
            pdfTextSize: 14,
        },

        fields: {
            partNumberSingleLineTextInput: {
                required: true,
                pdfHide: false,
                placeHolderText: {
                    en: 'Part Number Placeholder Text',
                    de: 'Part Number Placeholder Text',
                    tr: 'Part Number Placeholder Text',
                    fr: 'Part Number Placeholder Text',
                    es: 'Part Number Placeholder Text',
                    it: 'Part Number Placeholder Text',
                },
            },
            quantityNumericInput: {
                required: true,
                pdfHide: false,
            },
            descriptionMultiLineTextInput: {
                enable: true,
                required: true,
                pdfHide: false,
                placeHolderText: {
                    en: 'Description Placeholder Text',
                    de: 'Description Placeholder Text',
                    tr: 'Description Placeholder Text',
                    fr: 'Description Placeholder Text',
                    es: 'Description Placeholder Text',
                    it: 'Description Placeholder Text',
                },
            },
            deliverToStaticSingleSelect: {
                enable: true,
                required: true,
                pdfHide: false,
            },
            invoiceToStaticSingleSelect: {
                enable: true,
                required: true,
                pdfHide: false,
            },
            warrantyBooleanInput: {
                enable: true,
                pdfHide: false,
            },
        },
    },
},
```

```typescript (minimal)
{
    id: 'exampleSparePartsList_1',
    type: FormFieldTypesEnum.PART_LIST_INPUT,
    config: {
        label: {
            text: {
                en: 'Part List 1',
                de: 'Ersatzteilliste 1',
                tr: 'Part List 1 [TR]',
                fr: 'Part List 1 [FR]',
                es: 'Part List 1 [ES]',
                it: 'Part List 1 [IT]',
            },
        },
        fields: {
            partNumberSingleLineTextInput: {
                required: true,
                pdfHide: false,
                placeHolderText: {
                    en: 'Part Number Placeholder Text',
                    de: 'Part Number Placeholder Text',
                    tr: 'Part Number Placeholder Text',
                    fr: 'Part Number Placeholder Text',
                    es: 'Part Number Placeholder Text',
                    it: 'Part Number Placeholder Text',
                },
            },
            quantityNumericInput: {
                required: true,
                pdfHide: false,
            },
            descriptionMultiLineTextInput: {
                enable: true,
                required: true,
                pdfHide: false,
                placeHolderText: {
                    en: 'Description Placeholder Text',
                    de: 'Description Placeholder Text',
                    tr: 'Description Placeholder Text',
                    fr: 'Description Placeholder Text',
                    es: 'Description Placeholder Text',
                    it: 'Description Placeholder Text',
                },
            },
            deliverToStaticSingleSelect: {
                enable: true,
                required: true,
                pdfHide: false,
            },
            invoiceToStaticSingleSelect: {
                enable: true,
                required: true,
                pdfHide: false,
            },
            warrantyBooleanInput: {
                enable: true,
                pdfHide: false,
            },
        },
    },
},
```
# Configuration Parameters
---
## `label`

| Property                                                    | Description                       |
| :---------------------------------------------------------- | :-------------------------------- |
| [text](./24-general-properties/#text)                       | Localized label text of the field. Shown in the UI and the PDF. |
| [pdfHide](./24-general-properties/#pdfhide)                 | Setting this to `true` hides the label in the PDF. |
| [pdfTextSize](./24-general-properties/#pdftextsize)         | Text size of the label in the PDF. |
| [pdfTextColor](./24-general-properties/#pdftextcolor)       | Text color of the label in the PDF. |

---
## `fields`

| Property                                                      | Description                       |
| :------------------------------------------------------------ | :-------------------------------- |
| [partNumberSingleLineTextInput](#partNumberSingleLineTextInput)                 | An Input field in the UI to enter a specific part number|
| [quantityNumericInput](#quantityNumericInput)         | An Input in the UI to enter the amount of the parts  |
| [descriptionMultiLineTextInput](#descriptionMultiLineTextInput)        | Multi line input field in the UI to enter a description of the part  |
| [deliverToStaticSingleSelect](#deliverToStaticSingleSelect)         | A single select field in the UI to choose the delivery destination |
| [invoiceToStaticSingleSelect](#invoiceToStaticSingleSelect)         | A single select field in the UI to choose the invoice destination |
| [warrantyBooleanInput](#warrantyBooleanInput)         | A checkbox in the UI to mark "Coverd under warranty" |

---

### `partNumberSingleLineTextInput`

| Property                                                      | Description                       |
| :------------------------------------------------------------ | :-------------------------------- |
| [pdfHide](./24-general-properties/#pdfhide)                                  | Setting this to `true` hides the whole field in the PDF. |
| [required](./24-general-properties/#required)                                | If this is set to `true`, the field is considered invalid as long as no value is entered. |
| [placeHolderText](./24-general-properties/#placeholdertext)                  | Localized placeholder text that is shown in the UI when the field is focused but does not have a value. |

---
### `quantityNumericInput`

| Property                                                      | Description                       |
| :------------------------------------------------------------ | :-------------------------------- |
| [pdfHide](./24-general-properties/#pdfhide)                                  | Setting this to `true` hides the whole field in the PDF. |
| [required](./24-general-properties/#required)                                | If this is set to `true`, the field is considered invalid as long as no value is entered. |

---
### `descriptionMultiLineTextInput`

| Property                                                      | Description                       |
| :------------------------------------------------------------ | :-------------------------------- |
| [pdfHide](./24-general-properties/#pdfhide)                                  | Setting this to `true` hides the whole field in the PDF. |
| [required](./24-general-properties/#required)                                | If this is set to `true`, the field is considered invalid as long as no value is entered. |
| [placeHolderText](./24-general-properties/#placeholdertext)                  | Localized placeholder text that is shown in the UI when the field is focused but does not have a value. |
| [enable](./24-general-properties/#enable)                  | Setting this to `true` enables the poperty in the UI |

---
### `deliverToStaticSingleSelect`

| Property                                                      | Description                       |
| :------------------------------------------------------------ | :-------------------------------- |
| [enable](./24-general-properties/#enable)                     | Setting this to `true` enables the poperty in the UI |
| [pdfHide](./24-general-properties/#pdfhide)                   | Setting this to `true` hides the whole field in the PDF. |
| [required](./24-general-properties/#required)                 | If this is set to `true`, the field is considered invalid as long as no value is entered. |

---
### `invoiceToStaticSingleSelect`

| Property                                                      | Description                       |
| :------------------------------------------------------------ | :-------------------------------- |
| [enable](./24-general-properties/#enable)                     | Setting this to `true` enables the poperty in the UI |
| [pdfHide](./24-general-properties/#pdfhide)                   | Setting this to `true` hides the whole field in the PDF. |
| [required](./24-general-properties/#required)                 | If this is set to `true`, the field is considered invalid as long as no value is entered. |

---
### `warrantyBooleanInput`

| Property                                                      | Description                       |
| :------------------------------------------------------------ | :-------------------------------- |
| [enable](./24-general-properties/#enable)                     | Setting this to `true` enables the poperty in the UI |
| [pdfHide](./24-general-properties/#pdfhide)                   | Setting this to `true` hides the whole field in the PDF. |
