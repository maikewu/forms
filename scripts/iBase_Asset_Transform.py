import csv
import pandas as pd
import re
from dateutil.parser import parse
from datetime import datetime
from collections import defaultdict

# Input and output file paths
input_csv_file = '/Users/beateplendl/Downloads/2023-09-07_iBase_Python_TestAssets.csv'
output_csv_file = '/Users/beateplendl/Downloads/2023-09-07_iBase_Python_TestAssets_Transformed.csv'

# Define regular expression pattern
patternSpace = r'\s+'

# Function to transform a date cell to the desired format
def transform_date(date_str):
    if date_str is not None and date_str.strip() != '':
        try:
            date_obj = parse(date_str)
            formatted_date = date_obj.strftime('%Y-%m-%dT00:00:00.000Z')
            return formatted_date
        except ValueError:
            return date_str
    else:
        return ''

# Check Asset-ID for duplicates and empty cells
def check_for_duplicates_and_empty_cells(csv_file):
    serial_numbers = set()
    duplicates_found = False
    empty_cells_found_ids = False
    empty_cells_found_types = False
    
    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=";")
        for row_num, row in enumerate(reader, start=2):
            serial_number = row.get('serialNumber')
            asset_type = row.get('assetType')
            
            if serial_number is not None and serial_number.strip() != '':
                if serial_number in serial_numbers:
                    duplicates_found = True
                else:
                    serial_numbers.add(serial_number)
            
            if serial_number is None or serial_number.strip() == '':
                empty_cells_found_ids = True

            if asset_type is None or asset_type.strip() == '':
                empty_cells_found_types = True
    
    return duplicates_found, empty_cells_found_types, empty_cells_found_ids

if __name__ == "__main__":
    # Check for duplicates and empty cells before transforming the CSV
    duplicates_found, empty_cells_found_types, empty_cells_found_ids = check_for_duplicates_and_empty_cells(input_csv_file)
    
    if duplicates_found:
        print("Duplicates found in the 'serialNumber' column.")
    else:
        print("No duplicates found in the 'serialNumber' column.")
    
    if empty_cells_found_ids:
        print("Empty cells found in the 'serialNumber' column.")
    else:
        print("No empty cells found in the 'serialNumber' column.")

    if empty_cells_found_types:
        print("Empty cells found in the 'assetType' column.")
    else:
        print("No empty cells found in the 'assetType' column.")
    
    # Open input and output CSV files
    with open(input_csv_file, 'r', newline='', encoding='utf-8') as input_file, open(output_csv_file, 'w', newline='', encoding='utf-8') as output_file:
        reader = csv.reader(input_file, delimiter=";")
        writer = csv.writer(output_file, delimiter=";")
        header = next(reader)  # First row contains headers
        writer.writerow(header)  # Write headers to the output file

        for row in reader:
            transformed_row = []
            for cell, column_name in zip(row, header):
                if "customProp" in column_name:
                    transformed_row.append(transform_date(cell))
                else:
                    transformed_row.append(cell)
            writer.writerow(transformed_row)

    # Read the CSV file into a DataFrame
    df = pd.read_csv(output_csv_file, delimiter=";", dtype={'serialNumber': str, 'assetType':str})

    # Replace the column header "customerPerson" with "customerContact"
    df.rename(columns={"customerPerson": "customerContact"}, inplace=True)
    # Replace the column header "manufacturerPerson" with "manufacturerContact"
    df.rename(columns={"manufacturerPerson": "manufacturerContact"}, inplace=True)

    # Iterate through the "customerContact" column and apply the replacement
    for index, row in df.iterrows():
        customerContact = row['customerContact']
        if pd.notna(customerContact):
            cleaned_customerContact = re.sub(patternSpace, '', customerContact)
            df.at[index, 'customerContact'] = cleaned_customerContact

    # Iterate through the "manufacturerContact" column and apply the replacement
    for index, row in df.iterrows():
        manufacturerContact = row['manufacturerContact']
        if pd.notna(manufacturerContact):
            cleaned_manufacturerContact = re.sub(patternSpace, '', manufacturerContact)
            df.at[index, 'manufacturerContact'] = cleaned_manufacturerContact

    # Save the updated DataFrame to a new CSV file
    df.to_csv(output_csv_file, index=False, sep=";")

    print(f"CSV transformation completed. Output saved to {output_csv_file}")
