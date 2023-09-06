import pandas as pd
import re

# Input and output file paths
csv_file = '/Users/beateplendl/Downloads/2023-05-30_00-00_Company.csv'
output_csv_file = '/Users/beateplendl/Downloads/2023-05-30_00-00_Company_Python.csv'


# Define the regular expression pattern
pattern = r'[\.\-\_\(\)\/\\]+'

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file,delimiter=";")

# Iterate through the "phone" column and apply the replacement
for index, row in df.iterrows():
    phone_number = row['phone']
    if pd.notna(phone_number):  # Check for NaN values
        cleaned_phone_number = re.sub(pattern, ' ', phone_number)
        df.at[index, 'phone'] = cleaned_phone_number

# Save the updated DataFrame to a new CSV file
df.to_csv(output_csv_file, index=False)

print(f"CSV file '{output_csv_file}' created with cleaned 'phoneNumber' column.")
