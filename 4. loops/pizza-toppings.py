"""
take input of both toppings and standard pizza toppings as int

check that std toppings is less than total toppings - constraint for combination calculation
check that both are greater or equal to 0
if either are false ask for input again

initialise factorial variables
for i in range number of toppings
    factorial for N mulitplied by i equals factorial for N 
    if i < number of std toppings:
        factorial for K mulitplied by i equals factorial for K 
    if i < toppings - stdtoppings:
        factorial for N-K mulitplied by i equals factorial for N-K 

calculate combinations using given formula
print number of possible combinations
"""
print('Hello manager,')

while True:
    toppings = int(input('Please input the total number of toppings offered: '))
    stdtoppings = int(input('Please input the number of toppings on a standard pizza: '))
    if stdtoppings > toppings:
        print('Total number of toppings must be greater than the number of toppings on a standard pizza.')
    elif toppings < 0 or stdtoppings < 0:
        print('Both numbers must be greater than or equal to 0. Please try again.')
    else:
        break
        # stop asking for input as the necessary constraints are met

nfactorial = 1
kfactorial = 1
nminuskfact = 1
for i in range(toppings):
    nfactorial *= i + 1
    if i < stdtoppings:
        kfactorial *= i + 1
    if i < toppings - stdtoppings:
        nminuskfact *= i + 1

combos = int(nfactorial/(kfactorial*(nminuskfact)))

print(f'There are {combos} possible combinations of pizzas.')
