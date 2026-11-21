# Ganesha
# Author Ganesha 18-November-2026
# This script covers Input.

# 7-1. Rental Car: Write a program that asks the user what kind of rental car they 
# would like . Print a message about that car, such as “Let me see if I can find you 
# a Subaru .”
print('-'*40)
car = input("Hi Customer, please tell car type? ")
print(f"Let me see if I can find you a {car}")

# 7-2. Restaurant Seating: Write a program that asks the user how many people 
# are in their dinner group . If the answer is more than eight, print a message say
# ing they’ll have to wait for a table . Otherwise, report that their table is ready .
print('-'*40)
#Ganesha.
total = input("How many people dinner group? ")
total = int(total)
if total > 8:
    print("Please wait.")
else:
    print("Table ready.")

# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the 
# number is a multiple of 10 or not 
print('-'*40)
number = input("Number Please: ")
number = int(number)
remainder = number % 10
if remainder == 0:
    print(f"{number} is multiple of 10.")
else:
    print(f"{number} is not multiple of 10.")

# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of 
# pizza toppings until they enter a 'quit' value . As they enter each topping, 
# print a message saying you’ll add that topping to their pizza .
print('-'*40)
topping = ''
while topping != 'quit':
    print("\nEnter topping ('quit' to exit): ")
    if topping == 'quit':
        break
    else:
        print(f"Will add {topping} pizza.")

# 7-5. Movie Tickets: A movie theater charges different ticket prices depending on 
# a person’s age . If a person is under the age of 3, the ticket is free; if they are 
# between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is 
# $15 . Write a loop in which you ask users their age, and then tell them the cost 
# of their movie ticket.
print('-'*40)
age = ''
while age != 'quit':
    age = input("Enter age: ")
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print(f"age is {age}, ticket is free.")
    elif 3 <= age < 12:
        print(f"age is {age}, ticket is $10.")
    elif age >= 12:
        print(f"age is {age}, ticket is $15.")

# 7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5 
# that do each of the following at least once:
# •	Use a conditional test in the while statement to stop the loop .
# •	Use an active variable to control how long the loop runs .
# •	Use a break statement to exit the loop when the user enters a 'quit' value .
print('-'*40)
active = True
while active:
    age = input("Enter age: ")
    if age == 'quit':
        active = False
    else:
        age = int(age)
        if age < 3:
            print(f"age is {age}, ticket is free.")
        elif 3 <= age < 12:
            print(f"age is {age}, ticket is $10.")
        elif age >= 12:
            print(f"age is {age}, ticket is $15.")
        
# 7-7. Infinity: Write a loop that never ends, and run it . (To end the loop, press 
# ctrl-C or close the window displaying the output .)
print('-'*40)
print("This is infinite loop test" +
      "\nTo simulate in progress, I'm printing dot(..) characters alternate seconds.")
import time
while True:
    print('..', end='', sep='')
    time.sleep(2)
    
# 7-8. Deli: Make a list called sandwich_orders and fill it with the names of vari
# ous sandwiches . Then make an empty list called finished_sandwiches . Loop 
# through the list of sandwich orders and print a message for each order, such 
# as I made your tuna sandwich. As each sandwich is made, move it to the list 
# of finished sandwiches . After all the sandwiches have been made, print a 
# message listing each sandwich that was made .
# in finished_sandwiches .
print('-'*40)
sandwich_orders = ['cheese', 'corn', 'pepper', 'plain', 'vanil']
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"{sandwich} order done")
    finished_sandwiches.append(sandwich)
print("Each sandwich finish")

# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure 
# the sandwich 'pastrami' appears in the list at least three times . Add code 
# near the beginning of your program to print a message saying the deli has 
# run out of pastrami, and then use a while loop to remove all occurrences of 
# 'pastrami' from sandwich_orders . Make sure no pastrami sandwiches end up 
print('-'*40)

# 7-10. Dream Vacation: Write a program that polls users about their dream 
# vacation . Write a prompt similar to If you could visit one place in the world, 
# where would you go? Include a block of code that prints the results of the poll.
print('-'*40)

