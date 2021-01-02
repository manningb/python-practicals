"""
define factorial function that takes nonnegative integer as its only argument
    if input == 1:
        return 1
    else:
        return input * factorial(input - 1)
    # function uses recursion to calculate factorial

take input from user
if input >= 0:
    print factorial of input
else:
    print input must be >= 0
"""

def factorial(inputNum):
    # This function returns the factorial of a positive integer
    if inputNum == 0:
        return 1
    else:
        return inputNum * factorial(inputNum - 1)

inputNum = int(input('Please input a positive integer: '))
if inputNum >= 0:
    print(f'The factorial of {inputNum} is {factorial(inputNum)}.') 
else:
    print('Error: You must enter an integer >= 0.')