import openpyxl
import json 

# Load the Excel workbook
workbook = openpyxl.load_workbook('/Users/beateplendl/Downloads/2023-09-06_Forms_Python-Input.xlsx')
sheet = workbook.active

# Initialize a list to store the data
data_list = []

# Iterate through rows starting from the second row (assuming header in the first row)
for row in sheet.iter_rows(min_row=2, values_only=True):
    var1 = row[0]
    var2 = row[3]
    if row[5] == 'Header':
        column1_value = {
            "id": f"{var1}_header",
            "type": "htmlDisplay",
            "config": {
                "text": {
                    "en": "",
                    "de": f"<b style='font-size:10pt'>{var2}</b>",
                    "tr": "",
                    "fr": "",
                    "es": "",
                    "it": ""
                },
                "uiHide": False,
                "pdfHide": False,
                "pdfWidth": 0.6
            }
        }
        column2_value = {
            "id": f"{var1}_header-sichtpruefung",
            "type": "htmlDisplay",
            "config": {
                "text": {
                    "en": "",
                    "de": "<b style='font-size:10pt'>Sichtprüfung</b>",
                    "tr": "",
                    "fr": "",
                    "es": "",
                    "it": ""
                },
                "uiHide": True,
                "pdfHide": False,
                "pdfWidth": 0.4
            }
        }
    else:
        column1_value = {
            "id": f"{var1}_name",
            "type": "htmlDisplay",
            "config": {
                "text": {
                    "en": "",
                    "de": f"{var2}",
                    "tr": "",
                    "fr": "",
                    "es": "",
                    "it": ""
                },
                "uiHide": False,
                "pdfHide": False,
                "pdfWidth": 0.6
            }
        }
        column2_value = {
            "id": f"{var1}_sichtpruefung",
            "type": "staticSingleSelect",
            "config": {
                "label": {
                    "text": {
                        "de": "Sichtprüfung",
                        "en": "Visual inspection"
                    },
                    "pdfHide": True
                },
                "pdfWidth": 0.4,
                "pdfHideIfValueIsEmpty": False,
                "value": {
                    "options": {
                        "ok": {
                            "de": "i.O",
                            "en": "OK"
                        },
                        "nok": {
                            "de": "n.i.O",
                            "en": "not OK"
                        },
                        "nV": {
                            "de": "n.V.",
                            "en": "N/A"
                        }
                    }
                }
            }
        }

    # Append the values of column1 and column2 directly to the data list
    data_list.extend([column1_value, column2_value])

# Create a JSON file with the combined data
output_file = '/Users/beateplendl/Downloads/output.json'
with open(output_file, 'w') as json_file:
    json.dump(data_list, json_file, indent=2)

print(f'Data saved to {output_file}')