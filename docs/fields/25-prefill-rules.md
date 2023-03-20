---
title: PrefillRules
category: 635ce1e7775bc60045570ffb
parentDoc: 635ce486ae5fac003cef279e
---
## Concept

Prefill allows you to prepopulate fields with values when creating a new form instance.
To do this, prefill rules must be defined in the form code for the respective fields. 
The prefill rule schema contains targets, inputs and steps.

Each field can have multiple prefill rules. When a form is created, the backend tries to execute all the prefill rules successively until one of them can be fully applied because the required data is available.

Schema:
```json (Prefill schema)
"prefill": {
	"target_type": [
		{ // These brackets contain the first prefill rule
			"input": "provided_data1", 
			"steps": [
				"transformation_step1" // step to transform the data type
			]
		}
		{ // These brackets contain the second prefill rule, which got only applied when the first input value "rule1_value1" isn't available
			"input": "provided_data2",
			"steps": [
			  "transformation_step2_1", // steps to transform the data type
			  "transformation_step2_2"
			]
		}
	]
}
```

--- 
`target` locates the property to which data is to be written. The target name has to be written to the `"input":` section of the prefill rule

All available <code>target</code> values

| Section                  |      `target type`      |
| :------------------------- | :--------------|
| SignatureSection| `name`, `location`, `date`
   
| Field                  |      `target type`      |
| :------------------------- | :--------------|
|SingleLineTextInput| `value`
|MultiLineTextInput| `value`
|AddressInput| `value`
|BooleanInput| `value`
|RichTextInput| `value`
|StaticSingleSelect| `value`
|StaticMultiSelect| `value`
|AssetSingleSelect| `selectedAsset`
|DateInput| `value`
|TimeInput| `value`
|PhoneNumberInput| `value`
|DateTimeInput| `value`
|TaskListInput| `entries`
|UserSingleSelect| `value`
|CompanySingleSelect| `selectedCompany` 
</details>

---
Each field has an expected data type:

| Field name               | Expected data type                   |
| :----------------------------- | :---------------------------|
| `singleLineTextInput` | `STRING` |
| `multiLineTextInput` | `STRING` |
| `booleanInput`| `BOOLEAN`|
| `richTextInput`| `STRING`|
| `assetSingleSelect` | `ASSET_ID`|
| `addressInput` | `ADDRESS`|
| `dateInput` | `REMBERG_DATE`|
| `timeInput` | `REMBERG_TIME`|
| `dateTimeInput` | `REMBERG_DATETIME`|
| `staticSingleSelect` | `STRING`|
| `staticMultiSelect` | `ARRAY_OF_STRINGS`|
| `userSingleSelect` | `USER_ID`|
| `phoneNumberInput` | `PHONE_NUMBER`|
| `companySingleSelect` | `ACCOUNT_ID`|
| `taskListInput` | `TASKS`|

| `signatureSection`: property Name              | Expected data type                   |
| :----------------------------- | :---------------------------|
| `NAME` | `STRING`|
| `LOCATION` | `STRING`|
| `DATE` | `REMBERG_DATE`|

---
`input` can be a separate source that already contains information, e.g. a work order, or a own defined input value,
that should be prepopulate to the form

<details>
<summary>All available <code>input</code> sources, their values and data types</summary>

`none` has to be used, when you would like to prepopulate a own defined value to the property.

