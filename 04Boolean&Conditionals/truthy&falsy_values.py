# Truthy vs Falsy Values

# In Python, individual values can evaluate to either True or False.

# The Basis rules are:

#     Values that evaluate to False are considered Falsy.
#     Values that evaluate to True are considered Truthy.

# Falsy Values Includes:

# 1) Sequences and Collections:

#     Empty lists []
#     Empty tuples ()
#     Empty dictionaries {}
#     Empty sets set()
#     Empty strings ” “
#     Empty ranges range(0)

# 2) Numbers: Zero of any numeric type.

#     Integer: 0
#     Float: 0.0
#     Complex: 0j

# 3) Constants:

#     None
#     False

# Falsy values were the reason why there was no output in our initial example when the value of number was zero.

# Truthy Values Includes:

#     Non-empty sequences or collections (lists, tuples, strings, dictionaries, sets).
#     Numeric values that are not zero.
#     Constant: True

#ex

animal = input('what is your favorite animal: ')

if (animal):{#checks if user entered something or not.
    print(animal + ' is my favorite too') 
}