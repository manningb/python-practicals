'''
Write a program that takes as input a single length (a float) and calculates the following:
• The area of a square with side of that length
• The volume of a cube with side of that length
• The area of a circle with radius of that length
• The volume of a sphere with radius of that length
• The volume of a cylinder with radius of that length and side of that length
Import the math module and use the constant math.pi for the value π.
When the length is entered by the user, the program should check that it is non-negative. If the length is
negative, the message “Length must be >= 0. Please try again.” should be printed out and the program
should exit.
Save this program as p4-5p2.py
'''

'''
Practical Sheet 4
2. Write a program that takes as input a single length (a float) and calculates the following:
• The area of a square with side of that length
• The volume of a cube with side of that length
• The area of a circule with radius of that length
• The volume of a sphere with radius of that length
• The volume of a cylinder with radius of that length and side of that length
Import the math module and use the constant math.pi for the value .
Save this program as p4p2.py.

Algorithm design
1. Ask user for input of length and how many decimal places
2. Check if length is positive, if not start again
3. Print out the output for each calculation to the user
'''     

from math import pi

length = float(input('Please input a length:\n'))

# input from user
if length >= 0:
    decimal = int(input('How many decimal places would you like the results?\n'))

    # info for user
    print(f'\nThe area of a circle with side of that length is: \n{round((length ** 2)/4 * pi, decimal)}\n')
    print(f'The volume of a cube with side of that length is: \n{round(length ** 3, decimal)}\n')

    length = length * 2
    print(f'The area of a circle with radius of that length is: \n{round(pi * (length / 2) ** 2, decimal)}\n')
    print(f'The volume of a sphere with radius of that length is: \n{round((pi * length ** 3) / 6, decimal)}\n')
    print(f'The volume of a cylinder with radius of that length and side of that length is: \n{round(length * pi * ((length / 2) ** 2), decimal)}\n')
else:
    print('Length must be >= 0. Please try again.')