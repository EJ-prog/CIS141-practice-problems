'''
#2. Write a Python program that allows users to log their hiking trips. The program
should:
- Use a while loop to repeatedly ask for a hike name and distance in miles
- Save each entry to hiking_log.txt (each hike on a new line)
- When the user presses 0, exit the loop & print the contents of hiking_log.txt
'''

with open("hiking_log.txt", "a") as file:
    user = ""
    while (user != 0):
        user = input("What is the name of the hike and its distance? (Type 0 to exit) ")
        if(user == 0 or user == "0"):
            break
        file.write(user)
