---
title: Email Section
category: 635ce1e7775bc60045570ffb
parentDoc: 635ce4870b9fa40081aaa430
---

The EmailSection contains fields to send the finshed form.
# Configuration Overview

| Property                                                                     | Description                      |
| :--------------------------------------------------------------------------- | :--------------------------------|
| [headlineText](./24-general-properties/#mulitlanguagetext) (Required!)                 | Configurate the displayed field lable |
| [helpTextHtmlAbove](./02-signature-section/#helpTextHtmlabove)                         | HTML help text above the section|
| [helpTextHtmlBelow](./02-signature-section/#helpTextHtmlbelow)                         | HTML help text below the section|
| [pdfHide](./24-general-properties/#pdfhide) (Required!)                                | Setting this to `true` hides the whole field in the PDF. |
| [pdfHideIfValueIsEmpty](./24-general-properties/#pdfhideifvalueisempty)                | Setting this to `true` hides the whole field in the PDF in case the field value is empty. |
| [requiredAmountOfOutgoingMails](#requiredamountofoutgoingmails)                        | Setting the requried amount of outgoing emails that has to be sent or marked for sending. |
| [hidePreviewPdfButton](./02-signature-section/#hidepreviewpdfbutton)                                          | Setting this to `true` hides the preview PDF button in the UI. |
| [hideDownloadPdfButton](./02-signature-section/#hidedownloadpdfbutton)                                        |  Setting this to `true` hides the download PDF button in the UI.|
| [allowSendingWhenRequiredFieldsMissing](#allowsendingwhenrequiredfieldsmissing)        | Setting this to `true` allows to send the mail even if not every required field having been filled |
| [whitelistedDomains](#whitelisteddomains)                                              | Defining domains that are whitelisted to as recipients |
| [emailDialogPrefill](#emaildialogprefill)                                              | Configuration the email prefill after the FormEmailPrefillConfig. |

```json
{
    "id": "exampleEmailSection",
    "type": "emailSection",
    "config": {
        "pdfHide": false,
        "whitelistedDomains": [],
        "headlineText": {
            "en": "Example Email Section",
            "de": "Beispiel Email Sektion",
            "tr": "Example Email Section [TR]",
            "fr": "Example Email Section [FR]",
            "es": "Example Email Section [ES]",
            "it": "Example Email Section [IT]"
        },
        "helpTextHtmlAbove": {
            "en": "<b>Example HTML helptext before</b>",
            "de": "<b>Beispiel HTML Hilfstext davor</b>",
            "tr": "<b>Example HTML helptext before [TR]</b>",
            "fr": "<b>Example HTML helptext before [FR]</b>",
            "es": "<b>Example HTML helptext before [ES]</b>",
            "it": "<b>Example HTML helptext before [IT]</b>"
        },
        "helpTextHtmlBelow": {
            "en": "<b>Example HTML helptext below</b>",
            "de": "<b>Beispiel HTML Hilfstext derunter</b>",
            "tr": "<b>Example HTML helptext below [TR]</b>",
            "fr": "<b>Example HTML helptext below [FR]</b>",
            "es": "<b>Example HTML helptext below [ES]</b>",
            "it": "<b>Example HTML helptext below [IT]</b>"
        },
        "allowSendingWhenRequiredFieldsMissing": false,
        "requiredAmountOfOutgoingMails": 2,
        "hidePreviewPdfButton": false,
        "hideDownloadPdfButton": false,
        "pdfHideIfValueIsEmpty": false,
        "emailDialogPrefill": {
            "bcc": {
                "assignee": false,
                "creator": false,
                "currentUser": true,
                "staticEmails": []
            },
            "cc": {
                "assignee": false,
                "creator": true,
                "currentUser": false,
                "staticEmails": []
            },
            "to": {
                "assignee": true,
                "creator": false,
                "currentUser": false,
                "staticEmails": []
            },
            "body": {
                "dynamic": "tbd",
                "static": "Default Content"
            },
            "subject": {
                "dynamic": "tbd",
                "static": "Default Subject"
            }
        }
    }
}
```

# Configuration Parameters
## `requiredAmountOfOutgoingMails`


| `requiredAmountOfOutgoingMails`  |                 |
| :--------------------------| :-------------- |
| Possible Values            | Integer >= `0`  |
| Required                   | no              |
| Default Value              | `0`             |

By setting `requiredAmountOfOutgoingMails`, you define the amount of mails which have to be sent or marked for sending. One mail with several recipients is still one mail, even in to, cc or bcc.
```typescript
"requiredAmountOfOutgoingMails": 3,
```

---
## `allowSendingWhenRequiredFieldsMissing`


| `allowSendingWhenRequiredFieldsMissing`  |                 |
| :--------------------------| :-------------- |
| Possible Values            | `true`, `false`  |
| Required                   | no              |
| Default Value              | `false`             |

By setting `allowSendingWhenRequiredFieldsMissing` to `true` the user is able to send the mail without all required fields having been filled.

```typescript
"allowSendingWhenRequiredFieldsMissing": true,
```
---
## `whitelistedDomains`


| `whitelistedDomains`  |                 |
| :--------------------------| :-------------- |
| Possible Values            | Array of Strings  |
| Required                   | no              |
| Default Value              | -             |

By setting `whitelistedDomains` you ensure that mails are only sent to recipients with a specific email domain. It's a security mechanism to avoid sending sensitve data to the wrong destination.

```typescript
"whitelistedDomains": [ "remberg.de", "remberg.com"],
```

---
## `emailDialogPrefill`


| `emailDialogPrefill`  |                 |
| :--------------------------| :-------------- |
| Possible Values            | [FormEmailPrefillConfig](#formemailprefillconfig)  |
| Required                   | no              |

By setting `emailDialogPrefill` you ensure that mails are only sent to recipients with a specific email domain.

## `FormEmailPrefillConfig`

| Property                                                      | Description                       |
| :------------------------------------------------------------ | :-------------------------------- |
| [to](#to)                                         | Property to enter a date|
| [cc](#cc)                                         | Property to enter a date|
| [bcc](#bcc)                                         | Property to enter a date|
| [body](#body)                                         | Property to enter a date|
| [subject](#section)                                         | Property to enter a date|

```typescript
"emailDialogPrefill": {
    "to": {
        "assignee": true,
        "creator": false,
        "currentUser": false,
        "staticEmails": []
    },
    "cc": {
        "assignee": false,
        "creator": true,
        "currentUser": false,
        "staticEmails": []
    },
    "bcc": {
        "assignee": false,
        "creator": false,
        "currentUser": true,
        "staticEmails": []
    },
    "subject": {
        "dynamic": "tbd",
        "static": "Default Subject"
    },
    "body": {
        "dynamic": "tbd",
        "static": "Default Content"
    }
}
```

---
### `to`

Duplications happens when currentUser=assignee=creator!

| Property                                                      | Description                       |
| :------------------------------------------------------------ | :-------------------------------- |
| [currentUser]                                   | Setting this to `true` prefills the field with the current user. |
| [assignee]                                         | Setting this to `true` prefills the field with the assignee. |
| [creator]                                           | Setting this to `true` prefills the field with the creator. |
| [staticEmails]                                 | Defines list of email addresses |

```typescript
"to": {
    "assignee": true,
    "creator": false,
    "currentUser": false,
    "staticEmails": []
},
```
---
### `cc`

Duplications happens when currentUser=assignee=creator!

| Property                                                      | Description                       |
| :------------------------------------------------------------ | :-------------------------------- |
| [currentUser]                                   | Setting this to `true` prefills the field with the current user. |
| [assignee]                                         | Setting this to `true` prefills the field with the assignee. |
| [creator]                                           | Setting this to `true` prefills the field with the creator. |
| [staticEmails]                                 | Defines list of email addresses |

```typescript
"cc": {
    "assignee": false,
    "creator": true,
    "currentUser": false,
    "staticEmails": []
},
```
---
### `bcc`

Duplications happens when currentUser=assignee=creator!

| Property                                                      | Description                       |
| :------------------------------------------------------------ | :-------------------------------- |
| [currentUser]                                   | Setting this to `true` prefills the field with the current user. |
| [assignee]                                         | Setting this to `true` prefills the field with the assignee. |
| [creator]                                           | Setting this to `true` prefills the field with the creator. |
| [staticEmails]                                 | Defines list of email addresses |

```typescript
"bcc": {
    "assignee": false,
    "creator": false,
    "currentUser": true,
    "staticEmails": []
},
```
---

### `subject`


| Property                                                      | Description                       |
| :------------------------------------------------------------ | :-------------------------------- |
| [static]                                                      | Static text input that can be used to pedefine the value of the `subject`. |

Allows to predefine the subject of the mail. If the subject is empty the form name is used as subject. 

```typescript
"subject": {
    "dynamic": "tbd",
    "static": "Default Subject"
},
```
---
### `body`

| Property                                                      | Description                       |
| :------------------------------------------------------------ | :-------------------------------- |
| [static]                                                      | Static text input that can be used to predefine the value of the `body`. |

Allows to predefine a message in the body. 

```typescript
"body": {
    "dynamic": "tbd",
    "static": "Default Content"
}
```