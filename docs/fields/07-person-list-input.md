---
title: PersonListInput
category: 62ebf4654ae80e09e468624b
parentDoc: 62ec01bd561bab0aa775efe4
---

The PersonListInput field allows to enter user.
# Configuration Overview

| Property                                                                     | Description                      |
| :--------------------------------------------------------------------------- | :--------------------------------|
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
    id: 'examplePersonList_1',
    type: FormFieldTypesEnum.PERSON_LIST_INPUT,
    config: {
        disabled: false,
        pdfHide: false,
        pdfHideIfValueIsEmpty: false,
        requiredAmountOfEntries: 1,
        label: {
            text: {
                en: 'Person List 1',
                de: 'Person Ersatzteilliste 1',
                tr: 'Person List 1 [TR]',
                fr: 'Person List 1 [FR]',
                es: 'Person List 1 [ES]',
                it: 'Person List 1 [IT]',
            },
            pdfHide: false,
            pdfTextColor: '#facc2e',
            pdfTextSize: 14,
        },
        value: {
            pdfHide: false,
            pdfTextSize: 14,
            pdfTextColor: '#facc2e',
            pdfStartInNewLine: false,
            pdfAddLineBreaks: true,
            firstNameRequired: true,
            lastNameRequired: true,
            email: {
                required: true,
                pdfHide: false,
                hide: false,
            },
        },
    },
},
```

``` typescript (minimal)
{
    id: 'examplePersonList_1',
    type: FormFieldTypesEnum.PERSON_LIST_INPUT,
    config: {
        label: {
            text: {
                en: 'Person List 1',
                de: 'Person Ersatzteilliste 1',
                tr: 'Person List 1 [TR]',
                fr: 'Person List 1 [FR]',
                es: 'Person List 1 [ES]',
                it: 'Person List 1 [IT]',
            },
        },
        value: {
            firstNameRequired: true,
            lastNameRequired: true,
            email: {
                required: true,
                pdfHide: false,
                hide: false,
            },
        },
    },
},
```

---
# Configuration Parameters

## `label`

| Property                                                    | Description                       |
| :---------------------------------------------------------- | :-------------------------------- |
| [text](./24-general-properties/#text)                       | Localized label text of the field. Shown in the UI and the PDF. |
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
| [firstNameRequired](#firstnamerequired)                                         | Setting this to `true` makes field value mandatory to fill the form                             |
| [lastNameRequired](#lastnamerequired)                                           | Setting this to `true` makes field value mandatory to fill the form                                   |
| [email.required](./24-general-properties/#required)                             | If this is set to `true`, the field is considered invalid as long as no value is entered. |
| [email.pdfHide](./24-general-properties/#pdfhide)                               | Setting this to `true` hides the whole field in the PDF. |
| [email.hide](#hide)                                                             | Setting this to `true` hides the whole field in the UI and the PDF. |

---
## `firstNameRequired`

| `firstNameRequired`      |                 |
| :-------------- | :-------------- |
| Possible Values | `true`, `false` |
| Required        | no              |
| Default Value   | `false`         |

If `firstNameRequired` is set to `true`, the field is not shown in the PDF at all. 

``` typescript
firstNameRequired: true
```
---
## `lastNameRequired`

| `lastNameRequired`      |                 |
| :-------------- | :-------------- |
| Possible Values | `true`, `false` |
| Required        | no              |
| Default Value   | `false`         |

If `lastNameRequired` is set to `true`, the field is considered invalid as long as no value is entered.

``` typescript
lastNameRequired: true
```
---
## `hide`

| `hide`      |                 |
| :-------------- | :-------------- |
| Possible Values | `true`, `false` |
| Required        | no              |
| Default Value   | `false`         |

If `hide` is set to `true`, the field is not shown in the PDF and UI at all.

``` typescript
hide: true
```
