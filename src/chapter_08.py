# Ganesha
# Ganesha

# 8-1. Message: Write a function called display_message() that prints one sen
# tence telling everyone what you are learning about in this chapter . Call the 
# function, and make sure the message displays correctly .
print('-'*40)
def display_message():
    """display function"""
    
    print("You're learning function.")

display_message()

# 8-2. Favorite Book: Write a function called favorite_book() that accepts one 
# parameter, title . The function should print a message, such as One of my 
# favorite books is Alice in Wonderland . Call the function, making sure to 
# include a book title as an argument in the function call 
print('-'*40)
def favorite_book(title: str) -> None:
    """function printing book"""
    
    print(f"One of my favorite books is {title.title()}.")

favorite_book('ShriHari')

# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the 
# text of a message that should be printed on the shirt . The function should print 
# a sentence summarizing the size of the shirt and the message printed on it .
# Call the function once using positional arguments to make a shirt . Call the 
# function a second time using keyword arguments .
print('-'*40)
def make_shirt(size: int, text: str) -> None:
    """printing message tshirt"""
    
    print(f"My tshirt size is {size} with message {text}.")

make_shirt(5, 'Ganesha the greatest.')
make_shirt(size=5, text='Hari Hari')
make_shirt(text='Gajanana', size=5)

# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large 
# by default with a message that reads I love Python . Make a large shirt and a 
# medium shirt with the default message, and a shirt of any size with a different 
# message .
print('-'*40)
def make_shirt_2(size:str='large', text:str='I love Python'):
    """function default values"""
    
    print(f"My shirt size {size}, message {text}.")

make_shirt_2()
make_shirt_2(size='medium')
make_shirt_2(size='small', text='I love C')

# 8-5. Cities: Write a function called describe_city() that accepts the name of 
# a city and its country . The function should print a simple sentence, such as 
# Reykjavik is in Iceland . Give the parameter for the country a default value . 
# Call your function for three different cities, at least one of which is not in the 
# default country
print('-'*40)
def describe_city(city, country='India'):
    """function city country"""
    
    print(f"{city} is in {country}.")

describe_city('pune')
describe_city('mumbai')
describe_city('newyork', 'usa')

# 8-6. City Names: Write a function called city_country() that takes in the name 
# of a city and its country . The function should return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the value 
# that’s returned .
print('-'*40)
print('-'*40)
def describe_city_2(city: str, country: str):
    """function city country"""
    
    return f"{city.title()}, {country.title()}"

print(describe_city_2('pune', 'India'))
print(describe_city_2('mumbai', 'India'))
print(describe_city_2('newyork', 'usa'))

# 8-7. Album: Write a function called make_album() that builds a dictionary 
# describing a music album . The function should take in an artist name and an 
# album title, and it should return a dictionary containing these two pieces of 
# information . Use the function to make three dictionaries representing different 
# albums . Print each return value to show that the dictionaries are storing the 
# album information correctly .
# Add an optional parameter to make_album() that allows you to store the 
# number of tracks on an album . If the calling line includes a value for the num
# ber of tracks, add that value to the album’s dictionary . Make at least one new 
# function call that includes the number of tracks on an album .
print('-'*40)
def make_album(artist:str, album:str, tracks=0) -> dict:
    """function returning dictionary"""
    
    album_details = {}
    
    album_details['artist'] = artist
    album_details['album'] = album
    if tracks > 0:
        album_details['tracks'] = tracks
    
    return album_details

print(make_album('Ganesha', 'Sarvsreshth'))
print(make_album('Hari', 'Golokleela'))
print(make_album('Ram', 'Vairagya'))
print(make_album('Ram', 'Shant', tracks=1))
print(make_album('Ram', 'Vanvas', tracks=2))

# 8-8. User Albums: Start with your program from Exercise 8-7 . Write a while 
# loop that allows users to enter an album’s artist and title . Once you have that 
# information, call make_album() with the user’s input and print the dictionary 
# that’s created . Be sure to include a quit value in the while loop 
print('-'*40)
is_active = True
while is_active:
    artist = input("Artist please: ")
    album = input("Album please: ")
    print(make_album(artist, album))
    response = input("Do you wish to continue? (y/n): ")
    if response.lower() == 'n':
        is_active = False

