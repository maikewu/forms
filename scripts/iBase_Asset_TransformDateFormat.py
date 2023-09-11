import csv
from dateutil.parser import parse
from datetime import datetime


# Input and output file paths
input_csv_file = '/Users/beateplendl/Downloads/2023-09-06_00-00_Asset_TestRows.csv'
output_csv_file = '/Users/beateplendl/Downloads/2023-09-06_00-00_Asset_TestRows2.csv'

# Function to transform a date cell to the desired format
def transform_date(date_str):
  if date_str is not None and date_str != '':  
    try:
        date_obj = parse(date_str)
        formatted_date = date_obj.strftime('%Y-%m-%dT00:00:00.000Z')
        return formatted_date
    except ValueError:
        return date_str # Return the original value if the date format is not valid

# Open input and output CSV files
with open(input_csv_file, 'r', newline='', encoding='utf-8') as input_file, open(output_csv_file, 'w', newline='', encoding='utf-8') as output_file:
    reader = csv.reader(input_file, delimiter=";")
    writer = csv.writer(output_file, delimiter=";")

    for row in reader:
        transformed_row = [transform_date(cell) for cell in row]
        writer.writerow(transformed_row)

print(f"CSV transformation completed. Output saved to {output_csv_file}")
