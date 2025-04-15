import math
'''
# 3. Create a program that prompts for the side lengths of a triangle and
# computes the area using Heron's formula. 
# (https://en.wikipedia.org/wiki/Heron%27s_formula)
'''

side1 = int(input("What length do you want to make the first side of the triangle? "))
side2 = int(input("For the second side? "))
side3 = int(input("For the third side? "))
s = (side1 + side2 + side3)/2
area = math.sqrt(s*(s-side1)*(s-side2)*(s-side3))

print(f"The area of the triangle with those dimensions is {area}.")