'''
if (year is not exactly divisible by 4) then (it is a common year)
else
if (year is not exactly divisible by 100) then (it is a leap year)
else
if (year is not exactly divisible by 400) then (it is a common year)
else (it is a leap year)
'''



while True:
    year = int(input('Please input a year:\n'))
    if year % 4 != 0 and year % 100 == 0 or year % 400 != 0:
        print('Common year')
    else:
        print('Leap year')
    choice = input('Would you like to start again?').upper()
    if choice not in ('Y', 'YES'):
        break