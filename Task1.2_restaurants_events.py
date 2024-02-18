import json
import csv
import requests
from datetime import datetime

# Load the JSON data
# url = "https://raw.githubusercontent.com/Papagoat/brain-assessment/main/restaurant_data.json"
# response = requests.get(url)
# data = response.json()

# Alternative: Fetch the JSON data
# Load JSON data from file
with open('restaurant_data.json', 'r', encoding = 'utf-8') as f:
    data = json.load(f)

# Function to return true only if is april 2019
def is_april_2019(date_str):
    return date_str.startswith('2019-04')

# List to store the extracted data
extracted_data = []

# Set to store unique event IDs
unique_event_ids = set()

# Check of event count
event_count = 0

# Event ID is the unique key that differ the rest of the entry from the others
for entry in data:
    for restaurant in entry['restaurants']:
        res_id = restaurant['restaurant']['R']['res_id']
        res_name = restaurant['restaurant']['name']
        # Do no neeed the else case for no zomato_event, there is no start date and end date to double check for april 2019
        if 'zomato_events' in restaurant['restaurant']:
            # Initialize variables with "NA" so if there are no values filled, "NA" will be used
            event_id = 'NA'
            photo_url = "NA"
            title = "NA"
            start_date = 'NA'
            end_date = 'NA'
            # Iterate over each event and extract its details
            for item in restaurant['restaurant']['zomato_events']:
                event_id = item['event']['event_id']
                # Check if the event ID has been seen before
                if event_id not in unique_event_ids:
                    unique_event_ids.add(event_id)
                    start_date = item['event']['start_date']
                    end_date = item['event']['end_date']
                    # Check if the event occurred in April 2019
                    if is_april_2019(start_date) and is_april_2019(end_date):
                        # Check if the event has photos
                        if 'photos' in item['event']:
                            for photo in item['event']['photos']:
                                photo_url = photo['photo']['url']
                        # To double-check if the title exists in the event
                        if 'title' in item['event']:
                            title = item['event']['title']
                        # Increment event count
                        event_count += 1
                        # Print the event details
                        print(f"{event_count}) Event ID: {event_id}, Restaurant ID: {res_id}, Restaurant Name: {res_name}, Photo Url: {photo_url}, Event Title: {title}, Event Start Date: {start_date}, Event End Date: {end_date}")
                        # Append the extracted data for csv export
                        extracted_data.append([event_id, res_id, res_name, photo_url, title, start_date, end_date])




# Print the count of events processed
print(f"Total number of past event in the month of April 2019: {event_count}")                
        
# Define the CSV file path
csv_file_path = 'restaurant_events.csv'

# Write the extracted data to a CSV file
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header row that is wanted
    writer.writerow(['Event Id', 'Restaurant Id', 'Restaurant Name', 'Photo URL', 'Event Title', 'Event Start Date', 'Event End Date'])
    # Write the extracted data rows
    writer.writerows(extracted_data)

print("Data has been successfully written to", csv_file_path)
