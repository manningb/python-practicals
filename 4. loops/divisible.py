"""
input = input positive number
initialise variables for divisible by 2, 3, 5 and 7 to no
while input > 0:
    if input % 2 == 0:
        count = yes
    do same for 3, 5, 7
    re initialise variables

    input = input positive number
"""
times = 'times'
positive = int(input('Please input a positive number: '))
div2, div3, div5, div7 = 'No', 'No', 'No', 'No'
while positive > 0:
    if positive % 2 == 0:
        div2 = 'Yes'
    if positive % 3 == 0:
        div3 = 'Yes'
    if positive % 5 == 0:
        div5 = 'Yes'
    if positive % 7 == 0:
        div7 = 'Yes'
    print(f'The number of times {positive} is:')
    print(f'- divisible by 2: {div2}') 
    print(f'- divisible by 3: {div3}')
    print(f'- divisible by 5: {div5}')
    print(f'- divisible by 7: {div7}')
    div2, div3, div5, div7 = 'No', 'No', 'No', 'No'
    positive = int(input('Please input a positive number: '))
