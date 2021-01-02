"""
fucntion that takes string as input
    count equal 0
    stringIn = lowercase stringIn
    for i in range of length of string
        if first two letters = co and last letter = e and third letter is alpha
            count += 1
    return count

stringIn = input from user
countCode = codeCheck(stringIn)
if countCode:
    print number of times
else:
    print no
""" 

def codeCheck(stringIn):
    # count how many times the letters co followed by a letter followed by e appears in a given string
    count = 0
    stringIn = stringIn.lower()
    for i in range(len(stringIn)-3):
        if stringIn[i+3] == 'e' and stringIn[i:i+2] == 'co' and (stringIn[i+2]).isalpha() :
            count += 1
    return count

stringIn = str(input('Please input a string: '))
countCode = codeCheck(stringIn)
if countCode:
    print(f'The string \'co_e\' was found {countCode} times.')
else:
    print(f'The string \'co_e\' was not found.')