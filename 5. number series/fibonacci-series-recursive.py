"""
def fib(input):
    def fibNum(input):
        if input = 0 or 1
            return 1
        else:
            return fibNum(input - 1) + fibNum(input - 2)
    for i in of int input
        print that fibonnaci num

take input from user
if greater than or equal to
    print fibonnaci(input)
else
    print error

## NOTE I took it to mean 0 as input was asking for 0 terms of the fibonnaci sequence to be printed
When 1 is entered, 1 number of the fibonnaci sequence is printed (1) and so on
"""
print('Program to print out specified number of terms of the Fibonacci Series.')
def fibonacci(intInput):
    # Function to print sequence of fibonnaci numbers
    def fibNum(intInput):
        # Function to calculate the ith term in the fibonnaci sequence
        if intInput in (0, 1):
            return 1
        else:
            return fibNum(intInput-1) + fibNum(intInput-2)
    
    # prints out each term of fib series
    for i in range(intInput):
        print(fibNum(i), end=" ")

intInput = int(input('Please input a non negative integer: '))
if intInput >= 0:
    fibonacci(intInput)
else:
    print('Error: Integer must be greater than or equal to 0.')