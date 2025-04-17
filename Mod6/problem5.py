'''
#5. Create a list of integers. 
Use a loop to build a new list 
where each element is the square 
of the corresponding element in the
original list. Print the new list.
'''

numbers = [-20, 19, -40, 37, -27, -17, -63, 39, 59, 18, -5, 23, 0]
squared = []
for nums in numbers:
    squared.append(nums * nums)
print(squared)
