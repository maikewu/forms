---
title: HeadlineDisplay
category: 62ebf4654ae80e09e468624b
parentDoc: 62ec01bd561bab0aa775efe4
---

The HeadlineDisplay is a field that displays headlines to structure content in the form and provisde information.

# Configuration Overview

| Property                                                                     | Description                      |
| :--------------------------------------------------------------------------- | :--------------------------------|
| [pdfHide](./24-general-properties/#pdfhide)                                  | Setting this to `true` hides the whole field in the PDF. |
| [pdfWidth](./24-general-properties/#pdfwidth)                                | Configuration of the width of the field. |
| [pdfTextSize](./24-general-properties/#pdftextsize)         | Text size of the label in the PDF. |
| [pdfTextColor](./24-general-properties/#pdftextcolor)       | Text color of the label in the PDF. |
| [text](./24-general-properties/#text)                       | Localized label text of the field. Shown in the UI and the PDF. |
| [uiHide](./24-general-properties/#uihide)                   | Setting this to `true` hides the label in the UI. |
| [uiTextColor](./24-general-properties/#uitextcolor)         | Text color of a certain field in the UI.                                                                |
| [uiTextSize](#uitextsize)         | Text size of a certain field in the UI.                                                                |

---

```typescript
{
    id: 'exampleHeadlineDisplay_1',
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
        uiHide: false,
        uiTextSize: 'H1',
        uiTextColor: '#facc2e',
        pdfHide: false,
        pdfTextSize: 'H1',
        pdfTextColor: '#facc2e',
        pdfWidth: 0.5,
    },
},
```

---
## `uiTextSize`

| `uiTextSize`   |                  |
| :-------------- | :-------------- |
| Possible Values | String `[H1, H2, H3]`     |
| Required        | no              |
| Default Value   | `H1`              |

By setting `uiTextSize`, the field label will show up in the UI having the defined text size in pixels.

``` typescript
uiTextSize: H2
```
