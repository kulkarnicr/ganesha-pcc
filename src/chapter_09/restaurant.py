# Ganesha
"""Restaurant class module"""

class Restaurant():
    def __init__(self, restaurant_name: str, cuisine_type: str) -> None:
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type    
    
    def describe_restaurant(self):
        """method printing class info"""
        
        print(f"Restaurant: {self.restaurant_name}, Cuisine: {self.cuisine_type}")
    
    def open_restaurant(self):
        """Method indicating restaurant is open"""
        
        print(f"Restaurant {self.restaurant_name} is open.")
