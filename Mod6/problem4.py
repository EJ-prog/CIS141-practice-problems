'''
#4.  Create a list of integers. 
Write code that counts how many numbers are positive 
and how many are negative, then print both counts.
'''

numbers = [-20, 19, -40, 37, -27, -17, -63, 39, 59, 18, -5, 23, 0]
negatives = 0
positives = 0
for nums in numbers:
    if (nums < 0):
        negatives += 1
    elif (nums > 0):
        positives += 1
print(f"There are {negatives} negative numbers in the list.")
print(f"There are {positives} positive numbers in the list.")
