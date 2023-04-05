---
title: DateInput
category: 635ce1e7775bc60045570ffb
parentDoc: 635ce486ae5fac003cef279e
---


The DateInput field allows to input a date.
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

```json (complete)
{
  "id": "exampleDateInput_1",
  "type": "dateInput",
  "config": {
    "pdfHide": false,
    "disabled": false,
    "required": true,
    "pdfWidth": 0.7,
    "pdfHideIfValueIsEmpty": false,
    "label": {
      "text": {
        "en": "Date input 1",
        "de": "Date input 1 [DE]",
        "tr": "Date input 1 [TR]",
        "fr": "Date input 1 [FR]",
        "es": "Date input 1 [ES]",
        "it": "Date input 1 [IT]"
      },
      "uiHide": false,
      "pdfHide": false,
      "pdfTextSize": 14,
      "pdfTextColor": "#facc2e"
    },
    "value": {
      "pdfHide": false,
      "pdfTextSize": 14,
      "pdfTextColor": "#facc2e",
      "pdfStartInNewLine": false,
      "validators": {
        "minDate": "2000-02-22",
        "maxDate": "2022-02-22"
      },
      "autofill": ""
    },
    "prefill": {
      "value": [{
          "input": "none",
          "steps": [[
              "staticDate",
              "2022-02-22"
            ]]
        }]
    }
  }
},
```
```json (minimal)
{
  "id": "exampleDateInput_1",
  "type": "dateInput",
  "config": {
    "label": {
      "text": {
        "en": "Date input 1",
        "de": "Date input 1 [DE]",
        "tr": "Date input 1 [TR]",
        "fr": "Date input 1 [FR]",
        "es": "Date input 1 [ES]",
        "it": "Date input 1 [IT]"
      },
    },
    "value": {
    },
  }
},
```

---
# Configuration Parameters

## `label`

| Property                                                    | Description                       |
| :---------------------------------------------------------- | :-------------------------------- |
| [text](./24-general-properties/#text)                       | Localized label text of the field. Shown in the UI and the PDF. |
| [pdfHide](./24-general-properties/#pdfhide)                 | Setting this to `true` hides the label in the PDF. |
| [uiHide](./24-general-properties/#uihide)                   | Setting this to `true` hides the label in the UI. |
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
| [validators.minDate](#minDate)                                                  | Minimum number of characters for the input value to be valid.                                   |
| [validators.maxDate](#maxDate)                                                  | Maximum number of characters for the input value to be valid.                                   |
| autofill | Setting this to `always` will update the field with the current date every time the form is opened, regardless of the date being changed previously. Setting this to `only-empty` will autofill the current date only if field is empty |


---
### `validators.minDate`

| `validators.minDate`     |                 |
| :-------------- | :-------------- |
| Possible Values | date      |
| Required        | no              |
| Default Value   | -               |

By setting `validators.minDate`, the field will be marked as invalid if the date is later than the specified one.

```json
"validators": {
    "minDate": "2000-02-22"
}
```

---
### `validators.maxDate`

| `validators.maxDate`     |                 |
| :-------------- | :-------------- |
| Possible Values | date     |
| Required        | no              |
| Default Value   | -               |

By setting `validators.maxDate`, the field will be marked as invalid if the date is earlier than the specified one.

```json
"validators": {
    "maxDate": "2022-02-22"
}
```

---

## `prefill`

| `prefill`                  |                                                                     |
| :------------------------- | :--------------                                                     |
| Possible Values            | Array of [PrefillRules](./25-prefill-rules)            |
| Required                   | no                                                                  |
| Default Value              | -                                                                   |

This configuration follows the [general syntax for prefilling rules](./25-prefill-rules).
```json (static date)
"prefill": {
  "value": [{
      "input": "none",
      "steps": [[
          "staticDate",
          "2022-02-22"
        ]]
    }]
}
```
---
## `onChange`

| `onChange`                 |                                                                        |
| :------------------------- | :--------------                                                        |
| Possible Values            | Array of [DynamicFieldActions](./26-on-change-rules) |
| Required                   | no                                                                     |
| Default Value              | -                                                                      |


This configuration follows the [general syntax for dynamic field actions](./26-on-change-rules).


