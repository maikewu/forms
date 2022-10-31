---
title: DynamicFieldActions
category: 635ce1e7775bc60045570ffb
parentDoc: 635ce486ae5fac003cef279e
---

# Dynamic Field Actions (onChange)

## Concept

Dynamic Field Actions can be represented as a graph where nodes represent source / target fields and sections, 
and edges of the graph represent actions themselves:

![](https://drive.google.com/uc?export=view&id=1z-6-1gzkSJq-JJSqBlE2dgJzi-Ywfpgr)

---

## Data transfer between fields / sections

Data entered in fields / sections can be transferred in between. Each field or section provides and expects a specific data type. 
When the provided data type doesn't match the expected data type, transformation by using `steps` is necessary.

`steps` have an input (expected) data type and an output (provided) data type. 
By chaining steps, the desired data type can be achieved "step by step". 

After transforming the data, the `target` field must be defined by entering a field `id`. Fields with several properties need a `propertyName` additional.

### Example:
The `singleLineTextInput` provides a `STRING` and the `multiLineTextInput` expects a `STRING` ([List of expected / provided data types per field](#fields-and-data-type)). Therefore no transformation is necessary to send the data to the target field.

But if you would like to transfer the name from `userSingleSelect` (provided type: `USER_INFO`) to the `name` property of the `signatureSection` (expected type: `STRING`) then you need to transform the data:

``` JSON (Example: singleLineTextInput)
"onChange": [
    {
      "target": { "id": "exampleSignatureSection", "propertyName": "name" },
      "steps": []
    },
]
```
``` JSON (Example: userSingleSelect)
"onChange": [
    {
      "target": { "id": "exampleSignatureSection", "propertyName": "name" },
      "steps": ["userToFullNameString"]
    },
]
```

---
### More Examples

``` JSON (Address to signatureSection location)
"onChange": [{
    "target": { "id": "exampleSignatureSection", "propertyName": "location" },    
    "steps": ["addressToCityString"]
}]
```
``` JSON (Asset location to addressInput location)
"onChange": [{
    "target": {"id": "exampleAddressInput_1"},
    "steps": [ "assetInfoToAsset","assetToLocationAddress"]
}],
```
``` JSON (Asset name to STRING)
"onChange": [{
    "target": {"id": "exampleMultiLineTextInput_1"},
    "steps": ["assetToAssetTypeNameString"]
}]
```
``` JSON (Company to Asset)
"onChange": [{
    "target": {"id": "exampleAssetSingleSelect_1"},
    "steps": ["??? Need list from Uwe"]
}]
```
``` JSON (Company name to STRING)
"onChange": [{
    "target": { "id": "disabledSingleLineInput_1" },
    "steps": ["accountInfoTioCompanyName"],
}],
```
``` JSON (Company phone number to STRING)
"onChange": [{
    "target": { "id": "exampleSingleLineInput_2" },
    "steps": ["accountInfoToAccount", "accountToPhoneNumberString" ],                
}],
```
``` JSON (Company address to AddressInput)
"onChange": [{
    "target": { "id": "exampleAddressInput_1" },
    "steps": [ "accountInfoToAccount", "accountToBillingAddressAddress"],
}],
```
``` JSON (Company city to signature location)
"onChange": [{
    "target": { "id": "exampleSignatureSection", "propertyName": "location" },
    "steps": [ "accountInfoToAccount", "accountToBillingAddressAddress", "addressToCityString"],
}],
```
``` JSON (Company phone to phoneNumber )
"onChange": [{
    "target": { "id": "examplePhoneNumberInput_1" },
    "steps": [ "accountInfoToAccount", "accountToPhoneNumberString", "phoneNumberStringToPhoneNumberObject" ],
}],
```
``` JSON (User name to signature name)
"onChange": [{
        "target": { "id": "exampleSignatureSection", "propertyName": "name" },
        "steps": [ "userToFullNameString" ],
}],
```
``` JSON (User to phoneNumberInput)
"onChange": [{
    "target": { "id": "examplePhoneNumberInput_1" },
    "steps": ["userInfoToUser", "userToPhoneNumberString", "phoneNumberStringToPhoneNumberObject"],
}],
```

``` JSON

```
``` JSON

```
``` JSON

```
``` JSON

```
``` JSON

```
``` JSON

```

---
## Data type per field / section

### Fields and data type

| Field name               | Provided / expected data type                   |
| :----------------------------- | :---------------------------|
| `singleLineTextInput` | `STRING` |
| `multiLineTextInput` | `STRING` |
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

---

### SignatureSection and data type

| Property name               | Provided / expected data type                   |
| :----------------------------- | :---------------------------|
| `__default__` | `SIGNATURE` |
| `date` | `REMBERG_DATE` |
| `location`| `STRING`|
| `name` | `STRING`|
| `signature` | `STRING`|

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