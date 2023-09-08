import csv
import re
from datetime import datetime

# Input and output file paths
input_file = '/Users/beateplendl/Downloads/2023-09-06_00-00_Asset_TestRows.csv'
output_file = '/Users/beateplendl/Downloads/2023-09-06_00-00_Asset_TestRows_Python.csv'

# Function to transform the date format
def transform_date(date_str):
  if date_str is not None and date_str != '':  
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        formatted_date = date_obj.strftime('%Y-%m-%dT00:00:00.000Z')
        return formatted_date
    except ValueError:
        return date_str # Return the original value if the date format is not valid

def transform_prop16(customProp16):
    date_format_pattern = r'\d{4}-\d{2}-\d{2}'
    if re.match(date_format_pattern, customProp16):
        return "Ja - im Projekt beinhaltet"
    # Check if the input_value is empty or contains only whitespace
    if not customProp16.strip():
        return "Nein"
    # If neither condition is met, return the original input_value
    return customProp16

# Open input and output CSV files
with open(input_file, 'r', newline='', encoding='utf-8') as csvfile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(csvfile, delimiter=';')
    writer = csv.writer(outfile, delimiter=';')

    # Read and write the header row (first row) as is
    header = next(reader)
    writer.writerow(header)

    # Iterate through rows and transform the 10th,11th,12th,13th,14th and 15th columns of the csv
    for row in reader:
        if len(row) >= 15:
            row[9] = transform_date(row[9])
            row[10] = transform_date(row[10])
            row[11] = transform_prop16(row[11])
            row[12] = transform_date(row[12])
            row[13] = transform_date(row[13])
            row[14] = transform_date(row[14])
        writer.writerow(row)

print(f'Transformed values written to {output_file}')

