# Ganesha
# Author : Ganesha 18-November-2026
# This script covers exercises from Chapter 2 VARIABLES AND SIMPLE DATA TYPES.

# 2-1 Simple Message
message = "Ganesha God is great"
print(message)

# 2-2 Simple Messages
message2 = "Ganesha Bappa Morya"
print(message2)
message2 = "Bappa Morya Re Bappa Morya"
print(message2)


# Appendix C .
# 2-3. Personal Message: Store a person’s name in a variable, and print a mes
# sage to that person . Your message should be simple, such as, “Hello Eric, 
# would you like to learn some Python today?”
name = "Ganesha"
print(f"Hello {name}, would you like to learn some Python today?")

# 2-4. Name Cases: Store a person’s name in a variable, and then print that per
# son’s name in lowercase, uppercase, and titlecase .
name = "bappa"
print(name.lower())
print(name.upper())
print(name.title())

# 2-5. Famous Quote: Find a quote from a famous person you admire . Print the 
# quote and the name of its author . Your output should look something like the 
# following, including the quotation marks:
# Albert Einstein once said, “A person who never made a 
# mistake never tried anything new.”
name = "Eknath"
quote = "Hariprapti si upay dharawe Santanche te pay"
print(f'{name} once said, "{quote}."')

# 2-6. Famous Quote 2: Repeat Exercise 2-5, but this time store the famous per
# son’s name in a variable called famous_person . Then compose your message 
# and store it in a new variable called message . Print your message .
famous_person = "Tukaram"
message = f'{famous_person} once said, "Pahatechya prahari mhana Hari Hari, taya sukha sari nahi duje."'
print(message)

# 2-7. Stripping Names: Store a person’s name, and include some whitespace 
# characters at the beginning and end of the name . Make sure you use each 
# character combination, "\t" and "\n", at least once .
# Print the name once, so the whitespace around the name is displayed . 
# Then print the name using each of the three stripping functions, lstrip(), 
# rstrip(), and strip()
name = "   Ganesha \t \n    "
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())

# 2-8. Number Eight: Write addition, subtraction, multiplication, and division 
# operations that each result in the number 8 . Be sure to enclose your operations 
# in print statements to see the results . You should create four lines that look 
# like this:
# print(5 + 3)
# Your output should simply be four lines with the number 8 appearing once 
# on each line .
print(5 + 3)
print(8 - 0)
print(8 * 1)
print(8 // 1)   # 8 / 1 - printed 8.0

# 2-9. Favorite Number: Store your favorite number in a variable . Then, using 
# that variable, create a message that reveals your favorite number . Print that 
# message
my_favnumber = 7
print(f"My favourite number is {my_favnumber}.")