| Source               | `input` (provided) value | Data type |
| :----------------------------- | :----- | :-----|
| [Asset view](#asset-view) | `assetId`| `ASSET_ID` (equals `STRING`)
| Selected organization |`organizationId` | `ACCOUNT_ID` (equals `STRING`)
| Form creation date time |`creationDateTime` | `REMBERG_DATE`
| Current user | `currentUser` | `USER_INFO`
| Current user | `currentUserId` | `USER_ID` (equals `STRING`)
| Current account | `currentAccount` | `ACCOUNT`
| Current account  |`currentAccountId` | `ACCOUNT_ID` (equals `STRING`)
| [WorkOrder view](#work-order-view) |`assignedUserId` | `USER_ID` (equals `STRING`)
| [WorkOrder view](#work-order-view) |`workOrderId` | `WORK_ORDER_ID` (equals `STRING`)
| - | `none`| `NONE`

</details>

---
`steps` can be used to transform the data if the `input` data type does not match the expected data type of the `target`.

<details>
<summary>All available <code>steps</code> and their input and output data type </summary>

`steps` have an input (expected) data type and an output (provided) data type. 
By chaining steps, the desired data type can be achieved "step by step". 

**Note:** `OrganizationID` can use the same steps which convert the `accountID` datatype.

| `steps`               | input data type  | output data type |
| :----------------------------- | :----- | :-----|
| `dateTimeToDate` | `REMBERG_DATETIME`| `REMBERG_DATE`
| `assetIdToAsset` | `ASSET_ID`| `ASSET`
| `userIdToUser` | `USER_ID`| `USER_INFO`
| `accountIdToAccount` | `ACCOUNT_ID`| `ACCOUNT`
| `userToFullNameString` | `USER_INFO` | `STRING`
| `assetToLocationAddress` | `ASSET`| `ADDRESS`
| `assetToCustomerAccountId` | `ASSET`| `ACCOUNT_ID`
| `assetToAssetTypeNameString` | `ASSET`| `STRING`
| `assetToCustomPropertyValue` | `[ASSET, NUMBER]`| `UNKNOWN`
| `accountToBillingAddressAddress` | `ACCOUNT`| `ADDRESS`
| `addressToCityString` | `ADDRESS`| `STRING`
| `customPropertyValueToString` | `UNKNOWN`| `STRING`
| `customPropertyValueToArrayOfStrings` | `UNKNOWN`| `ARRAY_OF_STRINGS`
| `customPropertyValueToNumberString` | `UNKNOWN`| `STRING`
| `customPropertyValueToNumber` | `UNKNOWN`| `NUMBER`
| `customPropertyValueToBoolean` | `UNKNOWN`| `BOOLEAN`
| `customPropertyValueToAssetId` | `UNKNOWN`| `ASSET_ID`
| `customPropertyValueToAccountId` | `UNKNOWN`| `ACCOUNT_ID`
| `customPropertyValueToUserId` | `UNKNOWN`| `USER_ID`
| `customPropertyValueToDate` | `UNKNOWN`| `REMBERG_DATE`
| `customPropertyValueToDateTime` | `UNKNOWN`| `REMBERG_DATETIME`
| `workOrderIdToWorkOrder` | `WORK_ORDER_ID`| `WORK_ORDER`
| `workOrderToLocationAddress` | `WORK_ORDER`| `ADDRESS`
| `workOrderToTasks` | `WORK_ORDER`| `TASKS`
| `workOrderToTitleString` | `WORK_ORDER`| `STRING`
| `workOrderToDescriptionString` | `WORK_ORDER`| `STRING`
| `workOrderToDueDate` | `WORK_ORDER`| `REMBERG_DATE`
| `workOrderToStartDate` | `WORK_ORDER`| `REMBERG_DATE`
| `workOrderToEndDate` | `WORK_ORDER`| `REMBERG_DATE`
| `workOrderToERPReferenceString` | `WORK_ORDER`| `STRING`
| `workOrderToResponsibleUserId` | `WORK_ORDER`| `USER_ID`
| `workOrderToStatusNumberString` | `WORK_ORDER`| `STRING`
| `workOrderToTypeNumberString` | `WORK_ORDER`| `STRING`
| `workOrderToPriorityString` | `WORK_ORDER`| `STRING`
| `workOrderToPerformByUserId` | `WORK_ORDER`| `USER_ID`
| `workOrderToAdditionalContactInformationString` | `WORK_ORDER`| `STRING`
| `workOrderToCaseSubjectString` | `WORK_ORDER`| `STRING`
| `workOrderToCaseTicketAndSubjectString` | `WORK_ORDER`| `STRING`
| `workOrderToOrganizationAccountId` | `WORK_ORDER`| `ACCOUNT_ID`
| `workOrderToCustomPropertyValue` | `[WORK_ORDER, NUMBER]`| `UNKNOWN`
| `staticString` | `[NONE, STRING]`| `STRING`
| `staticStringArray` | `[NONE, ARRAY_OF_STRINGS]`| `ARRAY_OF_STRINGS`
| `staticBoolean` | `[NONE, BOOLEAN]`| `BOOLEAN`
| `staticAddress` | `[NONE, ADDRESS]`| `ADDRESS`
| `staticDate` | `[NONE, REMBERG_DATE]`| `REMBERG_DATE`
| `staticTime` | `[NONE, REMBERG_TIME]`| `REMBERG_TIME`
| `staticPhoneNumber` | `[NONE, PHONE_NUMBER]`| `PHONE_NUMBER`
| `staticDateTime` | `[NONE, REMBERG_DATETIME]`| `REMBERG_DATETIME`
| `staticTasks` | `[NONE, TASKS]`| `TASKS`

</details>

---

### Prefill: expected data type

| Field name               | Expected data type                   |
| :----------------------------- | :---------------------------|
| `singleLineTextInput` | `STRING` |
| `multiLineTextInput` | `STRING` |
| `booleanInput`| `BOOLEAN`|
| `richTextInput`| `STRING`|
| `assetSingleSelect` | `ASSET_ID`|
| `addressInput` | `ADDRESS`|
| `dateInput` | `REMBERG_DATE`|
| `timeInput` | `REMBERG_TIME`|
| `dateTimeInput` | `REMBERG_DATETIME`|
| `staticSingleSelect` | `STRING`|
| `staticMultiSelect` | `ARRAY_OF_STRINGS`|
| `userSingleSelect` | `USER_ID`|
| `phoneNumberInput` | `PHONE_NUMBER`|
| `companySingleSelect` | `ACCOUNT_ID`|
| `taskListInput` | `TASKS`|

| `signatureSection`: property Name              | Expected data type                   |
| :----------------------------- | :---------------------------|
| `NAME` | `STRING`|
| `LOCATION` | `STRING`|
| `DATE` | `REMBERG_DATE`|

---
## Asset View
If you create a new forms instance from an asset (Asset View), the following data is provided:

| Data | Condition | Description |
| :------------------------- | :--------------| :---- |
| `assetId`  |  |  The ID of the asset form which the new form is created
| `organizationId` | | The ID of the assigned company in the work order or from the asset
| `creationDateTime`  |  | The creation date time of form 
| `currentUser`  |  |  	Information about the current user, including the name, ID, etc.
| `currentUserId`  |  |  The ID of the user who is logged in and creates the form instance
| `currentAccount`  |  |  Information about the current space, including the name, address, ID, etc.
| `currentAccountId`  |  |  	The ID of the current space
| [customProperty](#custom-properties) |  | One of the specific custom asset properties
| `assignedUserId`  | Optional |  The ID of the user, who is assigned to the new form instance

Some Asset derived values first need be mapped to a real readable value, especially values from a custom property multi select. The following examples will illustrate the mapping process:

```json (assetToCustomPropertyValue)
{
	"id": "customPropertyValueToStringTestIdFromMultiSelect",
	"type": "staticMultiSelect",
	"config": {
		"label": {
			"text": {
				"en": "preffiled from asset custom property Multi Select",
				"de": "preffiled from asset custom property Multi Select"
			}
		},
		"value": {
			"options": {
				"Option 1": {
					"en": "Option 1",
					"de": "Option 1"
				},
				"Option 62374": {
					"en": "Option 62374",
					"de": "Option 62374"
				},
				"Option 101": {
					"en": "Option 101",
					"de": "Option 101"
				}
			}
		},
		"prefill": {
			"value": [
				{
					"input": "assetId",
					"steps": [
						"assetIdToAsset",
						[
							"assetToCustomPropertyValue",
							9
						],
						"customPropertyValueToArrayOfStrings"
					]
				}
			]
		}
	}
}
```

---
 ## Work Order View
If you create a new forms instance from a work order, the following data is provided:


| Data | Condition | Description |
| :------------------------- | :--------------| :---- |
| `WorkOrderId`  |  |  The ID of the work order from which the form is created
| `organizationId`  | If WO has connected company | The ID of the company (contact) which is connected to the work order
| `assetId`  | If WO has assets |  The ID of the asset which is part of the work order
| [customProperty](#custom-properties) |  | One of the specific custom work order properties
| `currentUser`  |  | Information about the current user, including the name, ID, etc.
| `currentUserId`  |  | The ID of the user who is logged in and creates the form instance
| `currentAccount`  |  | Information about the current space, including the name, address, ID, etc.
| `currentAccountId`  |  | The ID of the current space 
| `assignedUserId`  | Optional |  The ID of the user, who is assigned to the new form instance

Some Work Order derived values first need be mapped to a real readable value. The following examples will illustrate the mapping process:

```json (assetToCustomPropertyValue)
{
	"id": "statusFromWO",
	"type": "staticSingleSelect",
	"config": {
		"required": true,
		"label": {
			"text": {
				"en": "status prefilled from Workorder",
				"de": "Status vorauselektiert vom Auftrag"
			}
		},
		"value": {
			"options": {
				"0": {
					"en": "Open",
					"de": "Offen"
				},
				"1": {
					"en": "In Progress",
					"de": "In Bearbeitung"
				},
				"2": {
					"en": "On Hold",
					"de": "Angehalten"
				},
				"3": {
					"en": "Completed",
					"de": "Abgeschlossen"
				},
				"4": {
					"en": "Closed",
					"de": "Geschlossen"
				}
			}
		},
		"prefill": {
			"value": [
				{
					"input": "workOrderId",
					"steps": [
						"workOrderIdToWorkOrder",
						"workOrderToStatusNumberString"
					]
				}
			]
		}
	}
}
```

---
## Custom Properties

Custom Properties of the respective space can be extracted. These include Custom Work Order Properties and Custom Asset Properties. To extract a custom Property, one must first know their respective ID.

The following examples illustrate the extraction of a custom property, the custom property ID is always placed in between the [] brackets after the step `workOrderToCustomPropertyValue` or `assetToCustomPropertyValue`:


```json (CompanySingleSelect)
//prefill companySingleSelect in form with company of remberg_company custom property in work order
"prefill": {
	"selectedCompany": [
		{
			"input": "workOrderId",
			"steps": [
				"workOrderIdToWorkOrder",
				[
					"workOrderToCustomPropertyValue",
					8
				],
				"customPropertyValueToAccountId"
			]
		}
	]
}
```
```json (AssetSingleSelect)
//prefill assetSingleSelect in form with asset of remberg_asset custom property in work order
"prefill": {
	"selectedAsset": [
		{
			"input": "workOrderId",
			"steps": [
				"workOrderIdToWorkOrder",
				[
					"workOrderToCustomPropertyValue",
					9
				],
				"customPropertyValueToAssetId"
			]
		}
	]
}

//prefill remberg_asset_select custom asset property 
"prefill": {
	"selectedAsset": [
		{
			"input": "assetId",
			"steps": [
				"assetIdToAsset",
				["assetToCustomPropertyValue",1],
				"customPropertyValueToAssetId"
			]
		}
	]
}
```
```json (SingleLineTextInput)
//prefill work order singleLine custom property
"prefill": {
	"value": [
		{
			"input": "workOrderId",
			"steps": [
				"workOrderIdToWorkOrder",
				["workOrderToCustomPropertyValue",1],
				"customPropertyValueToString"
			]
		}
	]
}

//prefill string from asset custom property
"prefill": {
	"value": [
		{
			"input": "assetId",
			"steps": [
				"assetIdToAsset",
				["assetToCustomPropertyValue",5],
				"customPropertyValueToString"
			]
		}
	]
}
```
```json (MultiLineTextInput)
//prefill asset text area or text input custom property
"prefill": {
	"value": [
		{
			"input": "assetId",
			"steps": [
				"assetIdToAsset",
				["assetToCustomPropertyValue",5],
				"customPropertyValueToString"
			]
		}
	]
}
```
```json (BooleanInput)
//Prefill from work order custom property checkbox
"prefill": {
	"value": [
		{
			"input": "workOrderId",
			"steps": [
				"workOrderIdToWorkOrder",
				["workOrderToCustomPropertyValue",2],
				"customPropertyValueToBoolean"
			]
		}
	]
}

//prefill from asset custom property checkbox
"prefill": {
	"value": [
		{
			"input": "assetId",
			"steps": [
				"assetIdToAsset",
				["assetToCustomPropertyValue",4],
				"customPropertyValueToBoolean"
			]
		}
	]
}
```
```json (staticSingleSelect)
//prefill from work order single select custom property
"value": {
	"options": {
		"Option 01010": {
			"en": "Option 01010",
			"de": "Option 01010"
		},
		"Option 202020": {
			"en": "Option 202020",
			"de": "Option 202020"
		},
		"Option 0303030": {
			"en": "Option 0303030",
			"de": "Option 0303030"
		}
	}
},
"prefill": {
	"value": [
		{
			"input": "workOrderId",
			"steps": [
				"workOrderIdToWorkOrder",
				["workOrderToCustomPropertyValue",3],
				"customPropertyValueToString"
			]
		}
	]
}
```
```json (staticMultiSelect)
//prefill from work order multi select custom property (order of options must be same as in custom prop)
"value": {
	"options": {
		"multi Option 1": {
			"de": "multi Option 1",
			"en": "multi Option 1"
		},
		"multi Option 2": {
			"de": "multi Option 2",
			"en": "multi Option 2"
		},
		"multi Option 3": {
			"de": "multi Option 3",
			"en": "multi Option 3"
		}
	}
},
"prefill": {
	"value": [
		{
			"input": "workOrderId",
			"steps": [
				"workOrderIdToWorkOrder",
				["workOrderToCustomPropertyValue",4],
				"customPropertyValueToArrayOfStrings"
			]
		}
	]
}

//prefill from asset multi select custom property (order of options must be same as in custom prop)
"value": {
	"options": {
		"Option 1": {
			"en": "Option 1",
			"de": "Option 1"
		},
		"Option 62374": {
			"en": "Option 62374",
			"de": "Option 62374"
		},
		"Option 101": {
			"en": "Option 101",
			"de": "Option 101"
		}
	}
},
"prefill": {
	"value": [
		{
			"input": "assetId",
			"steps": [
				"assetIdToAsset",
				["assetToCustomPropertyValue",9],
				"customPropertyValueToArrayOfStrings"
			]
		}
	]
}
```
```json (DateInput)
//prefill from work order date custom property
"prefill": {
	"value": [
		{
			"input": "workOrderId",
			"steps": [
				"workOrderIdToWorkOrder",
				["workOrderToCustomPropertyValue",5],
				"customPropertyValueToDate"
			]
		}
	]
}

//prefill asset date custom property
"prefill": {
	"value": [
		{
			"input": "assetId",
			"steps": [
				"assetIdToAsset",
				["assetToCustomPropertyValue",7],
				"customPropertyValueToDate"
			]
		}
	]
}
```
```json (DateTimeInput)
// Do not copy comments!
//prefill work order datetime custom property
"prefill": {
	"value": [
		{
			"input": "workOrderId",
			"steps": [
				"workOrderIdToWorkOrder",
				["workOrderToCustomPropertyValue",6],
				"customPropertyValueToDateTime"
			]
		}
	]
}

//prefill asset datetime custom property
"prefill": {
	"value": [
		{
			"input": "assetId",
			"steps": [
				"assetIdToAsset",
				["assetToCustomPropertyValue",8],
				"customPropertyValueToDateTime"
			]
		}
	]
}
```
```json (userSingleSelect)
//prefill work order remberg_user custom property
"prefill": {
	"value": [
		{
			"input": "workOrderId",
			"steps": [
				"workOrderIdToWorkOrder",
				["workOrderToCustomPropertyValue",7],
				"customPropertyValueToUserId"
			]
		}
	]
}

//prefill manufacturer (tenant) contact person of asset
"prefill": {
	"value": [
		{
			"input": "assetId",
			"steps": [
				"assetIdToAsset",
				"assetToManufacturerPersonUserId"
			]
		}
	]
}

//prefill customer contact person of asset
"prefill": {
	"value": [
		{
			"input": "assetId",
			"steps": [
				"assetIdToAsset",
				"assetToCustomerPersonUserId"
			]
		}
	]
}

//prefill user from remberg_user custom asset property
"prefill": {
	"value": [
		{
			"input": "assetId",
			"steps": [
				"assetIdToAsset",
				["assetToCustomPropertyValue",2],
				"customPropertyValueToUserId"
			]
		}
	]
}
```
```json (customPropertyValueToNumberString)
"prefill": {
	"value": [
		{
			"input": "workOrderId",
			"steps": [
				"workOrderIdToWorkOrder",
				[
					"workOrderToCustomPropertyValue",
					10
				],
				"customPropertyValueToNumberString"
			]
		}   
	]
}
```

---
## Properties





<details>
<summary>All available <code>steps</code> and their input and output data type </summary>

`steps` have an input (expected) data type and an output (provided) data type. 
By chaining steps, the desired data type can be achieved "step by step". 

| `steps`               | input data type  | output data type |
| :----------------------------- | :----- | :-----|
| `dateTimeToDate` | `REMBERG_DATETIME`| `REMBERG_DATE`
| `assetIdToUser` | `ASSET_ID`| `ASSET`
| `userIdToUser` | `USER_ID`| `USER_INFO`
| `accountIdToAccount` | `ACCOUNT_ID`| `ACCOUNT`
| `userToFullNameString` | `USER_INFO` | `STRING`
| `assetToLocationAddress` | `ASSET`| `ADDRESS`
| `assetToCustomerAccountId` | `ASSET`| `ACCOUNT_ID`
| `assetToAssetTypeNameString` | `ASSET`| `STRING`
| `assetToCustomPropertyValue` | `[ASSET, NUMBER]`| `UNKNOWN`
| `accountToBillingAddressAddress` | `ACCOUNT`| `ADDRESS`
| `addressToCityString` | `ADDRESS`| `STRING`
| `customPropertyValueToString` | `UNKNOWN`| `STRING`
| `customPropertyValueToArrayOfStrings` | `UNKNOWN`| `ARRAY_OF_STRINGS`
| `customPropertyValueToNumberString` | `UNKNOWN`| `STRING`
| `customPropertyValueToNumber` | `UNKNOWN`| `NUMBER`
| `customPropertyValueToBoolean` | `UNKNOWN`| `BOOLEAN`
| `customPropertyValueToAssetId` | `UNKNOWN`| `ASSET_ID`
| `customPropertyValueToAccountId` | `UNKNOWN`| `ACCOUNT_ID`
| `customPropertyValueToUserId` | `UNKNOWN`| `USER_ID`
| `customPropertyValueToDate` | `UNKNOWN`| `REMBERG_DATE`
| `customPropertyValueToDateTime` | `UNKNOWN`| `REMBERG_DATETIME`
| `workOrderIdToWorkOrder` | `WORK_ORDER_ID`| `WORK_ORDER`
| `workOrderToLocationAddress` | `WORK_ORDER`| `ADDRESS`
| `workOrderToTasks` | `WORK_ORDER`| `TASKS`
| `workOrderToTitleString` | `WORK_ORDER`| `STRING`
| `workOrderToDescriptionString` | `WORK_ORDER`| `STRING`
| `workOrderToDueDate` | `WORK_ORDER`| `REMBERG_DATE`
| `workOrderToStartDate` | `WORK_ORDER`| `REMBERG_DATE`
| `workOrderToEndDate` | `WORK_ORDER`| `REMBERG_DATE`
| `workOrderToERPReferenceString` | `WORK_ORDER`| `STRING`
| `workOrderToResponsibleUserId` | `WORK_ORDER`| `USER_ID`
| `workOrderToStatusNumberString` | `WORK_ORDER`| `STRING`
| `workOrderToTypeNumberString` | `WORK_ORDER`| `STRING`
| `workOrderToPriorityString` | `WORK_ORDER`| `STRING`
| `workOrderToPerformByUserId` | `WORK_ORDER`| `USER_ID`
| `workOrderToAdditionalContactInformationString` | `WORK_ORDER`| `STRING`
| `workOrderToCaseSubjectString` | `WORK_ORDER`| `STRING`
| `workOrderToCaseTicketAndSubjectString` | `WORK_ORDER`| `STRING`
| `workOrderToOrganizationAccountId` | `WORK_ORDER`| `ACCOUNT_ID`
| `workOrderToCustomPropertyValue` | `[ASSET, NUMBER]`| `UNKNOWN`
| `staticString` | `[NONE, STRING]`| `STRING`
| `staticStringArray` | `[NONE, ARRAY_OF_STRINGS]`| `ARRAY_OF_STRINGS`
| `staticBoolean` | `[NONE, BOOLEAN]`| `BOOLEAN`
| `staticAddress` | `[NONE, ADDRESS]`| `ADDRESS`
| `staticDate` | `[NONE, REMBERG_DATE]`| `REMBERG_DATE`
| `staticTime` | `[NONE, REMBERG_TIME]`| `REMBERG_TIME`
| `staticPhoneNumber` | `[NONE, PHONE_NUMBER]`| `PHONE_NUMBER`
| `staticDateTime` | `[NONE, REMBERG_DATETIME]`| `REMBERG_DATETIME`
| `staticTasks` | `[NONE, TASKS]`| `TASKS`

</details>


--- 
### Schema and Examples

Prefill can have several rules for a target, which get executed sequentially until on rule can be applied when the required input data is available.

```json (CompanySingleSelect)
// Do not copy comments!
// Prefills company select with company of work order or asset (depending, on how form was created)

"prefill": {
	"selectedCompany": [
		{
			"input": "organizationId",
			"steps": []
		},
		{
			"input": "assetId",
			"steps": [
				"assetIdToAsset",
				"assetToCustomerAccountId"
			]
		}
	]
}

//prefill tenant account
"prefill": {
	"selectedCompany": [
		{
			"input": "currentAccountId",
			"steps": []
		}
	]
}

//prefill companySingleSelect in form with company of remberg_company custom property in work order
"prefill": {
	"selectedCompany": [
		{
			"input": "workOrderId",
			"steps": [
				"workOrderIdToWorkOrder",
				[
					"workOrderToCustomPropertyValue",
					8
				],
				"customPropertyValueToAccountId"
			]
		}
	]
}
```
```json (AssetSingleSelect)
// Do not copy comments!
// Prefills the asset

"prefill": {
	"selectedAsset": [
		{
			"input": "assetId",
			"steps": []
		}
	]
}

//prefill assetSingleSelect in form with asset of remberg_asset custom property in work order
"prefill": {
	"selectedAsset": [
		{
			"input": "workOrderId",
			"steps": [
				"workOrderIdToWorkOrder",
				[
					"workOrderToCustomPropertyValue",
					9
				],
				"customPropertyValueToAssetId"
			]
		}
	]
}

//prefill parent asset of prefilled asset (selected in work order or asset detail page)
"prefill": {
	"selectedAsset": [
		{
			"input": "assetId",
			"steps": [
				"assetIdToAsset",
				"assetToParentAssetId"
			]
		}
	]
}

//prefill remberg_asset_select custom asset property 
"prefill": {
	"selectedAsset": [
		{
			"input": "assetId",
			"steps": [
				"assetIdToAsset",
				["assetToCustomPropertyValue",1],
				"customPropertyValueToAssetId"
			]
		}
	]
}
```
```json (SignatureSection)
// Do not copy comments!
// Prefills signature section with name of the assigned user
// There are four different prefill rules for the location. 1. Work order address 2. Asset location 3. To enter the customers location 

"prefill": {
	"name": [
		{
			"input": "assignedUserId", 
			"steps": [
				"userIdToUser", "userToFullNameString"
			]
		}
	],
	"location": [
		{
			"input": "workOrderId",
			"steps": [
				"workOrderIdToWorkOrder", 
				"workOrderToLocationAddress", 
				"addressToCityString"
			]
		},
		{
			"input": "assetId",
			"steps": [
				"assetIdToAsset",
				"assetToLocationAddress",
				"addressToCityString"
			]
		},
		{
			"input": "organizationId",
			"steps": [
				"accountIdToAccount",
				"accountToBillingAddressAddress",
				"addressToCityString"
			]
		}
	],
	"date": [
		{
			"input": "creationDateTime",
			"steps": ["dateTimeToDate"]
		}
	]
}

//Prefill static location
"prefill": {
	"location": [
		{
			"input": "none",
			"steps": [
				[
					"staticString",
					"Entenhausen"
				]
			]
		}
	]
}	

//Prefill name of current user
"prefill": {
	"name": [
		{
			"input": "currentUserId", 
			"steps": [
				"userToFullNameString"
			]
		}
	]
}	

//Prefill location of the customer which the asset belongs to
"prefill": {
	"location": [
		{
			"input": "assetId",
			"steps": [
				"assetIdToAsset",
				"assetToCustomerAccountId",
				"accountIdToAccount",
				"accountToBillingAddressAddress",
				"addressToCityString"
			]
		}
	]
}	

//Prefill city of billing address of company associated in work order
"prefill": {
	"value": [
		{
			"input": "workOrderId",
			"steps": [
				"workOrderIdToWorkOrder",
				"workOrderToOrganizationAccountId",
				"accountIdToAccount",
				"accountToBillingAddressAddress",
				"addressToCityString"
		]
		}
	]
}

```
```json (AddressInput)
// Do not copy comments!
// Prefills the address with work order address, if empty then the asset location, if empty the company billing address

"prefill": {
	"value": [
		{
			"input": "workOrderId",
			"steps": ["workOrderIdToWorkOrder", "workOrderToLocationAddress"]
		},
		{
			"input": "assetId",
			"steps": ["assetIdToAsset", "assetToLocationAddress"]
		},
		{
			"input": "organizationId",
			"steps": ["accountIdToAccount","accountToBillingAddressAddress"]
		}
	]
}

// Prefills AddressInput with a default address when the form is created

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
}
```
```json (TaskListInput)
// Do not copy comments!
// Prefills task of the work order 

"prefill": {
	"entries": [
		{
			"input": "workOrderId",
			"steps": [ "workOrderIdToWorkOrder", "workOrderToTasks" ]
		}
	]
}

// Prefills predefined task to the taskList

"prefill": {
	"entries": [
		{
			"input": "none",
			"steps": [
				[
					"staticTasks",
					[{
						"done": false,
						"title": "Task 1",
						"comment": "This task was prefilled 1",
						"highPriority": false,
						"necessary": false
					},
					{
						"done": false,
						"title": "Task 2",
						"comment": "This task was prefilled 2",
						"highPriority": true,
						"necessary": true
					},
					{
						"done": true,
						"title": "Task 3",
						"comment": "This task was prefilled 3",
						"highPriority": false,
						"necessary": true
					},
					{
						"done": false,
						"title": "Task 4",
						"comment": "This task was prefilled 4",
						"highPriority": true,
						"necessary": false
					}]
				]
			]
		}
	]
}
```
```json (SingleLineTextInput)
// Do not copy comments!
//Prefill ERP Reference work order field
"prefill": {
	"value": [
		{
			"input": "workOrderId",
			"steps": [
				"workOrderIdToWorkOrder",
				"workOrderToERPReferenceString"
			]
		}
	]
}

//prefill WO subject
"prefill": {
	"value": [
		{
			"input": "workOrderId",
			"steps": [
				"workOrderIdToWorkOrder",
				"workOrderToTitleString"
			]
		}
	]
}

//prefill additional contact information string
"prefill": {
	"value": [
		{
			"input": "workOrderId",
			"steps": [
				"workOrderIdToWorkOrder",
				"workOrderToAdditionalContactInformationString"
			]
		}
	]
}

//prefill work order singleLine custom property; also works for URL property
"prefill": {
	"value": [
		{
			"input": "workOrderId",
			"steps": [
				"workOrderIdToWorkOrder",
				["workOrderToCustomPropertyValue",1],
				"customPropertyValueToString"
			]
		}
	]
}

//prefill string from asset custom property (also works if custom prop is a single select, number, url)
"prefill": {
	"value": [
		{
			"input": "assetId",
			"steps": [
				"assetIdToAsset",
				["assetToCustomPropertyValue",5],
				"customPropertyValueToString"
			]
		}
	]
}

// Prefills the name of the asset as a STRING 
"prefill": {
	"value": [
		{
			"input": "assetId",
			"steps": [
				"assetIdToAsset",
				"assetToAssetTypeNameString"
			]
		}
	]
}

//Prefill subject of case associated with work order
"prefill": {
	"value": [
		{
			"input": "workOrderId",
			"steps": [
				"workOrderIdToWorkOrder",
				"workOrderToCaseSubjectString"
			]
		}
	]
}

//Prefill subject & ID of case associated with work order
"prefill": {
	"value": [
		{
			"input": "workOrderId",
			"steps": [
				"workOrderIdToWorkOrder",
				"workOrderToCaseTicketAndSubjectString"
			]
		}
	]
}

//Prefill city of billing address of company associated in work order
"prefill": {
	"value": [
		{
			"input": "workOrderId",
			"steps": [
				"workOrderIdToWorkOrder",
				"workOrderToOrganizationAccountId",
				"accountIdToAccount",
				"accountToBillingAddressAddress",
				"addressToCityString"
		]
		}
	]
}
```
```json (MultiLineTextInput)
// Do not copy comments!
// Prefills a default multi line text

"prefill": {
	"value": [{
			"input": "none",
			"steps": [[
					"staticString",
					"Default \n Multi \n Line \n Text"
			 ]]
	 }]
}

//prefill asset text area or text input custom property
"prefill": {
	"value": [
		{
			"input": "assetId",
			"steps": [
				"assetIdToAsset",
				["assetToCustomPropertyValue",5],
				"customPropertyValueToString"
			]
		}
	]
}
```
```json (RichTextInput)
// Do not copy comments!
//Prefill work order description

"prefill": {
	"value": [
		{
			"input": "workOrderId",
			"steps": [
				"workOrderIdToWorkOrder",
				"workOrderToDescriptionString"
			]
		}
	]
}

// Prefills a default HTML text
"prefill": {
	"value": [
		{
			"input": "none",
			"steps": [
				[
					"staticString",
					"<b>Default rich text content</b>"
				]
			]
		}
	]
}
```
```json (UserSingleSelect)
// Do not copy comments!
// Prefills the current user

"prefill": {
	"value": [
		{
			"input": "currentUserId",
			"steps": []
		}
	]
}

//prefills the forms' assigned user
"prefill": {
	"value": [
		{
			"input": "assignedUserId",
			"steps": []
		}
	]
}

//prefill the work orders' responsible user
"prefill": {
	"value": [
		{
			"input": "workOrderId",
			"steps": [
				"workOrderIdToWorkOrder",
				"workOrderToResponsibleUserId"
			]
		}
	]
}

//prefill work order remberg_user custom property
"prefill": {
	"value": [
		{
			"input": "workOrderId",
			"steps": [
				"workOrderIdToWorkOrder",
				["workOrderToCustomPropertyValue",7],
				"customPropertyValueToUserId"
			]
		}
	]
}

//prefill manufacturer (tenant) contact person of asset
"prefill": {
	"value": [
		{
			"input": "assetId",
			"steps": [
				"assetIdToAsset",
				"assetToManufacturerPersonUserId"
			]
		}
	]
}

//prefill customer contact person of asset
"prefill": {
	"value": [
		{
			"input": "assetId",
			"steps": [
				"assetIdToAsset",
				"assetToCustomerPersonUserId"
			]
		}
	]
}

//prefill user from remberg_user custom asset property
"prefill": {
	"value": [
		{
			"input": "assetId",
			"steps": [
				"assetIdToAsset",
				["assetToCustomPropertyValue",2],
				"customPropertyValueToUserId"
			]
		}
	]
}
```
```json (BooleanInput)
// Do not copy comments!

//Prefill from work order custom property checkbox
"prefill": {
	"value": [
		{
			"input": "workOrderId",
			"steps": [
				"workOrderIdToWorkOrder",
				["workOrderToCustomPropertyValue",2],
				"customPropertyValueToBoolean"
			]
		}
	]
}

//prefill from asset custom property checkbox
"prefill": {
	"value": [
		{
			"input": "assetId",
			"steps": [
				"assetIdToAsset",
				["assetToCustomPropertyValue",4],
				"customPropertyValueToBoolean"
			]
		}
	]
}

// Prefills `true` 

"prefill": {
	"value": [{
		"input": "none",
		"steps": [["staticBoolean", true]]
	}]
}
```
```json (DateInput)
//Prefill with creation date
"prefill":{
	"value":[
		{
			"input": "creationDateTime",
			"steps": ["dateTimeToDate"]
		}
	]
}

//Prefill work order due date
"prefill": {
	"value": [
		{
			"input": "workOrderId",
			"steps": [
				"workOrderIdToWorkOrder",
				"workOrderToDueDate"
			]
		}
	]
}

//Prefill work order planned start date
"prefill": {
	"value": [
		{
			"input": "workOrderId",
			"steps": [
				"workOrderIdToWorkOrder",
				"workOrderToStartDate"
			]
		}
	]
}

//Prefill work order planned end date
"prefill": {
	"value": [
		{
			"input": "workOrderId",
			"steps": [
				"workOrderIdToWorkOrder",
				"workOrderToEndDate"
			]
		}
	]
}

//prefill from work order date custom property
"prefill": {
	"value": [
		{
			"input": "workOrderId",
			"steps": [
				"workOrderIdToWorkOrder",
				["workOrderToCustomPropertyValue",5],
				"customPropertyValueToDate"
			]
		}
	]
}

//prefill asset date custom property
"prefill": {
	"value": [
		{
			"input": "assetId",
			"steps": [
				"assetIdToAsset",
				["assetToCustomPropertyValue",7],
				"customPropertyValueToDate"
			]
		}
	]
}
```
```json (TimeInput)
// Do not copy comments!
// Prefills a default time 

"prefill": {
	"value": [{
		"input": "none",
		"steps": [[
			"staticTime",
			"22:22"
		]]
	}]
}
```
```json (DateTimeInput)
// Do not copy comments!
//prefill work order datetime custom property
"prefill": {
	"value": [
		{
			"input": "workOrderId",
			"steps": [
				"workOrderIdToWorkOrder",
				["workOrderToCustomPropertyValue",6],
				"customPropertyValueToDateTime"
			]
		}
	]
}

//prefill asset datetime custom property
"prefill": {
	"value": [
		{
			"input": "assetId",
			"steps": [
				"assetIdToAsset",
				["assetToCustomPropertyValue",8],
				"customPropertyValueToDateTime"
			]
		}
	]
}

// Prefills a default date time with of certain time timezone
"prefill": {
	"value": [{
		"input": "none",
		"steps": [[
			"staticDateTime",
			"2022-02-22T22:22:00.000Z_Europe/Berlin"
		]]
	}]
}
```
```json (staticSingleSelect)
// Do not copy comments!
// Prefill work order priority
"value": {
	"options": {
		"000_low": {
			"en": "Low priority",
			"de": "Niedrige prio"
		},
		"010_normal": {
			"en": "Normal priority",
			"de": "Normale prio"
		},
		"020_high": {
			"en": "High priority",
			"de": "Hohe prio"
		},
		"030_critical": {
			"en": "Critical priority",
			"de": "Priorität kritisch"
		}
	}
},
"prefill": {
	"value": [
		{
			"input": "workOrderId",
			"steps": [
				"workOrderIdToWorkOrder",
				"workOrderToPriorityString"
			]
		}
	]
}

//prefill work order type
//adapt value options to space's work order types -> keep option ids starting with 0
"value": {
	"options": {
		"0": {
			"en": "Repair",
			"de": "Reperatur"
		},
		"1": {
			"en": "Commissioning",
			"de": "Inbetriebnahme"
		},
		"2": {
			"en": "Maintenance",
			"de": "Instandhaltung"
		}
	}
},
"prefill": {
	"value": [
		{
			"input": "workOrderId",
			"steps": [
				"workOrderIdToWorkOrder",
				"workOrderToTypeNumberString"
			]
		}
	]
}

//prefill work order status
//adapt value options to space's work order status -> keep option ids starting with 0
"value": {
	"options": {
		"0": {
			"en": "Open",
			"de": "Offen"
		},
		"1": {
			"en": "In Progress",
			"de": "In Bearbeitung"
		},
		"2": {
			"en": "On Hold",
			"de": "Angehalten"
		},
		"3": {
			"en": "Completed",
			"de": "Abgeschlossen"
		},
		"4": {
			"en": "Closed",
			"de": "Geschlossen"
		}
	}
},
"prefill": {
	"value": [
		{
			"input": "workOrderId",
			"steps": [
				"workOrderIdToWorkOrder",
				"workOrderToStatusNumberString"
			]
		}
	]
}

//prefill from work order single select custom property
//Option IDs must be same as dropdown values of work order single select !case sensitivity!
"value": {
	"options": {
		"Option 01010": {
			"en": "Option 01010",
			"de": "Option 01010"
		},
		"Option 202020": {
			"en": "Option 202020",
			"de": "Option 202020"
		},
		"Option 0303030": {
			"en": "Option 0303030",
			"de": "Option 0303030"
		}
	}
},
"prefill": {
	"value": [
		{
			"input": "workOrderId",
			"steps": [
				"workOrderIdToWorkOrder",
				["workOrderToCustomPropertyValue",3],
				"customPropertyValueToString"
			]
		}
	]
}

//prefill from asset single select custom property
//Option IDs must be same as dropdown values of asset single select !case sensitivity!
"value": {
	"options": {
		"Option 01010": {
			"en": "Option 01010",
			"de": "Option 01010"
		},
		"Option 202020": {
			"en": "Option 202020",
			"de": "Option 202020"
		},
		"Option 0303030": {
			"en": "Option 0303030",
			"de": "Option 0303030"
		}
	}
},
"prefill": {
	"value": [
		{
			"input": "assetId",
			"steps": [
				"assetIdToAsset",
				["assetToCustomPropertyValue",9],
				"customPropertyValueToString"
			]
		}
	]
}
```
```json (staticMultiSelect)
//prefill from work order multi select custom property (order of options must be same as in custom prop)
//Option IDs must be same as dropdown values of work order multi select !case sensitivity!
"value": {
	"options": {
		"multi Option 1": {
			"de": "multi Option 1",
			"en": "multi Option 1"
		},
		"multi Option 2": {
			"de": "multi Option 2",
			"en": "multi Option 2"
		},
		"multi Option 3": {
			"de": "multi Option 3",
			"en": "multi Option 3"
		}
	}
},
"prefill": {
	"value": [
		{
			"input": "workOrderId",
			"steps": [
				"workOrderIdToWorkOrder",
				["workOrderToCustomPropertyValue",4],
				"customPropertyValueToArrayOfStrings"
			]
		}
	]
}

//prefill from asset multi select custom property (order of options must be same as in custom prop)
//Option IDs must be same as dropdown values of asset multi select !case sensitivity!
"value": {
	"options": {
		"Option 1": {
			"en": "Option 1",
			"de": "Option 1"
		},
		"Option 62374": {
			"en": "Option 62374",
			"de": "Option 62374"
		},
		"Option 101": {
			"en": "Option 101",
			"de": "Option 101"
		}
	}
},
"prefill": {
	"value": [
		{
			"input": "assetId",
			"steps": [
				"assetIdToAsset",
				["assetToCustomPropertyValue",9],
				"customPropertyValueToArrayOfStrings"
			]
		}
	]
}
```


