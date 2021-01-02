"""
take input 
initialise variables for each of the ranges
while input > 0:
    if input in range
        increment variable
        # do same for each range
    take input 
print each int value
"""
count0 = 0
count20 = 0
count40 = 0
count60 = 0
count80 = 0
count100 = 0
countgt100 = 0
userinput = int(input('Please input a positive integer: '))
while userinput >= 0:
    if userinput == 0:
        count0 += 1
    elif userinput <= 20:
        count20 += 1
    elif userinput <= 40:
        count40 += 1
    elif userinput <= 60:
        count60 += 1
    elif userinput <= 80:
        count80 += 1
    elif userinput <= 100:
        count100 += 1
    else:
        countgt100 += 1
    userinput = int(input('Please input a positive integer: '))

print('\nThe results from the inputted numbers:')
print(f'{count0} equal to 0')   
print(f'{count20} greater than 0 and less than or equal to 20')   
print(f'{count40} greater than 20 and less than or equal to 40')   
print(f'{count60} greater than 40 and less than or equal to 60')   
print(f'{count80} greater than 60 and less than or equal to 80')   
print(f'{count100} greater than 80 and less than or equal to 100')   
print(f'{countgt100} greater than 100')   