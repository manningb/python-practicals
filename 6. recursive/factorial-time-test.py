import time
import sys

sys.stdout = open("p14p2.txt", "w")
print('Program to calculate Factorial.')
countN, countR, number = 0, 0, 0
number = 950
while number < 1050:
    start_timeN = time.time() 
    #Factorial - Non-Recursive from p12p1
    nfactorial = 1
    if number < 0:
        print('Error: Number entered was less than 0.')
    else:
        for i in range(number):
            nfactorial *= i + 1
    print('Factorial of', number, 'is', nfactorial)
    end_timeN = time.time() 

    start_timeR = time.time() 
    #Factorial - Recursive from p13p6
    def factorial(inputNum):
        # This function returns the factorial of a positive integer
        if inputNum == 0:
            return 1
        else:
            return inputNum * factorial(inputNum - 1)

    if number >= 0:
        print(f'\nThe factorial of {number} is {factorial(number)}.')
    else:
        print('Error: Input must be a non-negative integer.')
    end_timeR = time.time() 

    print(f'\n\nInput = {number}\nNon-Recursive = {end_timeN-start_timeN}\nRecursive = {end_timeR-start_timeR}\n')
    if end_timeN - start_timeN > end_timeR - start_timeR:
        countN += 1
    else:
        countR += 1
    number += 1

    print(f'Recursive took longer than Non {(countR/(countR + countN))*100}% of the time.')
sys.stdout.close()
