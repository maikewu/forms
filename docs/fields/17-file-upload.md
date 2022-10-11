---
title: FileUpload
category: 62ebf4654ae80e09e468624b
parentDoc: 62ec01bd561bab0aa775efe4
---

The fieldUpload field allows to upload files.
# Configuration Overview

| Property                                                                     | Description                      |
| :--------------------------------------------------------------------------- | :--------------------------------|
| [disabled](./24-general-properties/#disabled)                                | Setting this to `true` permanently disables the field in the UI. |
| [pdfHide](./24-general-properties/#pdfhide)                                  | Setting this to `true` hides the whole field in the PDF. |
| [pdfHideIfValueIsEmpty](./24-general-properties/#pdfhideifvalueisempty)      | Setting this to `true` hides the whole field in the PDF in case the field value is empty. |
| [pdfWidth](./24-general-properties/#pdfwidth)                                | Configuration of the width of the field. |
| [label](#label)                                                              | Configuration of the field label. |
| [value](#value)                                                              | Configuration of the field value. |
| [maximumSingleFileSize](#maximumsinglefilesize)                              | This configuration limits which files can be uploaded based on their size in MB |
| [maximumAccumulatedFileSize](#maximumaccumulatedfilesize)                    | This configuration limits how many files can be uploaded by defining the total sum of the file sizes in MB |
| [acceptedFileTypes](#acceptedfiletypes)                                      | This configuration contains file types within an array, that are enabled for uploading |
| [requiredAmountOfFiles](#requiredamountoffiles)                              | By setting this, the amount of files get limited to the defined value |

``` typescript (complete)
{
    id: 'exampleFileUploadInput_1',
    type: FormFieldTypesEnum.FILE_UPLOAD,
    config: {
        pdfHide: false,
        disabled: false,
        pdfHideIfValueIsEmpty: false,
        requiredAmountOfFiles: 0,
        maximumSingleFileSize: 10000, // ~10 kb
        maximumAccumulatedFileSize: 100000, // ~100 kb
        acceptedFileTypes: [],
        label: {
            text: {
                en: 'File Upload 1 [EN]',
                de: 'File Upload 1 [DE]',
                tr: 'File Upload 1 [TR]',
                fr: 'File Upload 1 [FR]',
                es: 'File Upload 1 [ES]',
                it: 'File Upload 1 [IT]',
            },
            pdfHide: false,
            pdfTextColor: '#facc2e',
            pdfTextSize: 14,
        },
        value: {
            pdfHide: false,
            pdfTextSize: 12,
            pdfStartInNewLine: false,
        },
    },
},
```

``` typescript (minimal)
{
    id: 'exampleFileUploadInput_1',
    type: FormFieldTypesEnum.FILE_UPLOAD,
    config: {
        label: {
            text: {
                en: 'File Upload 1 [EN]',
                de: 'File Upload 1 [DE]',
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
| [pdfAddLineBreaks](./24-general-properties/#pdfaddlinebreaks)                   | Setting this to `true` will add a linebreak in the PDF. |

---
## `maximumSingleFileSize`

| `maximumSingleFileSize`     |                 |
| :-------------- | :-------------- |
| Possible Values | Integer     |
| Required        | no              |
| Default Value   | `15000000` (~15 MB)             |

By setting `maximumSingleFileSize`, the maximum file size that can be uploaded gets defined.  

``` typescript
maximumSingleFileSize: 100000, // ~100 kb
```

---
## `maximumAccumulatedFileSize`

| `maximumAccumulatedFileSize`     |                 |
| :-------------- | :-------------- |
| Possible Values | Integer     |
| Required        | no              |
| Default Value   | `150000000` (~150 MB)              |

By setting `maximumAccumulatedFileSize`, the maximum accumulated file size that can be uploaded gets defined.

``` typescript
maximumAccumulatedFileSize: 1000000, // ~1 MB
```

---

## `acceptedFileTypes`

| `acceptedFileTypes`     |                 |
| :-------------- | :-------------- |
| Possible Values | [Strings], e.g.  `image/png`, `application/pdf`    |
| Required        | no              |
| Default Value   | -               |

By setting `acceptedFileTypes`, the file types that can be uploaded gets defined in an array of strings.
You can find a list with all possible values [here](https://www.iana.org/assignments/media-types/media-types.xhtml)

``` typescript
acceptedFileTypes: [ `application/pdf`, `image/png`],
```

---

## `requiredAmountOfFiles`

| `requiredAmountOfFiles`     |                 |
| :-------------- | :-------------- |
| Possible Values | Integer    |
| Required        | no              |
| Default Value   | 0               |

By setting `requiredAmountOfFiles`, the amount of required entries to fill the form gets defined
``` typescript
requiredAmountOfFiles: 3,
```

---