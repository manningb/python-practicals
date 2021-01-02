"""
define function to convert any number with base less than or equal to 16 to decimal:
    define lettertonumbers dictionary:
        this stores each letter and its value (in hexadecimal essentially) but will work with any base greater than 10 and less than 16
    initialise quotient variable to 1 (greater than 0)
    while True:
        calc quotient
        cal remainder
        set the integerIn to be the value of the quotient
        if char is greater than 9:
            convert using dictionary to letter
            add to remainders variable
        else:
            add to remainders variable
    once for loop is finished 
    return remainders

take inputs of base and int
print output of function
"""
def baseToDec(integerIn, baseIn):
    # function to convert numbers in decimal to specific base
    numLetters = {
    10:'a',
    11:'b',
    12:'c',
    13:'d',
    14:'e',
    15:'f',
    }
    remainders = ''
    decimal = 0
    while True:
        quotient = integerIn // baseIn
        remainder = integerIn % baseIn
        integerIn = quotient
        if remainder > 9:
            remainders += (numLetters.get(remainder).upper())
        else:
            remainders += str(remainder)
        if quotient == 0:
            break
    return remainders[::-1]

integerIn = int(input('Please input a positive decimal number: '))
if integerIn < 0:
    print('You must enter a positive number.')
else:
    baseIn = int(input('Please enter the base of the number you would like to convert it to (2, 16): '))
    if 1 < baseIn < 17:
        print(f'{integerIn} in base {baseIn} is {baseToDec(integerIn, baseIn)}')
    else:
        print('You must enter a base in the specified range (2, 16).')