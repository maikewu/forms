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

                    removeUiTextColorFromSections(jsonData);
                    updateUiTextSizeFromSections(jsonData);

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

function removeUiTextColorFromSections(jsonData: any): void {
    for (const section of jsonData.sections ?? []) {
        if (section.type !== 'fieldSection') {
            continue;
        }

        for (const field of section.fields ?? []) {
            if (!field.config) {
                continue;
            }

            removeUiTextColorFromField(field);

            if (field.type === 'fieldRepeater' && field.config.fields) {
                for (const repeaterField of field.config.fields) {
                    if (!repeaterField.config) {
                        continue;
                    }

                    removeUiTextColorFromField(repeaterField);
                }
            }
        }
    }
}

function removeUiTextColorFromField(field: any) {
    if (field.config.uiTextColor) {
        delete field.config.uiTextColor;
    }
    if (field.config.label?.uiTextColor) {
        delete field.config.label.uiTextColor;
    }
}

function updateUiTextSizeFromSections(jsonData: any): void {
    for (const section of jsonData.sections ?? []) {
        if (section.type !== 'fieldSection') {
            continue;
        }

        for (const field of section.fields ?? []) {
            if (!field.config) {
                continue;
            }

            updateUiTextSizeForHeadlineDisplayField(field);

            if (field.type === 'fieldRepeater' && field.config.fields) {
                for (const repeaterField of field.config.fields) {
                    if (!repeaterField.config) {
                        continue;
                    }

                    updateUiTextSizeForHeadlineDisplayField(repeaterField);
                }
            }
        }
    }
}

function updateUiTextSizeForHeadlineDisplayField(field: any) {
    if (field.type === 'headlineDisplay' && field.config.uiTextSize) {
        field.config.type = field.config.uiTextSize;
        delete field.config.uiTextSize;
        delete field.config.pdfTextSize;
    }
}

updateJsonFiles(jsonRepositoryPath).catch();
