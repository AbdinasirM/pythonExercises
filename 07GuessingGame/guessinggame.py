# import the python random integer library from the random library
from random import randint as random_integer
# generate a random number using the randint library  from 1 to 10 and save it in the variable random_number
random_number = random_integer(1, 10)

# run the code below if all conditions are met
while True:
    # assign the input you get from the user to a variable called guess
    guess = int(input("GUess the secret number: "))
    # check if user's guessed number is less than the random generated number and if that is true then run the code inside
    if (guess < random_number):
        # print too low on the screen
        print("TOO LOW!")
    # check if user's guessed number is greater than the random generated number and if that is true then run the code inside
    elif (guess > random_number):
        # print too high on the screen
        print("TOO HIGH!")
    # lastly if user's guessed number is equal to the random generated number and if that is true then run the code inside
    else:
        # print you won on the screen
        print(f"You won!!!")
        # ask the user if they want to play again and save it in the variable called playagain
        playagin = input(
            "DO you want to Guess the secret number again? (y/n): ")
        # check if user type y (y for yes) and  if that is true then run the code inside
        if (playagin == 'y'):
            # generate a new random number using the randint library  from 1 to 10 and save it in the variable random_number
            random_number = random_integer(1, 10)
            # make the guess variable empty
            guess = None
        # check if user types n (n for no) and if that is true then run the code below
        else:
            # stop the whole program after the condition is met
            break
