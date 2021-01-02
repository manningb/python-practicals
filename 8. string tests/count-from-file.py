"""
function to read in filename and direct counts to file:
    initialise two lists for counts and symbols
    try:
        for line in file:
            for i in range of length of line:
                if current i = symbol1:
                    count1 += 1
                etc ...
        
        store origin stdout to variable
        with open (append results.txt) as var:
            redirect stdout to variable
            print counts
            direct stdout to original stdout using varialble
            see here: https://stackabuse.com/writing-to-a-file-with-pythons-print-function/
    except:
        print could not read file with error
"""
import sys
from os import path
from datetime import date

def results_handler(counts, countsOf):
    # function to handle the results of the html reader function
    results = 'results.txt'
    if path.exists(results):
        output_choice = int(input('Results file found. Would you like to\n1. Append to end of file\n2. Create a new file\n3. Print output to console\nInput the number corresponding to your choice and press enter. '))
        if output_choice == 1:
            with open(results, 'a') as f:
                print('Symbol\t|\tCounts', file=f)
                for i in range(len(counts)):
                    print(repr(countsOf[i])[1:-1], end='\t|\t', file=f)
                    print(counts[i], end='\n\n', file=f)
                print(f'Results printed to {results}')
        elif output_choice == 2: 
            results = f'results {date.today()}.txt'
            with open(results, 'w') as f:
                print('Symbol\t|\tCounts', file=f)
                for i in range(len(counts)):
                    print(repr(countsOf[i])[1:-1], end='\t|\t', file=f)
                    print(counts[i], end='\n\n', file=f)
                print(f'Results printed to {results}')
        elif output_choice == 3:
            print('Symbol\t|\tCounts')
            for i in range(len(counts)):
                print(repr(countsOf[i])[1:-1], end='\t|\t')
                print(counts[i], end='\n\n')
        else:
            print(f'{output_choice} choice not found.')
    else:
        with open(results, 'w') as f:
                results = f'results {date.today()}.txt'
                print('Symbol\t|\tCounts', file=f)
                for i in range(len(counts)):
                    print(repr(countsOf[i])[1:-1], end='\t|\t', file=f)
                    print(counts[i], end='\n\n', file=f)
                print(f'Results file created and printed to {results}')

def webChecker(fileName):
    # counts the number of certain symbols in a html file
    if path.exists(fileName):
        print('HTML file found.')
    else:
        print('HTML file not found.')
        exit()

    countsOf = ['<', '>', '\n', 'e', '<!--', '-->']
    counts = [0, 0, 0, 0, 0, 0]
    with open(fileName, 'r') as fileForInput:
        for line in fileForInput:
            for i in range(len(line)):
                if line[i] == countsOf[0]:
                    counts[0] += 1
                if line[i] == countsOf[1]:
                    counts[1] += 1
                if line[i:i+2] == countsOf[2]:
                    counts[2] += 1
                if line[i] == countsOf[3]:
                    counts[3] += 1
                if line[i:i+4] == countsOf[4]:
                    counts[4] += 1
                if line[i:i+3] == countsOf[5]:
                    counts[5] += 1
    return results_handler(counts, countsOf)


fileName = str(input('Please input the name of the file: '))
webChecker(fileName)