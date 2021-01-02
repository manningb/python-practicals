import os

i = 0
practicalno = int(input('Please input the pratical number: '))
limit = int(input('Please input the number of files: '))
while True:
    fh = open(f"p{practicalno}p{i+1}.py", "w")
    i += 1
    if i == limit:
        break



#os.path.exists(f"p{practicalno}p{i}.py")