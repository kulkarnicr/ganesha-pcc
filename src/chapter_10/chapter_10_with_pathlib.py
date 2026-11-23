# Ganesha
# Script for file operations.
# Author Ganesha 23-November-2026

'''
Ganesha

basically this script uses pathlib/Path for file operations
instead of "with open()..." context manager

json:

this has loads/dumps (str related) and load/dump (file related methods)
basically we try to convert python object to string/file

load(s) - string/file to pythonobj
dump(s) - pythonobj to string/file

1) Path(xxxx).read_text() -> json.loads() -> python-obj
2) dictionary/list -> json.dumps(<python-obj>) -> Path(xxxx).write_text()

'''


import sys
import time
import json
#using pathlib/Path for verification like reading file contents which we try with/open
from pathlib import Path
'''
# 10-1. Learning Python: Open a blank file in your text editor and write a few lines 
# summarizing what you’ve learned about Python so far. Start each line with the 
# phrase In Python you can. . . . Save the file as learning_python.txt in the same 
# directory as your exercises from this chapter. Write a program that reads the file 
# and prints what you wrote two times: print the contents once by reading in the 
# entire file, and once by storing the lines in a list and then looping over each line.
#Ganesha.
print('-'*40)
filename = './learning_python.txt'
path = Path(filename)
print("~~~ 1 read whole contents ~~~")
print( path.read_text().rstrip() )
print("~~~ 2 read by storing lines in a list ~~~")
contents = path.read_text().splitlines()
for index, line in enumerate(contents):
    print(f"{index}: {line}")
# sys.exit(0)

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
#Ganesha.
path = Path(filename)
contents = path.read_text().splitlines()
for index, line in enumerate(contents):
    print(f"{index}: {line}")
    line_lc = line.lower()
    line_lc_replaced = line_lc.replace('python', 'C') if 'python' in line_lc else "NO CHANGE"
    print(f"{index}: {line_lc_replaced}")
# sys.exit()

# 10-4. Guest: Write a program that prompts the user for their name. When they 
# respond, write their name to a file called guest.txt.
print('-'*40)
print("~~~~ 10-4. Guest")
#Ganesha.
user_name = input("Name please ")
Path('guests_pathlib.txt').write_text(user_name)

# 10-5. Guest Book: Write a while loop that prompts users for their name. Collect 
# all the names that are entered, and then write these names to a file called 
# guest_book.txt. Make sure each entry appears on a new line in the file.
print('-'*40)
print("~~~~ 10-5. Guest Book ~~~")
#Ganesha.
filename = './guest_book_pathlib.txt'
usernames = []
while True: #break condition - username='quit'
    username = input("Name please ")
    if username == 'quit':
        break
    usernames.append(username)
if usernames:
    usernames_string = ''
    for username in usernames:
        usernames_string += f"{username}\n"
    Path(filename).write_text(usernames_string)
sys.exit()

#Ganesha.
# 10-6. Addition: One common problem when prompting for numerical input 
# occurs when people provide text instead of numbers. When you try to convert 
# the input to an int, you’ll get a ValueError. Write a program that prompts for 
# two numbers. Add them together and print the result. Catch the ValueError if 
# either input value is not a number, and print a friendly error message. Test your 
# program by entering two numbers and then by entering some text instead of a 
# number.
print('-'*40)
print("~~~~ X ~~~")
#Ganesha.
try:
    num1 = int(input("Enter number1 "))
    num2 = int(input("Enter number2 "))
except ValueError:
    #Ganesha.
    print(f"Please ensure to enter number as integer.")
else:
    print(f"Addition {num1 + num2}")

# 10-7. Addition Calculator: Wrap your code from Exercise 10-5 in a while loop 
# so the user can continue entering numbers, even if they make a mistake and 
# enter text instead of a number.
print('-'*40)
print("~~~~ X ~~~")
#Ganesha.
while True:
    try:
        num1 = int(input("Enter number1 "))
        num2 = int(input("Enter number2 "))
    except ValueError:
        #Ganesha.
        print(f"Please ensure to enter number as integer.")
    else:
        print(f"Addition {num1 + num2}")
        break

# 10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three 
# names of cats in the first file and three names of dogs in the second file. Write 
# a program that tries to read these files and print the contents of the file to the 
# screen. Wrap your code in a try-except block to catch the FileNotFound error, 
# and print a friendly message if a file is missing. Move one of the files to a dif
# ferent location on your system, and make sure the code in the except block 
# executes properly.
print('-'*40)
print("~~~~ X ~~~")
print("[Step 1]: creating cats and dogs file")
cats_string = "chi\nchu\ncha"
dogs_string = "tom\nbom\nkom"
Path('cats.txt').write_text(cats_string)
Path('dogs.txt').write_text(dogs_string)
print("[Step 2]: reading cats and dogs file when files exist")
try:
    print("[Step 2-1]...reading cats.txt...")
    Path('cats.txt').read_text()
    print("[Step 2-2]...reading dogs.txt...")
    Path('dogs.txt').read_text()
except FileNotFoundError:
    print("Looks file does not exist")
print("[Step 3]: reading cats and dogs file when files DO NOT exist")
print("[Step 3-1]:...moving cats.txt to cats.txt.renamed...")
import shutil
shutil.move('cats.txt', 'cats.txt.renamed')
print("[Step 3-2]:...trying to read non existing file cats.txt (catch exception)...")
try:
    Path('cats.txt').read_text()
except FileNotFoundError:
    print("looks file cats.txt non existing")
print("[Step 3-3]...bring back cats.txt and then read...")
shutil.move('cats.txt.renamed', 'cats.txt')
try:
    Path('cats.txt').read_text()
except FileNotFoundError:
    print('oops, still error')

# 10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-7 to fail 
# silently if either file is missing.
print('-'*40)
print("~~~~ X ~~~")
print("There is just writing pass in except block for this exercise.")

# 10-10. Common Words: Visit Project Gutenberg (https://gutenberg.org ) and find 
# a few texts you’d like to analyze. Download the text files for these works, or 
# copy the raw text from your browser into a text file on your computer.
# You can use the count() method to find out how many times a word or 
# phrase appears in a string. For example, the following code counts the number 
# of times 'row' appears in a string:
# >>> line = "Row, row, row your boat"
# >>> line.count('row')
# 2
# >>> line.lower().count('row')
# 3
# Notice that converting the string to lowercase using lower() catches all 
# appearances of the word you’re looking for, regardless of how it’s formatted.
# Write a program that reads the files you found at Project Gutenberg and 
# determines how many times the word 'the' appears in each text. This will be 
# an approximation because it will also count words such as 'then' and 'there'. 
# Try counting 'the ', with a space in the string, and see how much lower your 
# count is.
print('-'*40)
print("~~~~ X ~~~")
#Ganesha.
#gutenberg.org website was down...so i will try to generate file..and then read
import string
import random

print("=== CREATE FILE ===")
# letters = [c for c in string.ascii_letters]
letters = ['t', 'h', 'e', 'T', 'H', 'E']
print(letters)

#generate word of random length (2-5)
#keep appending it to a string
#write this string to a file
#iterate above for sufficient times to see few "the" words generate
expected_total_the = 0
word = ''
for i in range(100_00):
    word_length = random.randint(2, 5)
    random_word = ''
    for _ in range(word_length):
        random_word += random.choice(letters)
    if random_word.lower() == 'the':
        expected_total_the += 1
    word += f"{random_word} "
    # add newline every alternate 10 words
    if i % 10 == 0:
        word += "\n"
Path('literature.txt').write_text(word)

print("=== READ FILE ===")
contents = Path('literature.txt').read_text()
actual_total_the = contents.lower().count('the')
print(f"Expected: {expected_total_the}")
print(f"Actual  : {actual_total_the}")

sys.exit()

#Ganesha.
#Ganesha.
# 10-11. Favorite Number: Write a program that prompts for the user’s favorite 
# number . Use json.dump() to store this number in a file . Write a separate pro
# gram that reads in this value and prints the message, “I know your favorite 
# number! It’s _____ .”
print('-'*40)
print("~~~~ X ~~~")
import json
filename = 'pro1011.json'
while True:
    try:
        number = int(input("Favorite number "))
    except ValueError:
        print("Number should be integer")
    else:
        print(f"WRITE: {number}")
        with open(filename, 'w') as f:
            json.dump(number, f)
        break
with open(filename) as fread:
    data = json.load(fread)
print(f"READ: {data}")

# 10-12. Favorite Number Remembered: Combine the two programs from 
# Exercise 10-11 into one file . If the number is already stored, report the favorite 
# number to the user . If not, prompt for the user’s favorite number and store it in a 
# file . Run the program twice to see that it works .
print('-'*40)
print("~~~~ X ~~~")
filename = 'pro1012.json'
def get_stored_number():
    """Return number stored in a json file, otherwise None"""
    if Path(filename).exists():
        contents = Path(filename).read_text()
        number = json.loads(contents)
        return number
    else:
        return None


def ask_number_and_store_in_file():
    """Get number from user and save"""
    while True:
        try:
            number = int(input("Number please "))
        except ValueError:
            print("Number should be integer")
        else:
            print(f"[WRITE] {number}")
            with open(filename, 'w') as fwrite:
                json.dump(str(number), fwrite)
            break

def get_number():
    if Path(filename).exists():
        number = get_stored_number()
        print(f"[READ] {number}")
    else:
        print( ask_number_and_store_in_file() )

#ensure file does not exist
Path(filename).unlink(missing_ok=True)

#call first time
get_number()
get_number()
'''

