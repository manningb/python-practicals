"""
define pal function that takes string as input
    initalise variable containing valid chars
    
"""

def palindrome(strIn):
    i = 0
    j = len(strIn)-i-1
    # Returns true if given string is a palindrome, else false
    letterCheck = 'abcdefghijklmnopqrstuvwxyz0123456789 *-'
    while i < len(strIn)//2 and j > len(strIn)//2:
        if strIn[j].lower() in letterCheck:
            j -= 1
        if strIn[i].lower() in letterCheck:
            i += 1
            print(i, j)
            if strIn[i] == strIn[j]:
                continue
                i += 1
                j -=1
                
            else:
                return False, "Not a palindrome"
        else:
            return False, "Invalid Character"
    return True, "Palindrome found"

strIn = str(input('Please input an string: '))
while strIn != "":
    print("Palindrome function returned:", palindrome(strIn))
    strIn = str(input('Please input an string: '))

print("Finished!")