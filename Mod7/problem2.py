'''
#2. Write a function called is_palindrome(s) that checks whether a string is a palindrome
(reads the same forward and backward, ignoring case). The function should
returns either True or False.
'''
#ask about ignoring spaces
def is_palindrome(s):
    s = s.lower()
    i = 0
    half = int(len(s)/2)
    for i in range(half):
        if (s[i] != s[len(s)-1-i]):
            return False
    return True
