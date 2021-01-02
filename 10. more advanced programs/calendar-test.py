"""
Program to calculate the date, month and year in the 2020-2021
academic year of a given day.

take input of day int from user

while input > 0:
    print what user entered

    if input less than or equal to 30
        print Day number, input, is, input, September 2020
    elif day less than 61 (30 days in September + 31 days in October)
        print Day number, input, is, (input - 30), Octoboer 2020 
        #Here we are subtracting the number of days in September from the input 
        #to get the date in the month of october
        #I will use elifs to evaluate for all of the months in the same way
        #The number subtracting will be cumulative each month so for August for instance 
        #it will be the total number of days in all other months of the year: 334
    
    take input from the user again

print Finished!
"""
print('Program to calculate the date, month and year in the 2020-2021\nacademic year of a given day.')
day_find = int(input('Enter the day for which you want to find the date (an integer): '))

while day_find > 0: #if user enters 0 or any negative number program will exit
    print('You entered:', day_find)
    if day_find > 365: #Check if number is greater than 1 year
        print('Day number', day_find, 'is not in the 2020-2021 academic year!')
    elif day_find <= 30: #September
        print('Day number', day_find, 'is', day_find, 'September 2020')
    elif day_find <= 61: #October
        print('Day number', day_find, 'is', day_find - 30, 'October 2020')
    elif day_find <= 91: #November
        print('Day number', day_find, 'is', day_find - 61, 'November 2020')
    elif day_find <= 122: #December
        print('Day number', day_find, 'is', day_find - 91, 'December 2020')
    elif day_find <= 153: #January
        print('Day number', day_find, 'is', day_find - 122, 'January 2021')
    elif day_find <= 181: #February
        print('Day number', day_find, 'is', day_find - 153, 'February 2021')
    elif day_find <= 212: #March
        print('Day number', day_find, 'is', day_find - 181, 'March 2021')
    elif day_find <= 242: #April
        print('Day number', day_find, 'is', day_find - 212, 'April 2021')
    elif day_find <= 273: #May
        print('Day number', day_find, 'is', day_find - 242, 'May 2021')
    elif day_find <= 303: #June
        print('Day number', day_find, 'is', day_find - 273, 'June 2021')
    elif day_find <= 334: #July
        print('Day number', day_find, 'is', day_find - 303, 'July 2021')
    elif day_find <= 365: #August
        print('Day number', day_find, 'is', day_find - 334, 'August 2021')
    
    day_find = int(input('Enter the day for which you want to find the date (an integer): '))

print('Finished!')