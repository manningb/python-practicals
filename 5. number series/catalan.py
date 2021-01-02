"""
take input from user
initialise catalan to 1
for i in range input + 1
    print(catalan)
    catalan = (2*catalan*(2*i + 1))//(i + 2) #catalan number formula given in q
"""

print('Catalan Numbers Program:')
number = int(input('Please input an integer: '))
catalan = 1
for i in range(number + 1):
    print(f'C{i}: {catalan}')
    catalan = (2*catalan*(2*i + 1))//(i + 2) 