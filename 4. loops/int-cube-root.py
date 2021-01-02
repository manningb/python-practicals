"""
take input from user
i = 0
while number not equal zero:
    while i**3 < number:
        increment i by 1
    if i**3 == number:
        print(i is cube root of number)
    else:
        print(number is not a cube rooot)
    take input from user
    i = 0
"""

print('Program to calculate Integer Cube Root of a Number')
number = int(input('Please input an integer: '))
i = 0
negative = 1
while number != 0:
    if number < 0:
        number = -number
        negative = -1 
    while i**3 < number:
        i += 1
    if i**3 == number:
        print(f'The cube root of {negative*number} is: {negative*i}.')
    else:
        print(f'{number*negative} is not a perfect cube root.')
    number = int(input('Please input an integer: '))
    i = 0
    negative = 1