'''
#3. Prompt the user for a sentence and a word to try to find in that sentence. 
Have the program print out whether the word was found in the sentence. (i.e. True or False)
'''

sentence = input("Please type in a sentence of your choice: ")
word = input("What word would you like to look for in your sentence? ")
print (word in sentence)
