"""
define factorial function that takes nonnegative integer as its only argument
    if input == 1:
        return 1
    else:
        print factorial info
        return input * factorial(input - 1)
    # function uses recursion to calculate factorial

take input from user
if input >= 0:
    print factorial of input
else:
    print input must be >= 0
"""

def fact(intInput):
    if intInput == 0:
        return 1
    else:
        prevFact = fact(intInput-1)
        factorial = intInput * prevFact
        print(f'The current factorial: {intInput} * {prevFact} = {factorial}.')
        return factorial

intInput = int(input('Please input a non-negative integer: '))
if intInput >= 0:
    print(f'\nThe factorial of {intInput} is {fact(intInput)}.')
else:
    print('Error: Input must be a non-negative integer.')