---
title: TimeTrackingListInput
category: 635ce1e7775bc60045570ffb
parentDoc: 635ce486ae5fac003cef279e
---

The timeTrackingListInput allows the user to enter times for travel, working or breaks.
# Configuration Overview

| Property                                                                     | Description                      |
| :--------------------------------------------------------------------------- | :--------------------------------|
| [pdfHide](./24-general-properties/#pdfhide)                                  | Setting this to `true` hides the whole field in the PDF. |
| [pdfHideIfValueIsEmpty](./24-general-properties/#pdfhideifvalueisempty)      | Setting this to `true` hides the whole field in the PDF in case the field value is empty. |
| [pdfWidth](./24-general-properties/#pdfwidth)                                | Configuration of the width of the field. |
| [requiredAmountOfEntries](./24-general-properties/#requiredamountofentries)  | Specify how many repeating entries are required to fill the form.                                                                                        |
| [maximumDuration](#maximumduration)                                          | Configuration of a maximum duration that can be set in minutes. |
| [label](#label)                                                              | Configuration of the field label. |


```json (complete)
 {
    "id": "exampleTimeTrackingListInput_1",
    "type": "timeTrackingListInput",
    "config": {
        "pdfHide": false,
        "pdfHideIfValueIsEmpty": false,
        "pdfWidth": 1,
        "requiredAmountOfEntries": 3,
        "maximumDuration": 480,
        "label": {
            "text": {
                "en": "Time tracking input 1",
                "de": "Time tracking input 1 [DE]",
                "tr": "Time tracking input 1 [TR]",
                "fr": "Time tracking input 1 [FR]",
                "es": "Time tracking input 1 [ES]",
                "it": "Time tracking input 1 [IT]"
            },
            "pdfHide": false,
            "pdfTextSize": 14,
            "pdfTextColor": "#facc2e"
        },
        "fields": {
            "timeTrackingTypeStaticSingleSelect": {
                "pdfHide": false
            },
            "startDateTimeInput": {
                "pdfHide": false
            },
            "endDateTimeInput": {
                "pdfHide": false
            },
            "breakNumericInput": {
                "disabled": false,
                "required": true,
                "pdfHide": false
            },
            "durationDisplay": {
                "disabled": false,
                "pdfHide": false
            },
            "distanceNumericInput": {
                "disabled": false,
                "required": true,
                "pdfHide": false
            },
            "technicianUserSingleSelect": {
                "disabled": false,
                "required": true,
                "pdfHide": false,
                "pdfPrintEmailAddress": true
            },
            "commentMultiLineTextInput": {
                "disabled": false,
                "required": true,
                "pdfHide": false
            }
        }
    }
},
```
```json (minimal)
 {
    "id": "exampleTimeTrackingListInput_1",
    "type": "timeTrackingListInput",
    "config": {
        "label": {
            "text": {
                "en": "Time tracking input 1",
                "de": "Time tracking input 1 [DE]",
                "tr": "Time tracking input 1 [TR]",
                "fr": "Time tracking input 1 [FR]",
                "es": "Time tracking input 1 [ES]",
                "it": "Time tracking input 1 [IT]"
            },
        },
    }
},
```

---
# Configuration Parameters

## `maximumDuration`

| `maximumDuration` |                 |
| :------------------------- | :-------------- |
| Possible Values            | Integer |
| Required                   | no              |
| Default Value              | -       |

 `maximumDuration` can be set in minutes. (e.g. 480; = 8h). If this duration (e.g. 8h working time) is exceeded by setting start and end datetime & breaks, input is considered invalid.

 ```json 
"maximumDuration": 480; // = 8 h
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

## `fields`

| Property                                                      | Description                       |
| :------------------------------------------------------------ | :-------------------------------- |
| [timeTrackingTypeStaticSingleSelect](#timetrackingtypestaticsingleselect)                 | User can select between different types which should be tracked |
| [startDateTimeInput](#startdatetimeinput)                     | UI section that contains the start date and time incl. timezone |
| [endDateTimeInput](#enddatetimeinput)                         | UI section that contains the end date and time incl. timezone |
| [breakNumericInput](#breaknumericinput)                       | UI section to enter break time|
| [durationDisplay](#durationdisplay)                           | Displays the duration of the entered times in the UI |
| [distanceNumericInput](#distancenumericinput)                 | UI input field to enter a distance in km |
| [technicianUserSingleSelect](#technicianusersingleselect)     | UI section where the user can select the respective technician |
| [commentMultiLineTextInput](./24-general-properties/#commenmultilinetextinput)        | Defines a comment section as multiLineTextInput  |

---
### `timeTrackingTypeStaticSingleSelect`

| Property                                                      | Description                       |
| :------------------------------------------------------------ | :-------------------------------- |
| [pdfHide](./24-general-properties/#pdfhide)                 | Setting this to `true` hides the label in the PDF. |

---
### `startDateTimeInput`

| Property                                                      | Description                       |
| :------------------------------------------------------------ | :-------------------------------- |
| [pdfHide](./24-general-properties/#pdfhide)                 | Setting this to `true` hides the label in the PDF. |

---
### `endDateTimeInput`

| Property                                                      | Description                       |
| :------------------------------------------------------------ | :-------------------------------- |
| [pdfHide](./24-general-properties/#pdfhide)                 | Setting this to `true` hides the label in the PDF. |

---
### `breakNumericInput`

| Property                                                      | Description                       |
| :------------------------------------------------------------ | :-------------------------------- |
| [required](./24-general-properties/#required)                 | If this is set to `true`, the field is considered invalid as long as no value is entered. |
| [disabled](./24-general-properties/#disabled)                 | Setting this to `true` permanently disables the field in the UI. |
| [pdfHide](./24-general-properties/#pdfhide)                   | Setting this to `true` hides the label in the PDF. |

---
### `durationDisplay`

| Property                                                      | Description                       |
| :------------------------------------------------------------ | :-------------------------------- |
| [disabled](./24-general-properties/#disabled)                 | Setting this to `true` permanently disables the field in the UI. |
| [pdfHide](./24-general-properties/#pdfhide)                 | Setting this to `true` hides the label in the PDF. |

---
### `distanceNumericInput`

| Property                                                      | Description                       |
| :------------------------------------------------------------ | :-------------------------------- |
| [required](./24-general-properties/#required)                 | If this is set to `true`, the field is considered invalid as long as no value is entered. |
| [disabled](./24-general-properties/#disabled)                 | Setting this to `true` permanently disables the field in the UI. |
| [pdfHide](./24-general-properties/#pdfhide)                   | Setting this to `true` hides the label in the PDF. |

---
### `technicianUserSingleSelect`

| Property                                                      | Description                       |
| :------------------------------------------------------------ | :-------------------------------- |
| [required](./24-general-properties/#required)                 | If this is set to `true`, the field is considered invalid as long as no value is entered. |
| [disabled](./24-general-properties/#disabled)                 | Setting this to `true` permanently disables the field in the UI. |
| [pdfHide](./24-general-properties/#pdfhide)                   | Setting this to `true` hides the label in the PDF. |