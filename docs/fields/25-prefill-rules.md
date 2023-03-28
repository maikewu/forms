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
## Target Values and Data Types

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
## Input Sources

`input` can be a separate source that already contains information, e.g. a work order, or a own defined input value,
that should be prepopulate to the form

All available <code>input</code> sources, their values and data types

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
| [Custom Property](#custom-property-view)  |`customPropertyID` | `UNKNOWN`
| [WorkOrder view](#work-order-view) |`workOrderId` | `WORK_ORDER_ID` (equals `STRING`)
| - | `none`| `NONE`


---
## Steps 
`steps` can be used to transform the data if the `input` data type does not match the expected data type of the `target`. There are [General Steps](#general-steps), [Asset Steps](#asset-steps), [Work Order Steps](#work-order-steps) and [Custom Property Steps](#custom-property-steps).

`steps` have an input (expected) data type and an output (provided) data type. 
By chaining steps, the desired data type can be achieved "step by step". 

**Note:** `OrganizationID` can use the same steps which convert the `accountID` datatype.

## General Steps

General steps can be used to transform data types to fit desired field data type.

| `steps`               | input data type  | output data type | description |
| :----------------------------- | :----- | :-----| :-----------------------------|
| `dateTimeToDate` | `REMBERG_DATETIME`| `REMBERG_DATE` | Extracts the date
| `userIdToUser` | `USER_ID`| `USER_INFO` | Converts the `USER_ID` to `USER_INFO`
| `accountIdToAccount` | `ACCOUNT_ID`| `ACCOUNT` | Converts the `ACCOUNT_ID` to `ACCOUNT`
| `userToFullNameString` | `USER_INFO` | `STRING` | Converts the `USER_INFO` to the full name as a `STRING`
| `accountToBillingAddressAddress` | `ACCOUNT`| `ADDRESS` | Converts the `ACCOUNT` to the associated billing address as `ADDRESS`
| `addressToCityString` | `ADDRESS`| `STRING` | Extract the city name from an `ADDRESS` as a `STRING`
| `staticString` | `[NONE, STRING]`| `STRING` | Provides a static `STRING`
| `staticStringArray` | `[NONE, ARRAY_OF_STRINGS]`| `ARRAY_OF_STRINGS` | Provides a static `ARRAY_OF_STRINGS`
| `staticBoolean` | `[NONE, BOOLEAN]`| `BOOLEAN` | Provides a static `BOOLEAN`
| `staticAddress` | `[NONE, ADDRESS]`| `ADDRESS` | Provides a static `ADDRESS`
| `staticDate` | `[NONE, REMBERG_DATE]`| `REMBERG_DATE` | Provides a static `ADDRESS`
| `staticTime` | `[NONE, REMBERG_TIME]`| `REMBERG_TIME` | Provides a static `REMBERG_TIME`
| `staticPhoneNumber` | `[NONE, PHONE_NUMBER]`| `PHONE_NUMBER` | Provides a static `PHONE_NUMBER`
| `staticDateTime` | `[NONE, REMBERG_DATETIME]`| `REMBERG_DATETIME` | Provides a static `REMBERG_DATETIME`
| `staticTasks` | `[NONE, TASKS]`| `TASKS` | Provides a static list of `TASKS`

## Asset Steps

When a new form instance is created from an asset detail page (Asset View), the `assetId` can be used to create prefilling steps that extract attributes of the related asset. Therefore, the first step must be `assetIdToAsset` followed by these available steps:

| `steps`               | input data type  | output data type | description |
| :----------------------------- | :----- | :-----| :-----------------------------|
| `assetIdToAsset` | `ASSET_ID`| `ASSET` | Converts the `ASSET_ID` to a `ASSET`
| `assetToLocationAddress` | `ASSET`| `ADDRESS` | Extracts the defined asset location
| `assetToCustomerAccountId` | `ASSET`| `ACCOUNT_ID` | Extracts the `ACCOUNT_ID` of the company associated with the asset
| `assetToAssetTypeNameString` | `ASSET`| `STRING` | Extracts the name of the asset type as a `STRING`
| `assetToCustomPropertyValue` | `[ASSET, NUMBER]`| `UNKNOWN` | Takes the `ASSET` and the number of the respective custom asset  property as `NUMBER` as inputs and extracts the respective custom property value 

## Work Order Steps

When a new form instance is created from an work order detail page (Work Order View), the `workOrderId` can be used to create prefilling steps that extract attributes of the related work order. Therefore, the first step must be `workOrderIdToWorkOrder` followed by these available steps:

| `steps`               | input data type  | output data type | description |
| :----------------------------- | :----- | :-----| :-----------------------------|
| `workOrderIdToWorkOrder` | `WORK_ORDER_ID`| `WORK_ORDER`| Converts the `WORK_ORDER_ID` to a `WORK_ORDER`
| `workOrderToLocationAddress` | `WORK_ORDER`| `ADDRESS` | Extracts the defined asset location of the work order
| `workOrderToTasks` | `WORK_ORDER`| `TASKS` | Extracts the tasks added to the work order
| `workOrderToTitleString` | `WORK_ORDER`| `STRING` | Extracts the title of the work order
| `workOrderToDescriptionString` | `WORK_ORDER`| `STRING` | Extracts the description of the work order
| `workOrderToDueDate` | `WORK_ORDER`| `REMBERG_DATE` | Extracts the due date of the work order
| `workOrderToStartDate` | `WORK_ORDER`| `REMBERG_DATE` | Extracts the start date of the work order
| `workOrderToEndDate` | `WORK_ORDER`| `REMBERG_DATE` | Extracts the start date of the work order
| `workOrderToERPReferenceString` | `WORK_ORDER`| `STRING` | Extracts the ERP reference of the work order as a `STRING`
| `workOrderToResponsibleUserId` | `WORK_ORDER`| `USER_ID` | Extracts the userId of the user responsible for the work order
| `workOrderToStatusNumberString` | `WORK_ORDER`| `STRING` | Extracts the status of the work order as a number: 0: Open, 1: In Progress, 2: On Hold, 3: Completed, 4: Closed
| `workOrderToTypeNumberString` | `WORK_ORDER`| `STRING` | Extracts the type of the work order as a number: 0: Repair, 1: Commissioning, 2: Maintenance
| `workOrderToPriorityString` | `WORK_ORDER`| `STRING` | Extracts the priority of the work order as a `STRING`: 000_low: Low priority, 010_normal: Normal priority, 020_high: High priority, 030_critical: Critical priority
| `workOrderToPerformByUserId` | `WORK_ORDER`| `USER_ID` | Extracts the `USER_ID` of the user performing the work order
| `workOrderToAdditionalContactInformationString` | `WORK_ORDER`| `STRING` | Extracts the additional contact information associated with the work order as a `STRING`
| `workOrderToCaseSubjectString` | `WORK_ORDER`| `STRING` | Extracts the prefilled subject title from the service case
| `workOrderToCaseTicketAndSubjectString` | `WORK_ORDER`| `STRING` | Extracts the prefilled subject and title from service case
| `workOrderToOrganizationAccountId` | `WORK_ORDER`| `ACCOUNT_ID` | Extracts the organization/company associated with the work order as an `ACCOUNT_ID`
| `workOrderToCustomPropertyValue` | `[WORK_ORDER, NUMBER]`| `UNKNOWN` | Takes the `WORK_ORDER` and the number of the respective custom work order property as `NUMBER` as inputs and extracts the respective custom property value 
 
## Custom Property Steps 

Custom Properties of the respective space can be extracted. These include Custom Work Order Properties and Custom Asset Properties. To extract a custom Property, one must first know their respective ID.

| `steps`               | input data type  | output data type | description |
| :----------------------------- | :----- | :-----| :-----------------------------|
| `workOrderToCustomPropertyValue` | `[ASSET, NUMBER]`| `UNKNOWN` | Takes the `WORK_ORDER` and the number of the respective custom work order property as `NUMBER` as inputs and extracts the respective custom property value 
| `assetToCustomPropertyValue` | `[ASSET, NUMBER]`| `UNKNOWN` | Takes the `ASSET` and the number of the respective custom asset  property as `NUMBER` as inputs and extracts the respective custom property value 
| `customPropertyValueToString` | `UNKNOWN`| `STRING` | Converts the customPropertyValue (which can have many types) to a `STRING`
| `customPropertyValueToArrayOfStrings` | `UNKNOWN`| `ARRAY_OF_STRINGS` | Converts the customPropertyValue (which can have many types) to an `ARRAY_OF_STRINGS`
| `customPropertyValueToNumberString` | `UNKNOWN`| `STRING` | Converts the customPropertyValue (which can have many types) to a number as a `STRING`
| `customPropertyValueToNumber` | `UNKNOWN`| `NUMBER` | Converts the customPropertyValue (which can have many types) to a `NUMBER`
| `customPropertyValueToBoolean` | `UNKNOWN`| `BOOLEAN` | Converts the customPropertyValue (which can have many types) to `BOOLEAN`
| `customPropertyValueToAssetId` | `UNKNOWN`| `ASSET_ID` | Converts the customPropertyValue (which can have many types) to an `ASSET_ID`
| `customPropertyValueToAccountId` | `UNKNOWN`| `ACCOUNT_ID` | Converts the customPropertyValue (which can have many types) to an `ACCOUNT_ID`
| `customPropertyValueToUserId` | `UNKNOWN`| `USER_ID` | Converts the customPropertyValue (which can have many types) to an `USER_ID`
| `customPropertyValueToDate` | `UNKNOWN`| `REMBERG_DATE` | Converts the customPropertyValue (which can have many types) to a `REMBERG_DATE`
| `customPropertyValueToDateTime` | `UNKNOWN`| `REMBERG_DATETIME` | Converts the customPropertyValue (which can have many types) to a `REMBERG_DATETIME`

The following examples illustrate the extraction of a custom property, the custom property ID is always placed in between the [] brackets after the step `workOrderToCustomPropertyValue` or `assetToCustomPropertyValue`:

**Note**: Some custom property derived values first need be mapped to a real readable value, especially values from a custom property multi select. The following examples will illustrate the mapping process:


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


