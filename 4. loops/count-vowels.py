"""
take input from user
while input != empty string:
    initialise count to 0
    for i in input:
        if i in [vowels list]
            count += 1
    print(count)
"""

print('Program to calculate number of vowels in a string.')
string = input('Please input a string: ')
while string != '':
    count = 0
    for i in string:
        if i.lower() in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    print(f'There are {count} vowels in {string}.')
    string = input('Please input a string: ')

