"""
define function to convert any number with base less than or equal to 16 to decimal:
    define lettertonumbers dictionary:
        this stores each letter and its value (in hexadecimal essentially) but will work with any base greater than 10 and less than 16
    reverse the integer inputted
    initialise decimal variable to 1
    for i in the range of the length of the input:
        let char variable equal the ith character in the input
        if char is a letter:
            convert using dictionary to number
            multiply by base to the power of i
            add to decimal variable
        else:
            multiply the char by the base to the power of i
            add to decimal variable
    once for loop is finished 
    return decimal

take inputs of base and int
print output of function
"""
def baseToDec(integerIn, baseIn):
    # function to convert numbers in specified base to decimal
    letterNums = {
    'a':10,
    'b':11,
    'c':12,
    'd':13,
    'e':14,
    'f':15,
    }
    reversed = integerIn[::-1]
    decimal = 0
    for i in range(len(reversed)):
        char = reversed[i]
        if char.isalpha():
            decimal += (letterNums.get(char.lower()))*baseIn**i
        else:
            decimal += int(char)*baseIn**i
    return decimal

integerIn = str(input('Please input a string of digits in any base between 1 and 16 inclusive: '))
baseIn = int(input('Please enter the base of the number you entered: '))
if 1 > baseIn > 16:
    print('You must enter a base between 1 and 16')
else:
    print(f'{integerIn} in base decimal is {baseToDec(integerIn, baseIn)}')