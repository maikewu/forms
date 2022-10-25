---
title: FieldRepeater
category: 62ebf4654ae80e09e468624b
parentDoc: 62ec01bd561bab0aa775efe4
---

 The fieldRepeater contains several fields, each field gets extra config options if it's part of a repeater.
 They get the [uiHideInRepeaterCardDisplay](#uihideinrepeatercarddisplay) and [pdfFieldRepeaterCellAlignment](#pdffieldrepeatercellalignment) config option.
# Configuration Overview


| Property                                                                     | Description                      |
| :--------------------------------------------------------------------------- | :--------------------------------|
| [pdfHide](./24-general-properties/#pdfhide)                                  | Setting this to `true` hides the whole field in the PDF. |
| [pdfHideIfValueIsEmpty](./24-general-properties/#pdfhideifvalueisempty)      | Setting this to `true` hides the whole field in the PDF in case the field value is empty. |
| [pdfWidth](./24-general-properties/#pdfwidth)                                | Configuration of the width of the field. |
| [requiredAmountOfEntries](./24-general-properties/#requiredamountofentries)  | Specify how many repeating entries are requried to fill the form.                                                                                        |
| [helptextBefore](#helptextbefore)                                            | Text that is displayed before the repeater |
| [helptextAfter](#helptextafter)                                              | Text that is dispalyed after the repeater |
| [uiHideInRepeaterCardDisplay](#uihideinrepeatercarddisplay)                  | Setting this to `true` hides the field in the UI. |
| [pdfFieldRepeaterCellAlignment](#pdffieldrepeatercellalignment)              | Configuration of the cell alignment. |
| [label](#label)                                                              | Configuration of the field label. |
| [fields](#fields)                                                            | Components of the field |


```typescript (General repeater config without fields)
{
    "id": "exampleFieldRepeater_1",
    "type": "fieldRepeater",
    "config": {
        "pdfHide": false,
        "pdfHideIfValuesIsEmpty": false,
        "requiredAmountOfEntries": 2,
        "pdfWidth": 1,
        "label": {
            "text": {
                "en": "Field Repeater 1",
                "de": "Feld Liste 1",
                "tr": "Field Repeater 1 [TR]",
                "fr": "Field Repeater 1 [FR]",
                "es": "Field Repeater 1 [ES]",
                "it": "Field Repeater 1 [IT]"
            },
            "pdfHide": false,
            "pdfTextColor": "#facc2e",
            "pdfTextSize": 14,
            "uiHide": false
        },
        "helptextBefore": {
            "en": "Example helptext before",
            "de": "Beispiel Hilfstext davor",
            "tr": "Example helptext before [TR]",
            "fr": "Example helptext before [FR]",
            "es": "Example helptext before [ES]",
            "it": "Example helptext before [IT]"
        },
        "helptextAfter": {
            "en": "Example helptext after",
            "de": "Beispiel Hilfstext danach",
            "tr": "Example helptext after [TR]",
            "fr": "Example helptext after [FR]",
            "es": "Example helptext after [ES]",
            "it": "Example helptext after [IT]"
        },
        "fields": [
            // Add here all fields you want to repeate
        ]
    }
},
```

```typescript (SingleLineTextInput Examples)
// SingleLineTextInput for mail addresses
{
    "id": "exampleFieldRepeater_1_singleLineTextInput_1",
    "type": "singleLineTextInput",
    "config": {
        "required": true,
        "uiHideInRepeaterCardDisplay": false,
        "pdfFieldRepeaterCellAlignment": "center" // or "left" or "right"
        "label": {
            "text": {
                "en": "Input 1",
                "de": "Eingabe 1",
                "tr": "Input 1 [TR]",
                "fr": "Input 1 [FR]",
                "es": "Input 1 [ES]",
                "it": "Input 1 [IT]"
            }
        },
        "value": {
            "validators": {
                "emailAddress": true
            }
        }
    }
},

// General SingleLineTextInput
{
    "id": "exampleFieldRepeater_1_singleLineTextInput_2",
    "type": "singleLineTextInput",
    "config": {
        "required": true,
        "uiHideInRepeaterCardDisplay": false,
        "pdfFieldRepeaterCellAlignment": "center" // or "left" or "right"
        "label": {
            "text": {
                "en": "Input 1",
                "de": "Eingabe 1",
                "tr": "Input 1 [TR]",
                "fr": "Input 1 [FR]",
                "es": "Input 1 [ES]",
                "it": "Input 1 [IT]"
            }
        },
    }
},
    
// SingleLineTextInput incl. regex pattern    
{
    "id": "exampleFieldRepeater_1_singleLineTextInput_3",
    "type": "singleLineTextInput",
    "config": {
        "required": true,
        "uiHideInRepeaterCardDisplay": false,
        "pdfFieldRepeaterCellAlignment": "center" // or "left" or "right"
        "label": {
            "text": {
                "en": "Input 1",
                "de": "Eingabe 1",
                "tr": "Input 1 [TR]",
                "fr": "Input 1 [FR]",
                "es": "Input 1 [ES]",
                "it": "Input 1 [IT]"
            }
        },
        "value": {
            "validators": {
                "regexPattern": "^[A-Z]*$"
            }
        }
    }
},
            {
            "id": "exampleFieldRepeater_1_exampleStaticSingleSelect_1",
            "type": "staticSingleSelect",
            "config": {
                "required": true,
                "label": {
                "text": {
                    "en": "Static Single Select 1",
                    "de": "Static Single Select 1 [DE]",
                    "tr": "Static Single Select 1 [TR]",
                    "fr": "Static Single Select 1 [FR]",
                    "es": "Static Single Select 1 [ES]",
                    "it": "Static Single Select 1 [IT]"
                }
                },
                "value": {
                "options": {
                    "exampleOptionOne": {
                    "en": "Example option 1",
                    "de": "Example option 1 [DE]",
                    "tr": "Example option 1 [TR]",
                    "fr": "Example option 1 [FR]",
                    "es": "Example option 1 [ES]",
                    "it": "Example option 1 [IT]"
                    },
                    "exampleOptionTwo": {
                    "en": "Example option 2",
                    "de": "Example option 2 [DE]",
                    "tr": "Example option 2 [TR]",
                    "fr": "Example option 2 [FR]",
                    "es": "Example option 2 [ES]",
                    "it": "Example option 2 [IT]"
                    }
                }
                }
            }
            },
            {
            "id": "exampleFieldRepeater_1_exampleStaticMultiSelect_1",
            "type": "staticMultiSelect",
            "config": {
                "label": {
                "text": {
                    "en": "Static Multi Select 1",
                    "de": "Static Multi Select 1 [DE]",
                    "tr": "Static Multi Select 1 [TR]",
                    "fr": "Static Multi Select 1 [FR]",
                    "es": "Static Multi Select 1 [ES]",
                    "it": "Static Multi Select 1 [IT]"
                }
                },
                "value": {
                "options": {
                    "exampleOptionOne": {
                    "en": "Example option 1",
                    "de": "Example option 1 [DE]",
                    "tr": "Example option 1 [TR]",
                    "fr": "Example option 1 [FR]",
                    "es": "Example option 1 [ES]",
                    "it": "Example option 1 [IT]"
                    },
                    "exampleOptionTwo": {
                    "en": "Example option 2",
                    "de": "Example option 2 [DE]",
                    "tr": "Example option 2 [TR]",
                    "fr": "Example option 2 [FR]",
                    "es": "Example option 2 [ES]",
                    "it": "Example option 2 [IT]"
                    }
                }
                }
            }
            },
            {
            "id": "exampleFieldRepeater_1_multiLineTextLineInput_1",
            "type": "multiLineTextInput",
            "config": {
                "required": true,
                "label": {
                "text": {
                    "en": "MultiLineTextInput 1",
                    "de": "Mehrzeilige Eingabe 1",
                    "tr": "MultiLineTextInput 1 [TR]",
                    "fr": "MultiLineTextInput 1 [FR]",
                    "es": "MultiLineTextInput 1 [ES]",
                    "it": "MultiLineTextInput 1 [IT]"
                }
                },
                "uiHideInRepeaterCardDisplay": false,
                "value": {
                "validators": {
                    "minCharacters": 3
                }
                }
            }
            },
            {
            "id": "exampleFieldRepeater_1_exampleHtmlDisplay_1",
            "type": "htmlDisplay",
            "config": {
                "text": {
                "en": "<h1>HTML Display 1</h1><p>This field is in: <b>EN</b></p><p><i>This should be an italic text</i></p>",
                "de": "<h1>HTML Display 1</h1><p>This field is in: <b>DE</b></p><p><i>This should be an italic text</i></p>",
                "tr": "<h1>HTML Display 1</h1><p>This field is in: <b>TR</b></p><p><i>This should be an italic text</i></p>",
                "fr": "<h1>HTML Display 1</h1><p>This field is in: <b>FR</b></p><p><i>This should be an italic text</i></p>",
                "es": "<h1>HTML Display 1</h1><p>This field is in: <b>ES</b></p><p><i>This should be an italic text</i></p>",
                "it": "<h1>HTML Display 1</h1><p>This field is in: <b>IT</b></p><p><i>This should be an italic text</i></p>"
                }
            }
            },
            {
            "id": "exampleFieldRepeater_1_exampleBooleanInput_1",
            "type": "booleanInput",
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
                }
            }
            },
            {
            "id": "exampleFieldRepeater_1_exampleAddressInput_1",
            "type": "addressInput",
            "config": {
                "required": {
                "street": false,
                "streetNumber": false,
                "supplement": false,
                "zipPostCode": false,
                "city": false,
                "state": false,
                "country": false
                },
                "label": {
                "text": {
                    "en": "Address Input 1",
                    "de": "Anschrift Input 1",
                    "tr": "Address Input 1 [TR]",
                    "fr": "Address Input 1 [FR]",
                    "es": "Address Input 1 [ES]",
                    "it": "Address Input 1 [IT]"
                },
                "pdfHide": false,
                "uiTextColor": "#facc2e",
                "pdfTextColor": "#facc2e",
                "pdfTextSize": 14
                },
                "value": {
                "pdfHide": false,
                "pdfStartInNewLine": false,
                "pdfAddLineBreaks": false,
                "pdfTextColor": "#facc2e",
                "pdfTextSize": 14
                },
                "disabled": false,
                "pdfHideAll": false,
                "pdfWidth": 1,
                "pdfHideAllIfValueIsEmpty": false,
                "uiHideInRepeaterCardDisplay": false
            }
            },
            {
            "id": "exampleFieldRepeater_1_dateInput_1",
            "type": "dateInput",
            "config": {
                "required": true,
                "label": {
                "text": {
                    "en": "Date Input 1",
                    "de": "Date Input 1 [DE]",
                    "tr": "Date Input 1 [TR]",
                    "fr": "Date Input 1 [FR]",
                    "es": "Date Input 1 [ES]",
                    "it": "Date Input 1 [IT]"
                },
                "uiHide": false,
                "pdfHide": false,
                "pdfTextSize": 14,
                "pdfTextColor": "#facc2e"
                },
                "uiHideInRepeaterCardDisplay": false,
                "value": {
                "pdfHide": false,
                "pdfTextSize": 14,
                "pdfTextColor": "#facc2e",
                "pdfStartInNewLine": false,
                "validators": {
                    "minDate": "2000-02-22",
                    "maxDate": "2022-02-22"
                }
                }
            }
            },
            {
            "id": "exampleFieldRepeater_1_timeInput_1",
            "type": "timeInput",
            "config": {
                "required": false,
                "label": {
                "text": {
                    "en": "Time Input 1",
                    "de": "Time Input 1 [DE]",
                    "tr": "Time Input 1 [TR]",
                    "fr": "Time Input 1 [FR]",
                    "es": "Time Input 1 [ES]",
                    "it": "Time Input 1 [IT]"
                },
                "uiHide": false,
                "pdfHide": false,
                "pdfTextSize": 14,
                "pdfTextColor": "#facc2e"
                },
                "uiHideInRepeaterCardDisplay": false,
                "value": {
                "dropdownInterval": 30,
                "pdfHide": false,
                "pdfTextSize": 14,
                "pdfTextColor": "#facc2e",
                "pdfStartInNewLine": false
                }
            }
            },
            {
            "id": "exampleFieldRepeater_1_exampleAssetSingleSelect_1",
            "type": "assetSingleSelect",
            "config": {
                "required": false,
                "disabled": false,
                "pdfHideAll": false,
                "pdfHideAllIfValueIsEmpty": false,
                "uiHideInRepeaterCardDisplay": false,
                "value": {
                "disableAssetFormInstanceRelationship": false,
                "disableCreation": false,
                "pdfHide": false,
                "pdfStartInNewLine": false,
                "pdfTextColor": "#facc2e",
                "pdfTextSize": 14
                },
                "label": {
                "text": {
                    "en": "Asset Select 3",
                    "de": "Asset Auswahl 3",
                    "tr": "Asset Select 3 [TR]",
                    "fr": "Asset Select 3 [FR]",
                    "es": "Asset Select 3 [ES]",
                    "it": "Asset Select 3 [IT]"
                },
                "pdfHide": false,
                "pdfTextColor": "#facc2e",
                "pdfTextSize": 14,
                "uiHide": false
                }
            }
            },
            {
            "id": "exampleFieldRepeater_1_exampleUserSingleSelect_1",
            "type": "userSingleSelect",
            "config": {
                "required": false,
                "disabled": false,
                "pdfHideAll": false,
                "pdfHideAllIfValueIsEmpty": false,
                "uiHideInRepeaterCardDisplay": false,
                "value": {
                "pdfHide": false,
                "pdfStartInNewLine": false,
                "pdfTextColor": "#facc2e",
                "pdfTextSize": 14,
                "pdfPrintEmailAddress": true
                },
                "label": {
                "text": {
                    "en": "User Select 1",
                    "de": "User Auswahl 1",
                    "tr": "User Select 1 [TR]",
                    "fr": "User Select 1 [FR]",
                    "es": "User Select 1 [ES]",
                    "it": "User Select 1 [IT]"
                },
                "pdfHide": false,
                "pdfTextColor": "#facc2e",
                "pdfTextSize": 14,
                "uiHide": false
                }
            }
            },
            {
            "id": "exampleFieldRepeater_1_headingDisplay_1",
            "type": "headlineDisplay",
            "config": {
                "text": {
                "en": "Headline display element sample",
                "de": "Headline display element sample [DE]",
                "tr": "Headline display element sample [TR]",
                "fr": "Headline display element sample [FR]",
                "es": "Headline display element sample [ES]",
                "it": "Headline display element sample [IT]"
                },
                "uiHideInRepeaterCardDisplay": false
            }
            },
            {
            "id": "exampleFieldRepeater_1_phoneNumberInput_1",
            "type": "phoneNumberInput",
            "config": {
                "disabled": false,
                "required": true,
                "pdfHideAll": false,
                "pdfHideAllIfValueIsEmpty": false,
                "uiHideInRepeaterCardDisplay": false,
                "pdfWidth": 300,
                "value": {
                "pdfHide": false,
                "pdfStartInNewLine": false,
                "pdfTextColor": "#facc2e",
                "pdfTextSize": 14,
                "validators": {
                    "minCharacters": 5
                }
                },
                "label": {
                "text": {
                    "en": "Phone number input min validation",
                    "de": "Phone number input min validation [DE]",
                    "tr": "Phone number input min validation [TR]",
                    "fr": "Phone number input min validation [FR]",
                    "es": "Phone number input min validation [ES]",
                    "it": "Phone number input min validation [IT]"
                },
                "pdfHide": false,
                "pdfTextColor": "#facc2e",
                "pdfTextSize": 14
                },
                "placeHolderText": {
                "en": "Phone number input placeholder",
                "de": "Phone number input placeholder [DE]",
                "tr": "Phone number input placeholder [TR]",
                "fr": "Phone number input placeholder [FR]",
                "es": "Phone number input placeholder [ES]",
                "it": "Phone number input placeholder [IT]"
                }
            }
            },
            {
            "id": "exampleFieldRepeater_1_dateTimeInput_1",
            "type": "dateTimeInput",
            "config": {
                "required": false,
                "label": {
                "text": {
                    "en": "Date time input 1",
                    "de": "Date time input 1 [DE]",
                    "tr": "Date time input 1 [TR]",
                    "fr": "Date time input 1 [FR]",
                    "es": "Date time input 1 [ES]",
                    "it": "Date time input 1 [IT]"
                },
                "uiHide": false,
                "pdfHide": false,
                "pdfTextSize": 14,
                "pdfTextColor": "#facc2e"
                },
                "uiHideInRepeaterCardDisplay": false,
                "value": {
                "dropdownInterval": 30,
                "pdfHide": false,
                "pdfTextSize": 14,
                "pdfTextColor": "#facc2e",
                "pdfStartInNewLine": false
                }
            }
            }
```
```typescript (SingleLineTextInput Example3)
      fields: [
          {
              id: 'exampleFieldRepeater_1_singleLineInput_3',
              type: FormFieldTypesEnum.SINGLE_LINE_INPUT,
              config: {
                  required: true,
                  label: {
                      text: {
                          en: 'Input 3',
                          de: 'Eingabe 3',
                          tr: 'Input 3 [TR]',
                          fr: 'Input 3 [FR]',
                          es: 'Input 3 [ES]',
                          it: 'Input 3 [IT]',
                      },
                  },
                  uiHideInRepeaterCardDisplay: true,
                  value: {
                      validators: {
                          regex: {
                              pattern: '^[A-Z]*$',
                              errorText: {
                                  en: 'Only uppercase letters allowed',
                                  de: 'Only uppercase letters allowed [DE]',
                                  tr: 'Only uppercase letters allowed [TR]',
                                  fr: 'Only uppercase letters allowed [FR]',
                                  es: 'Only uppercase letters allowed [ES]',
                                  it: 'Only uppercase letters allowed [IT]',
                              },
                          },
                      },
                  },
              },
          },
      ],
```
```typescript (StaticSingleSelect)
      fields: [
          {
              id: 'exampleFieldRepeater_1_exampleStaticSingleSelect_1',
              type: FormFieldTypesEnum.STATIC_SINGLE_SELECT,
              config: {
                  required: true,
                  label: {
                      text: {
                          en: 'Static Single Select 1',
                          de: 'Static Single Select 1 [DE]',
                          tr: 'Static Single Select 1 [TR]',
                          fr: 'Static Single Select 1 [FR]',
                          es: 'Static Single Select 1 [ES]',
                          it: 'Static Single Select 1 [IT]',
                      },
                  },
                  value: {
                      options: {
                          exampleOptionOne: {
                              en: 'Example option 1',
                              de: 'Example option 1 [DE]',
                              tr: 'Example option 1 [TR]',
                              fr: 'Example option 1 [FR]',
                              es: 'Example option 1 [ES]',
                              it: 'Example option 1 [IT]',
                          },
                          exampleOptionTwo: {
                              en: 'Example option 2',
                              de: 'Example option 2 [DE]',
                              tr: 'Example option 2 [TR]',
                              fr: 'Example option 2 [FR]',
                              es: 'Example option 2 [ES]',
                              it: 'Example option 2 [IT]',
                          },
                      },
                  },
              },
          },
      ],
```
```typescript (StaticMultiSelect)
      fields: [
          {
              id: 'exampleFieldRepeater_1_exampleStaticMultiSelect_1',
              type: FormFieldTypesEnum.STATIC_MULTI_SELECT,
              config: {
                  label: {
                      text: {
                          en: 'Static Multi Select 1',
                          de: 'Static Multi Select 1 [DE]',
                          tr: 'Static Multi Select 1 [TR]',
                          fr: 'Static Multi Select 1 [FR]',
                          es: 'Static Multi Select 1 [ES]',
                          it: 'Static Multi Select 1 [IT]',
                      },
                  },
                  value: {
                      options: {
                          exampleOptionOne: {
                              en: 'Example option 1',
                              de: 'Example option 1 [DE]',
                              tr: 'Example option 1 [TR]',
                              fr: 'Example option 1 [FR]',
                              es: 'Example option 1 [ES]',
                              it: 'Example option 1 [IT]',
                          },
                          exampleOptionTwo: {
                              en: 'Example option 2',
                              de: 'Example option 2 [DE]',
                              tr: 'Example option 2 [TR]',
                              fr: 'Example option 2 [FR]',
                              es: 'Example option 2 [ES]',
                              it: 'Example option 2 [IT]',
                          },
                      },
                  },
              },
          },
      ],
```
```typescript (CompanySingleSelect)
      fields: [
          {
              id: 'exampleFieldRepeater_1_exampleCompanySingleSelect_1',
              type: FormFieldTypesEnum.COMPANY_SINGLE_SELECT,
              config: {
                  label: {
                      text: {
                          en: 'Company Single Select 1',
                          de: 'Company Single Select 1 [DE]',
                          tr: 'Company Single Select 1 [TR]',
                          fr: 'Company Single Select 1 [FR]',
                          es: 'Company Single Select 1 [ES]',
                          it: 'Company Single Select 1 [IT]',
                      },
                  },
              },
          },
      ],
```
```typescript (MultiLineTextInput)
      fields: [
          {
              id: 'exampleFieldRepeater_1_multiLineTextLineInput_1',
              type: FormFieldTypesEnum.MULTI_LINE_TEXT_INPUT,
              config: {
                  required: true,
                  label: {
                      text: {
                          en: 'MultiLineTextInput 1',
                          de: 'Mehrzeilige Eingabe 1',
                          tr: 'MultiLineTextInput 1 [TR]',
                          fr: 'MultiLineTextInput 1 [FR]',
                          es: 'MultiLineTextInput 1 [ES]',
                          it: 'MultiLineTextInput 1 [IT]',
                      },
                  },
                  uiHideInRepeaterCardDisplay: false,
                  value: {
                      validators: {
                          minCharacters: 3,
                      },
                  },
              },
          },
      ],
```
```typescript (HtmlDisplay)
      fields: [
          {
              id: 'exampleFieldRepeater_1_exampleHtmlDisplay_1',
              type: FormFieldTypesEnum.HTML_DISPLAY,
              config: {
                  text: {
                      en: '<h1>HTML Display 1</h1><p>This field is in: <b>EN</b></p><p><i>This should be an italic text</i></p>',
                      de: '<h1>HTML Display 1</h1><p>This field is in: <b>DE</b></p><p><i>This should be an italic text</i></p>',
                      tr: '<h1>HTML Display 1</h1><p>This field is in: <b>TR</b></p><p><i>This should be an italic text</i></p>',
                      fr: '<h1>HTML Display 1</h1><p>This field is in: <b>FR</b></p><p><i>This should be an italic text</i></p>',
                      es: '<h1>HTML Display 1</h1><p>This field is in: <b>ES</b></p><p><i>This should be an italic text</i></p>',
                      it: '<h1>HTML Display 1</h1><p>This field is in: <b>IT</b></p><p><i>This should be an italic text</i></p>',
                  },
              },
          },
      ],
```
```typescript (BooleanInput)
      fields: [
          {
              id: 'exampleFieldRepeater_1_exampleBooleanInput_1',
              type: FormFieldTypesEnum.BOOLEAN_INPUT,
              config: {
                  label: {
                      text: {
                          en: 'Boolean input 1',
                          de: 'Boolean input 1 [DE]',
                          tr: 'Boolean input 1 [TR]',
                          fr: 'Boolean input 1 [FR]',
                          es: 'Boolean input 1 [ES]',
                          it: 'Boolean input 1 [IT]',
                      },
                  },
              },
          },
      ],
```
```typescript (AddressInput)
      fields: [
          {
              id: 'exampleFieldRepeater_1_exampleAddressInput_1',
              type: FormFieldTypesEnum.ADDRESS_INPUT,
              config: {
                  required: {
                      street: false,
                      streetNumber: false,
                      supplement: false,
                      zipPostCode: false,
                      city: false,
                      state: false,
                      country: false,
                  },
                  label: {
                      text: {
                          en: 'Address Input 1',
                          de: 'Anschrift Input 1',
                          tr: 'Address Input 1 [TR]',
                          fr: 'Address Input 1 [FR]',
                          es: 'Address Input 1 [ES]',
                          it: 'Address Input 1 [IT]',
                      },
                      pdfHide: false,
                      uiTextColor: '#facc2e',
                      pdfTextColor: '#facc2e',
                      pdfTextSize: 14,
                  },
                  value: {
                      pdfHide: false,
                      pdfStartInNewLine: false,
                      pdfAddLineBreaks: false,
                      pdfTextColor: '#facc2e',
                      pdfTextSize: 14,
                  },
                  disabled: false,
                  pdfHide: false,
                  pdfWidth: 1,
                  pdfHideIfValueIsEmpty: false,
                  uiHideInRepeaterCardDisplay: false,
              },
          },
      ],
```
```typescript (DateInput)
      fields: [
          {
              id: 'exampleFieldRepeater_1_dateInput_1',
              type: FormFieldTypesEnum.DATE_INPUT,
              config: {
                  required: true,
                  label: {
                      text: {
                          en: 'Date Input 1',
                          de: 'Date Input 1 [DE]',
                          tr: 'Date Input 1 [TR]',
                          fr: 'Date Input 1 [FR]',
                          es: 'Date Input 1 [ES]',
                          it: 'Date Input 1 [IT]',
                      },
                      uiHide: false,
                      pdfHide: false,
                      pdfTextSize: 14,
                      pdfTextColor: '#facc2e',
                  },
                  uiHideInRepeaterCardDisplay: false,
                  value: {
                      pdfHide: false,
                      pdfTextSize: 14,
                      pdfTextColor: '#facc2e',
                      pdfStartInNewLine: false,
                      validators: {
                          minDate: '2000-02-22',
                          maxDate: '2022-02-22',
                      },
                  },
              },
          },
      ],
```
```typescript (TimeInput)
      fields: [
          {
              id: 'exampleFieldRepeater_1_timeInput_1',
              type: FormFieldTypesEnum.TIME_INPUT,
              config: {
                  required: false,
                  label: {
                      text: {
                          en: 'Time Input 1',
                          de: 'Time Input 1 [DE]',
                          tr: 'Time Input 1 [TR]',
                          fr: 'Time Input 1 [FR]',
                          es: 'Time Input 1 [ES]',
                          it: 'Time Input 1 [IT]',
                      },
                      uiHide: false,
                      pdfHide: false,
                      pdfTextSize: 14,
                      pdfTextColor: '#facc2e',
                  },
                  uiHideInRepeaterCardDisplay: false,
                  value: {
                      dropdownInterval: 30,
                      pdfHide: false,
                      pdfTextSize: 14,
                      pdfTextColor: '#facc2e',
                      pdfStartInNewLine: false,
                  },
              },
          },
      ],
```
```typescript (AssetSingleSingleSelect)
      fields: [
          {
              id: 'exampleFieldRepeater_1_exampleAssetSingleSelect_1',
              type: FormFieldTypesEnum.ASSET_SINGLE_SELECT,
              config: {
                  required: false,
                  disabled: false,
                  pdfHide: false,
                  pdfHideIfValueIsEmpty: false,
                  uiHideInRepeaterCardDisplay: false,
                  value: {
                      disableAssetFormInstanceRelationship: false,
                      disableCreation: false,
                      pdfHide: false,
                      pdfStartInNewLine: false,
                      pdfTextColor: '#facc2e',
                      pdfTextSize: 14,
                  },
                  label: {
                      text: {
                          en: 'Asset Select 3',
                          de: 'Asset Auswahl 3',
                          tr: 'Asset Select 3 [TR]',
                          fr: 'Asset Select 3 [FR]',
                          es: 'Asset Select 3 [ES]',
                          it: 'Asset Select 3 [IT]',
                      },
                      pdfHide: false,
                      pdfTextColor: '#facc2e',
                      pdfTextSize: 14,
                      uiHide: false,
                  },
              },
          },
      ],
```
```typescript (UserSingleSelect)
      fields: [
          {
              id: 'exampleFieldRepeater_1_exampleUserSingleSelect_1',
              type: FormFieldTypesEnum.USER_SINGLE_SELECT,
              config: {
                  required: false,
                  disabled: false,
                  pdfHide: false,
                  pdfHideIfValueIsEmpty: false,
                  uiHideInRepeaterCardDisplay: false,
                  value: {
                      pdfHide: false,
                      pdfStartInNewLine: false,
                      pdfTextColor: '#facc2e',
                      pdfTextSize: 14,
                      pdfPrintEmailAddress: true,
                  },
                  label: {
                      text: {
                          en: 'User Select 1',
                          de: 'User Auswahl 1',
                          tr: 'User Select 1 [TR]',
                          fr: 'User Select 1 [FR]',
                          es: 'User Select 1 [ES]',
                          it: 'User Select 1 [IT]',
                      },
                      pdfHide: false,
                      pdfTextColor: '#facc2e',
                      pdfTextSize: 14,
                      uiHide: false,
                  },
              },
          },
      ],
```
```typescript (headlineDisplay)
      fields: [
          {
              id: 'exampleFieldRepeater_1_headingDisplay_1',
              type: FormFieldTypesEnum.HEADLINE_DISPLAY,
              config: {
                  text: {
                      en: 'Headline display element sample',
                      de: 'Headline display element sample [DE]',
                      tr: 'Headline display element sample [TR]',
                      fr: 'Headline display element sample [FR]',
                      es: 'Headline display element sample [ES]',
                      it: 'Headline display element sample [IT]',
                  },
                  uiHideInRepeaterCardDisplay: false,
              },
          },
      ],
```
```typescript (PhoneNumberInput)
      fields: [
          {
              id: 'exampleFieldRepeater_1_phoneNumberInput_1',
              type: FormFieldTypesEnum.PHONE_NUMBER_INPUT,
              config: {
                  disabled: false,
                  required: true,
                  pdfHide: false,
                  pdfHideIfValueIsEmpty: false,
                  uiHideInRepeaterCardDisplay: false,
                  pdfWidth: 300,
                  value: {
                      pdfHide: false,
                      pdfStartInNewLine: false,
                      pdfTextColor: '#facc2e',
                      pdfTextSize: 14,
                      validators: {
                          minCharacters: 5,
                      },
                  },
                  label: {
                      text: {
                          en: 'Phone number input min validation',
                          de: 'Phone number input min validation [DE]',
                          tr: 'Phone number input min validation [TR]',
                          fr: 'Phone number input min validation [FR]',
                          es: 'Phone number input min validation [ES]',
                          it: 'Phone number input min validation [IT]',
                      },
                      pdfHide: false,
                      pdfTextColor: '#facc2e',
                      pdfTextSize: 14,
                  },
                  placeHolderText: {
                      en: 'Phone number input placeholder',
                      de: 'Phone number input placeholder [DE]',
                      tr: 'Phone number input placeholder [TR]',
                      fr: 'Phone number input placeholder [FR]',
                      es: 'Phone number input placeholder [ES]',
                      it: 'Phone number input placeholder [IT]',
                  },
              },
          },
      ],
```
```typescript (DateTimeInput)
      fields: [
          {
              id: 'exampleFieldRepeater_1_dateTimeInput_1',
              type: FormFieldTypesEnum.DATE_TIME_INPUT,
              config: {
                  required: false,
                  label: {
                      text: {
                          en: 'Date time input 1',
                          de: 'Date time input 1 [DE]',
                          tr: 'Date time input 1 [TR]',
                          fr: 'Date time input 1 [FR]',
                          es: 'Date time input 1 [ES]',
                          it: 'Date time input 1 [IT]',
                      },
                      uiHide: false,
                      pdfHide: false,
                      pdfTextSize: 14,
                      pdfTextColor: '#facc2e',
                  },
                  uiHideInRepeaterCardDisplay: false,
                  value: {
                      dropdownInterval: 30,
                      pdfHide: false,
                      pdfTextSize: 14,
                      pdfTextColor: '#facc2e',
                      pdfStartInNewLine: false,
                  },
              },
          },
      ],
```

---
# Configuration Parameter


## `helptextBefore`

| `helptextBefore`     |                 |
| :-------------- | :-------------- |
| Possible Values | [MultiLanguageText](./24-general-properties/#multilanguagetext)    |
| Required        | no              |
| Default Value   | -               |

By setting `helptextBefore`, a text is dispalyed before the repeater.

``` typescript
      helptextBefore: {
          en: 'Example helptext before',
          de: 'Beispiel Hilfstext davor',
          tr: 'Example helptext before [TR]',
          fr: 'Example helptext before [FR]',
          es: 'Example helptext before [ES]',
          it: 'Example helptext before [IT]',
      },
```

---
## `helptextAfter`

| `helptextAfter`     |                 |
| :-------------- | :-------------- |
| Possible Values | [MultiLanguageText](./24-general-properties/#multilanguagetext)    |
| Required        | no              |
| Default Value   | -               |

By setting `helptextAfter`, a text is dispalyed before the repeater.

``` typescript
      helptextAfter: {
          en: 'Example helptext after',
          de: 'Beispiel Hilfstext danach',
          tr: 'Example helptext after [TR]',
          fr: 'Example helptext after [FR]',
          es: 'Example helptext after [ES]',
          it: 'Example helptext after [IT]',
      },
```
---
## `label`

Property                                                    | Description                       |
| :---------------------------------------------------------- | :-------------------------------- |
| [text](./24-general-properties/#text)                       | Localized label text of the field. Shown in the UI and the PDF. |
| [uiHide](./24-general-properties/#uihide)                   | Setting this to `true` hides the label in the UI. |
| [pdfHide](./24-general-properties/#pdfhide)                 | Setting this to `true` hides the label in the PDF. |
| [pdfTextSize](./24-general-properties/#pdftextsize)         | Text size of the label in the PDF. |
| [pdfTextColor](./24-general-properties/#pdftextcolor)       | Text color of the label in the PDF. |

---
## `fields`

| Property                                                      | Description                       |
| :------------------------------------------------------------ | :-------------------------------- |
| [RepeatableFormFieldConfig](#repeatableformfieldconfig)       | List of repeatable fields. |

---
### `repeatableFormFieldConfig`

A list of a fields that can be used in the fieldRepeater.

| Property                                                      | Description                       |
| :------------------------------------------------------------ | :-------------------------------- |
| [headlineDisplay](./03-headline-display) (not displayed in the PDF)                 | The HeadlineDisplay is a field that displays headlines to structure content in the form and provisde information.|
| [htmlDisplay](./23-html-display)   (not displayed in the PDF)                      | The HtmlDisplay allows the user to enter html text. |
| [singleLineTextInput](./01-single-line-text-input)       | The SingleLineTextInput field allows entering one line of unformatted text. |
| [multiLineTextInput](./02-mutli-line-text-input)         | The MultiLineTextInput field allows entering larger amounts of unformatted text.  |
| [addressInput](./04-address-input)                       | The AddressInput contains various fields for every information of an address. |
| [assetSingleSelect](./05-asset-single-select)            | The AssetSingleSelect field allows to select an asset from the account or a certain costumer.  |
| [companySingleSelect](./06-company-single-select)        | The CompanySingleSelect field allows the user to choose one of the customer companys. |
| [userSingleSelect](./08-user-single-select)              | The UserSingleSelect field allows to select a user from the own or from a customers organisation. |
| [phoneNumberInput](./09-phone-number-input)              | The PhoneNumberInput field allows to input telephone numbers in the common format. | 
| [dateInput](./10-date-input)                             | The DateInput field allows to input a date. |
| [timeInput](./11-time-input)                             | The TimeInput field allows to enter a time. |
| [dateTimeInput](./12-date-time-input)                    | The DateTimeInput field allows to enter a datetime. |
| [staticSingleSelect](./13-static-single-select)          | The StaticSingleSelect field allows to choose one option of the dropdown. |
| [staticMultiSelect](./14-static-multi-select)            | The StaticMultiSelect field allows to choose one or more options of the dropdown. |
| [booleanInput](./15-boolean-input)                       | The BooleanInput allows the user to mark a checkbox true or false. |

## `uiHideInRepeaterCardDisplay`

**This propertie can be part of every field config of the repeated fields.**

| `uiHideInRepeaterCardDisplay`     |                 |
| :-------------- | :-------------- |
| Possible Values | `true`, `false`    |
| Required        | no              |
| Default Value   | `false`               |

By setting `uiHideInRepeaterCardDisplay` to `true` the field isn't shown in the UI.

``` typescript
uiHideInRepeaterCardDisplay: true,
```

## `pdfFieldRepeaterCellAlignment`

**This propertie can be part of every field config of the repeated fields.**


| `pdfFieldRepeaterCellAlignment`     |                 |
| :-------------- | :-------------- |
| Possible Values | `left`, `center`, `right`   |
| Required        | no              |
| Default Value   | `left`               |

By setting `pdfFieldRepeaterCellAlignment` the cell alignment gets defined.

``` typescript
pdfFieldRepeaterCellAlignment: `right`,
```
