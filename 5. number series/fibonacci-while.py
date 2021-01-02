"""
take input from user
initialise 3 variables: fib0 fib1 and i
while i < input:
    print(a)
    make the fib1 variable equal to fib0 + fib1, make fib0 equal to fib1
    increment i by 1
"""
print('Program to print Fibonacci Series:')
number = int(input('Please input an integer: '))
fib_0, fib_1, i = 1, 1, 0
while i < number:
    print(fib_0, end=' ')
    fib_0, fib_1 = fib_1, fib_0 + fib_1
    i += 1