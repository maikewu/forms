---
title: PrefillRules
category: 62ebf4654ae80e09e468624b
parentDoc: 62ec01bd561bab0aa775efe4
---
## Concept

Prefill allows you to prepopulate fields with values when creating a new form instance.
To do this, prefill rules must be defined in the form code for the respective fields. 
The prefill rule schema contains targets, inputs and steps. 

--- 
`target` locates the property to which data is to be written
<details> <summary>All available <code>target</code> values </summary>

| Section                  |      `target`      |
| :------------------------- | :--------------|
| SignatureSection| `name`, `location`, `date`
   
| Field                  |      `target`      |
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
`input` can be a seperate source that already contains informations, e.g. a work order, or a own defined input value,
that should be prepopulate to the form

<details>
<summary>All available <code>input</code> sources, their values and data types</summary>

`none` has to be used, when you would like to prepopulate a own defined value to the property.

| Source               | `input` (provided) value | Data type |
| :----------------------------- | :----- | :-----|
| Asset view | `assetId`| `ASSET_ID` (equals `STRING`)
| Selected organization |`organizationId` | `ACCOUNT_ID` (equals `STRING`)
| Form creation date time |`creationDateTime` | `REMBERG_DATE`
| Current user | `currentUser` | `USER_INFO`
| Current user | `currentUserId` | `USER_ID` (equals `STRING`)
| Current account | `currentAccount` | `ACCOUNT`
| Current account  |`currentAccountId` | `ACCOUNT_ID` (equals `STRING`)
| WorkOrder view |`assignedUserId` | `USER_ID` (equals `STRING`)
| WorkOrder view |`workOrderId` | `WORK_ORDER_ID` (equals `STRING`)
| - | `none`| `NONE`

</details>

---
`steps` can be used to transform the data if the `input` data type does not match the expected data type of the `target`.

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
| `accountToBillingAddressAddress` | `ACCOUNT`| `ADDRESS`
| `addressToCityString` | `ADDRESS`| `STRING`
| `workOrderIdToWorkOrder` | `WORK_ORDER_ID`| `WORK_ORDER`
| `workOrderToLocationAddress` | `WORK_ORDER`| `ADDRESS`
| `workOrderToTasks` | `WORK_ORDER`| `TASKS`
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
## Asset View
If you create a new forms instance from an asset (Asset View), the following data is provided:

| Data | Condition | Description |
| :------------------------- | :--------------| :---- |
| `assetId`  |  |  The ID of the asset form which the new form is created
| `organizationId` | | The ID of the company to which the asset belongs
| `creationDateTime`  |  | The creation date time of ??? 
| `currentUser`  |  |  	Information about the current user, including the name, ID, etc.
| `currentUserId`  |  |  The ID of the user who is logged in and creates the form instance
| `currentAccount`  |  |  Information about the current space, including the name, address, ID, etc.
| `currentAccountId`  |  |  	The ID of the current space
| `assidnedUserId`  | Optional |  The ID of the user who is assigned to the asset

---
 ## Work Order
If you create a new forms instance from a work order, the following data is provided:


| Data | Condition | Description |
| :------------------------- | :--------------| :---- |
| `relatedWorkOrderId`  |  |  The ID of the work order from which the form is created
| `organizationId`  | If WO has connected company | The ID of the company (contact) which is connected to the work order
| `assetId`  | If WO has assets |  The ID of the asset which is part of the work order
| `currentUser`  |  | Information about the current user, including the name, ID, etc.
| `currentUserId`  |  | The ID of the user who is logged in and creates the form instance
| `currentAccount`  |  | Information about the current space, including the name, address, ID, etc.
| `currentAccountId`  |  | The ID of the current space 
| `assignedUserId`  | Optional | The ID of the user who is assigned to the work order

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
| `accountToBillingAddressAddress` | `ACCOUNT`| `ADDRESS`
| `addressToCityString` | `ADDRESS`| `STRING`
| `workOrderIdToWorkOrder` | `WORK_ORDER_ID`| `WORK_ORDER`
| `workOrderToLocationAddress` | `WORK_ORDER`| `ADDRESS`
| `workOrderToTasks` | `WORK_ORDER`| `TASKS`
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
### Schema & Examples

