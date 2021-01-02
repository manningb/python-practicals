"""
Prompt the user for two positive integers
if the numbers entered are not positive then
    print out an error message
else
    find the perf num less than num1
    print out perf num less than num1


function perfectNum(num1)
initialise divisors
for i from 1 to num1 do
    if num1 mod i == 0 then
        add i to divisors
sum the common divisors
if sum == num1:
    return True
else:
    false
"""

# Program to get the common divisors of two positive integers supplied # Demonstrates the use of tuples
def perfectNum(num1):
    """Checks if a number is a perfect number and returns true/false based on result"""
    divisors = ()
    for i in range(1, num1):
        if num1 % i == 0:
            divisors += (i,)
    #print(divisors)
    total = 0
    for d in divisors:
        total += d
    
    if total == num1:
        return True
    else:
        return False


number1 = int(input('Enter a positive integer: '))
perfectNumbers = ()
if number1 <= 0:
    print('Number should be > 0.')
else:
    # First of all, get the common divisors and print them out
    for i in range(number1):
        if perfectNum(i+1):
            perfectNumbers += (i+1,)
        #else:
            #print(f'{i} is not a perfect number.')
if perfectNumbers == ():
    print(f'There are no perfect numbers less than/equal to {number1}')
else:
    print(f'Perfect numbers less than/equal to {number1}: {str(perfectNumbers)[1:-1]}')