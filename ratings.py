# """Restaurant rating lister."""
# Your job is to write a program named ratings.py that:

# Reads the ratings in from the file
# Stores them in a dictionary
# And finally, spits out the ratings in alphabetical order by restaurant
# Hint 1: Using .items() to get a list of your dictionary entries will help with sorting.

# Hint 2: Refer to the Python docs on the sorted() function if you need a reminder of how to sort.

# # put your code here

restaurant_file = open("scores.txt")

def get_restaurant_ratings(file):
    restaurants = {}

    for line in file:
        line = line.strip()
        restaurant = line.split(":")
        restaurant_name = restaurant[0]
        restaurant_rating = restaurant[1]
        restaurants[restaurant_name] = restaurant_rating


        