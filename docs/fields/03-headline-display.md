---
title: HeadlineDisplay
category: 635ce1e7775bc60045570ffb
parentDoc: 635ce486ae5fac003cef279e
---

The HeadlineDisplay is a field that displays headlines to structure content in the form.

# Configuration Overview

| Property                                                                     | Description                      |
| :--------------------------------------------------------------------------- | :--------------------------------|
| [pdfHide](./24-general-properties/#pdfhide)                                  | Setting this to `true` hides the whole field in the PDF. |
| [pdfWidth](./24-general-properties/#pdfwidth)                                | Configuration of the width of the field. |
| [pdfTextColor](./24-general-properties/#pdftextcolor)       | Text color of the label in the PDF. |
| [text](./24-general-properties/#text)                       | Localized label text of the field. Shown in the UI and the PDF. |
| [uiHide](./24-general-properties/#uihide)                   | Setting this to `true` hides the label in the UI. |
| [type](#type)         | Text size of a certain field in the UI.                                                                |

---

```json
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
        "uiHide": false,
        "type": "H1",
        "pdfHide": false,
        "pdfTextColor": "#facc2e",
        "pdfWidth": 0.5
    }
},
```

---
## `type`

| `type`   |                  |
| :-------------- | :-------------- |
| Possible Values | String `[H1, H2, H3]`     |
| Required        | no              |
| Default Value   | `H1`              |

By setting `type`, the field label will show up in the UI having the defined text size in pixels.

```json
"type": "H2"
```
