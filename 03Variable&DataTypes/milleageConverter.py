#ask user how many kilometers they ran and convert it to miles
kilometers = float(input('How many kilometers did you cycle today? '))
miles =  kilometers/1.60934
#round function rounds a number by taking two arguments round(thing to round,and how many decimal points)
rounded_answer = round(miles, 2)
print(f"you have ran {kilometers} KM which is equivilent to {rounded_answer}miles")
