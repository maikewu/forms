---
title: HtmlDisplay
category: 635ce1e7775bc60045570ffb
parentDoc: 635ce486ae5fac003cef279e
---

The HtmlDisplay allows the user to enter html text.
# Configuration Overview

| Property                                                                     | Description                      |
| :--------------------------------------------------------------------------- | :--------------------------------|
| [pdfHide](./24-general-properties/#pdfhide)                                  | Setting this to `true` hides the whole field in the PDF. |
| [pdfWidth](./24-general-properties/#pdfwidth)                                | Configuration of the width of the field. |
| [text](./24-general-properties/#text)                       | Localized label text of the field. Shown in the UI and the PDF. |#
| [uiHide](./24-general-properties/#uihide)                   | Setting this to `true` hides the label in the UI. |

```JSON
{
    "id": "exampleHtmlDisplay_1",
    "type": "htmlDisplay",
    "config": {
        "pdfHide": false,
        "pdfWidth": 1,
        "uiHide": false,
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