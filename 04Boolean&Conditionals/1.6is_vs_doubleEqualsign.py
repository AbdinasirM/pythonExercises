# What is == Operator?
# To compare objects based on their values, Python’s equality operators (==) are employed. It calls the left object’s __eq__() class method, which specifies the criteria for determining equality. However, these constraints are typically written so that the equality operator == returns True if two objects, have the same value, and return False if both have different value

# What is the ‘is’ Operator?
# Python identity operators (is, is not) are used to compare objects based on their identity. When the variables on either side of an operator point at the exact same object, the is operator’s evaluation is true. Otherwise, it would provide us with a false assessment.

# == compares the values of the two variables where 'is' looks if both values are stored in the same place in memory.

#in case below both 'is' and  == are working the same
x = 3
y = 3

print(x == y)
print(x is y)

#in the case below 'is' and  == are not working the same

a = 'abdi'
b = 'abdi'

print(a == b)
print(a is b)


account_number = eval(input('what is your account number: '))

customerAccount = 126

if (account_number is customerAccount):{
    print('Abdi is one of our customer')
}
else:{
    print(f'{account_number} is not in our database')
}