import json
import csv
import requests
import pandas as pd

# # Fetch the JSON data
# url = "https://raw.githubusercontent.com/Papagoat/brain-assessment/main/restaurant_data.json"
# response = requests.get(url)
# data = response.json()

# Alternative: Fetch the JSON data
# Load JSON data from file
with open('restaurant_data.json', 'r', encoding = 'utf-8') as f:
    data = json.load(f)

# Function to map country codes to country names
import pandas as pd

def map_country_code_to_name(country_code):
    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel('Country-Code.xlsx')

    # Set the 'Country Code' column as the index and convert it to a dictionary
    country_code_mapping = df.set_index('Country Code')['Country'].to_dict()

    # Return the country name corresponding to the country code, or the code itself if not found
    return country_code_mapping.get(country_code, country_code)

# Set to store unique restaurant names
unique_names = set() 

# Restaurant count
res_count = 0

# List to store the extracted data
extracted_data = []

for entry in data:
    for restaurant in entry['restaurants']:
        res_id = restaurant['restaurant']['R']['res_id']
        res_name = restaurant['restaurant']['name']
        res_country_id = restaurant['restaurant']['location']['country_id']
        #mapping the id to the country name using the xlsx file given
        res_country = map_country_code_to_name(res_country_id)
        res_city = restaurant['restaurant']['location']['city']
        res_user_votes = restaurant['restaurant']['user_rating']['votes']
        #explicitly converting the restaurant aggregate rating
        res_agg_rating = float(restaurant['restaurant']['user_rating']['aggregate_rating'])
        res_cuisines = restaurant['restaurant']['cuisines']
        #check for unique res_name
        if res_name not in unique_names:
            unique_names.add(res_name)
            # Count of Restaurant for checking with excel
            res_count += 1
            # Append the extracted data to the list
            extracted_data.append([res_id, res_name, res_country, res_city, res_user_votes, res_agg_rating, res_cuisines])
            
            #Checking if all variable is printing
            print(f"{res_count}) Restaurant ID: {res_id}, Name: {res_name}, Country:{res_country}, City: {res_city}, User Rating Votes: {res_user_votes}, User Aggregate Rating: {res_agg_rating}, Cuisines: {res_cuisines}")

# Define the CSV file path
csv_file_path = 'restaurants.csv'

# Write the extracted data to a CSV file 
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(['Restaurant ID', 'Name', 'Country', 'City', 'User Rating Votes', 'User Aggregate Rating', 'Cuisines'])
    # Write the extracted data rows
    writer.writerows(extracted_data)

print("Data has been successfully written to", csv_file_path)