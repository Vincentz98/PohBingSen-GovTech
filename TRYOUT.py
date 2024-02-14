import requests
import json
import csv
import pandas as pd

# Function to map country codes to country names
def map_country_code_to_name(country_code):
    # Define an empty dictionary to store country code mapping
    country_code_mapping = {}

    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel('Country-Code.xlsx')

    # Iterate through rows in the DataFrame and populate the mapping dictionary
    for index, row in df.iterrows():
        country_code_mapping[row['Country Code']] = row['Country']

    # Return the country name corresponding to the country code, or the code itself if not found
    return country_code_mapping.get(country_code, country_code)

# Fetch the JSON data from the URL
url = "https://raw.githubusercontent.com/Papagoat/brain-assessment/main/restaurant_data.json"
response = requests.get(url)
data = response.json()

# Function to recursively flatten nested JSON objects
def flatten_json(data):
    flattened_data = {}

    def flatten(x, name=''):
        if isinstance(x, dict):
            for a in x:
                flatten(x[a], name + a + '_')
        elif isinstance(x, list):
            for i, a in enumerate(x):
                flatten(a, name + str(i) + '_')
        else:
            flattened_data[name[:-1]] = x

    flatten(data)
    return flattened_data

# List to store the extracted data
extracted_data = []



# Iterate through the JSON data
for entry in data:
    flattened_entry = flatten_json(entry)
    # Extract the specified fields
    res_id = flattened_entry.get('restaurant_R_res_id')
    print(res_id)
#     res_name = flattened_entry.get('restaurant_name')
#     res_country_id = flattened_entry.get('restaurant_location_country_id')
#     # Mapping the country code to country name
#     res_country = map_country_code_to_name(res_country_id)
#     res_city = flattened_entry.get('restaurant_location_city')
#     res_user_votes = flattened_entry.get('restaurant_user_rating_votes')
#     res_agg_rating = flattened_entry.get('restaurant_user_rating_aggregate_rating')
#     if res_agg_rating is not None:
#         res_agg_rating = float(res_agg_rating)
#     res_cuisines = flattened_entry.get('restaurant_cuisines')

#     # Append the extracted data to the list
#     extracted_data.append([res_id, res_name, res_country, res_city, res_user_votes, res_agg_rating, res_cuisines])

# # Define the CSV file path
# csv_file_path = 'restaurants.csv'

# # Write the extracted data to a CSV file
# with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     # Write the header row
#     writer.writerow(['Restaurant Id', 'Restaurant Name', 'Country', 'City', 'User Rating Votes', 'User Aggregate Rating', 'Cuisines'])
#     # Write the extracted data rows
#     writer.writerows(extracted_data)

# print("Data has been successfully written to", csv_file_path)
