"""
define sqrt function with two arguments num and tolerance
    step = tolerance squared
    initalise the root variable
    while the abs value of (number inputted - root squared) is greater than or equal to the tolerance and the root squared 
    is less than or equal to the number:
        root += step
    if abs value of (number inputted - root squared) is less than tolerance:
        return root variable
    else return False

take float input from user
if number greater than or equal to 0:
    run root function with float number and predefined tolerance
    print root
else:
    print error
"""

def sqrt(num, tolerance):
    step = tolerance ** 2
    root = 0
    root_test = root ** 2
    while root_test <= num and abs(num - root_test) >= tolerance:
        root += step
    if abs(num - root_test) < tolerance:
        return root
    else:
        return False

tolerance = 0.1
num = float(input('Please input a non-negative float: '))
if num >= 0:
    root = sqrt(num, tolerance)
    print(f'The approx. square root of {num} is {root}')
else:
    print('Please input a non negative floating point number.')