# Exercise 1: Type the following statements in the Python interpreter to see what they do:
# 5
# x = 5
# x + 1
5
x = 5
x + 1

#Exercise 2: Write a program that uses input to prompt a user
#for their name and then welcomes them.
user_name = input('welcome,please input your name:')
print("welcome, " + user_name)

# Exercise 3: Write a program to prompt the user for hours and rate per hour to compute gross pay.
# Enter Hours: 35
# Enter Rate: 2.75
# Pay: 96.25
hours = float(input('please enter the hours: '))
rate = float(input('please enter the rate: '))
pay = hours * rate
print('You need to pay: ' + str(pay))

# Exercise 4: Assume that we execute the following assignment statements:
# width = 17
# height = 12.0
# For each of the following expressions, write the value of the expression
# and the type (of the value of the expression).
# 1. width//2
# 2. width/2.0
# 3. height/3
# 4. 1 + 2 * 5
# Use the Python interpreter to check your answers.
width = 17
height = 12.0
assignment1 = width // 2
print(assignment1)
assignment2 = width/2.0
print(assignment2)
assignment3 = height/3
print(assignment3)
assignment4 = 1 + 2 * 5
print(assignment4)

# Exercise 5: Write a program which prompts the user for a Celsius temperature,
# convert the temperature to Fahrenheit, and print out the converted temperature.
celsius_temp = float(input('please enter the temperature(Celcius): '))
fahrenheit_temp = celsius_temp * 33.8
print('the fahrenheit temperature is: ')
print(fahrenheit_temp)

