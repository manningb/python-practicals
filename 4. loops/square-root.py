"""
take input from user
initalise i to 0
while True:
    if square of i == number:
        root = i
        break
    elif: square of i > number:
        root = False
        break
    else
        increment i

if root is false
    print no sq rt
else
    print root
"""
print('Program to calculate Integer Square Root of a Number')
number = int(input('Please input an integer: '))
i = 0

if number < 0:
    print('Negative numbers do not have square roots.')
else:
    while number > 0:
        if i**2 == number:
            root = i
            break
        elif i**2 > number:
            root = False
            break
        else:
            i += 1

    if root == False:
        print(f'{number} is not a perfect square root.')
    else:
        print(f'The square root of {number} is: {root}.')