Prefill can have severeal rules for a target, which get executed sequenctially until on rule can be applied when the required input data is available.
<details>
<summary>Prefill examples of certain fields</summary>

``` JSON (SignatureSection)
"prefill": {
    "name": [
        {
            "input": "currentUser",
            "steps": [
                "userToFullNameString",
            ],
        },
    ],
    "location": [
        {
            "input": "assetId",
            "steps": [
                "assetIdToAsset",
                "assetToLocationAddress",
                "addressToCityString",
            ],
        },
        {
            "input": "assetId",
            "steps": [
                "assetIdToAsset",
                "assetToCustomerAccountId",
                "accountIdToAccount",
                "accountToBillingAddressAddress",
                "addressToCityString",
            ],
        },
        {
            "input": "organizationId",
            "steps": [
                "accountIdToAccount",
                "accountToBillingAddressAddress",
                "addressToCityString",
            ],
        },
        {
            "input": "none",
            "steps": [
                [
                    "staticString",
                    "Default Location",
                ],
            ],
        },
    ],
    "date": [
        {
            "input": "creationDateTime",
            "steps": ["dateTimeToDate"],
        },
    ],
},
```
``` JSON (AddressInput)
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
                        "company": "Default Company",
                    },
                ],
            ],
        },
    ],
},
```
``` JSON (AddressInput2)
"prefill": {
    "value": [
        {
            "input": "workOrderId",
            "steps": [
                "workOrderIdToWorkOrder",
                "workOrderToLocationAddress",
            ],
        },
    ],
},
```
``` JSON (TaskListInput)
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
                        "necessary": false,
                    },
                    {
                        "done": false,
                        "title": "Task 2",
                        "comment": "This task was prefilled 2",
                        "highPriority": true,
                        "necessary": true,
                    },
                    {
                        "done": true,
                        "title": "Task 3",
                        "comment": "This task was prefilled 3",
                        "highPriority": false,
                        "necessary": true,
                    },
                    {
                        "done": false,
                        "title": "Task 4",
                        "comment": "This task was prefilled 4",
                        "highPriority": true,
                        "necessary": false,
                    }],
                ],
            ],
        },
    ],
},
```
``` JSON (TaskListInput2)
"prefill": {
    "entries": [
        {
            "input": "workOrderId",
            "steps": [ "workOrderIdToWorkOrder", "workOrderToTasks" ],
        },
    ],
},
```
``` JSON (SingleLineTextInput)
"prefill": {
    "value": [
        {
            "input": "assetId",
            "steps": [
                "assetIdToAsset",
                "assetToAssetTypeNameString",
            ],
        },
    ],
},
```
``` JSON (MultiLineTextInput)
"prefill": {
    "value": [{
            "input": "none",
            "steps": [[
                    "staticString",
                    "Default \n Multi \n Line \n Text",
             ]],
     }],
},
```
``` JSON (RichTextInput)
"prefill": {
    "value": [
        {
            "input": "none",
            "steps": [
                [
                    "staticString",
                    "<h1>Default rich text content</h1>",
                ],
            ],
        },
    ],
},
```
``` JSON (UserSingleSelect)
"prefill": {
    "value": [{
            "input": "currentUserId",
            "steps": [],
    }],
},
```
``` JSON (BooleanInput)
"prefill": {
    "value": [{
        "input": "none",
        "steps": [["staticBoolean", true]],
    }],
},
```
``` JSON (TimeInput)
"prefill": {
    "value": [{
        "input": "none",
        "steps": [[
            "staticTime",
            "22:22",
        ]],
    }],
},
```
``` JSON (DateTimeInput)
"prefill": {
    "value": [{
        "input": "none",
        "steps": [[
            "staticDateTime",
            "2022-02-22T22:22:00.000Z_Europe/Berlin",
        ]],
    }],
},
```
</details>


Schema:
``` JSON (PreFill schema general)
"prefill": {
    "target": [
        {
            "input": "rule1_value1",
            "steps": [
                "step1-1",
            ],
        },
        {
            "input": "rule2_value2",
            "steps": [
              "step2-1",
              "step2-2",
            ],
        },
    ],
},
```