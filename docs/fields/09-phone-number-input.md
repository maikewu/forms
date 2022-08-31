---
title: PhoneNumberInput
category: 62ebf4654ae80e09e468624b
parentDoc: 62ec01bd561bab0aa775efe4
---

# PhoneNumberInput
>🚧 
>
> In progress

The PhoneNumberInput field allows to input telephone numbers in the common format.
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
| [onChange](#onchange)                                                        | ??? |

``` typescript (complete)
{
    id: 'examplePhoneNumberInput_1',
    type: FormFieldTypesEnum.PHONE_NUMBER_INPUT,
    config: {
        disabled: false,
        required: true,
        pdfHide: false,
        pdfHideIfValueIsEmpty: false,
        uiHideInRepeaterCardDisplay: false,
        pdfWidth: 0.5,
        placeHolderText: {
            en: 'Phone number input placeholder',
            de: 'Phone number input placeholder [DE]',
            tr: 'Phone number input placeholder [TR]',
            fr: 'Phone number input placeholder [FR]',
            es: 'Phone number input placeholder [ES]',
            it: 'Phone number input placeholder [IT]',
        },
        label: {
            text: {
                en: 'Phone number input required',
                de: 'Phone number input required [DE]',
                tr: 'Phone number input required [TR]',
                fr: 'Phone number input required [FR]',
                es: 'Phone number input required [ES]',
                it: 'Phone number input required [IT]',
            },
            pdfHide: false,
            pdfTextColor: '#facc2e',
            pdfTextSize: 14,
        },
        value: {
            pdfHide: false,
            pdfStartInNewLine: false,
            pdfTextColor: '#facc2e',
            pdfTextSize: 14,
            validators: {
                maxCharacters: 11,
            },
        },
        prefill: {
            value: [
                {
                    input: 'none',
                    steps: [
                        [
                            'staticPhoneNumber',
                            {
                                countryPrefix: '49',
                                number: '1753463937',
                            },
                        ],
                    ],
                },
            ],
        },
    },
},
```
``` typescript (minimal)
{ 
  id: 'examplePhoneNumberInput_1',
  type: FormFieldTypesEnum.PHONE_NUMBER_INPUT,
  config: {
      required: true,
      pdfWidth: 0.5,
      label: {
          text: {
              en: 'Phone number input required',
              de: 'Phone number input required [DE]',
              tr: 'Phone number input required [TR]',
              fr: 'Phone number input required [FR]',
              es: 'Phone number input required [ES]',
              it: 'Phone number input required [IT]',
          },
          pdfHide: false,
          pdfTextColor: '#facc2e',
          pdfTextSize: 14,
      },
      value: {
          pdfHide: false,
          pdfStartInNewLine: false,
          pdfTextColor: '#facc2e',
          pdfTextSize: 14,
          validators: {
              maxCharacters: 11,
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
| [supportedNonNumericCharacters](#supportedNonNumericCharacters)                 | By setting this, the field will support a list of non numeric characters.              
| [validators.minCharacters](./24-general-properties/#validatorsmincharacters)    | Minimum number of characters for the input value to be valid.                                   |
| [validators.maxCharacters](./24-general-properties/#validatorsmaxcharacters)    | Maximum number of characters for the input value to be valid.                                   |
| [validators.supportedNonNumericCharacters](#supportedNonNumericCharacters)      | By setting this, the field will support a list of non numeric characters.                                             |

---
### `supportedNonNumericCharacters`

| `supportedNonNumericCharacters`     |                 |
| :-------------- | :-------------- |
| Possible Values | `String [Array]     |
| Required        | no              |
| Default Value   | empty [Array]               |

By setting `supportedNonNumericCharacters`, the field will support a list of non numeric characters. The charcaters are case sensitive.

``` typescript (value)
value:{
supportedNonNumericsCharacters: [A, I, *]
}
```
``` typescript (validators)
validators:{
supportedNonNumericsCharacters: [A, I, *]
}
```

---
### `validators.regexPattern`

| `validators.regexPattern`     |                 |
| :-------------- | :-------------- |
| Possible Values | String     |
| Required        | no              |
| Default Value   | -              |

By defining `validators.regexPattern`, you set a regular expression. ???

``` typescript
validators:{
regexPattern: ^[A-Z]*$
}
```

---
## `prefill`

| `prefill`                  |                                                                     |
| :------------------------- | :--------------                                                     |
| Possible Values            | Array of [PrefillRules](#???) that output a value of type `string` |
| Required                   | no                                                                  |
| Default Value              | -                                                                   |

This configuration follows the [general syntax for prefilling rules](#???).
The provided PrefillRules need to have an output value of type string.

``` typescript (static phone number)
        prefill: {
            value: [
                {
                    input: 'none',
                    steps: [
                        [
                            'staticPhoneNumber',
                            {
                                countryPrefix: '49',
                                number: '1753463937',
                            },
                        ],
                    ],
                },
            ],
        },
```

---
## `onChange`

| `onChange`                 |                   |
| :------------------------- | ------------------|
| Possible Values            | Array of Fuctions |
| Required                   | no                |
| Default Value              | -     

*???Description???*