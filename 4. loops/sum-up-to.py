"""
prompt user for poisitive integer
set sum = 0

while positive integer greater than 0
    for i in range(positive):
        add i + 1 to sum
    print sum
    set sum to 0
    ask for input again
"""


positive = int(input('Please input a positive integer: '))
sum = 0
while positive > 0:
    for i in range(positive):
        sum += i + 1
    print(f'The sum of all positive integers up to {positive} = {sum}.')
    sum = 0
    positive = int(input('Please input a positive integer: '))

