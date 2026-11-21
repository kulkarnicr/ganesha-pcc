# Ganesha

# 5-1. Conditional Tests: Write a series of conditional tests . Print a statement 
# describing each test and your prediction for the results of each test . Your code 
# should look something like this:
# ----------------------------------------------------------
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')
# ----------------------------------------------------------
# •	Look closely at your results, and make sure you understand why each line 
# evaluates to True or False .
# •	Create at least 10 tests . Have at least 5 tests evaluate to True and another 
# 5 tests evaluate to False .
print('-'*40)
num1 = 10
num2 = 20
num3 = 30
print(f"### num1: {num1}, num2: {num2}, num3: {num3} ###")

print("Is num1 == 10? I predict True.")
print(num1 == 10)

print("Is num1 <= num2? I predict True.")
print(num1 <= num2)

print("Is num1 >= num2? I predict False.")
print(num1 >= num2)

print("Is num1 == num3? I predict False.")
print(num1 == num3)

print("Is num1 < num2? I predict True.")
print(num1 < num2)

print("Is num1 > num2? I predict False.")
print(num1 > num2)

print("Is num1 != num2? I predict True.")
print(num1 != num2)

print("Is num1 != num3? I predict True.")
print(num1 != num3)

print("Is num1 > num3? I predict False.")
print(num1 > num3)

print("Is num1 == 0? I predict False.")
print(num1 == 0)

print("Is num1 == 100? I predict False.")
print(num1 == 100)

# 5-2. More Conditional Tests: You don’t have to limit the number of tests you 
# create to 10 . If you want to try more comparisons, write more tests and add 
# them to conditional_tests.py . Have at least one True and one False result for 
# each of the following:
# •	Tests for equality and inequality with strings
# •	Tests using the lower() function
# •	Numerical tests involving equality and inequality, greater than and 
# less than, greater than or equal to, and less than or equal to
# •	Tests using the and keyword and the or keyword
# •	Test whether an item is in a list
# •	Test whether an item is not in a list
print('-'*40)
str1 = "Ganesha"
str2 = "ganesha"
print(f"### str1: {str1}, str2: {str2} ###")
print("Is str1 == str2? I predict False.")
print(str1 == str2)

print("Is str1 != str2? I predict True.")
print(str1 != str2)

print("Is str1.lower() == str2? I predict True.")
print(str1.lower() == str2)

mylist = ["Ganesha", "Bappa", "Morya"]
print("Is Ganesha in mylist? I predict True")
print("Ganesha" in mylist)

print("Is ganesha in mylist? I predict True")
print("ganesha" in mylist)

print('Is str1 == "Ganesha" and str2 == "ganesha"? I predict True')
print(str1 == "Ganesha" and str2 == "ganesha")

print('Is str1 != "Ganesha" or str2 == "ganesha"? I predict True')
print(str1 != "Ganesha" or str2 == "ganesha")

# 5-3. Alien Colors #1: Imagine an alien was just shot down in a game . Create a 
# variable called alien_color and assign it a value of 'green', 'yellow', or 'red' .
# •	Write an if statement to test whether the alien’s color is green . If it is, print 
# a message that the player just earned 5 points .
# •	Write one version of this program that passes the if test and another that 
# fails . (The version that fails will have no output .)
print('-'*40)
alien_color = 'green'
print(f'alien_color is {alien_color}. If color is green, player gets 5 points, otherwise no.')
if alien_color == 'green':
    print('Player has earned 5 points.')
alien_color = 'yellow'
print(f'alien_color is {alien_color}. If color is green, player gets 5 points, otherwise no.')
if alien_color == 'green':
    print('Player has earned 5 points.')

# 5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and 
# write an if-else chain .
# •	If the alien’s color is green, print a statement that the player just earned 
# 5 points for shooting the alien .
# •	If the alien’s color isn’t green, print a statement that the player just earned 
# 10 points .
# •	Write one version of this program that runs the if block and another that 
# runs the else block
print('-'*40)
alien_color = 'yellow'
print(f'alien_color is {alien_color}. If color is green, player gets 5 points, otherwise 10 points.')
if alien_color == 'green':
    print('Player has earned 5 points.')
else:
    print('Player has earned 10 points.')

alien_color = 'yellow'
if alien_color == 'green':
    print('Player has earned 5 points.')
if alien_color != 'green':
    print('Player has earned 10 points.')


# 5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif
# else chain .
# •	If the alien is green, print a message that the player earned 5 points .
# •	If the alien is yellow, print a message that the player earned 10 points .
# •	If the alien is red, print a message that the player earned 15 points .
# •	Write three versions of this program, making sure each message is printed 
# for the appropriate color alien .
print('-'*40)
print('Points earning based on alien color. green=5, yellow=10, red=15.')
possible_alien_colors = ['green', 'yellow', 'red', 'black']
for alien_color in possible_alien_colors:
    if alien_color == 'green':
        print(f'color is {alien_color}, so Player earned 5 points')
    elif alien_color == 'yellow':
        print(f'color is {alien_color}, so Player earned 10 points')
    elif alien_color == 'red':
        print(f'color is {alien_color}, so Player earned 15 points')
    else:
        print(f'wrong color value {alien_color}, so no points.')

