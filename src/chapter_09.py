# Ganesha
# PEP8 suggestions
# - one blank line between two methods in a class
# - two blank lines between two classes in same file

# try It yourself
# 9-1. Restaurant: Make a class called Restaurant . The __init__() method for 
# Restaurant should store two attributes: a restaurant_name and a cuisine_type . 
# Make a method called describe_restaurant() that prints these two pieces of 
# information, and a method called open_restaurant() that prints a message indi
# cating that the restaurant is open .
# Make an instance called restaurant from your class . Print the two attri
# butes individually, and then call both methods .
print('-'*40)
#Ganesha.
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
        
restaurant = Restaurant('Vishnuvardhan', 'Marathi')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9-2. Three Restaurants: Start with your class from Exercise 9-1 . Create three 
# different instances from the class, and call describe_restaurant() for each 
# instance .
print('-'*40)
restaurant1 = Restaurant('Aapli Marathi', 'main course')
restaurant2 = Restaurant('Amruttulya', 'chaha')
restaurant3 = Restaurant('Sudamyache Pohe', 'breakfast')
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

# 9-3. Users: Make a class called User . Create two attributes called first_name 
# and last_name, and then create several other attributes that are typically stored 
# in a user profile . Make a method called describe_user() that prints a summary 
# of the user’s information . Make another method called greet_user() that prints 
# a personalized greeting to the user .
# Create several instances representing different users, and call both methods 
# for each user
print('-'*40)
#Ganesha.
class User():
    def __init__(self, first_name: str, last_name: str, age: int, height: float) -> None:
        """define user attributes"""
        
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
    
    def describe_user(self) -> None:
        """method to print user info"""
        
        print("User information:")
        print(f"\tFirst name: {self.first_name}")
        print(f"\tLast name : {self.last_name}")
        print(f"\tAge       : {self.age}")
        print(f"\tHeight    : {self.height}")
    
    def greet_user(self) -> None:
        """method to print personalized greeting to the user"""
        
        print(f"Hi '{self.first_name} {self.last_name}', welcome to the user class.")


# create instances of User class
# and call both methods on them
user1 = User('Ganesha', 'Kailas', 99, 10.5)
user2 = User('Shiva', 'Aadi', 99, 10.6)
user3 = User('Hari', 'Aadi', 99, 10.6)
users = [user1, user2, user3]
print("======= Describing all users =======")
for user in users:
    user.describe_user()
print("======= Greeting all users =======")
for user in users:
    user.greet_user()

# 9-4. Number Served: Start with your program from Exercise 9-1 (page 166) . 
# Add an attribute called number_served with a default value of 0 . Create an 
# instance called restaurant from this class . Print the number of customers the 
# restaurant has served, and then change this value and print it again .
# Add a method called set_number_served() that lets you set the number 
# of customers that have been served . Call this method with a new number and 
# print the value again .
# Add a method called increment_number_served() that lets you increment 
# the number of customers who’ve been served . Call this method with any num
# ber you like that could represent how many customers were served in, say, a 
# day of business .
print('-'*40)
class RestaurantWithNumberServed():
    def __init__(self, restaurant_name: str, cuisine_type: str) -> None:
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        """method printing class info"""
        
        print(f"Restaurant: {self.restaurant_name}, Cuisine: {self.cuisine_type}")
    
    def open_restaurant(self):
        """Method indicating restaurant is open"""
        
        print(f"Restaurant {self.restaurant_name} is open.")

    def set_number_served(self, number_served: int):
        """Method to set number of customers served"""
        
        if number_served < self.number_served:
            print(f"[ERROR] Currently already served customers are {self.number_served}." + 
                  f"You can not set or roll back to {number_served} (which is less).")
        else:
            self.number_served = number_served

    def increment_number_served(self, number_served: int):
        """Method to increment number of customers served"""
        
        if number_served > 0:
            self.number_served += number_served


restaurant = RestaurantWithNumberServed('Vishnuvardhan', 'Marathi')
print(f"Currently total served customers : {restaurant.number_served}")
print("manually updating served-customers")
restaurant.number_served = 10
print(f"Currently total served customers : {restaurant.number_served}")

print("calling method to set served-customers to 5")
restaurant.set_number_served(5)
print(f"Currently total served customers : {restaurant.number_served}")
print("calling method to set served-customers to 15")
print(f"Currently total served customers : {restaurant.number_served}")
restaurant.set_number_served(15)
print(f"Currently total served customers : {restaurant.number_served}")

print("calling method to increment served-customers by 5")
print(f"Currently total served customers : {restaurant.number_served}")
restaurant.increment_number_served(5)
print(f"Currently total served customers : {restaurant.number_served}")
print("calling method to increment served-customers by 5")
print(f"Currently total served customers : {restaurant.number_served}")
restaurant.increment_number_served(5)
print(f"Currently total served customers : {restaurant.number_served}")

