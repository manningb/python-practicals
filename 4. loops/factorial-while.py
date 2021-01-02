"""
prompt user for poisitive integer
set factorial = 1

while positive integer greater than 0
    set i = 1
    while i less than positive int:
        factorial multiplied by i equals factorial
        i += 1
    print factorial
    set factorial to 1
    ask for input again
"""


positive = int(input('Please input a positive integer: '))
factorial = 1
while positive >= 0:
    i = 1
    while i < positive:
        factorial *= i + 1
        i += 1
    print(factorial)
    factorial = 1
    positive = int(input('Please input a positive integer: '))

