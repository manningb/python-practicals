"""
define pal function that takes string as input
    for range of half the length of the string:
        if string[i] == string[lengeth of string - 1 -i]
            continue
        else
            return False if a letter isnt the same at the opposite index
    return true if loop runs through whole string

take input
run function
print output
"""

def iterativeIsPal(stringIn):
    # Returns true if given string is a palindrome, else false
    for i in range(len(stringIn)//2):
        if stringIn[i] == stringIn[len(stringIn)-i-1]:
            continue
        else:
            return False
    return True

stringIn = str(input('Please input a string: '))
if iterativeIsPal(stringIn):
    print(f'{stringIn} is a palindrome.')
else:
    print(f'{stringIn} is not a palindrome.')