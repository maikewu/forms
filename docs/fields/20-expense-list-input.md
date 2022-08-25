---
title: ExpenseListInput
category: 62ebf4654ae80e09e468624b
parentDoc: 62ec01bd561bab0aa775efe4
---

>🚧 
>
> In progress

The Expense List Input allows the user to add expenses.

# Configuration Overview

| Property                                              | Description                      |
| :---------------------------------------------------- | :--------------------------------|
| [pdfHide](#pdfhide)                                   | Setting this to `true` hides the whole field in the PDF. |
| [pdfHideIfValueIsEmpty](#pdfhideifvalueisempty)       | Setting this to `true` hides the whole field in the PDF in case the field value is empty. |
| [pdfWidth](#pdfwidth)                                 | Configuration of the width of the field. |
| [requiredAmountOfEntries](#requiredamountofentries)   | The value specifies the required amount of entries to fill the form |
| [fields](#fields)                                     | ??? |


```typescript (complete)
{
    id: 'exampleExpenseListInput_1',
    type: FormFieldTypesEnum.EXPENSE_LIST_INPUT,
    config: {
        pdfHide: false,
        pdfHideIfValueIsEmpty: false,
        requiredAmountOfEntries: 2,
        fields: {
            dateInput: {
                pdfHide: false,
                disabled: false,
                required: true,
            },
            commentMultiLineTextInput: {
                pdfHide: false,
                disabled: false,
                required: true,
            },
            expenseAmountNumericInput: {
                pdfHide: false,
                disabled: false,
                required: true,
            },
            expenseTypeSingleSelectInput: {
                pdfHide: false,
                disabled: false,
                required: true,
                values: {
                    exampleSelect_1: {
                        en: 'Example select 1',
                        de: 'Example select 1 [DE]',
                        tr: 'Example select 1 [TR]',
                        fr: 'Example select 1 [FR]',
                        es: 'Example select 1 [ES]',
                        it: 'Example select 1 [IT]',
                    },
                    exampleSelect_2: {
                        en: 'Example select 2',
                        de: 'Example select 2 [DE]',
                        tr: 'Example select 2 [TR]',
                        fr: 'Example select 2 [FR]',
                        es: 'Example select 2 [ES]',
                        it: 'Example select 2 [IT]',
                    },
                },
            },
        },
    },
},

```

```typescript (minimal)
{
                    id: 'exampleExpenseListInput_1',
                    type: FormFieldTypesEnum.EXPENSE_LIST_INPUT,
                    config: {
                    },
}
```

---
## `requiredAmountOfEntries`

| `requiredAmountOfEntries`   |                 |
| :-------------------------- | :-------------- |
| Possible Values             | Integer         |
| Required                    | no              |
| Default Value               | 0               |

The value of `requiredAmountOfEntries` can specify how many repeating entries (expenses) are required to fill the form.

``` typescript
requiredAmountOfEntries: 3
```

---
## `fields`

| Property                                                      | Description                       |
| :------------------------------------------------------------ | :-------------------------------- |
| [dateInput](#dateinput)                                       | Setting this to `true` makes field value mandatory |
| [expenseTypeSingleSelectInput](#expensetypesingleselectinput) | Defines a set of types which can be selected as the kind of entry (expense) |
| [commentMultiLineTextInput](#commenmultilinetextinput)        | ??? |
| [expenseAmountNumericInput](#expenseamountnumericinput)       | ??? |

---
### `dateInput`

| Property               | Description                                                                               |
| :----------------------| :---------------------------------------------------------------------------------------- |
| [required](#required)  | If this is set to `true`, the field is considered invalid as long as no value is entered. |
| [disabled](#disabled)  | Setting this to `true` permanently disables the field in the UI.                          |
| [pdfHide](#pdfhide)    | Setting this to `true` hides the whole field in the PDF.                                  |

---
### `expenseTypeSingleSelectInput`

| Property               | Description                                                                               |
| :----------------------| :---------------------------------------------------------------------------------------- |
| [required](#required)  | If this is set to `true`, the field is considered invalid as long as no value is entered. |
| [disabled](#disabled)  | Setting this to `true` permanently disables the field in the UI.                          |
| [pdfHide](#pdfhide)    | Setting this to `true` hides the whole field in the PDF.                                  |
| [values](#values)      | The values defines the kind of entries (expenses) that the user can select.               |

---
### `commentMultiLineTextInput`

| Property               | Description                                                                               |
| :----------------------| :---------------------------------------------------------------------------------------- |
| [required](#required)  | If this is set to `true`, the field is considered invalid as long as no value is entered. |
| [disabled](#disabled)  | Setting this to `true` permanently disables the field in the UI.                          |
| [pdfHide](#pdfhide)    | Setting this to `true` hides the whole field in the PDF.                                  |

---
### `expenseAmountNumericInput`

| Property               | Description                                                                               |
| :----------------------| :---------------------------------------------------------------------------------------- |
| [required](#required)  | If this is set to `true`, the field is considered invalid as long as no value is entered. |
| [disabled](#disabled)  | Setting this to `true` permanently disables the field in the UI.                          |
| [pdfHide](#pdfhide)    | Setting this to `true` hides the whole field in the PDF.                                  |





