# Ganesha
# Author Ganesha 18-November-2026
# This script covers dictionary.

# 6-1. Person: Use a dictionary to store information about a person you know . 
# Store their first name, last name, age, and the city in which they live . You 
# should have keys such as first_name, last_name, age, and city . Print each 
# piece of information stored in your dictionary .
print('-'*40)
person_1 = {
    'first_name': 'Ganesh',
    'last_name': 'Kailas',
    'age': float('inf'),
    'city': 'universe',
}
print(person_1['first_name'])
print(person_1['last_name'])
print(person_1['age'])
print(person_1['city'])

# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers . 
# Think of five names, and use them as keys in your dictionary . Think of a favorite 
# number for each person, and store each as a value in your dictionary . Print 
# each person’s name and their favorite number . For even more fun, poll a few 
# friends and get some actual data for your program .
print('-'*40)
fav_number = {
    'Ganesha': 7,
    'Hari': 4,
    'Vishnu': 5,
    'Shiva': 5,
    'Brahmadev': 9,
}
for person, number in fav_number.items():
    print(f"{person}'s favourite number is " +
          f"{number}")

# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary . 
# However, to avoid confusion, let’s call it a glossary .
# •	Think of five programming words you’ve learned about in the previous 
# chapters . Use these words as the keys in your glossary, and store their 
# meanings as values .
# •	Print each word and its meaning as neatly formatted output . You might 
# print the word followed by a colon and then its meaning, or print the word 
# on one line and then print its meaning indented on a second line . Use the 
# newline character (\n) to insert a blank line between each word-meaning 
# pair in your output.
print('-'*40)
#Ganesha.
glossary = {
    'list': 'a group or collection of items',
    'dictionary': 'key-value pair items',
    'slicing': 'a list operation that allows to extract portion of a list',
    'indexing': 'accessing list elements by their position',
    'for': 'this is a looping construct to iterate over list or dictionary items',
}
for word, meaning in glossary.items():
    print(f"\n{word}:\n\t{meaning}")
print(f"Total words in glossary are: {len(glossary)}")

# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean 
# up the code from Exercise 6-3 (page 102) by replacing your series of print 
# statements with a loop that runs through the dictionary’s keys and values . 
# When you’re sure that your loop works, add five more Python terms to your 
# glossary . When you run your program again, these new words and meanings 
# should automatically be included in the output .
print('-'*40)
print("Adding more words and meanings to glossary...")
glossary['if'] = 'conditional construct to execute a code portion if some condition holds true'
glossary['True'] = 'boolean truthy value'
glossary['False'] = 'boolean falsy value'
glossary['items'] = 'dictionary method to return key, value as pair'
glossary['del'] = 'keyword to delete an element from list or dictionary'
print("Adding done...now will print glossary again...this time it should print 10 items...")
count = 1
for word, meaning in glossary.items():
    print(f"\n({count}){word}:\n\t{meaning}")
    count += 1
print(f"Total words in glossary are: {len(glossary)}")

# 6-5. Rivers: Make a dictionary containing three major rivers and the country 
# each river runs through . One key-value pair might be 'nile': 'egypt' .
# •	Use a loop to print a sentence about each river, such as The Nile runs 
# through Egypt .
# •	Use a loop to print the name of each river included in the dictionary .
# •	Use a loop to print the name of each country included in the dictionary .
print('-'*40)
rivers = {
    'ganga': 'India',
    'sarswati': 'Asia',
    'nile': 'egypt'
}
print("printing rivers and countries (key, value)")
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()} .")
print("printing rivers (key)")
for river in rivers.keys():
    print(river)
print("printing countries (value)")
for country in rivers.values():
    print(country)

