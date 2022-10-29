---
title: SingleLineTextInput
category: 635ce1e7775bc60045570ffb
parentDoc: 635ce486ae5fac003cef279e
---

The SingleLineTextInput field allows entering one line of unformatted text. It dosen't respects line breaks.

# Configuration Overview

| Property                                                                     | Description                      |
| :--------------------------------------------------------------------------- | :--------------------------------|
| [required](./24-general-properties/#required)                                | If this is set to `true`, the field is considered invalid as long as no value is entered. |
| [disabled](./24-general-properties/#disabled)                                | Setting this to `true` permanently disables the field in the UI. |
| [pdfHide](./24-general-properties/#pdfhide)                                  | Setting this to `true` hides the whole field in the PDF. |
| [pdfHideIfValueIsEmpty](./24-general-properties/#pdfhideifvalueisempty)      | Setting this to `true` hides the whole field in the PDF in case the field value is empty. |
| [pdfWidth](./24-general-properties/#pdfwidth)                                | Configuration of the width of the field. |
| [placeHolderText](./24-general-properties/#placeholdertext)                  | Localized placeholder text that is shown in the UI when the field is focused but does not have a value. |
| [label](#label)                                                              | Configuration of the field label. |
| [value](#value)                                                              | Configuration of the field value. |
| [prefill](#prefill)                                                          | Configuration to prefill the field with a value upon creation of the form instance. |
| [onChange](#onchange)                                                        | Configuration to change the field with a certain value when pre defined event get executed | 

``` JSON (complete)
{
  "id": "exampleSingleLineInput_1",
  "type": "singleLineInput",
  "config": {
      "required": true,
      "disabled": false,
      "pdfHide": false,
      "pdfHideIfValueIsEmpty": false,
      "pdfWidth": 0.5,
      "placeHolderText": {
        "en": "Example Placeholder",
        "de": "Platzhalter",
        "tr": "Example Placeholder [TR]",
        "fr": "Example Placeholder [FR]",
        "es": "Example Placeholder [ES]",
        "it": "Example Placeholder [IT]"
      },
      "label": {
          "text": {
                "en": "Single Line Input 1",
                "de": "Einzeiliger Input 1",
                "tr": "Single Line Input 1 [TR]",
                "fr": "Single Line Input 1 [FR]",
                "es": "Single Line Input 1 [ES]",
                "it": "Single Line Input 1 [IT]"
          },
          "pdfHide": false,
          "pdfTextColor": "#facc2e",
          "pdfTextSize": 14,
          "uiHide": false,
      },
      "value": {
          "pdfHide": false,
          "pdfStartInNewLine": false,
          "pdfTextColor": "#facc2e",
          "pdfTextSize": 14,
          "validators": {
              "emailAddress": false,
              "maxCharacters": 10,
              "minCharacters": 3,
              "regexPattern": "^[A-Z]*$",
          },
      },
      "prefill": {
        "value": [{
                "input": "assetId",
                "steps": [ "assetIdToAsset", "assetToAssetTypeNameString"],
        }], 
      },
  },
},
```
``` JSON (minimal)
{
  "id": "exampleSingleLineInput_1",
  "type": "singleLineInput",
  "config": {
      "label": {
          "text": {
                "en": "Single Line Input 1",
                "de": "Einzeiliger Input 1",
                "tr": "Single Line Input 1 [TR]",
                "fr": "Single Line Input 1 [FR]",
                "es": "Single Line Input 1 [ES]",
                "it": "Single Line Input 1 [IT]"
          },
      },
      "value": {
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
| [validators.minCharacters](./24-general-properties/#validatorsmincharacters)    | Minimum number of characters for the input value to be valid.                                   |
| [validators.maxCharacters](./24-general-properties/#validatorsmaxcharacters)    | Maximum number of characters for the input value to be valid.                                   |
| [validators.emailAddress](#validatorsemailaddress)                              | Setting this to `true` forces the input to match email address format.                                              |
| [validators.regexPattern](#validatorsregexpattern)                              | Defines regular expression that is valid                          |

---
### `validators.emailAddress`

| `validators.emailAddress`     |                 |
| :-------------- | :-------------- |
| Possible Values | `true`, `false`     |
| Required        | no              |
| Default Value   | `false`               |

By setting `emailAddress` to `true`, input must match email address format.

```JSON
"validators": {
"emailAddress": true
}
```

---
### `validators.regexPattern`

| `validators.regexPattern`     |                 |
| :-------------- | :-------------- |
| Possible Values | String     |
| Required        | no              |
| Default Value   | `NULL`              |

By defining `validators.regexPattern`, you set a regular expression that is valid. 
```JSON
"validators":{
"regexPattern": "^[A-Z]*$"
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

``` JSON (static string)
"prefill": {
        "value": [{
                "input": "none",
                "steps": [[ "staticString", "Default Single Line Text" ]]
        }]
    },
```
``` JSON (asset type name)
"prefill": {
        "value": [{
                "input": "assetId",
                "steps": [ "assetIdToAsset", "assetToAssetTypeNameString"],
        }],
},
```

---
## `onChange`

| `onChange`                 |                                                                        |
| :------------------------- | :--------------                                                        |
| Possible Values            | Array of [DynamicFieldActions](./26-on-change-rules) |
| Required                   | no                                                                     |
| Default Value              | -                                                                      |


This configuration follows the [general syntax for dynamic field actions](./26-on-change-rules).