import random

print(random.randint(5, 10))
print(random.randrange(5, 10))

nums = [1, 2, 3]
print(random.choice(nums))

# Exercise 2: Move the last line of this program to the top,
# so the function
# call appears before the definitions.
# Run the program and see what error message you get.
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')
    print('\n')
def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()

# Exercise 6: Rewrite your pay computation with time-and-a-half
# for overtime and create a function called computepay
# which takes two parameters (hours and rate).
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

def computepay(hours, rate):
    hours = float(input('please enter the hours: '))
    rate = float(input('please enter the rate: '))

    if hours <= 40:
        pay = hours * rate
    else:
        pay = (hours - 40) * 1.5 * rate + 40 * rate
    return pay

salary = computepay(45, 10)
print('Your salary is: ', str(salary))

