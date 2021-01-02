"""
get input from user
i = 1
j = 1
while i <= input:
    print(i*j, end=' ')
    if j less than input:
        print(new line)
        increment i 
        make j = 1 again
"""

userinput = int(input('Please input an integer number: '))
i = 1
j = 1

while i <= userinput:
    if j == 1:
        print('| ', end='') # table lines
    print(i*j, end = '\t') 
    j += 1
    if j > userinput:
        print(' |', end='') # table lines
        print()
        i += 1
        j = 1