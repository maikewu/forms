---
title: FieldRepeater
category: 635ce1e7775bc60045570ffb
parentDoc: 635ce486ae5fac003cef279e
---

 The fieldRepeater contains several fields which gonna be used to create a table of customer properties, each field gets extra config options if it's part of a repeater.
 They get the [uiHideInRepeaterCardDisplay](#uihideinrepeatercarddisplay) and [pdfFieldRepeaterCellAlignment](#pdffieldrepeatercellalignment) config option.
# Configuration Overview


| Property                                                                    | Description                      |
|:----------------------------------------------------------------------------| :--------------------------------|
| [pdfHide](./24-general-properties/#pdfhide)                                 | Setting this to `true` hides the whole field in the PDF. |
| [pdfHideIfValueIsEmpty](./24-general-properties/#pdfhideifvalueisempty)     | Setting this to `true` hides the whole field in the PDF in case the field value is empty. |
| [pdfWidth](./24-general-properties/#pdfwidth)                               | Configuration of the width of the field. |
| [requiredAmountOfEntries](./24-general-properties/#requiredamountofentries) | Specify how many repeating entries are required to fill the form.                                                                                        |
| [helpTextBefore](#helpTextBefore)                                           | Text that is displayed before the repeater |
| [helpTextAfter](#helpTextafter)                                             | Text that is displayed after the repeater |
| [uiHideInRepeaterCardDisplay](#uihideinrepeatercarddisplay)                 | Setting this to `true` hides the field in the UI. |
| [pdfFieldRepeaterCellAlignment](#pdffieldrepeatercellalignment)             | Configuration of the cell alignment. |
| [label](#label)                                                             | Configuration of the field label. |
| [fields](#fields)                                                           | Components of the field |


```json (General repeater config without fields)
{
    "id": "exampleFieldRepeater_1",
    "type": "fieldRepeater",
    "config": {
        "pdfHide": false,
        "pdfHideIfValueIsEmpty": false,
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
        "helpTextBefore": {
            "en": "Example helptext before",
            "de": "Beispiel Hilfstext davor",
            "tr": "Example helptext before [TR]",
            "fr": "Example helptext before [FR]",
            "es": "Example helptext before [ES]",
            "it": "Example helptext before [IT]"
        },
        "helpTextAfter": {
            "en": "Example helptext after",
            "de": "Beispiel Hilfstext danach",
            "tr": "Example helptext after [TR]",
            "fr": "Example helptext after [FR]",
            "es": "Example helptext after [ES]",
            "it": "Example helptext after [IT]"
        },
        "fields": [
         "ENTER ENTRIES / FIELDS FOR THE REPEATER HERE. A LIST WITH ALL POSSIBLE FIELDS CAN BE FOUND BELOW"
        ]
    }
},
```
---
# Fields that can be used in the field repeater
### `repeatableFormFieldConfig`

A list of all fields that can be used in the fieldRepeater. Code examples can be find below

| Property                                                      | Description                       |
| :------------------------------------------------------------ | :-------------------------------- |
| [headlineDisplay](./03-headline-display) (not displayed in the PDF)                 | The HeadlineDisplay is a field that displays headlines to structure content in the form and provide information.|
| [htmlDisplay](./23-html-display)   (not displayed in the PDF)                      | The HtmlDisplay allows the user to enter html text. |
| [singleLineTextInput](./01-single-line-text-input)       | The SingleLineTextInput field allows entering one line of unformatted text. |
| [multiLineTextInput](./02-mutli-line-text-input)         | The MultiLineTextInput field allows entering larger amounts of unformatted text.  |
| [addressInput](./04-address-input)                       | The AddressInput contains various fields for every information of an address. |
| [assetSingleSelect](./05-asset-single-select)            | The AssetSingleSelect field allows to select an asset from the account or a certain costumer.  |
| [companySingleSelect](./06-company-single-select)        | The CompanySingleSelect field allows the user to choose one of the customer companies. |
| [userSingleSelect](./08-user-single-select)              | The UserSingleSelect field allows to select a user from the own or from a customers organization. |
| [phoneNumberInput](./09-phone-number-input)              | The PhoneNumberInput field allows to input telephone numbers in the common format. | 
| [dateInput](./10-date-input)                             | The DateInput field allows to input a date. |
| [timeInput](./11-time-input)                             | The TimeInput field allows to enter a time. |
| [dateTimeInput](./12-date-time-input)                    | The DateTimeInput field allows to enter a datetime. |
| [staticSingleSelect](./13-static-single-select)          | The StaticSingleSelect field allows to choose one option of the dropdown. |
| [staticMultiSelect](./14-static-multi-select)            | The StaticMultiSelect field allows to choose one or more options of the dropdown. |
| [booleanInput](./15-boolean-input)                       | The BooleanInput allows the user to mark a checkbox true or false. |

```json (HeadlineDisplay)
{
    "id": "exampleHeadlineDisplay_1",
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
        "uiHideInRepeaterCardDisplay": false,
        "pdfFieldRepeaterCellAlignment": "right", 
        "uiHide": false,
        "type": "H1",
        "pdfHide": false,
        "pdfTextColor": "#facc2e",
        "pdfWidth": 0.5
    }
},
```
```json (HtmlDisplay)
{
    "id": "exampleHtmlDisplay_1",
    "type": "htmlDisplay",
    "config": {
        "pdfHide": false,
        "pdfWidth": 1,
        "uiHide": false,
        "uiHideInRepeaterCardDisplay": false,
        "pdfFieldRepeaterCellAlignment": "right", 
        "text": {
            "en": "<h1>HTML Display 1</h1><p>This field is in: <b>EN</b></p><p><i>This should be an italic text</i></p>",
            "de": "<h1>HTML Display 1</h1><p>This field is in: <b>DE</b></p><p><i>This should be an italic text</i></p>",
            "tr": "<h1>HTML Display 1</h1><p>This field is in: <b>TR</b></p><p><i>This should be an italic text</i></p>",
            "fr": "<h1>HTML Display 1</h1><p>This field is in: <b>FR</b></p><p><i>This should be an italic text</i></p>",
            "es": "<h1>HTML Display 1</h1><p>This field is in: <b>ES</b></p><p><i>This should be an italic text</i></p>",
            "it": "<h1>HTML Display 1</h1><p>This field is in: <b>IT</b></p><p><i>This should be an italic text</i></p>"
        },
    }
},
```
```json (SingleLineTextInput)
{
    "id": "exampleSingleLineInput_1",
    "type": "singleLineInput",
    "config": {
        "required": true,
        "disabled": false,
        "pdfHide": false,
        "pdfHideIfValueIsEmpty": false,
        "pdfWidth": 0.5,
        "uiHideInRepeaterCardDisplay": false,
        "pdfFieldRepeaterCellAlignment": "right", 
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
                "regex": {
                    "pattern": "^[A-Z]*$",
                    "errorText": {
                        "de": " ",
                        "en": " "
                    }
                }
            },
        },
        "prefill": {
            "value": [{
                    "input": "assetId",
                    "steps": [
                        "assetIdToAsset",
                        "assetToAssetTypeNameString",
                    ]},
            ],
        },
    },
},
```
```json (MultiLineTextInput)
{
  "id": "exampleMultiLineTextInput_1",
  "type": "multiLineTextInput",
  "config": {
      "required": true,
      "disabled": false,
      "pdfHide": false,
      "pdfWidth": 0.5,
      "pdfHideIfValueIsEmpty": false,
      "uiHideInRepeaterCardDisplay": false,
      "pdfFieldRepeaterCellAlignment": "right", 
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
              "maxCharacters": 10,
              "minCharacters": 3,
            },
            "uiMaxRows": 5,
            "uiMinRows": 2,
        },
        "prefill": {
            "value": [
                {
                    "input": "none",
                    "steps": [
                        [
                            "staticString",
                            "Default \n Multi \n Line \n Text",
                        ],
                    ],
                },
            ],
        },
    },
}
```
```json (AddressInput)
{
    "id": "exampleAddressInput_1",
    "type": "addressInput",
    "config": {
      "required": {
        "street": false,
        "streetNumber": false,
        "company": false,
        "supplement": false,
        "zipPostCode": false,
        "city": false,
        "state": false,
        "country": false
      },
      "disabled": false,
      "pdfHide": false,
      "pdfHideIfValueIsEmpty": false,
      "pdfWidth": 1,
      "uiHideInRepeaterCardDisplay": false,
      "pdfFieldRepeaterCellAlignment": "right", 
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
      "prefill": {
        "value": [
          {
            "input": "none",
            "steps": [
              [
                "staticAddress",
                {
                  "city": "Default City",
                  "street": "Default Street",
                  "streetNumber": "1",
                  "country": "Default Country",
                  "other": "Default supplement",
                  "countryProvince": "Default state",
                  "company": "Default Company"
                }
              ]
            ]
          }
        ]
      },
      "onChange": [{
          "steps": [
            "addressToCityString"
          ],
          "target": {
            "id": "exampleSignatureSection",
            "propertyName": "location"
          }
        }]
    }
},
```
```json (AssetSingleSelect)
{
    "id": "exampleAssetSingleSelect_1",
    "type": "assetSingleSelect",
    "config": {
      "required": true,
      "disabled": false,
      "pdfHide": false,
      "pdfHideIfValueIsEmpty": false,
      "pdfWidth": 1,
      "uiHideInRepeaterCardDisplay": false,
      "pdfFieldRepeaterCellAlignment": "right", 
      "label": {
            "text": {
            "en": "Asset Select 1",
            "de": "Asset Auswahl 1",
            "tr": "Asset Select 1 [TR]",
            "fr": "Asset Select 1 [FR]",
            "es": "Asset Select 1 [ES]",
            "it": "Asset Select 1 [IT]"
            },
            "pdfHide": false,
            "pdfTextColor": "#facc2e",
            "pdfTextSize": 14,
            "uiHide": false
        },
        "value": {
              "disableAssetFormInstanceRelationship": false,
              "disableCreation": false,
              "pdfHide": false,
              "pdfStartInNewLine": false,
              "pdfTextColor": "#facc2e",
              "pdfTextSize": 14
        },
            "prefill": {
              "selectedAsset": [
                {
                  "input": "assetId",
                  "steps": []
                }
              ],
              "accountFilter": [
                {
                  "input": "organizationId",
                  "steps": []
                }
              ]
            },
            "onChange": [
              {
                "steps": [
                  "assetInfoToAsset",
                  "assetToLocationAddress"
                ],
                "target": {
                  "id": "exampleAddressInput_1"
                }
              },
              {
                "steps": [
                  "assetToAssetTypeNameString"
                ],
                "target": {
                  "id": "exampleMultiLineTextInput_1"
                }
            }
        ]
    },
},
```
```json (CompanySingleSelect)
{
    "id": "exampleCompanySingleSelect_1",
    "type": "companySingleSelect",
    "config": {
        "disabled": false,
        "pdfHide": false,
        "pdfHideIfValueIsEmpty": false,
        "pdfWidth": 1,
        "uiHideInRepeaterCardDisplay": false,
        "pdfFieldRepeaterCellAlignment": "right",
        "label": {
            "text": {
                "en": "Company Single Select 1",
                "de": "Einfache Unternehmensauswahl",
                "tr": "Company Single Select 1 [TR]",
                "fr": "Company Single Select 1 [FR]",
                "es": "Company Single Select 1 [ES]",
                "it": "Company Single Select 1 [IT]",
            },
            "pdfHide": false,
            "pdfTextColor": "#facc2e",
            "pdfTextSize": 14,
            "uiHide": false,
        },
        "value": {
            "disableCreation": false,
            "pdfPrintCompanyNumber": false,
            "pdfHide": false,
            "pdfStartInNewLine": false,
            "pdfTextColor": "#facc2e",
            "pdfTextSize": 14,
        },
        "prefill": {
            [ "selectedCompany" ]: [
                {
                    "input": "currentAccountId",
                    "steps": [],
                },
            ],
        },
        "onChange": [
            {
                "steps": ["accountInfoToCompanyName"],
                "target": { "id": "disabledSingleLineInput_1" },
            },
            {
                "steps": [ "accountInfoToAccount", "accountToBillingAddressAddress"],
                "target": { "id": "exampleAddressInput_1" },
            },
            {
                "steps": [ "accountInfoToAccount", "accountToBillingAddressAddress", "addressToCityString"],
                "target": { "id": "exampleSignatureSection", "propertyName": "location" },
            },
            {
                "steps": ["accountInfoToAccount", "accountToPhoneNumberString" ],
                "target": { "id": "exampleSingleLineInput_2" },
            },
            {
                "steps": [ "accountInfoToAccount", "accountToPhoneNumberString", "phoneNumberStringToPhoneNumberObject" ],
                "target": { "id": "examplePhoneNumberInput_1" },
            },
        ],
    },
},
```
```json (UserSingleSelect)
{
    "id": "exampleUserSingleSelect_1",
    "type": "userSingleSelect",
    "config": {
        "required": true,
        "disabled": false,
        "pdfHide": false,
        "pdfHideIfValueIsEmpty": false,
        "pdfWidth": 1,
        "uiHideInRepeaterCardDisplay": false,
        "pdfFieldRepeaterCellAlignment": "right", 
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
        },
         "value": {
            "pdfHide": false,
            "pdfStartInNewLine": false,
            "pdfTextColor": "#facc2e",
            "pdfTextSize": 14,
            "pdfPrintEmailAddress": true
        },
      "prefill": {
          "value": [
              {
                  "input": "currentUserId",
                  "steps": [],
              },
          ],
      },
      "onChange": [
          {
              "steps": [ "userToFullNameString" ],
              "target": { "id": "exampleSignatureSection", "propertyName": "name" },
          },
          {
              "steps": ["userInfoToUser", "userToPhoneNumberString", "phoneNumberStringToPhoneNumberObject"],
              "target": { "id": "examplePhoneNumberInput_1" },
          },
      ],
  },
},
```
```json (PhoneNumberInput)
{
    "id": "examplePhoneNumberInput_1",
    "type": "phoneNumberInput",
    "config": {
        "disabled": false,
        "required": true,
        "pdfHide": false,
        "pdfHideIfValueIsEmpty": false,
        "pdfWidth": 1,
        "uiHideInRepeaterCardDisplay": false,
        "pdfFieldRepeaterCellAlignment": "right", 
        "label": {
            "pdfHide": false,
            "pdfTextColor": "#facc2e",
            "pdfTextSize": 14,
            "text": {
                "en": "Phone number input required",
                "de": "Phone number input required [DE]",
                "tr": "Phone number input required [TR]",
                "fr": "Phone number input required [FR]",
                "es": "Phone number input required [ES]",
                "it": "Phone number input required [IT]"
            },
        }, 
       "placeHolderText": {
            "en": "Phone number input placeholder",
            "de": "Phone number input placeholder [DE]",
            "tr": "Phone number input placeholder [TR]",
            "fr": "Phone number input placeholder [FR]",
            "es": "Phone number input placeholder [ES]",
            "it": "Phone number input placeholder [IT]"
        },
        "value": {
            "pdfHide": false,
            "pdfStartInNewLine": false,
            "pdfTextColor": "#facc2e",
            "pdfTextSize": 14,
            "validators": {
                "minCharacters": 6,
                "maxCharacters": 10,
                "supportedNonNumericsCharacters": ["A", "I", "*"]   
            }
        },
        "prefill": {
            "value": [{
                "input": "none",
                "steps": [[
                    "staticPhoneNumber",
                    {
                    "countryPrefix": "49",
                    "number": "1753463937"
                    }
                ]]
            }]
        },
    }
}
```
```json (DateInput)
{
  "id": "exampleDateInput_1",
  "type": "dateInput",
  "config": {
    "pdfHide": false,
    "disabled": false,
    "required": true,
    "pdfWidth": 0.7,
    "pdfHideIfValueIsEmpty": false,
    "uiHideInRepeaterCardDisplay": false,
    "pdfFieldRepeaterCellAlignment": "right", 
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
      }
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
```json (TimeInput)
{
    "id": "exampleTimeInput_1",
    "type": "timeInput",
    "config": {
        "pdfHide": false,
        "disabled": false,
        "required": false,
        "pdfWidth": 1,
        "pdfHideIfValueIsEmpty": false,
        "uiHideInRepeaterCardDisplay": false,
        "pdfFieldRepeaterCellAlignment": "right", 
        "label": {
            "text": {
                "en": "Time input 1",
                "de": "Time input 1 [DE]",
                "tr": "Time input 1 [TR]",
                "fr": "Time input 1 [FR]",
                "es": "Time input 1 [ES]",
                "it": "Time input 1 [IT]"
            },
            "uiHide": false,
            "pdfHide": false,
            "pdfTextSize": 14,
            "pdfTextColor": "#facc2e"
        },
        "value": {
            "dropdownInterval": 30,
            "pdfHide": false,
            "pdfTextSize": 14,
            "pdfTextColor": "#facc2e",
            "pdfStartInNewLine": false
        },
        "prefill": {
            "value": [{
                "input": "none",
                "steps": [[
                    "staticTime",
                    "22:22"
                ]]
            }]
        }
    }
},
```
```json (DateTimeInput)
{
    "id": "exampleDateTimeInput_1",
    "type": "dateTimeInput",
    "config": {
        "pdfHide": false,
        "disabled": false,
        "required": false,
        "pdfWidth": 1,
        "pdfHideIfValueIsEmpty": false,
        "uiHideInRepeaterCardDisplay": false,
        "pdfFieldRepeaterCellAlignment": "right", 
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
        "value": {
            "dropdownInterval": 30,
            "pdfHide": false,
            "pdfTextSize": 14,
            "pdfTextColor": "#facc2e",
            "pdfStartInNewLine": false
        },
        "prefill": {
            "value": [{
                "input": "none",
                "steps": [[
                    "staticDateTime",
                    "2022-02-22T22:22:00.000Z_Europe/Berlin"
                ]]
            }]
        }
    }
},
```
```json (StaticSingleSelect)
 {
    "id": "exampleStaticSingleSelect_1",
    "type": "staticSingleSelect",
    "config": {
        "required": true,
        "disabled": false,
        "pdfHide": false,
        "pdfHideIfValueIsEmpty": false,
        "pdfWidth": 1,
        "uiHideInRepeaterCardDisplay": false,
        "pdfFieldRepeaterCellAlignment": "right", 
        "label": {
            "text": {
                "en": "Static Single Select 1",
                "de": "Static Single Select 1 [DE]",
                "tr": "Static Single Select 1 [TR]",
                "fr": "Static Single Select 1 [FR]",
                "es": "Static Single Select 1 [ES]",
                "it": "Static Single Select 1 [IT]"
            },
            "pdfHide": false,
            "pdfTextColor": "#facc2e",
            "pdfTextSize": 14,
            "uiHide": false
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
            },
            "pdfHide": false,
            "pdfStartInNewLine": false,
            "pdfTextColor": "#facc2e",
            "pdfTextSize": 14
        },
        "prefill": {
            "value": [{
                "input": "none",
                "steps": [[
                    "staticString",
                    "exampleOptionOne"
                ]]
            }]
        }
    }
},
```
```json (StaticMultiSelect)
{
    "id": "exampleStaticMultiSelect_1",
    "type": "staticMultiSelect",
    "config": {
        "disabled": false,
        "pdfHide": false,
        "pdfWidth": 1,
        "pdfHideIfValueIsEmpty": false,
        "minAmountOfSelections": 2,
        "maxAmountOfSelections": 3,
        "uiHideInRepeaterCardDisplay": false,
        "pdfFieldRepeaterCellAlignment": "right",      
        "label": {
            "text": {
                "en": "Static Multi Select 1",
                "de": "Static Multi Select 1 [DE]",
                "tr": "Static Multi Select 1 [TR]",
                "fr": "Static Multi Select 1 [FR]",
                "es": "Static Multi Select 1 [ES]",
                "it": "Static Multi Select 1 [IT]"
            },
            "pdfHide": false,
            "pdfTextColor": "#facc2e",
            "pdfTextSize": 14,
            "uiHide": false
        },
        "value": {
            "pdfHide": false,
            "pdfStartInNewLine": false,
            "pdfTextColor": "#facc2e",
            "pdfTextSize": 14,
            "pdfAddLineBreaks": true,
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
                },
                "exampleOptionThree": {
                    "en": "Example option 3",
                    "de": "Example option 3 [DE]",
                    "tr": "Example option 3 [TR]",
                    "fr": "Example option 3 [FR]",
                    "es": "Example option 3 [ES]",
                    "it": "Example option 3 [IT]"
                }
            },
        },
        "prefill": {
            "value": [{
                "input": "none",
                "steps": [[
                    "staticStringArray",
                    [
                    "exampleOptionOne",
                    "exampleOptionTwo"
                    ]
                ]]
            }]
        }
    }
},
```
```json (BooleanInput)
{
    "id": "exampleBooleanInput_1",
    "type": "booleanInput",
    "config": {
        "required": true,
        "disabled": false,
        "pdfHide": false,
        "pdfHideIfValueIsEmpty": false,
        "pdfWidth": 1,
        "uiHideInRepeaterCardDisplay": false,
        "pdfFieldRepeaterCellAlignment": "right", 
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
        "prefill": {
            "value": [{
                "input": "none",
                "steps": [[
                    "staticBoolean",
                    true
                ]]
            }]
        }
    }
},
```

---
# Configuration Parameter


## `helpTextBefore`

| `helpTextBefore`     |                 |
| :-------------- | :-------------- |
| Possible Values | [MultiLanguageText](./24-general-properties/#multilanguagetext)    |
| Required        | no              |
| Default Value   | -               |

By setting `helpTextBefore`, a text is displayed before the repeater.

```json
      "helpTextBefore": {
          "en": "Example helptext before",
          "de": "Beispiel Hilfstext davor",
          "tr": "Example helptext before [TR]",
          "fr": "Example helptext before [FR]",
          "es": "Example helptext before [ES]",
          "it": "Example helptext before [IT]",
      },
```

---
## `helpTextAfter`

| `helpTextAfter`     |                 |
| :-------------- | :-------------- |
| Possible Values | [MultiLanguageText](./24-general-properties/#multilanguagetext)    |
| Required        | no              |
| Default Value   | -               |

By setting `helpTextAfter`, a text is displayed before the repeater.

```json
      "helpTextAfter": {
          "en": "Example helptext after",
          "de": "Beispiel Hilfstext danach",
          "tr": "Example helptext after [FR]",
          "es": "Example helptext after [ES]",
          "it": "Example helptext after [IT]",
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
| [headlineDisplay](./03-headline-display) (not displayed in the PDF)                 | The HeadlineDisplay is a field that displays headlines to structure content in the form and provide information.|
| [htmlDisplay](./23-html-display)   (not displayed in the PDF)                      | The HtmlDisplay allows the user to enter html text. |
| [singleLineTextInput](./01-single-line-text-input)       | The SingleLineTextInput field allows entering one line of unformatted text. |
| [multiLineTextInput](./02-mutli-line-text-input)         | The MultiLineTextInput field allows entering larger amounts of unformatted text.  |
| [addressInput](./04-address-input)                       | The AddressInput contains various fields for every information of an address. |
| [assetSingleSelect](./05-asset-single-select)            | The AssetSingleSelect field allows to select an asset from the account or a certain costumer.  |
| [companySingleSelect](./06-company-single-select)        | The CompanySingleSelect field allows the user to choose one of the customer companies. |
| [userSingleSelect](./08-user-single-select)              | The UserSingleSelect field allows to select a user from the own or from a customers organization. |
| [phoneNumberInput](./09-phone-number-input)              | The PhoneNumberInput field allows to input telephone numbers in the common format. | 
| [dateInput](./10-date-input)                             | The DateInput field allows to input a date. |
| [timeInput](./11-time-input)                             | The TimeInput field allows to enter a time. |
| [dateTimeInput](./12-date-time-input)                    | The DateTimeInput field allows to enter a datetime. |
| [staticSingleSelect](./13-static-single-select)          | The StaticSingleSelect field allows to choose one option of the dropdown. |
| [staticMultiSelect](./14-static-multi-select)            | The StaticMultiSelect field allows to choose one or more options of the dropdown. |
| [booleanInput](./15-boolean-input)                       | The BooleanInput allows the user to mark a checkbox true or false. |

## `uiHideInRepeaterCardDisplay`

**This property can be part of every field config of the repeated fields.**

| `uiHideInRepeaterCardDisplay`     |                 |
| :-------------- | :-------------- |
| Possible Values | `true`, `false`    |
| Required        | no              |
| Default Value   | `false`               |

By setting `uiHideInRepeaterCardDisplay` to `true` the field isn't shown in the UI.

```json
"uiHideInRepeaterCardDisplay": true,
```

## `pdfFieldRepeaterCellAlignment`

**This property can be part of every field config of the repeated fields.**


| `pdfFieldRepeaterCellAlignment`     |                 |
| :-------------- | :-------------- |
| Possible Values | `left`, `center`, `right`   |
| Required        | no              |
| Default Value   | `left`               |

By setting `pdfFieldRepeaterCellAlignment` the cell alignment gets defined.

```json
"pdfFieldRepeaterCellAlignment": "right",
```
