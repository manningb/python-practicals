"""
def letter fix functin:
    takes string as inputted
    uses a for loop to replace any unwanted characters and return the desired string

def pal function that takes str as input:
    run the letter fix function
    for i range of half the length of the string:
        if the ith char of the string equals the length minus the ith character minus 1
            continue
        else
            return false
    return true if function continues through the whole string

take string as input
while loop while string not empty
    run pal function
    print output
"""
def letterfix(strIn):
    # function to remove any unwanted characters from a string
    letterCheck = 'abcdefghijklmnopqrstuvwxyz0123456789 '
    for i in strIn:
        if i.lower() not in letterCheck:
            strIn = strIn.replace(i, "")
    return strIn

def palindrome(strIn):
    # Returns true if given string is a palindrome, else false
    strIn = letterfix(strIn)
    for i in range(len(strIn)//2):
        if strIn[i] == strIn[len(strIn)-i-1]:
            continue
        else:
            return False
    return True


strIn = str(input('Enter a string (empty string to exit): '))
#run till empty string inputted
while strIn != "":
    # run pal function on the inputted string and return output
    if palindrome(strIn):
        print(strIn, 'is a palindrome.')
    else:
        print(strIn, 'is not a palindrome.')
    strIn = str(input('Enter a string (empty string to exit): '))

print("Finished!")




