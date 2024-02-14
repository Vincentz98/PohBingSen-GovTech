import json
import urllib.request

# URL of the JSON file
url = "https://raw.githubusercontent.com/Papagoat/brain-assessment/main/restaurant_data.json"

# Fetch the JSON data from the URL
response = urllib.request.urlopen(url)
data = response.read()

# Decode the JSON data
decoded_data = data.decode('utf-8')

# Load the JSON data into a Python dictionary
restaurant_data = json.loads(decoded_data)

# Print the readable data
print(json.dumps(restaurant_data, indent=4))

