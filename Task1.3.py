import json

# Load JSON data from file
with open('restaurant_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Initialize dictionary to store aggregate ratings for each category
aggregate_ratings = {}

# Extract aggregate ratings and corresponding rating texts
for entry in data:
    for restaurant in entry['restaurants']:
        aggregate_rating = float(restaurant['restaurant']['user_rating']['aggregate_rating'])
        rating_text = restaurant['restaurant']['user_rating']['rating_text']
        
        # Check if the rating category already exists in the dictionary
        if rating_text not in aggregate_ratings:
            aggregate_ratings[rating_text] = [aggregate_rating]
        else:
            aggregate_ratings[rating_text].append(aggregate_rating)

# Define rating categories that was given 
rating_categories = ['Excellent', 'Very Good', 'Good', 'Average', 'Poor']

# Initialize dictionary to store thresholds for each rating category
thresholds = {}

# Calculate threshold for each rating category
# Iterate in all category in rating_categories to find the minimum cut off
for category in rating_categories:
    # Get aggregate ratings for the current rating category
    category_ratings = aggregate_ratings[category]
    
    # Calculate the threshold as the minimum aggregate rating in the category
    threshold = min(category_ratings)
    
    # Store the threshold for the current rating category
    thresholds[category] = threshold


# Print the thresholds for each rating category
for category, threshold in thresholds.items():
    print(f"{category}: {threshold}")

# CHECKING

# # Print all ratings for each category for checking
# for category in rating_categories:
#     # Get ratings for the current category
#     ratings = aggregate_ratings.get(category, [])
    
#     # Print the category and its ratings
#     print(f"{category} Ratings:")
#     for rating in ratings:
#         print(rating)
#     print()  # Add a newline for better readability

# # Print the number of ratings for each category
# for category in rating_categories:
#     # Get the number of ratings in the current category
#     num_ratings = len(aggregate_ratings.get(category, []))
    
#     # Print the category and the number of ratings
#     print(f"{category}: {num_ratings}")