# MultiLineTextInput

The MultiLineTextInput field allows entering larger amounts of unformatted text. It respects line breaks and can be configured to limit the possible content length.

## Configuration

=== "Test"
  Hello

=== "ZZZ"
  ZZZ?

=== "Type"
  ``` typescript
  interface MultiLineTextInputFieldConfig {
      required?: boolean;
      pdfHideAll?: boolean;
      disabled?: boolean;
      placeHolderText?: MultiLanguageText;
      pdfHideAllIfValueIsEmpty?: boolean;
      uiHideInRepeaterCardDisplay?: boolean;
      label: {
          text: MultiLanguageText;
          uiHide?: boolean;
          pdfHide?: boolean;
          pdfTextSize?: number;
          pdfTextColor?: string;
      };
      value?: {
          uiMinRows?: number;
          uiMaxRows?: number;
          pdfHide?: boolean;
          pdfTextSize?: number;
          pdfTextColor?: string;
          pdfStartInNewLine?: boolean;
          validators?: MultiLineTextInputValidatorConfig;
      };
      prefill?: PrefillConfig<MultiLineTextInputPrefillTargetsEnum>;
  }
  ```

=== "Example"

  ``` json
  {

  }
  ```

| Property | Description               |
| :------- | :-------------------------|
| id       | String id to identify the field. This id needs to be unique across the whole form! |
| id       | String id to identify the field. |
| disabled | String id to identify the field. |
| id       | String id to identify the field. |
| id       | String id to identify the field. |
| id       | String id to identify the field. |
| id       | String id to identify the field. |
| id       | String id to identify the field. |


### Grouping other content

When a content tab contains more than one code block, it is rendered with
horizontal spacing. Vertical spacing is never added, but can be achieved
by nesting tabs in other blocks:

``` title="Content tabs"
=== "Unordered list"

    * Sed sagittis eleifend rutrum
    * Donec vitae suscipit est
    * Nulla tempor lobortis orci

=== "Ordered list"

    1. Sed sagittis eleifend rutrum
    2. Donec vitae suscipit est
    3. Nulla tempor lobortis orci
```

=== "Unordered list"

    * Sed sagittis eleifend rutrum
    * Donec vitae suscipit est
    * Nulla tempor lobortis orci

=== "Ordered list"

    1. Sed sagittis eleifend rutrum
    2. Donec vitae suscipit est
    3. Nulla tempor lobortis orci
