'''
#2. Prompt the user for their name and their age. Calculate their age next year. 
Use string concatenation to print "Hello, <name>! You are <age1> years old. 
Next year, you will be <age2> years old."
'''

name = input("What is your name? ")
age1 = int(input("What is your current age? "))
age2 = age1 + 1
print("Hello, " + name + "! You are " + age1 + " years old. Next year, you will be " + age2 + " years old.")
