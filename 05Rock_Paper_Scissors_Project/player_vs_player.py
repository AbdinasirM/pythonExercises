'''
Rock paper Scissor player vs player
'''

# ask each players name and save it to the variables player1_name and player2_name
player1_name = str(input('what is your name(player1): '))
player2_name = str(input('what is your name(player1): '))

# take both players choice


player1_choice = str(input('Choose one: Rock, Paper, Scissors: ').lower())
player2_choice = str(input('Choose one: Rock, Paper, Scissors: ').lower())
    # print(player1_name + ' chose ' + player1_choice)
    # print(player2_name + ' chose ' + player2_choice)


#check if both choices are the same like rock and rock
if player1_choice == player2_choice :{
    print("it's a tie")
}

#Logic 1 : check if player1 chooses rock and compare it with if player2 chooses scissors then player 1 wins but if player2 chooses paper then player2 wins
elif (player1_choice == 'rock'):
    #player1 chose rock and compare it with if player2 chooses scissors then player 1 wins 
    if(player2_choice == 'scissors'):{
        print(player1_name + ' won')
        }
    #player1 chose rock and compare it with if player2 chooses paper then player 2 wins
    elif(player2_choice == 'paper'):{
            print(player2_name + ' won')
            }
#Logic 2 : check if player1 chooses paper and compare it with if player2 chooses rock then player 1 wins but if player2 chooses scissors then player2 wins
elif (player1_choice == 'paper'):
    
    #player1 chose paper and compare it with if player2 rock scissors then player 1 wins 
    if(player2_choice == 'rock'):
        print(player1_name + ' won')

    #player1 chose paper and compare it with if player2 chooses scissors then player 2 wins
    elif(player2_choice == 'scissors'):
            print(player2_name + ' won')
    else:
        print("it's a tie")


#Logic 3 : check if player1 chooses scissors and compare it with if player2 chooses paper then player 1 wins but if player2 chooses scissors then player2 wins
elif (player1_choice == 'scissors'):

    #player1 chose scissors and compare it with if player2 paper scissors then player 1 wins 
    if(player2_choice == 'paper'):
        print(player1_name + ' won')

    #player1 chose scissors and compare it with if player2 chooses rock then player 2 wins
    elif(player2_choice == 'rock'):
            print(player2_name + ' won')

#Logic 4: if players enter something different than rock paper scissors then print out the line below.
else:
    print("sorry something went wrong")