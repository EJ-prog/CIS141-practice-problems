'''
#2. Create a list of strings. 
Write code that counts how many times the word "Olympic" appears in the list,
and then print the count.
'''

count = 0
string_list = ["Olympic College", "Olympic", "College", "Bremerton", "Poulsbo", "Shelton"]
for strings in string_list:
    if ("Olympic" in strings):
        count += 1
print(count)
