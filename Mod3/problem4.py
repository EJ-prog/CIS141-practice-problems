'''
#4. Prompt the user for: a word, a first index, and a last index.
Slice the word at the indexes provided by the user and print to the screen.
'''

word = input("Could you please give me a word? ")
first_index = int(input("At what index would you like to start slicing the word? "))
last_index = int(input("At what index do you want to stop slicing the word? "))
print(word[first_index:last_index])
