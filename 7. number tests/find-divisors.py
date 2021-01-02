"""
Prompt the user for two positive integers
if the numbers entered are not positive then
    print out an error message
else
    find the common divisors
    print out the common divisors
    sum the common divisors
    print out the total

function findDivisors(num1, num2)
initialise divisors with (1, )
find min of inputs
if either number odd
    for i from 3 to min//2 step of 2 do
        if num1 mod i == 0 and num2 mod i == 0 then
            add i to divisors
else
    for i from 2 to min//2 do
        if num1 mod i == 0 and num2 mod i == 0 then
            add i to divisors
    return divisors
"""

# Program to get the common divisors of two positive integers supplied # Demonstrates the use of tuples
def findDivisors(num1, num2):
    """Finds the common divisors of num1 and num2
    Assumes that num1 and num2 are positive integers
    Returns a tuple containing the common divisors of num1 and num2"""
    divisors = (1, )
    minVar = min(num1, num2)
    if max(num1, num2) % minVar == 0: #check if the larger of the two is divisible by the smaller
        divisors += (minVar,) # if so make the smaller a common divisor
    if num1 % 2 != 0 or num2 % 2 != 0: # OPTIMIZATION: if either number is odd, we only need to check odd factors as odd numbers only have odd factors
        for i in range(3, minVar//2 + 1, 2):
            if num1 % i == 0 and num2 % i == 0:
                divisors += (i,)
    else:
        for i in range(2, minVar//2 + 1):
            if num1 % i == 0 and num2 % i == 0:
                divisors += (i,)

    return divisors

number1 = int(input('Enter a positive i(nteger: '))
number2 = int(input('Enter another positive integer: '))

if number1 <= 0 or number2 <= 0:
    print('Numbers should be > 0.')
else:
    # First of all, get the common divisors and print them out
    divisors = findDivisors(number1, number2)
    print('The common divisors of', number1, 'and', number2, 'are:', divisors)

# Now sum them and print the total
    total = 0
    for d in divisors:
        total += d
    print('Sum of the common divisors is:', total)

print('Finished!')