# 5-6. Stages of Life: Write an if-elif-else chain that determines a person’s 
# stage of life . Set a value for the variable age, and then:
# •	If the person is less than 2 years old, print a message that the person is 
# a baby .
# •	If the person is at least 2 years old but less than 4, print a message that 
# the person is a toddler .
# •	If the person is at least 4 years old but less than 13, print a message that 
# the person is a kid .
# •	If the person is at least 13 years old but less than 20, print a message that 
# the person is a teenager .
# •	If the person is at least 20 years old but less than 65, print a message that 
# the person is an adult .
# •	If the person is age 65 or older, print a message that the person is an 
# elder .
print('-'*40)
possible_ages = [1, 3, 12, 20, 65, 78]
for age in possible_ages:
    if age < 2:
        print(f'person age is {age}, hence person is baby')
    elif age < 4:
        print(f'person age is {age}, hence person is baby')
    elif age < 13:
        print(f'person age is {age}, hence person is baby')
    elif age < 20:
        print(f'person age is {age}, hence person is baby')
    elif age < 65:
        print(f'person age is {age}, hence person is baby')
    elif age >= 65:
        print(f'person age is {age}, hence person is baby')
    else:
        print(f'invalid value for {age}, hence person stage of life can not be determined'
               'as baby/kid/toddler/teenager/adult/elder.')
        
# 5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of 
# independent if statements that check for certain fruits in your list .
# •	Make a list of your three favorite fruits and call it favorite_fruits .
# •	Write five if statements . Each should check whether a certain kind of fruit 
# is in your list . If the fruit is in your list, the if block should print a statement, 
# such as You really like bananas.
print('-'*40)
favorite_fruits = ["mango", "guava", "apple"]
testing_fruits = ["bananas", "grapes"] + favorite_fruits
for testing_fruit in testing_fruits:
    if testing_fruit in favorite_fruits:
        print(f"You really like {testing_fruit}!")
    else:
        print(f"Nope, you do not like {testing_fruit}.")

# 5-8. Hello Admin: Make a list of five or more usernames, including the name 
# 'admin' . Imagine you are writing code that will print a greeting to each user 
# after they log in to a website . Loop through the list, and print a greeting to 
# each user:
# •	If the username is 'admin', print a special greeting, such as Hello admin, 
# would you like to see a status report?
# •	Otherwise, print a generic greeting, such as Hello Eric, thank you for log
# ging in again.
print('-'*40)
#Ganesha.
usernames = ['Ganesha', 'Bappa', 'Morya', 'admin', 'juggler']
for username in usernames:
    if username == 'admin':
        print(f"Hello {username}, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")

# 5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is 
# not empty .
# •	If the list is empty, print the message We need to find some users!
# •	Remove all of the usernames from your list, and make sure the correct 
# message is printed .
print('-'*40)
usernames = []
if not usernames:
    print('Please note usernames list is empty. Please add few usernames before proceeding.')
else:
    for username in usernames:
        pass

# 5-10. Checking Usernames: Do the following to create a program that simulates 
# how websites ensure that everyone has a unique username .
# •	Make a list of five or more usernames called current_users .
# •	Make another list of five usernames called new_users . Make sure one or 
# two of the new usernames are also in the current_users list .
# •	Loop through the new_users list to see if each new username has already 
# been used . If it has, print a message that the person will need to enter a 
# new username . If a username has not been used, print a message saying 
# that the username is available .
# •	Make sure your comparison is case insensitive . If 'John' has been used, 
# 'JOHN' should not be accepted .
print('-'*40)
current_users = ["Ganesha", "Bappa", "Morya", "Agnidev", "Vayudev"]
new_users = ["Indradev", "jaldev", "Vayudev", "Agnidev", "Brahma"]
current_users_lc = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lc:
        print(f"this username {new_user} is already taken, please enter a new username")
    else:
        print(f"Welcome username {new_user}, this is available.")

# 5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such 
# as 1st or 2nd . Most ordinal numbers end in th, except 1, 2, and 3 .
# •	Store the numbers 1 through 9 in a list .
# •	Loop through the list .
# •	Use an if-elif-else chain inside the loop to print the proper ordinal end
# ing for each number . Your output should read "1st 2nd 3rd 4th 5th 6th 
# 7th 8th 9th", and each result should be on a separate line 
print('-'*40)
#Ganesha.
for number in range(1,10):
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")