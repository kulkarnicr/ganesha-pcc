# Ganesha
# Author: Ganesha 18-November-2026
# Script covers chapter 3 Introducing Lists.

# Try these short programs to get some firsthand experience with Python’s lists . 
# You might want to create a new folder for each chapter’s exercises to keep 
# them organized .
# 3-1. Names: Store the names of a few of your friends in a list called names . Print 
# each person’s name by accessing each element in the list, one at a time .
print('-'*40)
names = ['Ganesha', 'Vishnu', 'Shiv', 'Hari']
print(names[0])
print(names[1])
print(names[2])
print(names[3])

# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just 
# printing each person’s name, print a message to them . The text of each mes
# sage should be the same, but each message should be personalized with the 
# person’s name .
print('-'*40)
for name in names:
    print(f"Bowing to Prabhu {name}.")

# 3-3. Your Own List: Think of your favorite mode of transportation, such as a 
# motorcycle or a car, and make a list that stores several examples . Use your list 
# to print a series of statements about these items, such as “I would like to own a 
# Honda motorcycle .
print('-'*40)
modes = ['car', 'motorcycle']
for mode in modes:
    print(f"I would like to own a {mode}.")

# The following exercises are a bit more complex than those in Chapter 2, but 
# they give you an opportunity to use lists in all of the ways described .
# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who 
# would you invite? Make a list that includes at least three people you’d like to 
# invite to dinner . Then use your list to print a message to each person, inviting 
# them to dinner .
print('-'*40)
guests = ["aai", "aaji", "sitamata", "ram", "hanuman"]
for guest in guests:
    print(f"Hey {guest}, please come to dinner.")

# 3-5. Changing Guest List: You just heard that one of your guests can’t make the 
# dinner, so you need to send out a new set of invitations . You’ll have to think of 
# someone else to invite .
# •	Start with your program from Exercise 3-4 . Add a print statement at the 
# end of your program stating the name of the guest who can’t make it .
# •	Modify your list, replacing the name of the guest who can’t make it with 
# the name of the new person you are inviting .
# •	Print a second set of invitation messages, one for each person who is still 
# in your list .
print('-'*40)
print(f"guests[1] can't make dinner.")
guests[1] = "Bappa"
for guest in guests:
    print(f"{guest}, please come for dinner.")

# 3-6. More Guests: You just found a bigger dinner table, so now more space is 
# available . Think of three more guests to invite to dinner .
# •	Start with your program from Exercise 3-4 or Exercise 3-5 . Add a print 
# statement to the end of your program informing people that you found a 
# bigger dinner table .
# •	Use insert() to add one new guest to the beginning of your list .
# •	Use insert() to add one new guest to the middle of your list .
# •	Use append() to add one new guest to the end of your list .
# •	Print a new set of invitation messages, one for each person in your list.
print('-'*40)
print("We found a bigger dinner table.")
print(f"My original guests are: {guests}.")
print("Inviting few more...")
guests.insert(0, "Brahma")
guests.insert(len(guests)//2, "Hari")
guests.append("Har")
print("List of guests is prepared, now sending invitations...")
for guest in guests:
    print(f"New welcome invite. Please {guest} come over for dinner.")

# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t 
# arrive in time for the dinner, and you have space for only two guests .
# •	Start with your program from Exercise 3-6 . Add a new line that prints a 
# message saying that you can invite only two people for dinner .
# •	Use pop() to remove guests from your list one at a time until only two 
# names remain in your list . Each time you pop a name from your list, print 
# a message to that person letting them know you’re sorry you can’t invite 
# them to dinner .
# •	Print a message to each of the two people still on your list, letting them 
# know they’re still invited .
# •	Use del to remove the last two names from your list, so you have an empty 
# list . Print your list to make sure you actually have an empty list at the end 
# of your program.
print('-'*40)
print("Oh no. New dinner table won't arrive in time for the dinner. Space for only two guests.")
total_guests = len(guests)
total_guests_to_remove = total_guests - 2
for i in range(total_guests_to_remove):
    popped_guest = guests.pop()
    print(f"Hi {popped_guest}, I'm sorry to say but I can't invite you for dinner :(.")
print(f"{guests[0]}, you're still invited for dinner. Please come.")
print(f"{guests[1]}, you're still invited for dinner. Please come.")
print("Removing guests now...")
del guests[1]
del guests[0]
print(f"There should not be any guest now...printing guests list...{guests}.")

# 3-8. Seeing the World: Think of at least five places in the world you’d like to 
# visit .
# •	Store the locations in a list . Make sure the list is not in alphabetical order .
# •	Print your list in its original order . Don’t worry about printing the list neatly, 
# just print it as a raw Python list .
# •	Use sorted() to print your list in alphabetical order without modifying the 
# actual list .
# •	Show that your list is still in its original order by printing it .
# •	Use sorted() to print your list in reverse alphabetical order without chang
# ing the order of the original list .
# •	Show that your list is still in its original order by printing it again .
# •	Use reverse() to change the order of your list . Print the list to show that its 
# order has changed .
# •	Use reverse() to change the order of your list again . Print the list to show 
# it’s back to its original order .
# •	Use sort() to change your list so it’s stored in alphabetical order . Print the 
# list to show that its order has been changed .
# •	Use sort() to change your list so it’s stored in reverse alphabetical order . 
# Print the list to show that its order has changed .
print('-'*40)
locations = ["haridwar", "mathura", "ayodhya", "kurukshetra", "chitrakut"]
print(f"original locations list...{locations}")
sorted_locations = sorted(locations)
print(f"sorted locations list...{sorted_locations}")
print(f"original list unchanged...{locations}")
locations.reverse()
print(f"Original list after using reverse() function is reversed...{locations}")
locations.reverse()
print(f"Original list after using reverse() function twice comes back to original...{locations}")
locations.sort()
print(f"locations list in alphabetical order...{locations}")
locations.sort(reverse=True)
print(f"locations list in reverse alphabetical order...{locations}")

# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 
# through 3-7 (page 46), use len() to print a message indicating the number 
# of people you are inviting to dinner .
print('-'*40)
guests = ["aai", "aaji", "sitamata", "ram", "hanuman"]
print(f"We are inviting {len(guests)} guests for dinner.")

# 3-10. Every Function: Think of something you could store in a list . For example, 
# you could make a list of mountains, rivers, countries, cities, languages, or any
# thing else you’d like . Write a program that creates a list containing these items 
# and then uses each function introduced in this chapter at least once 
print('-'*40)
cities = ["mumbai", "pune", "nashik"]
for city in cities:
    print(city.upper(), city.lower(), city.title())