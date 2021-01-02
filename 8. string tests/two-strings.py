"""
define two strings function that takes string 1 and string 2 as inputs
    convert inputs to lower
    if length of first is less than second:
        if end of string 2 for length of  str 1== str 1
            return true and 2 to represent string 2 being the longer string
    else:
        if end of string 1 for length of  str 2== str 2
            return true and 1 to represent string 1 being the longer string

str1 and str2 take as inputs 
if function returns true
    if fucntion returns 1
        print output with 1 as long string
    if function returns 2 
        print output with 2 as long string
else 
    print false
"""

def twoStrings(str1, str2):
    # checks if string1 or string2 is found at the end of the other string
    str1, str2 = str1.lower(), str2.lower()
    if len(str1) < len(str2):
        if str2[len(str2)-len(str1):len(str2)] == str1:
            return (True, 2)
    else:
        if str1[len(str1)-len(str2):len(str1)] == str2:
            return (True, 1)

str1 = str(input('Please input string 1: '))
str2 = str(input('Please input string 2: '))

if (num := twoStrings(str1, str2)):
    if num[1] == 1:
        print(f'String 2 ({str2}) was found the end of String 1 ({str1})')
    else:
        print(f'String 1 ({str1}) was found the end of String 2 ({str2})')
else:
    print('Neither of the strings are at the end of the other.')
