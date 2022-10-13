#ask for age
age = input('how old are you: ')

#if user input is not empty
if (age != ''):
    # 18 - 21 have to have a wristband
    if (int(age) >= 18 and int(age) <= 21):{
        print('show me your wristband')
    }
    #21+ can drink, normal entry
    elif (int(age) >= 21):{
        print('you can have a drink and you can go through the normal entry without wristband')
    }
    else:{
        #sorry you are young
        print('Sorry, you are young and can\'t enter')
    }
else:{
    print('please run this program again and enter an age')
}
