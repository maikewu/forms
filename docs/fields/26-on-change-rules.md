---
title: DynamicFieldActions
category: 62ebf4654ae80e09e468624b
parentDoc: 62ec01bd561bab0aa775efe4
---

# Dynamic Field Actions (onChange)

## Concept

Dynamic Field Actions can be represented as a graph where nodes represent source / target fields and sections, 
and edges of the graph represent actions themselves:

![](https://drive.google.com/uc?export=view&id=1z-6-1gzkSJq-JJSqBlE2dgJzi-Ywfpgr)

---

## Data transfer between fields / sections

Data entered in fields / sections can be transferred in between. Each field or section povides and expects a specific data type. 
When the provided data type doesn't match the expected data type, transformation by using `steps` is necessary.

`steps` have an input (expected) data type and an output (provided) data type. 
By chaining steps, the desired data type can be achieved "step by step". 

After transforming the data, the `target` field must be defined by entering a field `id`. Fields with several properties need a `propertyName` additional.

### Example:
The `singleLineTextInput` provides a `STRING` and the `mulitLineTextInput` expects a `STRING`. Therefore no transformation is necessary to send the data to the target field.

But if you would like to transfer the name from `userSingleSelect` (provided type: `USER_INFO`) to the `name` property of the `signatureSection` (expected type: `STRING`) then you need to transform the data:

``` JSON (Example: userSingleSelect)
"onChange": [
    {
      "steps": ["userToFullNameString"],
      "target": { "id": "exampleSignatureSection", "propertyName": "name" },
    },
]
```
``` JSON (Example: singleLineTextInput)
"onChange": [
    {
      "steps": [],
      "target": { "id": "exampleMultiLineTextInput_1"},
    },
]
```
---
### More Examples

> 🚧 In progess
> 
> More real code examples will be added

## Data type per field / section

<details>
<summary>Fields and data type</summary>

| Field name               | Provided / expected data type                   |
| :----------------------------- | :---------------------------|
| `singleLineTextInput` | `STRING` |
| `mutliLineTextInput` | `STRING` |
| `booleanInput`| `BOOLEAN`|
| `assetSingleSelect` | `ASSET_INFO`|
| `addressInput` | `ADDRESS`|
| `richTextInput` | `HTML_STRING`|
| `dateInput` | `REMBERG_DATE`|
| `timeInput` | `REMBERG_TIME`|
| `dateTimeInput` | `REMBERG_DATETIME`|
| `staticSingleSelect` | `STRING`|
| `staticMultiSelect` | `ARRAY_OF_STRINGS`|
| `userSingleSelect` | `USER_INFO`|
| `phoneNumberInput` | `PHONE_NUMBER`|
| `companySingleSelect` | `ACCOUNT_INFO`|
</details>

<details>
<summary>SignatureSection and data type</summary>

| Property name               | Provided / expected data type                   |
| :----------------------------- | :---------------------------|
| `__default__` | `SIGNATURE` |
| `date` | `REMBERG_DATE` |
| `location`| `STRING`|
| `name` | `STRING`|
| `signature` | `STRING`|
</details>

---

## List of all dynamic action steps

You can find a list below, that contains all implemented `steps`, which can be used to transform data.

| `dynamic action steps`               | input data type  | output data type |
| :----------------------------- | :----- | :-----|
| `accountIdToAccount` | `ACCOUNT_ID`| `ACCOUNT` |
| `accountToBillingAddressAddress` | `ACCOUNT`| `ADDRESS` |
| `accountInfoToCompanyName` | `ACCOUNT_INFO`| `STRING` |
| `accountInfoToCustomerNumber` | `ACCOUNT_INFO` | `STRING`|
| `accountToAccountInfo` | `ACCOUNT`| `ACCOUNT_INFO` |
| `accountInfoToAccount` | `ACCOUNT_INFO`| `ACCOUNT` |
| `accountToPhoneNumberString` | `ACCOUNT`| `STRING` |
| `addressToCityString` | `ADDRESS`| `STRING` |
| `assetIdToAsset` | `ASSET_ID`| `ASSET` |
| `assetInfoToAsset` | `ASSET_INFO`| `ASSET` |
| `assetToAssetTypeNameString` | `ASSET_INFO`| `STRING` |
| `assetToCustomerAccountId` | `ASSET`| `STRING` |
| `assetToLocationAddress` | `ASSET`| `ADDRESS` |
| `assetToCustomPropertyValue` | `[ ASSET, NUMBER ]` | `ANY` |
| `assetInfoToCustomerId` | `ASSET_INFO` | `ACCOUNT_ID` |
| `phoneNumberStringToPhoneNumberObject` | `STRING` | `PHONE_NUMBER` |
| `userToFullNameString` | `USER_INFO` | `STRING` |
| `userInfoToUser` | `USER_INFO` | `USER` |
| `userToPhoneNumberString` | `USER`| `STRING` |
| `logValue` | `ANY`| `ANY` |
