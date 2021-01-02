"""
take input from user
set factorial = 1
for i in range(input):
    factorial multiplied by i equals factorial

print(factorial)
"""

positive = int(input('Please input a positive integer: '))
factorial = 1
for i in range(positive):
    factorial *= i + 1

if positive > 0:
    print(f'The factorial of {positive} is {factorial}.')
elif positive < 0:
    print('You must enter a positive integer.')
else:
    print('The factorial of 0 is 1.')