"""
def countCatorDog
    catCount, dogCount = 0, 0
    cat = 'cat'
    dog = 'dog'
    for loop from 0 to length of input
        if slice of 3 letters equals cat
            increment catcount
        elif slice of 3 letters equals dog
            increment dogcount
    if catcount == dogcount
        return catcount
    else
        return false

take str input
countCheck = countcatordog(intput)
if countCheck:
    print same number
else:
    print not same number
"""

def countCatOrDog(strInput):
    cat = 'cat' #created variables so these could be changed in the future
    dog = 'dog'
    catCount = 0
    dogCount = 0
    for i in range(0, len(strInput)):
        if strInput[i:i+len(cat)] == cat:
            catCount += 1
        elif strInput[i:i+len(dog)] == dog:
            dogCount += 1
    if catCount == dogCount:
        return (True, catCount)
    else:
        return (False, catCount, dogCount)

strInput = input('Please input a string: ')
countCheck = countCatOrDog(strInput)
if countCheck[0]:
    print(f'There were the same number ({countCheck[1]}) of cats and dogs.')
else:
    print(f'There were not the same number of cats ({countCheck[1]}) and dogs ({countCheck[2]}).')