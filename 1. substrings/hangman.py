import random
animals = ['cat', 'horse', 'cow', 'pig', 'elephant', 'tiger']
word = random.choice(animals)
length = len(word)
space = length * '_ '
#print(f'length is {length}')
score = 7
check = False
win = 0
letters_used = []

print(f'Word: {space}\n')
while (score != 0) & (win != length):
    choice = input('Choose a letter from the alphabet\n')
    letters_used = letters_used + [choice] 
    for i in range(length):
        if choice == word[i]:
            temp = list(space)
            temp[i*2] = choice
            space = ''.join(temp)
            win += 1
            check = True
        if i == length - 1:
            if check == False:
                score -= 1
                print(f'You did not pick a correct letter. Score = {score}\n{space}\n')
            else:
                print(f'You picked a correct letter!\n{space}\n')
    check = False
    print("Letters used: ")
    print(*letters_used, sep = ", ", end="\n\n")  

if score == 0:
    print('You did not guess the correct word!')
else:
    print('Congratulations!')