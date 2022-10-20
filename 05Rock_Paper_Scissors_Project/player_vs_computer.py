'''
Rock paper Scissor player vs computer
'''
                                                            #setting up the computer for the game

#-----------------------------------------------------------------------------------------------------------------------------------------
#from the library random import random int as a randnum
from random import randint

#assign a random number between (0 to 2) to the variable random_number using the randint from the random library
random_number = randint(0,2)

#check if generated random number is 0 and assing 'rock' to the variable computer 
if (random_number == 0):
    computer = 'rock'

#check if generated random number is 1 and assing 'paper' to the variable computer
elif (random_number == 1):
    computer = 'paper'

#check if generated random number is 0 and assing 'rock ' to the variable computer
else:
    computer = 'scissors'

#-------------------------------------------------------------------------------------------------------------------------------------------


                                                        #creating the rock paper scissors Logic for the game
#--------------------------------------------------------------------------------------------------------------------------------------------

# ask the player to enter a  name and save it to the variable player_name
player_name = str(input('what is your name: '))

# take player's choice
player_choice = str(input('Choose one: Rock, Paper, Scissors: ').lower())


#check if both choices are the same like rock and rock
if player_choice == computer :{
    print("it's a tie")
}

#Logic 1 : check if player1 chooses rock and compare it with if computer chooses scissors then player 1 wins but if computer chooses paper then computer wins
elif (player_choice == 'rock'):
    #player1 chose rock and compare it with if computer chooses scissors then player 1 wins 
    if(computer == 'scissors'):{
        print(player_name + ' won')
        }
    #player1 chose rock and compare it with if computer chooses paper then computer wins
    elif(computer == 'paper'):{
            print(f"Computer plays {computer}")
            }
#Logic 2 : check if player1 chooses paper and compare it with if computer chooses rock then player 1 wins but if computer chooses scissors then computer wins
elif (player_choice == 'paper'):
    
    #player1 chose paper and compare it with if computer rock scissors then player 1 wins 
    if(computer == 'rock'):
        print(player_name + ' won')

    #player1 chose paper and compare it with if computer chooses scissors then computer wins
    elif(computer == 'scissors'):
            print(f"Computer plays {computer}")
    else:
        print("it's a tie")


#Logic 3 : check if player1 chooses scissors and compare it with if computer chooses paper then player 1 wins but if computer chooses scissors then computer wins
elif (player_choice == 'scissors'):

    #player1 chose scissors and compare it with if computer paper scissors then player 1 wins 
    if(computer == 'paper'):
        print(player_name + ' won')

    #player1 chose scissors and compare it with if computer chooses rock then computer wins
    elif(computer == 'rock'):
            print(f"Computer plays {computer}")

#Logic 4: if players enter something different than rock paper scissors then print out the line below.
else:
    print("Please enter rock, paper or scissors")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------