'''
1. Write a program that takes as input an amount of currency (a float) and an exchange rate to another currency
(a float) and prints out the value of the original amount in the other currency. For the exchange rate, pick
two currencies and use today’s exchange rate.
When the currency amount is entered by the user, the program should check that the amount is non-negative.
If the amount is negative, the message “Amount must be >= 0. Please try again.” should be printed out and
the program should exit.
Save this program as p4-5p1.py

Algorithm design:
1. Ask for input for the currency and exchange rate
2. Check if both amounts are numbers - if not start again
3. Check if the currency amount is positive - if not start again
4. Print the exchanged amount
'''

# exchange rates on 6 October 2020 at 15:00, with symbol for output
exchange = {'EUR:USD' : [1.1778, '$'], 
            'EUR:GBP' : [0.9095, '£']}

# loop to take input from user and return converted amounts
try:
    amount = float(input('Please input an amount of euro:\n'))
    if amount <= 0: 
        raise ValueError('Amount less than 0.')
    for key, value in exchange.items():
        if input(f'Would you like to convert using: {key}? (y/n)\n').lower() in ('y', 'yes'):
            print(f'€{round(amount, 3)} = {value[1]}{round(amount * value[0], 3)} on 6th of October 2020 at 15:00') 
except:
    print('Amount must be >= 0. Please try again.')