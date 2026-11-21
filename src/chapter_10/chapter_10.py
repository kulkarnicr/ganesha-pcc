# Ganesha
# Script for file operations.
# Author Ganesha 20-November-2026

import time
#using pathlib/Path for verification like reading file contents which we try with/open
from pathlib import Path

# 10-1. Learning Python: Open a blank file in your text editor and write a few 
# lines summarizing what you’ve learned about Python so far . Start each line 
# with the phrase In Python you can... . Save the file as learning_python.txt in the 
# same directory as your exercises from this chapter . Write a program that reads 
# the file and prints what you wrote three times . Print the contents once by read
# ing in the entire file, once by looping over the file object, and once by storing 
# the lines in a list and then working with them outside the with block .
print('-'*40)
filename = './learning_python.txt'

#read entire file
print("---------#read entire file-----------")
with open(filename, 'r') as f:
    data = f.read()
print(f"\nFile contents are:---\n{data}")

#read by looping over file object
print("---------#read by looping over file object-----------")
with open(filename, 'r') as f:
    for line in f:
        #removing ending newline with rstrip()
        print(line.rstrip())
        
#read by storing lines in a list and then working with them outside the with block
print("---------#read by storing lines in a list and then working with them outside the with block-----------")
with open(filename, 'r') as f:
    lines = f.readlines()
for line in lines:
    print(line.rstrip())

# 10-2. Learning C: You can use the replace() method to replace any word in a 
# string with a different word . Here’s a quick example showing how to replace 
# 'dog' with 'cat' in a sentence:
# >>> message = "I really like dogs." 
# >>> message.replace('dog', 'cat') 
# 'I really like cats.' 
# Read in each line from the file you just created, learning_python.txt, and 
# replace the word Python with the name of another language, such as C . Print 
# each modified line to the screen 
print('-'*40)
print("~~~ display lines having python word replaced it with c ~~~")
with open(filename, 'r') as f:
    for line in f:
        if 'python' in line.lower():
            print( line.lower().replace('python', 'C').rstrip() )

# 10-3. Guest: Write a program that prompts the user for their name . When they 
# respond, write their name to a file called guest.txt .
print('-'*40)
print("~~~~ 10-3. Guest ~~~")
username = input("Name please ")
filename = 'guest.txt'
with open(filename, 'w') as f:
    f.write(username)
print("[VERIFICATION]...start")
print( Path(filename).read_text() )
print("[VERIFICATION]...comple")

# 10-4. Guest Book: Write a while loop that prompts users for their name . When 
# they enter their name, print a greeting to the screen and add a line recording 
# their visit in a file called guest_book.txt . Make sure each entry appears on a 
# new line in the file .
print('-'*40)
print("~~~~ 10-4. Guest Book ~~~")
filename = 'guest_book.txt'
username = ''
with open(filename, 'w') as f:
    while username != 'quit':
        username = input("Enter username (to quit write 'quit'): ")
        if username != 'quit':
            f.write(username + "\n")
print("[VERIFICATION]...start")
print( Path(filename).read_text() )
print("[VERIFICATION]...comple")
time.sleep(5)

# 10-5. Programming Poll: Write a while loop that asks people why they like 
# programming . Each time someone enters a reason, add their reason to a file 
# that stores all the responses 
print('-'*40)
print("~~~~ 10-5. Programming Poll ~~~")
#Ganesha.
filename = 'reasons.txt'
reason = ''
with open(filename, 'w') as f:
    while reason != 'quit':
        reason = input("Please tell why do you like programming? ")
        if reason != 'quit':
            f.write(reason+"\n")
print("[VERIFICATION]...start")
print( Path(filename).read_text() )
print("[VERIFICATION]...comple")
time.sleep(5)

#Ganesha.
# 10-6. Addition: One common problem when prompting for numerical input 
# occurs when people provide text instead of numbers . When you try to convert 
# the input to an int, you’ll get a TypeError . Write a program that prompts for 
# two numbers . Add them together and print the result . Catch the TypeError if 
# either input value is not a number, and print a friendly error message . Test your 
# program by entering two numbers and then by entering some text instead of a 
# number 
print('-'*40)
print("~~~~ X ~~~")

# 10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop 
# so the user can continue entering numbers even if they make a mistake and 
# enter text instead of a number .
print('-'*40)
print("~~~~ X ~~~")

# 10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt . Store at least three 
# names of cats in the first file and three names of dogs in the second file . Write 
# a program that tries to read these files and print the contents of the file to the 
# screen . Wrap your code in a try-except block to catch the FileNotFound error, 
# and print a friendly message if a file is missing . Move one of the files to a dif
# ferent location on your system, and make sure the code in the except block 
# executes properly .
print('-'*40)
print("~~~~ X ~~~")

# 10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail 
# silently if either file is missing .
# 10-10. Common Words: Visit Project Gutenberg (http://gutenberg.org/ ) 
# and find a few texts you’d like to analyze . Download the text files for these 
# works, or copy the raw text from your browser into a text file on your 
# computer .
# You can use the count() method to find out how many times a word or 
# phrase appears in a string . For example, the following code counts the number 
# of times 'row' appears in a string:
# >>> line = "Row, row, row your boat" 
# >>> line.count('row') 
# 2 
# >>> line.lower().count('row')
# 3 
# Notice that converting the string to lowercase using lower() catches 
# all appearances of the word you’re looking for, regardless of how it’s 
# formatted .
# Write a program that reads the files you found at Project Gutenberg and 
# determines how many times the word 'the' appears in each text 
print('-'*40)
print("~~~~ X ~~~")

# 10-11. Favorite Number: Write a program that prompts for the user’s favorite 
# number . Use json.dump() to store this number in a file . Write a separate pro
# gram that reads in this value and prints the message, “I know your favorite 
# number! It’s _____ .”
print('-'*40)
print("~~~~ X ~~~")

# 10-12. Favorite Number Remembered: Combine the two programs from 
# Exercise 10-11 into one file . If the number is already stored, report the favorite 
# number to the user . If not, prompt for the user’s favorite number and store it in a 
# file . Run the program twice to see that it works .
print('-'*40)
print("~~~~ X ~~~")

# 10-13. Verify User: The final listing for remember_me.py assumes either that the 
# user has already entered their username or that the program is running for the 
# first time . We should modify it in case the current user is not the person who 
# last used the program .
# Before printing a welcome back message in greet_user(), ask the user if 
# this is the correct username . If it’s not, call get_new_username() to get the correct 
# username
print('-'*40)
print("~~~~ X ~~~")
