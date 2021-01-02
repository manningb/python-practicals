import random

animal = 'elephant'
letter = animal[1]

def animalPrint():
    # printing each letter of the string
    for i in range(len(animal)):
        print(f"animal[{i}]: {animal[i]}")

    # testing out string concatenation with random amounts
    randomWord = ''
    for i in range(random.randint(0, len(animal))):
        randomWord = randomWord + random.choice(list(animal))
    print(f"The concatenation of the random letters is: \'{randomWord}\'.\n")    

def main():
    # https://stackabuse.com/writing-to-a-file-with-pythons-print-function/ code for printing stdout to file
    import sys
    original_stdout = sys.stdout # Save a reference to the original standard output
    with open('p2p4.txt', 'w') as f:
        sys.stdout = f # Change the standard output to the file we created.
        animalPrint()
        sys.stdout = original_stdout # Reset the standard output to its original value
    
    animalPrint()
    try:
        letterNum = int(input(f"Please input a number between 0 and {len(animal) - 1}\n"))
        print(f"Letter {letterNum} in the variable animal is: {animal[letterNum]}")
    except:
        print("The number must be between 0 and 7.")

if __name__ == "__main__":
    main()