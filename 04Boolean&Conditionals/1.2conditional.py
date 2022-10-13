# conditional statements

# Python supports the usual logical conditions from mathematics:

#     Equals: a == b
#     Not Equals: a != b
#     Less than: a < b
#     Less than or equal to: a <= b
#     Greater than: a > b
#     Greater than or equal to: a >= b

# These conditions can be used in several ways, most commonly in "if statements" and loops.

# An "if statement" is written by using the if keyword.

# ex1
name = 'L'
if name == 'Puka':{
    print('Subscribe')
}
elif(name == 'L'):{
    print('What is that?')
}
else:{
    print('I dont know')
}

#ex2
#check if a number is odd or even
num = eval (input("Enter a number here: "))

if num % 2 != 0:
    print("odd")
else:
    print("even")


