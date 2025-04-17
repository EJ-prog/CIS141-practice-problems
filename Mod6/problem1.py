'''
#1. Create a list of integers (you get to pick!). 
Write code to iterate through the list and calculate the sum of all even numbers. 
Print the resulting sum.
'''

numbers = [41, 29, 18, 48, 68, 35, 60, 73, 39, 84]
even_nums = []
for num in numbers:
    if (num % 2 == 0):
        even_nums.append(num)
sum_of_even_nums = sum(even_nums)
print(sum_of_even_nums)