# 10-13. User Dictionary: The remember_me.py example only stores one piece of 
# information, the username. Expand this example by asking for two more pieces 
# of information about the user, then store all the information you collect in a 
# dictionary. Write this dictionary to a file using json.dumps(), and read it back 
# in using json.loads(). Print a summary showing exactly what your program 
# remembers about the user.
print('-'*40)
print("~~~~ X ~~~")
#Ganesha.
filename = 'prog1013.json'
data = {}

print(f"[STEP-1] collect user info and save to file {filename}")
try:
    user_name = input("  Name ")
    age = int(input("  Age "))
    height = int(input("  Height "))
except ValueError:
    print("Please ensure to enter age and height as integer.")
else:
    data['user_name'] = user_name
    data['age'] = age
    data['height'] = height
    contents = json.dumps(data, indent=4)
    Path(filename).write_text(contents)

print(f"[STEP-2] Read back user info from file {filename}")
rcontents = Path(filename).read_text()
rdata = json.loads(rcontents)

print(f"[STEP-3] printing")
for attr, value in rdata.items():
    print(f"  {attr:<10}: {value}")

# 10-14. Verify User: The final listing for remember_me.py assumes either that the 
# user has already entered their username or that the program is running for the 
# first time . We should modify it in case the current user is not the person who 
# last used the program .
# Before printing a welcome back message in greet_user(), ask the user if 
# this is the correct username . If it’s not, call get_new_username() to get the correct 
# username
print('-'*40)
print("~~~~ X ~~~")
print("this is minor-change-not-redoing.")