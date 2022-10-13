#ex
#AND
#ticket price for all ages
# age = eval(input('How old are you: \n'));

# if ((age > 2 ) and (age <= 6)):{
#     print('Ticket price is $4')
# }
# elif ((age >= 7 ) and (age <= 18)):{
#     print('Ticket price is $7')
# }
# else:{
#     print('Ticket price is $15')
# }

#ex
#OR

city = input('Where do you live: \n');

if (city =='Los angles' or city == 'San Francisco'):{
    print('You live in California')
}
else:{
    print('you live somewhere else')
}

#ex
#NOT

age = eval(input('How old are you: \n'));
# 
if (not ((age > 2  and age <= 6) or age >= 65)):{
    print('Ticket price is $15 and you are not a child and senior')
}
else:{
    print('Ticket price is $7 and you are a child or senior')
}

