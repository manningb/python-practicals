"""
for number in specified range:
    for i in range of lower bound, number:
        if number even:
            print how to calc numebr by multiplying two of its factors lowest
            break
    else:
        # loop fell through without finding a factor
        print(number, 'is a prime number')
print('Finished!')
"""

# Program to illustrate the use of the else statement on a for loop
# Search for prime numbers in a range of integers
# Look for prime numbers in a range of integers
for number in range(2, 20):
    for i in range(2, number):
        if number % i == 0:
            print(number, 'equals', i, '*', number//i)
            break
    else:
        # loop fell through without finding a factor
        print(number, 'is a prime number')
print('Finished!')