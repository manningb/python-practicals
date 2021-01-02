"""
fucntion that takes string as input
    stringIn = lowercase stringIn
    for i in range of length of string
        if characters i+1 to i+4 equal xyz and char i not equal .
        or i ==0 and chars i to i+3 equal xyz
            return count

stringIn = input from user
countCode = codeCheck(stringIn)
if countCode:
    print number of times
else:
    print no
""" 

def xyzCheck(stringIn):
    # check if xyz is found without a full stop preceding it in a given string
    stringIn = stringIn.lower()
    for i in range(len(stringIn)):
        if (stringIn[i+1:i+4] == 'xyz' and stringIn[i] != '.') or (i == 0 and stringIn[i:i+3] == 'xyz'):
            return True
    else:
        return False

stringIn = str(input('Please input a string: '))
if xyzCheck(stringIn):
    print(f'True: The string \'xyz\' without . before it was found in {stringIn}.')
else:
    print(f'False: The string \'xyz\' without . before it was not found in {stringIn}.')