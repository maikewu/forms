---
title: Field Section
category: 635ce1e7775bc60045570ffb
parentDoc: 635ce4870b9fa40081aaa430
---

The FieldSection contains all fields of the form.

# Configuration Overview

| Property                                                                     | Description                      |
| :--------------------------------------------------------------------------- | :--------------------------------|
| [headlineText](#fields)                   | Configurate the displayed field lable |
| [fields](#fields)                                                            | Field properties of a form. |


```json
"sections": [
    {
      "id": "exampleFieldSection",
      "type": "fieldSection",
      "config": {
        "headlineText": {
          "en": "Example Field Section",
          "de": "Beispiel Feld Sektion",
          "tr": "Example Field Section [TR]",
          "fr": "Example Field Section [FR]",
          "es": "Example Field Section [ES]",
          "it": "Example Field Section [IT]"
        }
      },
      "fields": [
                {
                  ... // enter field properties
                }
            ]
        }
    ]
```
---

# Configuration Parameters

## `fields` 

The field section contains all fields of a form that are necessary for the service to be done.
You can find a list of possible fields below. Besides them a form consists of a [signatureSection](./02-signature-section) or a [emailSection](./03-email-section)

| Property                                                 | Description                                                                                                  |
| :--------------------------------------------------------| :----------------------------------------------------------------------------------------------------------- |
| [singleLineTextInput](./01-single-line-text-input)       | The SingleLineTextInput field allows entering one line of unformatted text. |
| [multiLineTextInput](./02-mutli-line-text-input)         | The MultiLineTextInput field allows entering larger amounts of unformatted text.  |
| [headlineDisplay](./03-headline-display)                 | The HeadlineDisplay is a field that displays headlines to structure content in the form and provisde information.|
| [addressInput](./04-address-input)                       | The AddressInput contains various fields for every information of an address. |
| [assetSingleSelect](./05-asset-single-select)            | The AssetSingleSelect field allows to select an asset from the account or a certain costumer.  |
| [companySingleSelect](./06-company-single-select)        | The CompanySingleSelect field allows the user to choose one of the customer companys. |
| [personListInput](./07-person-list-input)                | The PersonListInput field allows to enter user. |
| [userSingleSelect](./08-user-single-select)              | The UserSingleSelect field allows to select a user from the own or from a customers organisation. |
| [phoneNumberInput](./09-phone-number-input)              | The PhoneNumberInput field allows to input telephone numbers in the common format. | 
| [dateInput](./10-date-input)                             | The DateInput field allows to input a date. |
| [timeInput](./11-time-input)                             | The TimeInput field allows to enter a time. |
| [dateTimeInput](./12-date-time-input)                    | The DateTimeInput field allows to enter a datetime. |
| [staticSingleSelect](./13-static-single-select)          | The StaticSingleSelect field allows to choose one option of the dropdown. |
| [staticMultiSelect](./14-static-multi-select)            | The StaticMultiSelect field allows to choose one or more options of the dropdown. |
| [booleanInput](./15-boolean-input)                       | The BooleanInput allows the user to mark a checkbox true or false. |
| [timeTrackingListInput](./16-time-trackiing-list-input)  | The TimeTrackingListInput allows the user to enter times for travel, working or breaks. |
| [fileUpload](./17-file-upload)                           | The FieldUpload field allows to upload files. |
| [taskListInput](./18-task-list-input)                    | The TaskListInput enables the user to create performed tasks. |
| [partListInput](./19-part-list-input)                    | Within the PartListInput, the user can add parts to an form. |
| [expensesListInput](./20-expense-list-input)             | The ExpenseListInput allows the user to add expenses. |
| [fieldRepeater](./21-field-repeater)                     | The FieldRepeater allows the user to add a table of certain fields. |
| [richTextInput](./22-rich-text-input)                    | The RichTextInput is a text field that allows text formatting. |
| [htmlDisplay](./23-html-display)                         | The HtmlDisplay allows the user to enter html text. |

## `headlineText`

| Property                                                    | Description                       |
| :---------------------------------------------------------- | :-------------------------------- |
| [text](./24-general-properties/#text)                       | Localized label text of the field. Shown in the UI and the PDF. |
| [pdfHide](./24-general-properties/#pdfhide)                 | Setting this to `true` hides the label in the PDF. |


