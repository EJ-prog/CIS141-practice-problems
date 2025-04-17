'''
#3. Create a list of strings. 
Write code to create a new list that includes only the strings longer than three characters.
Print the resulting filtered list.
'''

string_list = ["the", "fruit", "a", "vegetable", "several", "shops", "do", "sell", "these"]
long_strings = []
for strings in string_list:
    if (len(strings) > 3):
        long_strings.append(strings)
print(long_strings)
