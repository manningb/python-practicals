"""
take input from user
i = 0
while i < 22:
    print i and print i*input

"""

userinput = int(input('Please input a number: '))
i = 0

print(f'Times {userinput} Table')
while i < 21:
    print(f'|{i}\t|{i * userinput}\t|')
    i += 1