---
title: HtmlDisplay
category: 62ebf4654ae80e09e468624b
parentDoc: 62ec01bd561bab0aa775efe4
---

# Configuration Overview

| Property                                                                     | Description                      |
| :--------------------------------------------------------------------------- | :--------------------------------|
| [pdfHide](./24-general-properties/#pdfhide)                                  | Setting this to `true` hides the whole field in the PDF. |
| [pdfWidth](./24-general-properties/#pdfwidth)                                | Configuration of the width of the field. |
| [text](./24-general-properties/#text)                       | Localized label text of the field. Shown in the UI and the PDF. |#
| [uiHide](./24-general-properties/#uihide)                   | Setting this to `true` hides the label in the UI. |

```Typescript
{
    id: 'exampleHtmlDisplay_1',
    type: FormFieldTypesEnum.HTML_DISPLAY,
    config: {
        pdfHide: false,
        pdfWidth: 1,
        uiHide: false,
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
```