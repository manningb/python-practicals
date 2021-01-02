"""
take input from user
initalise factorial var to 1
if input < 0:
    error
else:
    for i in range(input):
        factorial *= i + 1
print(factorial)
"""

print('Program to calculate Factorial.')
number = int(input('Enter the number for which you wish to calculate the factorial (an int >= 0): '))
nfactorial = 1
if number < 0:
    print('Error: Number entered was less than 0.')
else:
    for i in range(number):
        nfactorial *= i + 1
print('Factorial of', number, 'is', nfactorial)