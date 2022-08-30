---
title: SingleLineTextInput
category: 62ebf4654ae80e09e468624b
parentDoc: 62ec01bd561bab0aa775efe4
---

# Single Line Text Input
>🚧 
>
> in Progress

The SingleLineTextInput field allows entering one line of unformatted text. It dosen't respects line breaks.

# Configuration Overview

| Property                                              | Description                      |
| :---------------------------------------------------- | :--------------------------------|
| [required](./24-general-properties.md)                | If this is set to `true`, the field is considered invalid as long as no value is entered. |
| [disabled](./24-general-properties.md)                | Setting this to `true` permanently disables the field in the UI. |
| [pdfHide](./24-general-properties.md)                 | Setting this to `true` hides the whole field in the PDF. |
| [pdfHideIfValueIsEmpty](./24-general-properties.md)   | Setting this to `true` hides the whole field in the PDF in case the field value is empty. |
| [pdfWidth](./24-general-properties.md)                | Configuration of the width of the field. |
| [placeHolderText](./24-general-properties.md)         | Localized placeholder text that is shown in the UI when the field is focused but does not have a value. |
| [label](#label)                                       | Configuration of the field label. |
| [value](#value)                                       | Configuration of the field value. |
| [prefill](./24-general-properties.md)                 | Configuration to prefill the field with a value upon creation of the form instance. |
| [onChange](./24-general-properties.md)                | ??? |

``` typescript (complete)