# 8-9. Magicians: Make a list of magician’s names . Pass the list to a function 
# called show_magicians(), which prints the name of each magician in the list .
print('-'*40)
def show_magicians(magicians):
    for magician in magicians:
        print(magician)

magicians = ['Ganesha', 'Vishnu', 'Hari', 'Har']
show_magicians(magicians)

# 8-10. Great Magicians: Start with a copy of your program from Exercise 8-9 . 
# Write a function called make_great() that modifies the list of magicians by add
# ing the phrase the Great to each magician’s name . Call show_magicians() to 
# see that the list has actually been modified .
print('-'*40)
def make_great(magicians):
    """in place modify"""
    
    magicians = [f'the Great {magician}' for magician in magicians]

magicians = ['Ganesha', 'Vishnu', 'Hari', 'Har']
print(f"Before: {magicians}")
make_great(magicians)
print(f"After: {magicians}")
show_magicians(magicians)

# 8-11. Unchanged Magicians: Start with your work from Exercise 8-10 . Call the 
# function make_great() with a copy of the list of magicians’ names . Because the 
# original list will be unchanged, return the new list and store it in a separate list . 
# Call show_magicians() with each list to show that you have one list of the origi
# nal names and one list with the Great added to each magician’s name.
print('-'*40)
def make_great_2(magicians):
    """in place modify"""
    
    magicians = [f'the Great {magician}' for magician in magicians]

    return magicians

magicians = ['Ganesha', 'Vishnu', 'Hari', 'Har']
print(f"Before magician: {magicians}")
great_magicians = make_great_2(magicians[:])
print(f"After magicians: {magicians}")
print(f"After great_mag: {great_magicians}")
show_magicians(magicians)
show_magicians(great_magicians)

# 8-12. Sandwiches: Write a function that accepts a list of items a person wants 
# on a sandwich . The function should have one parameter that collects as many 
# items as the function call provides, and it should print a summary of the sand
# wich that is being ordered . Call the function three times, using a different num
# ber of arguments each time .
print('-'*40)
def make_sandwich(items: list):
    print("The sandwich ingedients:")
    for item in items:
        print(f"\t{item}")

make_sandwich(['cucumber', 'corn'])
make_sandwich(['cucumber', 'corn', 'pasta'])
make_sandwich(['cucumber', 'corn', 'mutte'])

# 8-13. User Profile: Start with a copy of user_profile.py from page 153 . Build 
# a profile of yourself by calling build_profile(), using your first and last names 
# and three other key-value pairs that describe you .
print('-'*40)
def make_profile(first_name: str, last_name: str, **kwargs) -> None:
    print("User profile is:")
    print(f"\tFirst Name: {first_name}")
    print(f"\tLast Name: {last_name}")
    for key, value in kwargs:
        print(f"\t{key}: {value}")

# 8-14. Cars: Write a function that stores information about a car in a diction
# ary . The function should always receive a manufacturer and a model name . It 
# should then accept an arbitrary number of keyword arguments . Call the func
# tion with the required information and two other name-value pairs, such as a 
# color or an optional feature . Your function should work for a call like this one:
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# Print the dictionary that’s returned to make sure all the information was 
# stored correctly.
print('-'*40)
def car_function(manufacturer: str, model: str, **kwargs):
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in kwargs.items():
        car[key] = value

    return car

car = car_function('toyoto', 'innova', color='white', tow_package=True)
print(car)

# 8-15. Printing Models: Put the functions for the example print_models.py in a 
# separate file called printing_functions.py . Write an import statement at the top 
# of print_models.py, and modify the file to use the imported functions .
print('-'*40)

# 8-16. Imports: Using a program you wrote that has one function in it, store that 
# function in a separate file . Import the function into your main program file, and 
# call the function using each of these approaches:
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *
print('-'*40)

# 8-17. Styling Functions: Choose any three programs you wrote for this chapter, 
# and make sure they follow the styling guidelines described in this section.
print('-'*40)