# 9-5. Login Attempts: Add an attribute called login_attempts to your User 
# class from Exercise 9-3 (page 166) . Write a method called increment_
# login_attempts() that increments the value of login_attempts by 1 . Write 
# another method called reset_login_attempts() that resets the value of login_
# attempts to 0 .
# Make an instance of the User class and call increment_login_attempts() 
# several times . Print the value of login_attempts to make sure it was incremented 
# properly, and then call reset_login_attempts() . Print login_attempts again to 
# make sure it was reset to 0
print('-'*40)
class UserWithLoginAttempts():
    def __init__(self, first_name: str, last_name: str, age: int, height: float) -> None:
        """define user attributes"""
        
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.login_attempts = 0
    
    def describe_user(self) -> None:
        """method to print user info"""
        
        print("User information:")
        print(f"\tFirst name: {self.first_name}")
        print(f"\tLast name : {self.last_name}")
        print(f"\tAge       : {self.age}")
        print(f"\tHeight    : {self.height}")
    
    def greet_user(self) -> None:
        """method to print personalized greeting to the user"""
        
        print(f"Hi '{self.first_name} {self.last_name}', welcome to the user class.")

    def increment_login_attempts(self) -> None:
        """method to increment login attempts"""
        
        self.login_attempts += 1

    def reset_login_attempts(self) -> None:
        """method to reset 0 login attempts"""
        
        self.login_attempts = 0

# create instances of User class
# and call both methods on them
user1_1 = UserWithLoginAttempts('Ganesha', 'Kailas', 99, 10.5)
print(f"Current login attempts for user {user1_1.first_name} are {user1_1.login_attempts}.")
print("Simulate login 5 times...")
for i in range(5):
    print(f"[Attempt {i}] logging in...")
    user1_1.increment_login_attempts()
reset_status = "PASS" if user1_1.login_attempts == 5 else "FAIL"
print(f"{reset_status}: Current login attempts for user {user1_1.first_name} are {user1_1.login_attempts}.")
print("Reset login attempts to zero")
user1_1.reset_login_attempts()
print("Ensure login attempts is back to zero.")
reset_status = ""
reset_status = "PASS" if user1_1.login_attempts == 0 else "FAIL"
print(f"{reset_status}: Current login attempts for user {user1_1.first_name} are {user1_1.login_attempts}.")

# #Ganesha.
# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant . Write 
# a class called IceCreamStand that inherits from the Restaurant class you wrote 
# in Exercise 9-1 (page 166) or Exercise 9-4 (page 171) . Either version of 
# the class will work; just pick the one you like better . Add an attribute called 
# flavors that stores a list of ice cream flavors . Write a method that displays 
# these flavors . Create an instance of IceCreamStand, and call this method .
print('-'*40)
#Ganesha.
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name: str, cuisine_type: str) -> None:
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanila', 'chocolate', 'butterscotch']
    
    def display_flavors(self):
        """method to print icecream flavors"""
        print("Our restaurant offers below icecream flavors:")
        for flavor in self.flavors:
            print(f"\t{flavor}")


ice_cream_stand = IceCreamStand('Naturals', 'Than')
ice_cream_stand.describe_restaurant()
ice_cream_stand.display_flavors()

# 9-7. Admin: An administrator is a special kind of user . Write a class called 
# Admin that inherits from the User class you wrote in Exercise 9-3 (page 166) 
# or Exercise 9-5 (page 171) . Add an attribute, privileges, that stores a list 
# of strings like "can add post", "can delete post", "can ban user", and so on . 
# Write a method called show_privileges() that lists the administrator’s set of 
# privileges . Create an instance of Admin, and call your method .
print('-'*40)
#Ganesha.
class Admin(User):
    def __init__(self, first_name: str, last_name: str, age: int, height: float) -> None:
        super().__init__(first_name, last_name, age, height)
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user",
            "can reset passwords for users periodically",
            "can unlock user"
        ]
    
    def show_privileges(self):
        """method to print admin privileges"""
        print("Admin privileges are:")
        for privilege in self.privileges:
            print(f"\t{privilege}")

admin_user = Admin('Ganesha', 'Kailas', 99, 10.6)
admin_user.describe_user()
admin_user.show_privileges()

# 9-8. Privileges: Write a separate Privileges class . The class should have one 
# attribute, privileges, that stores a list of strings as described in Exercise 9-7 . 
# Move the show_privileges() method to this class . Make a Privileges instance 
# as an attribute in the Admin class . Create a new instance of Admin and use your 
# method to show its privileges .
print('-'*40)
class Privileges:
    def __init__(self):
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user",
            "can reset passwords for users periodically",
            "can unlock user"
        ]
    
    def show_privileges(self):
        """method to print admin privileges"""
        print("Admin privileges are:")
        for privilege in self.privileges:
            print(f"\t{privilege}")

class AdminWithPrivilegesAsAttribute(User):
    def __init__(self, first_name: str, last_name: str, age: int, height: float) -> None:
        super().__init__(first_name, last_name, age, height)
        self.privileges = Privileges()

