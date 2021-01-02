'''
Practical Sheet 4
3. Write a program that takes as input an amount (a float), divides the amount in the ratio 60:40, calculates
the tax due according to two dierent tax rates (13.5% on the larger amount and 23% on the smaller), and
prints out the initial amount, the two dierent tax amounts, the total tax and the total amount (initial amount
plus taxes).
Save this program as p4p3.py.

Algorithm design
1. Ask the user for input of how much money
2. If the amount is less that 0 exit the program
3. Define tax rates and calculation for tax amounts
4. Return the required values to the user
'''

amount = float(input('How much money in Euro?\n'))
if amount >= 0:
    # tax rates
    lowrate = 0.23
    highrate = 0.41

    # tax amounts
    lowband = amount * 0.6 * lowrate
    highband = amount * 0.4 * highrate
    totaltax = lowband + highband

    # info for user
    print(f'\nThe inital income: €{amount}')
    print(f'The amount at the lower rate ({lowrate * 100}%): €{round(lowband, 3)}')
    print(f'The amount at the higher rate ({highrate * 100}%): €{round(highband, 3)}')
    print(f'The total tax: €{round(totaltax, 3)}')
    print(f'The net income (inital amount less taxes): €{round(amount - totaltax, 3)}')
else:
    print('Amount of income must be >= 0. Please try again.')