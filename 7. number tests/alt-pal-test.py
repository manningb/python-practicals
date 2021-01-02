"""
main function: takes in string and returns true if palindrome else false
    sub function toChars:
        convert string to lower
        initalise empty string variable
        for letter in lower string:
            if letter is a letter in the alphabet  
                add letter to end of empty string variable
        return string variable with all letters
    
    sub function isPal():
        return whether string palindrome or not (true or false)
        if length of string <= 1:
            print About to return True from isPal from the base case
            return True
        else: 
            result = (first letter == last letter) and (isPal(string minus first and last letter))
            print About to return result', result, 'from isPal with argument', s
            return result
            
    return isPal(tochars(input))

take string input
while string not empty:
    if ispalindrome(input)
        print(true)
    else:
        print false
    take string input
finished!

"""

# Program to check whether a string is a palindromes
# Prompts the user for strings and checks each one
# Exits when an empty string is entered
def isPalindrome(s):
    """Checks whether the string s is a palindrome
    Assumes s is a str.
    Returns True if the letters in s form a palindrome;
    Returns False otherwise.
    Case and non-letters are ignored."""

    def toChars(s):
        """Converts a string to lowercase and removes non-letters
        Assumes s is a str.
        Converts uppercase letters to lowercase and removes non-letters."""
        # First of all, convert uppercase letters to lowercase
        s = s.lower()
        # Start with an empty string
        letterstring = ''
        # Go through s...
        for c in s:
            # ... and add the character to the string if it is a letter
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letterstring += c
        return letterstring

    def isPal(s):
        """Checks whether the string s is a palindrome
        Assumes that s is a str with only lowercase letters and no non-letters.
        Returns True if s is a palindrome;
        Returns False otherwise.
        Recursive function.
        Has print statements to trace its operation."""
        print('isPal function called with argument', s)
        if len(s) <= 1:
            # A palindrome of length 0 or 1 is a palindrome
            print('About to return True from isPal from the base case')
            return True
        else:
            # Compare the first and the last letters and check the remainder of the string
            result = s[0] == s[-1] and isPal(s[1:-1])
            print('About to return result', result, 'from isPal with argument', s)
            return result

    return isPal(toChars(s))

str = input('Enter a string (empty string to exit): ')
while str != '':
    if isPalindrome(str):
        print(str, 'is a palindrome')
    else:
        print(str, 'is not a palindrome')
    str = input('Enter a string (empty string to exit): ')
print('Finished!')