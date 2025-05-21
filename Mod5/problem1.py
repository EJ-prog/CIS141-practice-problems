'''
#1. Prompt the user for a positive integer n. 
Use a while loop to sum all the integers from 1 up to n.
Print the final sum.
'''

n = int(input("Please give me a positive number: "))
loop = 1
sum = 0;
while (loop <= n):
  sum += loop
  loop = loop + 1
print(sum)
