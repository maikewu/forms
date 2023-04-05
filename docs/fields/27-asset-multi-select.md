---
title: AssetMultiSelect
category: 635ce1e7775bc60045570ffb
parentDoc: 635ce486ae5fac003cef279e
---

The AssetMultiSelect field allows to select assets from the account or a certain customer.

# Configuration Overview

| Property                                                                     | Description                      |
| :--------------------------------------------------------------------------- | :--------------------------------|
| [requiredAmountOfEntries](./24-general-properties/#requiredamountofentries)  | If this is set to anything above `0`, the field is considered invalid as long as no value is entered. |
| [disabled](./24-general-properties/#disabled)                                | Setting this to `true` permanently disables the field in the UI. |
| [pdfHide](./24-general-properties/#pdfhide)                                  | Setting this to `true` hides the whole field in the PDF. |
| [pdfHideIfValueIsEmpty](./24-general-properties/#pdfhideifvalueisempty)      | Setting this to `true` hides the whole field in the PDF in case the field value is empty. |
| [pdfWidth](./24-general-properties/#pdfwidth)                                | Configuration of the width of the field. |
| [label](#label)                                                              | Configuration of the field label. |
| [value](#value)                                                              | Configuration of the field value. |
| [prefill](#prefill)                                                          | Configuration to prefill the field with a value upon creation of the form instance. |

```json (complete)
{
  "id": "uniqueId",
  "type": "assetMultiSelect",
  "config": {
    "disabled": false,
    "pdfHide": false,
    "pdfHideIfValueIsEmpty": false,
    "pdfWidth": 1,
    "requiredAmountOfEntries": 0,
    "label": {
      "text": {
        "en": "",
        "de": "",
        "tr": "",
        "fr": "",
        "es": "",
        "it": ""
      },
      "pdfHide": false,
      "pdfTextColor": "#000000",
      "pdfTextSize": 14
    },
    "value": {
      "disableAssetFormInstanceRelationship": false,
      "disableCreation": false,
      "pdfHide": false,
      "pdfStartInNewLine": false,
      "pdfTextColor": "#000000",
      "pdfTextSize": 14,
      "pdfAddLineBreaks": false
    },
    "prefill": {
      "selectedAssets": [
        {
          "input": "workOrderId",
          "steps": [
            "workOrderIdToWorkOrder",
            "workOrderToAssetIds"
          ]
        }
      ]
    }
  }
}
```

---
# Configuration Parameters

## `label`

| Property                                                    | Description                       |
| :---------------------------------------------------------- | :-------------------------------- |
| [text](./24-general-properties/#text)                       | Localized label text of the field. Shown in the UI and the PDF. |
| [uiHide](./24-general-properties/#uihide)                   | Setting this to `true` hides the label in the UI. |
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
| [disableCreation](./24-general-properties/#disablecreation)                                             | Hides the create button, so that no new asset can be created.  |
| [disableAssetFormInstanceRelationship](./24-general-properties.md/#disableAssetFormInstanceRelationship) | Setting this to `true` will unlink the form from the asset detail pages |

---
## `prefill`

| `prefill`                  |                                                                     |
| :------------------------- | :--------------                                                     |
| Possible Values            | Array of [PrefillRules](./25-prefill-rules)            |
| Required                   | no                                                                  |
| Default Value              | -                                                                   |

This configuration follows the [general syntax for prefilling rules](./25-prefill-rules).
```json (assetID)
"prefill": {
	"selectedAssets": [
		{
			"input": "workOrderId",
			"steps": [
				"workOrderIdToWorkOrder",
				"workOrderToAssetIds"
			]
		}
	]
}
```

