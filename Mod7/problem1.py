'''
#1. Write a function called count_vowels(input) that takes a string
and returns the number of vowels (a, e, i, o, u) in it.
'''

def count_vowels(input):
    vowels = 0
    input = input.tolower() #Are we supposed to ignore case or just count lowercase vowels?
    for words in input:
        if ("a" in words or "e" in words or "i" in words or "o" in words or "u" in words):
            vowels += 1
    return vowels
