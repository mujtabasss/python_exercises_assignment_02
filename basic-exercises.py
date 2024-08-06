"""Assign a message to a variable and then print that message.
"""
personal_message:str = "My name is mujtaba , i am a applied gen ai cloud native engineer "
print(personal_message)

"""Question:02 : Assign a message to a variable and print that message.
● Change the value of the variable to a new message, and print the new message"""

message:str = "My name is mujtaba , i am a applied gen ai cloud native engineer "
print(message)
message ="my name is mujtaba and i am piaic batch 62 student"
print(message)

"""Question 03"""
"""Use a variable to represent a person’s name.
● Print a message to that person, such as, “Hello Eric, would you like to learn some
Python today?"""

person_name : str = "sir irfan malik"
print(f"hello {person_name},would you like to teach me freelancing ?")

"""Question 04 : Use a variable to represent a person’s name.
● Print the person’s name in lowercase, uppercase, and title case."""

print(person_name.upper())
print(person_name.lower())
print(person_name.title())

"""Question 05:
● Find a quote from a famous person you admire.
● Print the quote and the name of its author.
The output should look something like the following:
Albert Einstein once said, “A person who never made a mistake never
tried anything new."""
qoute: str = "Think a hundred times before you take a decision, but once that decision is taken, stand by it as one man."
author_name : str = "Quaid e azam muhammad ali jinnah"
print(f'{author_name} once said,"{qoute}"')

"""Question : 06
● Use a variable called famous_person to represent the famous person’s name.
● Compose the message and represent it with a variable called message.
● Print the message."""
famous_person : str = "quaid e azam muhammad ali jinnah"
message1 : str = f'{famous_person} once said: "Work, work, and work, and we are bound to success "'
print(message1)

"""question 07:7. Stripping Names
Task:
● Use a variable to represent a person’s name, and include some whitespace characters
at the beginning and end of the name.
● Make sure you use each character combination, \t and \n, at least once.
● Print the name once, so the whitespace around the name is displayed.
● Print the name using each of the three stripping functions: lstrip(), rstrip(), and
strip()."""
persons_name : str = "\n\t  muhammad mujtaba hussain   \t\n"
print(f"orignal name with whitespaces : '{persons_name}'")
print(persons_name.strip())
print(persons_name.lstrip())
print(persons_name.rstrip())


"""question 08: Assign the values 5, 10, and 15 to three variables x, y, and z. Print their sum."""
x : int = 5
y : int = 10 
z : int = 15 
print (x+y+z)

"""QUESTION 09 : : Swap the values of two variables a and b. Print the values before and after the swap."""
a:int =5 
b:int =12
print(f"values of the variable a is {a} and the b is {b} before swapping")
temp = a 
a = b
b = temp
print(f"values of the variable a is {a} and the b is {b}  after swapping")

"""QUESTION 10: Create a variable with your favorite color and print it. Then change the variable name to
something else and print the color again """
fav_color : str = "black"
print(fav_color)
fav_color1 :str = "black"
print(fav_color1)

"""QUESTION 11 : Create a variable pet_name and set it to "Buddy". Change the value of pet_name to
"Max" and print the new value."""
pet_name : str = "buddy"
pet_name = "Max"
print(pet_name)

"""Question 12 :  Assign the value "Sunshine" to a variable and print it. 
Then, mistakenly try to print a variable with a different name (like sunsine) and observe the error"""
world : str = "sunshine"
#print(sunshine) // name error message 

"""QUESTION 13 : Assign the value 100 to a variable score and print it. Then assign a new value to score
and print it again."""
score : int = 100
score = 1100
print(score)

"""QUESTION 14 :  Create a string variable city and assign it the name of a city you like. 
Print the city name."""
 
Fav_city :str = "gilgit baltistan"
print(Fav_city)

"""Question 15:  Create a variable text with the value "python programming" and print it in title case"""

text : str = "python programing"
print(text.title())

"""Question 16: : Assign a string with mixed cases to a variable and print it in all lowercase letters"""
mix_cases : str = "HellO_woRld"
print(mix_cases.lower())

"""Question 17 : Assign a string with mixed cases to a variable and print it in all uppercase letters"""
Mix_cases : str = "HelLo_wOrlD"
print(Mix_cases.upper())

"""Question 18 : Create a variable temperature with the value 25. Print "The current temperature is
[temperature] degrees." using the variable."""
temprature : int = 25
print(f"The current temprature is {temprature} degrees")

"""Question 19 : Create a variable poem with a short poem that has multiple lines. Print the poem with
each line starting on a new line"""
poem: str = "The secrets of selfhood are hidden in your soul\n,Look within yourself to find your true goal,\nThe journey of life is long and steep,\nwaken your spirit from its deep sleep."
print(poem)