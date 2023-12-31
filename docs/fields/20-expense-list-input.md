---
title: ExpenseListInput
category: 635ce1e7775bc60045570ffb
parentDoc: 635ce486ae5fac003cef279e
---

The Expense List Input allows the user to add expenses.

# Configuration Overview

| Property                                              | Description                      |
| :---------------------------------------------------- | :--------------------------------|
| [pdfHide](./24-general-properties/#pdfhide)                                  | Setting this to `true` hides the whole field in the PDF. |
| [pdfHideIfValueIsEmpty](./24-general-properties/#pdfhideifvalueisempty)      | Setting this to `true` hides the whole field in the PDF in case the field value is empty. |
| [pdfWidth](./24-general-properties/#pdfwidth)                                | Configuration of the width of the field. |
| [requiredAmountOfEntries](./24-general-properties/#requiredamountofentries)  | Specify how many repeating entries are required to fill the form.                                                                                        |
| [label](#label)                                                              | Configuration of the field label. |
| [fields](#fields)                                     | Components of the field |


```json (complete)
{ 
    "id": "exampleExpenseListInput_1",
    "type": "expenseListInput",
    "config": {
        "pdfHide": false,
        "pdfHideIfValueIsEmpty": false,
        "pdfWidth": 1,  
        "requiredAmountOfEntries": 2,
        "label": {
            "text": {
                "en": "Expense List 1",
                "de": "Ausgabenliste 1",
                "tr": "Expense List 1 [TR]",
                "fr": "Expense List 1 [FR]",
                "es": "Expense List 1 [ES]",
                "it": "Expense List 1 [IT]"
            },
            "pdfHide": false,
            "pdfTextColor": "#facc2e",
            "pdfTextSize": 14,
            "uiHide": false
        },
        "fields": {
            "dateInput": {
            "pdfHide": false,
            "disabled": false,
            "required": true
            },
            "commentMultiLineTextInput": {
            "pdfHide": false,
            "disabled": false,
            "required": true
            },
            "expenseAmountNumericInput": {
            "pdfHide": false,
            "disabled": false,
            "required": true
            },
            "expenseTypeSingleSelectInput": {
                "pdfHide": false,
                "disabled": false,
                "required": true,
                "values": {
                    "flight": {
                        "de": "Flug",
                        "en": "Flight"
                    },
                    "rental_car": {
                        "de": "Mietauto",
                        "en": "Rental Car"
                    },
                    "board": {
                        "de": "Verpflegung",
                        "en": "Board"
                    },
                    "accommodation": {
                        "de": "Unterkunft",
                        "en": "Accommodation"
                    },
                    "parking": {
                        "de": "Parken",
                        "en": "Parking"
                    },
                    "toll": {
                        "de": "Maut",
                        "en": "Toll"
                    },
                    "transportation": {
                        "de": "Transport",
                        "en": "Transportation"
                    },
                    "vignette": {
                        "de": "Vingette",
                        "en": "Vingette"
                    },
                    "other": {
                        "de": "Sonstiges",
                        "en": "Other"
                    },                        
                 }
            }
        }
    }
}
```
```json (minimal)
{
    "id": "exampleExpenseListInput_1",
    "type": "expenseListInput",
    "config": {
        "label": {
            "text": {
                "en": "Expense List 1",
                "de": "Ausgabenliste 1",
                "tr": "Expense List 1 [TR]",
                "fr": "Expense List 1 [FR]",
                "es": "Expense List 1 [ES]",
                "it": "Expense List 1 [IT]"
            }
        },
        "fields": {
            "expenseTypeSingleSelectInput": {
                "pdfHide": false,
                "disabled": false,
                "required": true,
                "values": {
                    "flight": {
                        "de": "Flug",
                        "en": "Flight"
                    },
                    "rental_car": {
                        "de": "Mietauto",
                        "en": "Rental Car"
                    },
                    "board": {
                        "de": "Verpflegung",
                        "en": "Board"
                    },
                    "accommodation": {
                        "de": "Unterkunft",
                        "en": "Accommodation"
                    },
                    "parking": {
                        "de": "Parken",
                        "en": "Parking"
                    },
                    "toll": {
                        "de": "Maut",
                        "en": "Toll"
                    },
                    "transportation": {
                        "de": "Transport",
                        "en": "Transportation"
                    },
                    "vignette": {
                        "de": "Vingette",
                        "en": "Vingette"
                    },
                    "other": {
                        "de": "Sonstiges",
                        "en": "Other"
                    },                        
                 }
            }
        }
    }
}
```
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
| [dateInput](#dateinput)                                       | Date selection is part of the field |
| [expenseTypeSingleSelectInput](#expensetypesingleselectinput) | Defines a set of types which can be selected as the kind of entry (expense) |
| [commentMultiLineTextInput](./24-general-properties/#commenmultilinetextinput)        | Defines a comment section as multiLineTextInput  |
| [expenseAmountNumericInput](#expenseamountnumericinput)       | Defines a input section where the amount of the expense can be entered |

---
### `dateInput`

| Property               | Description                                                                               |
| :----------------------| :---------------------------------------------------------------------------------------- |
| [required](./24-general-properties/#required)                                | If this is set to `true`, the field is considered invalid as long as no value is entered. |
| [disabled](./24-general-properties/#disabled)                                | Setting this to `true` permanently disables the field in the UI. |
| [pdfHide](./24-general-properties/#pdfhide)                 | Setting this to `true` hides the label in the PDF. |

---
### `expenseAmountNumericInput`

| Property               | Description                                                                               |
| :----------------------| :---------------------------------------------------------------------------------------- |
| [required](./24-general-properties/#required)                                | If this is set to `true`, the field is considered invalid as long as no value is entered. |
| [disabled](./24-general-properties/#disabled)                                | Setting this to `true` permanently disables the field in the UI. |
| [pdfHide](./24-general-properties/#pdfhide)                 | Setting this to `true` hides the label in the PDF. |

---
### `expenseTypeSingleSelectInput`

| Property               | Description                                                                               |
| :----------------------| :---------------------------------------------------------------------------------------- |
| [required](./24-general-properties/#required)                                | If this is set to `true`, the field is considered invalid as long as no value is entered. |
| [disabled](./24-general-properties/#disabled)                                | Setting this to `true` permanently disables the field in the UI. |
| [pdfHide](./24-general-properties/#pdfhide)                 | Setting this to `true` hides the label in the PDF. |
| [values](#values)      | The values defines the kind of entries (expenses) that the user can select.               |

---
#### `values`

| `values`       |                 |
| :-------------- | :-------------- |
| Possible Values | `MultiLanguageText`   |
| Required        | no              |
| Default Value   | -             |

In `values` the content of the dropdown can be defined.

```json
"values": {
    "exampleSelect_1": {
        "en": "Example select 1",
        "de": "Example select 1 [DE]",
        "tr": "Example select 1 [TR]",
        "fr": "Example select 1 [FR]",
        "es": "Example select 1 [ES]",
        "it": "Example select 1 [IT]"
        },
    "exampleSelect_2": {
        "en": "Example select 2",
        "de": "Example select 2 [DE]",
        "tr": "Example select 2 [TR]",
        "fr": "Example select 2 [FR]",
        "es": "Example select 2 [ES]",
        "it": "Example select 2 [IT]"
    }
}
```


