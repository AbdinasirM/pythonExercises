'''A for loop is used for iterating over a sequence
(that is either a list, a tuple, a dictionary, a set, or a string).
'''

#basic forloop that goes printout each letter in the word School
for letter in "school":
    print(letter) 
'''
To loop through a set of code a specified number of times, we can use the range() function,
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
'''

#forloop and  range with 1 parameter
for x in range(2):#range from 0 to 2
    print(x)
#forloop and  range with 2 parameter
for x in range(1,2): #range from 1 to 2
    print(x)

#forloop and  range with 3 parameter
for x in range(1,10,2): #range from 1 to 10 and skip 2 steps eveytime
    print(x)
    
#forloop and  range with 3 parameters
for x in range(1,6, -1): #range from 1 to 6 but now starts from 6 to 1 
    print(x)


#Exercise1:

# from 10 to 20 add all the odd numbers
y=0
for n in range(10,21):
    if(n%2!=0):
        print(y+n)

#Exercise2:
times_to_repeat = int(input('How many times do I have to repeat? '))
for time in range(times_to_repeat):
    print('CLEAN')

#Exercise3:

numb = 0
for n in range(1,21):
    numb =+n
    if (numb == 4 or numb ==13):
        print(f'{numb} is UNLUCKY!') 
    elif (numb % 2 != 0):
        print(f'{numb} is odd')
    else:
        print(f'{numb} is even') 


#With the break statement we can stop the loop even if the while condition is true:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break