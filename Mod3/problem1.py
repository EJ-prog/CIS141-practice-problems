'''
# 1. Prompt the user for a word. Then, prompt the user for how many 
times they'd like that word repeated. Use the skills you learned in 
this module to print the word the correct number of times.
'''

word = input("What word would you like to have repeated? ")
word = word + "\n"
repeat = int(input("How many times would like to repeat this word? "))
print(word * repeat)
