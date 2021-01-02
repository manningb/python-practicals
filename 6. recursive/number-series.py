"""
def seriesNum(input):
    count variable = 0
    if count is 0:
        count += 1
        initiliase empty series to store series
        for i in range input 
            print calculating term i of series
            add to series
        print series
        count += 1
    
    if intInput == 0:
        return 13
    elif intInput == 1:
        return 8
    elif count == 1:
        currentNum = seriesNum(intInput-2) + 13 * seriesNum(intInput-1)
        return currentNum

take input from user
while input > 0
    set count var = 0
    seriesNum(input)
    ask for input
else
    print error
"""

def seriesNum(intInput):
    global count
    if count == 0:
        count += 1 # increase count so this only runs on the first iteration
        series = []
        for i in range(intInput+1):
            print(f'\nCalculating term {i} of the Series')
            series.append(seriesNum(i))
        print(f'\nThe series for n = {intInput} is:')
        print(*series, sep=" ")
        count += 1 # increase count again

    if intInput == 0:
        return 13
    elif intInput == 1:
        return 8
    elif count == 1: # This ensures it doesnt run after the series has been printed
        currentNum = seriesNum(intInput-2) + 13 * seriesNum(intInput-1)
        print(f'Current number - {intInput}, Current series number {currentNum}')
        return currentNum

intInput = int(input('Please input a positive integer: '))
while intInput >= 0:
    count = 0
    seriesNum(intInput)
    intInput = int(input('\nPlease input a positive integer: '))
else:
    print('Error: Integer must be greater than 0.')
