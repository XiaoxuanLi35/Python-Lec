# Exercise 2: Write another program that prompts for a list of numbers as above
# and at the end prints out both the maximum and
# minimum of the numbers instead of the average.

nums = []
count = 0

while True:
    user_input = input('enter a number: ')

    if user_input == 'done':
        break

    try:
        num = float(user_input)
        nums.append(num)
        count += 1


    except:
        if isinstance(user_input, str):
            print('Invalid input')

if count > 0:
    index = 0

    while index < len(nums):
        letter = nums[index]
        print(letter)
        index += 1

    maxNum = nums[0]
    minNum = nums[0]

    for num in nums: # is equivalent to saying "for each element in the list nums, do the following:"

        if maxNum < letter:
            maxNum = letter


        if minNum > letter:
            minNum = letter


    print('maximum is:', maxNum)
    print('minimum is:', minNum)