# 6-6. Polling: Use the code in favorite_languages.py (page 104) .
# •	Make a list of people who should take the favorite languages poll . Include 
# some names that are already in the dictionary and some that are not . 
# •	Loop through the list of people who should take the poll . If they have 
# already taken the poll, print a message thanking them for responding . 
# If they have not yet taken the poll, print a message inviting them to take 
# the poll.
print('-'*40)
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
people = ['alex', 'bob', 'phil', 'alice', 'edward']
for person in people:
    if person in favorite_languages:
        print(f"{person}, thank you for taking poll.")
    else:
        print(f"{person}, request you to take poll.")

# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 102) . 
# Make two new dictionaries representing different people, and store all three 
# dictionaries in a list called people . Loop through your list of people . As you 
# loop through the list, print everything you know about each person 
print('-'*40)
person_2 = {
    'first_name': 'ShriHari',
    'last_name': 'Ultimate',
    'age': float('inf'),
    'city': 'Vaikunthdham',
}
person_3 = {
    'first_name': 'Narayan',
    'last_name': 'Ultimate God',
    'age': float('inf'),
    'city': 'Sagar',
}
people = [person_1, person_2, person_3]
for person in people:
    print(person['first_name'])
    print(person['last_name'])
    print(person['age'])
    print(person['city'])
    print("===")

# 6-8. Pets: Make several dictionaries, where the name of each dictionary is the 
# name of a pet . In each dictionary, include the kind of animal and the owner’s 
# name . Store these dictionaries in a list called pets . Next, loop through your list 
# and as you do print everything you know about each pet .
print('-'*40)
tom = {'type': 'dog', 'owner': 'jessy'}
mew = {'type': 'cat', 'owner': 'manimau'}
pets = [tom, mew]
for pet in pets:
    print(f"\n{pet['type']}'s owner is {pet['owner']}.")

# 6-9. Favorite Places: Make a dictionary called favorite_places . Think of three 
# names to use as keys in the dictionary, and store one to three favorite places 
# for each person . To make this exercise a bit more interesting, ask some friends 
# to name a few of their favorite places . Loop through the dictionary, and print 
# each person’s name and their favorite places .
print('-'*40)
#Ganesha.
favorite_places = {}
favorite_places['Ganesha'] = ['Kailas', 'Vaikunth']
favorite_places['Hari'] = ['BhaktaHridy', 'Vaikunthdham', 'Sarvatra']
favorite_places['Shiva'] = ['Kailas', 'HariHridya']
for person, places in favorite_places.items():
    print(f"\nGod {person} places are:")
    for place in places:
        print(f"\t{place}")
    print("===")

# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so 
# each person can have more than one favorite number . Then print each person’s 
# name along with their favorite numbers .
print('-'*40)
print('-'*40)
fav_numbers = {
    'Ganesha': [7, 77],
    'Hari': [4, 44],
    'Vishnu': [5, 55],
    'Shiva': [5, 55],
    'Brahmadev': [9, 99],
}
for person, numbers in fav_numbers.items():
    print(f"{person}'s favourite numbers are:")
    for number in numbers:
        print(f"\t{number}")
    print("===")

# 6-11. Cities: Make a dictionary called cities . Use the names of three cities as 
# keys in your dictionary . Create a dictionary of information about each city and 
# include the country that the city is in, its approximate population, and one fact 
# about that city . The keys for each city’s dictionary should be something like 
# country, population, and fact . Print the name of each city and all of the infor
# mation you have stored about it .
print('-'*40)
cities = {
    'pune': {
        'country': 'India',
        'population': 12466,
        'fact': 'city of education',
    },
    'newyork': {
        'country': 'US',
        'population': 412466,
        'fact': 'city of buildings',        
    },
    'tokiyo': {
        'country': 'Japan',
        'population': 5612466,
        'fact': 'city of work',        
    },
}
for city, info in cities.items():
    print(f"{city} info:")
    for key, value in info.items():
        print(f"\t{key}: {value}")
    print("===")

# 6-12. Extensions: We’re now working with examples that are complex enough 
# that they can be extended in any number of ways . Use one of the example pro
# grams from this chapter, and extend it by adding new keys and values, chang
# ing the context of the program or improving the formatting of the output . 
print('-'*40)
print("I'm passing this program...")