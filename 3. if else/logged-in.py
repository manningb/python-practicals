"""
create password string variable]
create count int variable
create loggedin variable as false

while count less than 4 (as 4 is the max number of inputs from user) or logged in is false
    increment count
    if it is the first go
        if the password is correct
            loggedin = true
        else print user has to enter password 3 times
    else
        if password incorrect:
            loggedin = denied
        elif count == 4 and password correct
            loggedin = true

if loggedin is true
    print you have successfully loggedin
elif loggedin is denied
    print you have been denied access
"""

password = 'password'
logged_in = False
count = 0

#login process
while logged_in == False:
    count += 1
    passcheck = input('Please input your password: ')
    if count == 1:
        if password == passcheck:
            logged_in = True
        else:
            print('Sorry, the password is wrong.\nPlease enter the password 3 times.')
    else:
        if password != passcheck:
            logged_in = 'Denied'
        elif count == 4 and password == passcheck:
            logged_in = True

#login message       
if logged_in == True:
    print('You have successfully logged in.')
elif logged_in == 'Denied':
    print('You have been denied access.')