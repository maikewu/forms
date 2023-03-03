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
<details> <summary>All available <code>target</code> values </summary>

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
| [customProperty](#Custom-Properties) |  | One of the specific custom asset properties
| `assignedUserId`  | Optional |  The ID of the user, who is assigned to the new form instance

---
 ## Work Order View
If you create a new forms instance from a work order, the following data is provided:


| Data | Condition | Description |
| :------------------------- | :--------------| :---- |
| `WorkOrderId`  |  |  The ID of the work order from which the form is created
| `organizationId`  | If WO has connected company | The ID of the company (contact) which is connected to the work order
| `assetId`  | If WO has assets |  The ID of the asset which is part of the work order
| [customProperty](#Custom-Properties) |  | One of the specific custom work order properties
| `currentUser`  |  | Information about the current user, including the name, ID, etc.
| `currentUserId`  |  | The ID of the user who is logged in and creates the form instance
| `currentAccount`  |  | Information about the current space, including the name, address, ID, etc.
| `currentAccountId`  |  | The ID of the current space 
| `assignedUserId`  | Optional |  The ID of the user, who is assigned to the new form instance

---
## Custom Properties

Custom Properties of the respective space can be extracted. These include Custom Work Order Properties and Custom Asset Properties. To extract a custom Property, one must first know their respective ID.

The following examples illustrate the extraction of a custom property, the custom property ID is always placed in between the [] brackets after the step `workOrderToCustomPropertyValue` or `assetToCustomPropertyValue`:


```json (customPropertyValueToAccountId)
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
```json (customPropertyValueToAssetId)
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
<details>
<summary>Prefill examples of certain fields</summary>

```json (SignatureSection)
// Do not copy comments!
// Prefills signature section with name of the current user
// There are four different prefill rules for the location. 1. To enter the asset location 2. To enter the location of the costumer which the asset belongs to 3. To enter the customers location 4. To enter a default location

"prefill": {
    "name": [
        {
            "input": "currentUser", 
            "steps": [
                "userToFullNameString"
            ]
        }
    ]
    "location": [
        {
            "input": "assetId",
            "steps": [
                "assetIdToAsset",
                "assetToLocationAddress",
                "addressToCityString"
            ]
        }
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
        {
            "input": "organizationId",
            "steps": [
                "accountIdToAccount",
                "accountToBillingAddressAddress",
                "addressToCityString"
            ]
        }
        {
            "input": "none",
            "steps": [
                [
                    "staticString",
                    "Default Location"
                ]
            ]
        }
    ]
    "date": [
        {
            "input": "creationDateTime",
            "steps": ["dateTimeToDate"]
        }
    ]
}
```
```json (AddressInput)
// Do not copy comments!
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
```json (AddressInput2)
// Do not copy comments!
// Prefills the address of the work order of the connected company 

"prefill": {
    "value": [
        {
            "input": "workOrderId",
            "steps": [
                "workOrderIdToWorkOrder",
                "workOrderToLocationAddress"
            ]
        }
    ]
}
```
```json (TaskListInput)
// Do not copy comments!
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
```json (TaskListInput2)
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
```
```json (SingleLineTextInput)
// Do not copy comments!
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
```
```json (RichTextInput)
// Do not copy comments!
// Prefills a default HTML text

"prefill": {
    "value": [
        {
            "input": "none",
            "steps": [
                [
                    "staticString",
                    "Default rich text content"
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
    "value": [{
            "input": "currentUserId",
            "steps": []
    }]
}
```
```json (BooleanInput)
// Do not copy comments!
// Prefills `true` 

"prefill": {
    "value": [{
        "input": "none",
        "steps": [["staticBoolean", true]]
    }]
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
</details>


