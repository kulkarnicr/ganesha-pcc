#Ganesha.
# Author Ganesha 18-November-2026
# This script covers Chapter 4 Working with Lists.

# 4-1. Pizzas: Think of at least three kinds of your favorite pizza . Store these 
# pizza names in a list, and then use a for loop to print the name of each pizza .
# •	Modify your for loop to print a sentence using the name of the pizza 
# instead of printing just the name of the pizza . For each pizza you should 
# have one line of output containing a simple statement like I like pepperoni 
# pizza .
# •	Add a line at the end of your program, outside the for loop, that states 
# how much you like pizza . The output should consist of three or more lines 
# about the kinds of pizza you like and then an additional sentence, such as 
# I really love pizza!
print('-'*40)
pizzas = ['cheese', 'tomato', 'chilli']
for pizza in pizzas:
    print(pizza)
for pizza in pizzas:
    print(f"I like {pizza} pizza.")
print("I really love pizza.")

# 4-2. Animals: Think of at least three different animals that have a common char
# acteristic . Store the names of these animals in a list, and then use a for loop to 
# print out the name of each animal .
# •	Modify your program to print a statement about each animal, such as 
# A dog would make a great pet.
# •	Add a line at the end of your program stating what these animals have in 
# common . You could print a sentence such as Any of these animals would 
# make a great pet
print('-'*40)
animals = ['dog', 'cat', 'tiger']
for animal in animals:
    print(animal)
for animal in animals:
    print(f"A {animal} would make a great pet.")
print("Any of these animals would make a great pet.")


# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, 
# inclusive .
print('-'*40)
print("Printing numbers from 1 to 20, inclusive.")
for i in range(1,21):
    print(i)

# 4-4. One Million: Make a list of the numbers from one to one million, and then 
# use a for loop to print the numbers . (If the output is taking too long, stop it by 
# pressing ctrl-C or by closing the output window .)
print('-'*40)
numbers = range(1, 1_000_001)
for number in numbers:
    print(number)

# 4-5. Summing a Million: Make a list of the numbers from one to one million, 
# and then use min() and max() to make sure your list actually starts at one and 
# ends at one million . Also, use the sum() function to see how quickly Python can 
# add a million numbers .
print('-'*40)
numbers = range(1, 1_000_001)
print(f"minimum is: {min(numbers)}")
print(f"maximum is: {max(numbers)}")
print(f"Sum is: {sum(numbers)}")

# 4-6. Odd Numbers: Use the third argument of the range() function to make a list 
# of the odd numbers from 1 to 20 . Use a for loop to print each number .
print('-'*40)
odds = range(1, 20, 2)
for odd in odds:
    print(odd)
    
# 4-7. Threes: Make a list of the multiples of 3 from 3 to 30 . Use a for loop to 
# print the numbers in your list .
print('-'*40)
threes = range(3,31,3)
for th in threes:
    print(th)

# 4-8. Cubes: A number raised to the third power is called a cube . For example, 
# the cube of 2 is written as 2**3 in Python . Make a list of the first 10 cubes (that 
# is, the cube of each integer from 1 through 10), and use a for loop to print out 
# the value of each cube .
print('-'*40)
cubes = []
for i in range(1,11):
    cubes.append(i**3)

for cube in cubes:
    print(cube)

# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the 
# first 10 cubes 
print('-'*40)
cubes = [i**3 for i in range(1,11)]

# 4-10. Slices: Using one of the programs you wrote in this chapter, add several 
# lines to the end of the program that do the following:
# •	Print the message, The first three items in the list are: . Then use a slice to 
# print the first three items from that program’s list .
# •	Print the message, Three items from the middle of the list are: . Use a slice 
# to print three items from the middle of the list .
# •	Print the message, The last three items in the list are: . Use a slice to print 
# the last three items in the list .
print('-'*40)
cubes = [i**3 for i in range(1,11)]
middle = len(cubes) // 2
low, high = middle-1, middle+2  # we skip last element hence middle+2

print(f"The first three items in the list are: {cubes[:3]}")
print(f"The first three items in the list are: {cubes[low:high]}")
print(f"The first three items in the list are: {cubes[-3:]}")

# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 
# (page 60) . Make a copy of the list of pizzas, and call it friend_pizzas . 
# Then, do the following:
# •	Add a new pizza to the original list .
# •	Add a different pizza to the list friend_pizzas .
# •	Prove that you have two separate lists . Print the message, My favorite 
# pizzas are:, and then use a for loop to print the first list . Print the message, 
# My friend’s favorite pizzas are:, and then use a for loop to print the sec
# ond list . Make sure each new pizza is stored in the appropriate list .
print('-'*40)
pizzas = ['malai', 'cheese', 'chilli']
friend_pizzas = pizzas[:]
pizzas.append('tomato')
friend_pizzas.append('mirchi')
print("My favourite pizzas are:")
for pizza in pizzas:
    print(f"\t{pizza}")
print("My friend's favourite pizzas are:")
for friend_pizza in friend_pizzas:
    print(f"\t{friend_pizza}")

# 4-12. More Loops: All versions of foods.py in this section have avoided using 
# for loops when printing to save space . Choose a version of foods.py, and 
# write two for loops to print each list of foods
print('-'*40)
my_foods = ['pizza', 'falafel', 'carrot cake']
print("Print foods using for loop and food item")
for food in my_foods:
    print(food)
print("Print foods using for loop and length")
for i in range(len(my_foods)):
    print(my_foods[i])
    
# 4-13. Buffet: A buffet-style restaurant offers only five basic foods . Think of five 
# simple foods, and store them in a tuple .
# •	Use a for loop to print each food the restaurant offers .
# •	Try to modify one of the items, and make sure that Python rejects the 
# change .
# •	The restaurant changes its menu, replacing two of the items with different 
# foods . Add a block of code that rewrites the tuple, and then use a for 
# loop to print each of the items on the revised menu 
print('-'*40)
tuple_simple_foods = ("dal", "roti", "rice", "sabji", "roti")
print("Our restaurant offers simple food like: ")
for food in tuple_simple_foods:
    print(food)
tuple_revised_foods = ("masalarice", "bundi", "ladu", "cake")
print("Revised food items are: ")
for food in tuple_revised_foods:
    print(food)
print("Trying to modify food item from tuple, should fail")
# deliberately commented below statment, it errors out as we're trying to modify tuple.
# tuple_simple_foods[0] = "varan" #editor color codes this statement hinting syntax error