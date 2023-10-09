# Exercise 2: Rewrite your pay program using try and except
# so that your program handles non-numeric input gracefully
# by printing a message and exiting the program.
# The following shows two executions of the program:
# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input
# Enter Hours: forty
# Error, please enter numeric input

# the problem of the following code is:
# When the try is executed, the program still asks for input
# try:
#     hours = float(input('please enter the hours: '))
#     rate = float(input('please enter the rate: '))
#     if hours <= 40:
#         pay = hours * rate
#     else:
#         pay = (hours - 40) * 1.5 * rate + 40 * rate
#
#     print('You need to pay: ' + str(pay))
#
# except:
#     print('Error, please enter numeric input')

# ChatGPT version:
while True:
    try:
        hours = float(input('Please enter the hours: '))
        rate = float(input('Please enter the rate: '))
        break  # break out of the loop if input is successfully converted to float
    except:
        print('Error, please enter numeric input')