"""
Program to calculate the number of integers evenly divisible by 3, 5, 7 and 11
initilise variables for numbers divisible by 3,5,7,11 to 0
ask user for input of an integer non negative
print what the user enter
if number less than 0:
    print error message
while count < input:
    if count % 3 == 0:
        div_3 += 1
    if count % 5 == 0:
        div_5 += 1 
    if count % 7 == 0:
        div_7 += 1 
    if count % 11 == 0:
        div_11 += 1 

print div_3,5,7,11
print finished
"""

count = 1
div_3 = 0
div_5 = 0
div_7 = 0
div_11 = 0

print('Program to calculate the number of integers evenly divisible by 3, 5, 7 and 11')

number = int(input('Enter a positive integer: '))
print('You entered:', number)

if number < 0: #Check if negative, return an error if so
    print('Number entered should be >= 0.')
else:
    while count <= number :
        if count % 3 == 0:
            div_3 += 1
        if count % 5 == 0:
            div_5 += 1
        if count % 7 == 0:
            div_7 += 1
        if count % 11 == 0:
            div_11 += 1
        count += 1
    print('Number of numbers divisible by 3:', div_3)
    print('Number of numbers divisible by 5:', div_5)
    print('Number of numbers divisible by 7:', div_7)
    print('Number of numbers divisible by 11:', div_11)

print('Finished!')