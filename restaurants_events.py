import json
import csv
import requests
from datetime import datetime

def is_april_2019(date_str):
    # Parse the date string as 'YYYY-MM-DD'
    date = datetime.strptime(date_str, '%Y-%m-%d')
    # Check if the year is 2019 and the month is April
    return date.year == 2019 and date.month == 4

# Load the JSON data
url = "https://raw.githubusercontent.com/Papagoat/brain-assessment/main/restaurant_data.json"
response = requests.get(url)
data = response.json()

# List to store the extracted data
extracted_data = []

# # Iterate through the JSON data
# for entry in data:
#     for restaurant in entry['restaurants']:
#         res_id = restaurant['restaurant']['R']['res_id']
#         res_name = restaurant['restaurant']['name']
#         # Check if the restaurant has any events
#         if 'zomato_events' in restaurant['restaurant']:
#             # Iterate over each event and extract its ID
#             for item in restaurant['restaurant']['zomato_events']:
#                 event_id = item['event']['event_id']
#                 if 'photos' in restaurant['restaurant']['zomato_events']['event']:
#                     photo_url = item['event']['photos']['photo']['url']
#                 title = item['event']['title']
#                 start_date = item['event']['start_date']
#                 end_date = item['event']['end_date']
#                 print(f"Event ID: {event_id}, Restaurant ID: {res_id}, Restaurant Name: {res_name}, Photo Url: {photo_url}, Event Title: {title}, Event Start Date: {start_date}, Event End Date: {end_date}")
                
#         else: 
#             print("NA")

# Set to store unique event IDs
unique_event_ids = set()

for entry in data:
    for restaurant in entry['restaurants']:
        res_id = restaurant['restaurant']['R']['res_id']
        res_name = restaurant['restaurant']['name']
        
        # Check if the restaurant has any events
        if 'zomato_events' in restaurant['restaurant']:
            # Iterate over each event and extract its details
            for item in restaurant['restaurant']['zomato_events']:
                event_id = item['event']['event_id']
                # Check if the event ID has been seen before
                if event_id not in unique_event_ids:
                    unique_event_ids.add(event_id)
                    title = item['event']['title']
                    start_date = item['event']['start_date']
                    end_date = item['event']['end_date']
                    
                    # Check if the event has photos
                    if 'photos' in item['event']:
                        # Iterate over each photo and extract its URL
                        for photo in item['event']['photos']:
                            photo_url = photo['photo']['url']
                            print(f"Event ID: {event_id}, Restaurant ID: {res_id}, Restaurant Name: {res_name}, Photo Url: {photo_url}, Event Title: {title}, Event Start Date: {start_date}, Event End Date: {end_date}")
                    else:
                        print(f"Event ID: {event_id}, Restaurant ID: {res_id}, Restaurant Name: {res_name}, Photo Url: NA, Event Title: {title}, Event Start Date: {start_date}, Event End Date: {end_date}")
                
        else: 
            # print(f"NA, Restaurant ID: {res_id}, Restaurant Name: {res_name}, Photo Url: NA, Event Title: NA, Event Start Date: NA, Event End Date: NA")
            print("NA")
        
        # Check if the event occurred in April 2019
        if is_april_2019(start_date):
            print(f"Event ID: {event_id}, Restaurant ID: {res_id}, Restaurant Name: {res_name}, Photo Url: {photo_url}, Event Title: {title}, Event Start Date: {start_date}, Event End Date: {end_date}")
            # Append the extracted data to the list
            extracted_data.append([event_id, res_id, res_name, photo_url, title, start_date, end_date])

# # Define the CSV file path
# csv_file_path = 'restaurant_events.csv'

# # Write the extracted data to a CSV file
# with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     # Write the header row
#     writer.writerow(['Event Id', 'Restaurant Id', 'Restaurant Name', 'Photo URL', 'Event Title', 'Event Start Date', 'Event End Date'])
#     # Write the extracted data rows
#     writer.writerows(extracted_data)

# print("Data has been successfully written to", csv_file_path)