admin_user_with_privileges_instance = AdminWithPrivilegesAsAttribute('Ganesha', 'Kailas', 99, 10.6)
admin_user_with_privileges_instance.describe_user()
admin_user_with_privileges_instance.privileges.show_privileges()

# 9-9. Battery Upgrade: Use the final version of electric_car.py from this section . 
# Add a method to the Battery class called upgrade_battery() . This method 
# should check the battery size and set the capacity to 85 if it isn’t already . 
# Make an electric car with a default battery size, call get_range() once, and 
# then call get_range() a second time after upgrading the battery . You should 
# see an increase in the car’s range.
print('-'*40)
########## NOT IMPLEMENTED 9-9 ###################
# class Car():
#     """A simple attempt to represent a car."""
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#     def get_descriptive_name(self):
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#     def read_odometer(self):
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
#     def increment_odometer(self, miles):
#         self.odometer_reading += miles


# class ElectricCar(Car):
#     """Represent aspects of a car, specific to electric vehicles"""
#     def __init__(self, make, model, year):
#         """Initialize attributes of the parent class."""
#         super().__init__(make, model, year)
#         self.battery_size = 70
        
#     def describe_battery(self):
#         """Print a statement describing the battery size."""
#         print("This car has a " + str(self.battery_size) + "-kWh battery.")

# 9-10. Imported Restaurant: Using your latest Restaurant class, store it in a mod
# ule . Make a separate file that imports Restaurant . Make a Restaurant instance, 
# and call one of Restaurant’s methods to show that the import statement is work
# ing properly .
print('-'*40)
# Implemented in folder chapter_09/ as restaurant.py and test_restaurant.py

# 9-11. Imported Admin: Start with your work from Exercise 9-8 (page 178) . 
# Store the classes User, Privileges, and Admin in one module . Create a sepa
# rate file, make an Admin instance, and call show_privileges() to show that 
# everything is working correctly .
print('-'*40)
# Implemented in folder chapter_09/ as admin.py and test_admin.py

# 9-12. Multiple Modules: Store the User class in one module, and store the 
# Privileges and Admin classes in a separate module . In a separate file, create 
# an Admin instance and call show_privileges() to show that everything is still 
# working correctly
print('-'*40)
# Implemented in folder chapter_09/ as user.py, privileges_admin.py and test_separate_modules_admin_9-12.py

# 9-13. OrderedDict Rewrite: Start with Exercise 6-4 (page 108), where you 
# used a standard dictionary to represent a glossary . Rewrite the program using 
# the OrderedDict class and make sure the order of the output matches the order 
# in which key-value pairs were added to the dictionary .
print('-'*40)
from collections import OrderedDict
glossary = OrderedDict()
glossary['list'] = 'a group or collection of items'
glossary['dictionary'] = 'key-value pair items',
glossary['slicing'] = 'a list operation that allows to extract portion of a list',
glossary['indexing'] = 'accessing list elements by their position',
glossary['for'] = 'this is a looping construct to iterate over list or dictionary items',

expected_key_order = ['list', 'dictionary', 'slicing', 'indexing', 'for']
glossary_keys = glossary.keys()

if expected_key_order == glossary_keys:
    print("[PASS]OrderDict retains insertionorder.")
else:
    print("[FAIL]OrderDict retains insertionorder.")
    
# 9-14. Dice: The module random contains functions that generate random num
# bers in a variety of ways . The function randint() returns an integer in the 
# range you provide . The following code returns a number between 1 and 6:
# from random import randint
# x = randint(1, 6)
# Make a class Dice with one attribute called sides, which has a default 
# value of 6 . Write a method called roll_dice() that prints a random number 
# between 1 and the number of sides the dice has . Make a 6-sided dice and roll 
# it 10 times .
# Make a 10-sided dice and a 20-sided dice . Roll each dice 10 times .
print('-'*40)
#Ganesha.
from random import randint
class Dice:
    def __init__(self, sides=6) -> None:
        self.sides = sides
    
    def roll_dice(self) -> None:
        random_number = randint(1,self.sides)
        print(f"...{random_number}...")

dice_6 = Dice()
dice_10 = Dice(10)
dice_20 = Dice(20)

dices = [dice_6, dice_10, dice_20]
for dice in dices:
    print(f"\n~~~ Rolling {dice} 10 times ~~~")
    for i in range(1, 11):
        dice.roll_dice()
    print('%%%%%%%%%%%%%%%%%%%%%%%%%')
    
# 9-15. Python Module of the Week: One excellent resource for exploring the 
# Python standard library is a site called Python Module of the Week . Go to 
# http://pymotw.com/ and look at the table of contents . Find a module that 
# looks interesting to you and read about it, or explore the documentation of 
# the collections and random modules.
#TBD I wish to read https://pymotw.com/3/pathlib/index.html useful as qa