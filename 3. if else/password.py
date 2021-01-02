"""
take password as input
count = 0
while >= 0:
    increment count by one
    take password as input again (ask user to reenter their password)
    if password1 == password2:
        print you guessed your password in {count} times
    else if count = 3 print denied access
"""

password = 'password'
count = 0

while count < 3:
    count += 1
    if password == input('Please input your password again: '):
        print(f'You have successfully logged in.\nYou got your password in {count} guesses.')
        break
    if count == 3:
        print('You have been denied access.')