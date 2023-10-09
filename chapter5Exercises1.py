# Exercise 1: Write a program which repeatedly reads numbers
# until the user enters “done”.
# Once “done” is entered, print out the total, count,and average of the numbers.
# If the user enters anything other than a number,
# detect their mistake using try and except
# and print an error message and skip to the next number.
# Enter a number: 4
# Enter a number: 5
# Enter a number: bad data
# Invalid input
# Enter a number: 7
# Enter a number: done
# 16 3 5.333333333333333

total = 0
count = 0

while True:
    user_input = input('enter a number: ')

    if user_input == 'done':
        break

    try:
        data = float(user_input)
        total += data
        count += 1

    except:
        if isinstance(user_input, str):
            print('Invalid input')

# The `isinstance()` function in Python is used to check
# if an object is an instance of a specified class or a tuple of classes.
# It returns `True` if the object is an instance of any of the given classes, and `False` otherwise.
# The syntax is as follows:
# isinstance(object, classinfo)
# `object`: The object to be checked.
# `classinfo`: A class or a tuple of classes to check against.

if count > 0:
    average = total / count
    print('total is: ', total, 'count is: ', count, 'average is: ', average)



