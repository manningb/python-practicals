"""
Pseudo code
for loop in range 3
    take input
    if even
        remove from odd numbers list

if 1 odd num
    large odd = this num
elif more than 1 odd num
    if second odd > first odd
        large odd = second odd
    else
        large odd = first odd
    if three odd numbers inputted
        if third odd > previous largest odd
            large odd = third odd

if no odd numbers
    print no odd numbers
else 
    print largest odd is x
"""
odd_num = [] #empty list to store odd numbers

for i in range(3):
    odd_num.append(int(input('Please input a number: '))) #take input as integer and append to input list
    if odd_num[len(odd_num)-1] % 2 == 0: #check if input was even
        odd_num.pop() #if even remove the item from the list
    
if len(odd_num) == 1: #if this is the first odd number, assign it as the large number
    large_odd = odd_num[0]
elif len(odd_num) > 1:
    if odd_num[1] > odd_num[0]: #check odd number 2 against first odd number
        large_odd = odd_num[1]
    else:
        large_odd = odd_num[0]
    if len(odd_num) == 3:
        if odd_num[2] > large_odd: #check odd number 3 against largest of first 2 odd numbers
            large_odd = odd_num[2]

if len(odd_num) == 0:
    print('There were no odd numberes inputted.')
else:
    print(f'The largest odd number you inputted was {large_odd}.')    
