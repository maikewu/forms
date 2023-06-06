import fs from 'fs-extra';
import path from 'path';

const jsonRepositoryPath = './forms2';

async function updateJsonFiles(directory: string): Promise<void> {
  try {
    const items = await fs.readdir(directory);

    for (const item of items) {
      const itemPath = path.join(directory, item);
      const stat = await fs.stat(itemPath);

      if (stat.isDirectory()) {
        try {
          await updateJsonFiles(itemPath);
        } catch (e) {
          console.error(`An error occurred when updating file ${itemPath}!`, e);
        }
      } else if (path.extname(item) === '.json') {
        try {
          if (fs.readFileSync(itemPath).length === 0) {
            console.warn(`Skipped ${itemPath} because it's empty!`);
            continue;
          }

          const jsonData = await fs.readJson(itemPath);

          updateConfig(jsonData);

          await fs.writeJson(itemPath, jsonData, { spaces: 2 });
          console.log(`Updated ${itemPath}`);
        } catch (e) {
          console.error(`An error occurred when updating file ${itemPath}!`, e);
        }
      }
    }
  } catch (err) {
    console.error('Error updating JSON files:', err);
  }
}

function updateConfig(jsonData: any): void {
  for (const section of jsonData.sections ?? []) {
    // delete pdfHide and pdfHideIfValueIsEmpty props in EmailSectionConfig
    if (section.type === 'emailSection') {
      if (Object.prototype.hasOwnProperty.call(section.config, 'pdfHide')) {
        delete section.config.pdfHide;
      }

      if (Object.prototype.hasOwnProperty.call(section.config, 'pdfHideIfValueIsEmpty')) {
        delete section.config.pdfHideIfValueIsEmpty;
      }
    }

    if (section.type === 'fieldSection') {
      // replace enable flag with disabled flag for PartListInputFieldConfig
      for (const field of section.fields) {
        if (field.type === 'partListInput') {
          if (field.config.fields) {
            const partListInputFields = field.config.fields;

            for (const partListInputFieldKey of Object.keys(partListInputFields)) {
              if (partListInputFieldKey === 'descriptionMultiLineTextInput' ||
                partListInputFieldKey === 'deliverToStaticSingleSelect' ||
                partListInputFieldKey === 'invoiceToStaticSingleSelect' ||
                partListInputFieldKey === 'warrantyBooleanInput') {
                const partListInputField = partListInputFields[partListInputFieldKey];

                if (!partListInputField) {
                  partListInputFields[partListInputFieldKey] = {
                    disabled: true,
                  };
                }

                if (partListInputField && !Object.prototype.hasOwnProperty.call(partListInputField, 'enable')) {
                  partListInputField.disabled = true;
                }

                if (partListInputField && Object.prototype.hasOwnProperty.call(partListInputField, 'enable')) {
                  partListInputField.disabled = !partListInputField.enable;
                  delete partListInputField.enable;
                }
              }
            }
          } else {
            field.config.fields = {
              descriptionMultiLineTextInput: {
                disabled: true,
              },
              deliverToStaticSingleSelect: {
                disabled: true,
              },
              invoiceToStaticSingleSelect: {
                disabled: true,
              },
              warrantyBooleanInput: {
                disabled: true,
              },
            };
          }
        }

        // rename helptextBefore and helptextAfter props in RepeaterFieldConfig
        if (field.type === 'fieldRepeater') {
          const fieldConfig = field.config;

          if (Object.prototype.hasOwnProperty.call(fieldConfig, 'helptextBefore')) {
            fieldConfig.helpTextBefore = fieldConfig.helptextBefore;
            delete fieldConfig.helptextBefore;
          }

          if (Object.prototype.hasOwnProperty.call(fieldConfig, 'helptextAfter')) {
            fieldConfig.helpTextAfter = fieldConfig.helptextAfter;
            delete fieldConfig.helptextAfter;
          }
        }
      }
    }
  }
}

updateJsonFiles(jsonRepositoryPath).catch();
