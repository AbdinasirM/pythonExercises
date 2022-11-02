'''
With the while loop we can execute a set of statements as long as a condition is true.

The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1.

'''
#basic while loop examples:

#password checker
password_input = str(input('what is the password: '))
while password_input != 'test678':
    print("Access Denied")
    password_input = str(input('what is the password: '))
print('Welcome')


#print out numbers from 1 to 10 using while loops
numb = 1
while numb < 11:
    numb = numb +1
    print(numb)



#Emoji Art
emoji = '\U0001F600'
emoji_count = 1

while emoji_count < 11:    
    print(emoji * emoji_count)
    emoji_count +=1


# stop copying me example with wile loop
# a while loop that doesn't stop until user enters stop copying me
question = str(input("hey how's it going? "))
while question != "stop copying me":
    print(question)
    question = str(input("hey how's it going? "))
    
print('UGH, you win')

# break keyword with while loop
#With the break statement we can stop the loop even if the while condition is true:

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1 