'''
#4. Create a poll.txt file that contains a list of "yea" or "nay" votes separated
by commas. Write a program that reads the poll.txt file
Count how many votes "yea" or "nay" received and print the results.
'''

yeas = 0
nays = 0
with open("poll.txt", "r") as file:
    votes = file.read().split(", ")
    for choice in votes:
        if (choice.lower() == "yea"):
            yeas += 1
        elif (choice.lower() == "nay"):
            nays += 1
    print(f"There are {yeas} yeas and {nays} nays.")
