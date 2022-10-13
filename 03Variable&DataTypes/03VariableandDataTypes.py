#Variables are container that store something that you pull out later
#variables can hold numbers, booleans(true and false), and strings
#variables must start with a letter or underscore, lowercase,

from re import S


container = 'hammer'
num = 5
correct = True
incorrect = False
print(container)
print(num)
print(correct)
print(incorrect)
empty = None
print(empty)

#strings

#single quote
name = 'abdi'
print(name)
#single quote
name2 = 'abdi'
print(name2)

#string escape characters:look at the image for more info

#newline = \n
newline = 'hello \n world'
print(newline)

#escape a character = \character
greeting = 'This is Abdi\' car'
print(greeting)

#string concatenation

greet = 'hello '
name = 'abdi'

print(greet + name)

#formatting strings using f"{}"
guess = 8

print(f"{guess + 8} is not the ")

fruit ='banana'
ripeness = 'unripe'

print(f"That {fruit} is rotten {ripeness}")

#strings and indexes

words = "animal Human"
print(words[0]) #gives you the first letter

print(words[-1]) #gives you the last letter

# converting data types

#integer to float
n = 12
n = float(n)
print(n)

#float to integer
f = 5.633
f = int(f)
print(f)

#string  to integer
s = "65"
s = int(s)
print(s)

# integer to string
n1 = 5
n1 = str(n1)
print(n1)















