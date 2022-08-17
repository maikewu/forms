---
title: ExpenseListInput
category: 62ebf4654ae80e09e468624b
parentDoc: 62ec01bd561bab0aa775efe4
---

>🚧 
>
> In progress

***???DESCRIBTION???***

# Configuration Overview

| Property                                              | Description                      |
| :---------------------------------------------------- | :--------------------------------|
| [pdfHide](#pdfhide)                                   | Setting this to `true` hides the whole field in the PDF. |
| [pdfHideIfValueIsEmpty](#pdfhideifvalueisempty)       | Setting this to `true` hides the whole field in the PDF in case the field value is empty. |
| [pdfWidth](#pdfwidth)                                 | Configuration of the width of the field. |
| [requiredAmountOfEntries](#requiredamountofentries)   | ??? |
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
# Configuration Parameters

## `pdfHide`

| `pdfHide`      |                 |
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
| :------------------------- | :-------------- |
| Possible Values            | `true`, `false` |
| Required                   | no              |
| Default Value              | `false`         |

If `pdfHideIfValueIsEmpty` is set to `true` and the field value is empty, the field is not shown in the PDF at all.
If the field value is not empty, the field will still be shown (unless `pdfHide` is not set to `true`). 

``` typescript
pdfHideIfValueIsEmpty: true
```

---
## `pdfWidth`

| `pdfWdith`                 |                      |
| :------------------------- | :------------------- |
| Possible Values            | `0.25, 0.3, 0.5, 1`  |
| Required                   | no                   |
| Default Value              | `1 (full wdith)`     |

*???Description???*

``` typescript
pdfWidth: 0.5
```

---
## `requiredAmountOfEntries`

| `requiredAmountOfEntries`   |                 |
| :-------------------------- | :-------------- |
| Possible Values             |  |
| Required                    | no              |
| Default Value               |          |

???

``` typescript
requiredAmountOfEntries: 
```

---
## `fields`

| Property                                                      | Description                       |
| :------------------------------------------------------------ | :-------------------------------- |
| [dateInput](#dateinput)                                       | ??? |
| [expenseTypeSingleSelectInput](#expensetypesingleselectinput) | ??? |
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
| [values](#values)      | ???                                  |

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

---
#### `required`

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
#### `disabled`

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
#### `pdfHide`

| `pdfHide`      |                 |
| :-------------- | :-------------- |
| Possible Values | `true`, `false` |
| Required        | no              |
| Default Value   | `false`         |

If `pdfHide` is set to `true`, the field is not shown in the PDF at all. This takes precedence over `pdfHideIfValueIsEmpty`.

``` typescript
pdfHide: true
```

---
#### `values`

| `values`      |                 |
| :-------------- | :-------------- |
| Possible Values | [SelectOptionDictionary] (#todo) |
| Required        | no              |


???
``` typescript
???
```

![](https://drive.google.com/uc?export=view&id=1-3lrykYKpzDD4GXOAMF53Xn97UuacEpm)