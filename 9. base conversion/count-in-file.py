"""
function to read in filename and direct counts to file:
    initialise two lists for counts and symbols
    with open of the file:
        while True:
            i = one char of the file
            if i is not a character:
                break
            for j in range(8):
                if character == the jth char
                    count of the jth item in counts list increment by one
    
    initialise a check var to True
    for loop over 8, adding two each time
        check if ith count != i+1th count:
            print not equal
            checker = False
        else:
            print equal
    return checker, counts and countsof

take filename as input
run function
"""

def webChecker(fileName):
    #Function to check the number of brackets in a file and return true if each bracket has an even number of opening and closings
    countsOf = ['[', ']', '(', ')', '{', '}', '<', '>']
    counts = [0, 0, 0, 0, 0, 0, 0, 0]

    with open(fileName, 'r') as fileForInput:
        while True:
            i = fileForInput.read(1)
            if not i:
                break
            for j in range(8):
                if i == countsOf[j]:
                    counts[j] += 1
                
    checker = True
    for i in range(0, 8, 2):
        if counts[i] != counts[i+1]:
            print(f'There was not an equal number of {countsOf[i]+" - "+str(counts[i])} and {countsOf[i+1]+" - "+str(counts[i+1])}')
            checker = False
        else:
             print(f'There was an equal number of {countsOf[i]+" - "+str(counts[i])} and {countsOf[i+1]+" - "+str(counts[i+1])}')
    return checker, countsOf, counts

fileName = str(input('Please input the name of the file: '))

if webChecker(fileName)[0]:
    print(f'Congratulations! The file {fileName} did have the same number of left and right brackets.')
else:
    print(f'Unfortunately, the file {fileName} did not have the same number of left and right brackets.')