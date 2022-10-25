---
title: TaskListInput
category: 62ebf4654ae80e09e468624b
parentDoc: 62ec01bd561bab0aa775efe4
---

TaskListInput enables the user to create performed tasks.

---
# Configuration Overview

| Property                                                                     | Description                      |
| :--------------------------------------------------------------------------- | :--------------------------------|
| [pdfHide](./24-general-properties/#pdfhide)                                  | Setting this to `true` hides the whole field in the PDF. |
| [pdfHideIfValueIsEmpty](./24-general-properties/#pdfhideifvalueisempty)      | Setting this to `true` hides the whole field in the PDF in case the field value is empty. |
| [pdfWidth](./24-general-properties/#pdfwidth)                                | Configuration of the width of the field. |
| [requiredAmountOfEntries](./24-general-properties/#requiredamountofentries)  | Specify how many repeating entries are requried to fill the form.                                                                                        |
| [label](#label)                                                              | Configuration of the field label. |
| [prefill](#prefill)                                                          | Configuration to prefill the field with a value upon creation of the form instance. |
| [fields](#fields)                                     | Components of the field |


``` JSON (complete)
 {
    "id": "exampleTaskListInput_1",
    "type": "taskListInput",
    "config": {
        "pdfHide": false,
        "pdfHideIfValueIsEmpty": false,
        "pdfWidth": 1,
        "requiredAmountOfEntries": 2,
        "label": {
            "pdfHide": false,
            "pdfTextColor": "#facc2e",
            "pdfTextSize": 14,
            "text": {
                "en": "Boolean input 1",
                "de": "Boolean input 1 [DE]",
                "tr": "Boolean input 1 [TR]",
                "fr": "Boolean input 1 [FR]",
                "es": "Boolean input 1 [ES]",
                "it": "Boolean input 1 [IT]"
            }
        },
        "fields": {
            "checkboxBooleanInput": {
                "checkedByDefault": false,
                "pdfHide": false
            },
            "titleSingleLineTextInput": {
                "required": false,
                "pdfHide": false
            },
            "commentMultiLineTextInput": {
                "disabled": false,
                "required": false,
                "pdfHide": false
            },
            "highPrioBooleanInput": {
                "disabled": false,
                "pdfHide": false
            },
            "notNecessaryBooleanInput": {
                "disabled": false,
                "pdfHide": false
            }
        },
        "prefill": {
            "entries": [{
                "input": "none",
                "steps": [[
                    "staticTasks",
                    [{
                        "done": false,
                        "title": "Task 1",
                        "comment": "This task was prefilled 1",
                        "highPriority": false,
                        "necessary": false
                        },
                        {
                        "done": false,
                        "title": "Task 2",
                        "comment": "This task was prefilled 2",
                        "highPriority": true,
                        "necessary": true
                        },
                        {
                        "done": true,
                        "title": "Task 3",
                        "comment": "This task was prefilled 3",
                        "highPriority": false,
                        "necessary": true
                        },
                        {
                        "done": false,
                        "title": "Task 4",
                        "comment": "This task was prefilled 4",
                        "highPriority": true,
                        "necessary": false
                        }]
                    ]]
                }]
        }
    }
},
```
``` JSON (minimal)
 {
    "id": "exampleTaskListInput_2",
    "type": "taskListInput",
    "config": {
        "label": {
            "text": {
                "en": "Boolean input 1",
                "de": "Boolean input 1 [DE]",
                "tr": "Boolean input 1 [TR]",
                "fr": "Boolean input 1 [FR]",
                "es": "Boolean input 1 [ES]",
                "it": "Boolean input 1 [IT]"
            }
        },
        "fields": {
            "checkboxBooleanInput": {
                "checkedByDefault": false,
            },
        },
    }
},
```

---
## `label`

| Property                                                    | Description                       |
| :---------------------------------------------------------- | :-------------------------------- |
| [text](./24-general-properties/#text)                       | Localized label text of the field. Shown in the UI and the PDF. |
| [pdfHide](./24-general-properties/#pdfhide)                 | Setting this to `true` hides the label in the PDF. |
| [pdfTextSize](./24-general-properties/#pdftextsize)         | Text size of the label in the PDF. |
| [pdfTextColor](./24-general-properties/#pdftextcolor)       | Text color of the label in the PDF. |

---
## `prefill`

| `prefill`                  |                                                                     |
| :------------------------- | :--------------                                                     |
| Possible Values            | [PrefillRules](./25-prefill-rules)  |
| Required                   | no                                                                  |
| Default Value              | -                                                                   |

This configuration follows the [general syntax for prefilling rules](./25-prefill-rules).

``` JSON (set prefilled tasks)
"prefill": {
    "entries": [{
        "input": "none",
        "steps": [[
            "staticTasks",
            [{
                "done": false,
                "title": "Task 1",
                "comment": "This task was prefilled 1",
                "highPriority": false,
                "necessary": false
                },
                {
                "done": false,
                "title": "Task 2",
                "comment": "This task was prefilled 2",
                "highPriority": true,
                "necessary": true
                },
                {
                "done": true,
                "title": "Task 3",
                "comment": "This task was prefilled 3",
                "highPriority": false,
                "necessary": true
                },
                {
                "done": false,
                "title": "Task 4",
                "comment": "This task was prefilled 4",
                "highPriority": true,
                "necessary": false
                }]
            ]]
        }]
},
```
``` JSON (set workorder tasks)
"prefill": {
    "entries": [{
            "input": "workOrderId",
            "steps": [ "workOrderIdToWorkOrder", "workOrderToTasks" ],
        }]
},
```

---
## `fields`

| Property                                                      | Description                       |
| :------------------------------------------------------------ | :-------------------------------- |
| [checkboxBooleanInput](#checkboxbooleaninput)                 | Checkbox, that can be set checked per dafault |
| [titleSingleLineTextInput](#titlesinglelinetextinput)         | Titel of the task that is shown in the UI and PDF |
| [commentMultiLineTextInput](./24-general-properties/#commenmultilinetextinput)        | Defines a comment section as multiLineTextInput  |
| [highPrioBooleanInput](#highpriobooleaninput)         | `High prio` checkbox of the task that is shown in the UI and PDF |
| [notNecessaryBooleanInput](#notnecessarybooleaninput)         | `Not necessary` checkbox of the task that is shown in the UI and PDF |

---
### `checkboxBooleanInput`

| Property               | Description                                                                               |
| :----------------------| :---------------------------------------------------------------------------------------- |
| [checkedByDefault](#checkedbydefault)                                | If this is set to `true`, the checkbox is checked by default. |
| [pdfHide](./24-general-properties/#pdfhide)                                  | Setting this to `true` hides the label in the PDF. |

### `titleSingleLineTextInput`

| Property               | Description                                                                               |
| :----------------------| :---------------------------------------------------------------------------------------- |
| [required](./24-general-properties/#required)                                | If this is set to `true`, the field is considered invalid as long as no value is entered. |
| [pdfHide](./24-general-properties/#pdfhide)                                  | Setting this to `true` hides the label in the PDF. |

### `highPrioBooleanInput`

| Property               | Description                                                                               |
| :----------------------| :---------------------------------------------------------------------------------------- |
| [disabled](./24-general-properties/#disabled)                                | Setting this to `true` permanently disables the field in the UI. |
| [pdfHide](./24-general-properties/#pdfhide)                                  | Setting this to `true` hides the label in the PDF. |

### `notNecessaryBooleanInput`

| Property               | Description                                                                               |
| :----------------------| :---------------------------------------------------------------------------------------- |
| [disabled](./24-general-properties/#disabled)                                | Setting this to `true` permanently disables the field in the UI. |
| [pdfHide](./24-general-properties/#pdfhide)                                  | Setting this to `true` hides the label in the PDF. |
