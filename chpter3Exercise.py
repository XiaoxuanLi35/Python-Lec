#  Exercise 1: Rewrite your pay computation
#  to give the employee 1.5 times the hourly rate
#  for hours worked above 40 hours
#  Enter Hours: 45
#  Enter Rate: 10
#  Pay: 475.0


# revised version by ChatGPT:
# hours = float(input('Please enter the hours: '))
# rate = float(input('Please enter the rate: '))
#
# regular_hours = min(40, hours)
# overtime_hours = max(0, hours - 40)
#
# pay = regular_hours * rate + overtime_hours * 1.5 * rate
#
# print(f'You need to pay: {pay}')

# hours = float(input('please enter the hours: '))
# rate = float(input('please enter the rate: '))
#
# if hours <= 40:
#     pay = hours * rate
# else:
#     pay = (hours - 40) * 1.5 * rate + 40 * rate
#
# print('You need to pay: ' + str(pay))

# Exercise 3:
# Write a program to prompt for a score between 0.0 and 1.0.
# If the score is out of range,
# print an error message.
# If the score is between 0.0 and 1.0,
# print a grade using the following table:
# 3.11. EXERCISES 41
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# Enter score: 0.95
# A
# Enter score: perfect
# Bad score
# Enter score: 10.0
# Bad score
# Enter score: 0.75
# C
# Enter score: 0.5
# F
# Run the program repeatedly as shown above to test the various different values for
# input.

while True:
    try:
        score = float(input('please enter your score(between 0.0 and 1.0): '))
        if 0.0 <= score <= 1.0:
            if score >= 0.9:
                print('A')
            elif score >= 0.8:
                print('B')
            elif score >= 0.7:
                print('C')
            elif score >= 0.6:
                print('D')
            else:
                print('F')
            break
        else:
            print('Bad Score')

    except:
        print('Bad Score')



