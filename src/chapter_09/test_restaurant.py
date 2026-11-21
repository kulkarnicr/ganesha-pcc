# Ganesha
from restaurant import Restaurant

print("=== TESTING import class from another module ===")
restaurant = Restaurant('Vishnuvardhan', 'Marathi')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
