"""
def fibNum(input):
    count variable = 0
    if count is 0:
        count += 1
        initiliase empty series to store fib series
        for i in range input plus 1
            print calculating term i of fib
            add to series
        print series
        count += 1

    if input = 0:
        return 0
    elif input = 1:
        return 1
    elif count == 1:
        fibcurrent = fib(input -1) + fib(input - 2)
        return fibcurrent

take input from user
while input >= 0
    set count var = 0
    fibonnaci(input)
    ask for input
else
    print error

NOTE when 0 is inputted, the program outputs 0 rather than no terms at all
when 1 is inputted, the program outputs 0 1 rather than one term
this can be changed by removing the +1 in the range function of the for loop
which would mean that if 0 is inputted, the prorgam would print no terms etc
"""

def fibNum(intInput):
    global count
    if count == 0:
        count += 1 # increase count so this only runs on the first iteration
        series = []
        for i in range(intInput+1):
            print(f'\nCalculating term {i} of the Fibonacci Series')
            series.append(fibNum(i))
        print(f'\nThe fibonnaci series for {intInput} terms is:')
        print(*series, sep=" ")
        count += 1 # increase count again

    if intInput == 0:
        return 0
    elif intInput == 1:
        return 1
    elif count == 1: # This ensures it doesnt run after the fib series has been printed
        fibCurrent = fibNum(intInput-1) + fibNum(intInput-2)
        print(f'Current number - {intInput}, Current fibonacci number {fibCurrent}')
        return fibCurrent

intInput = int(input('Please input a non negative integer: '))
while intInput >= 0:
    count = 0
    fibNum(intInput)
    intInput = int(input('\nPlease input a non negative integer: '))
else:
    print('Error: Integer must be greater than or equal to 0.')