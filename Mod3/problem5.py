'''
#5. Print 3 words with a | character (called a pipe) in between them.
Use the appropriate keyword argument in print() to do so.
'''

words = "Hello there world"
three_words = words.split(" ") 
print("|".join(three_words))
