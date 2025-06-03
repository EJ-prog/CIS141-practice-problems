'''
#3. Create a text file called song_lyrics.txt and copy the lyrics of a song into
it. Write a Python program that:
- Reads the file
- Requests 5 inputs from the user: 5 words the user would like to count the frequency of
- Counts how many times each word appears
- Creates a dictionary of the words and their counts
- Print the dictionary to the console
'''


words = input("What five words would you like to count the frequency of? (separate them with ',') ")
words_list = words.lower().split(",")
print(words_list)
words_count = {}
lyrics = open("song_lyrics.txt", "r")
for line in lyrics:
    lyric_lines = line.lower().strip().split(" ")
#    print(lyric_lines)
    for word in lyric_lines:
        if (word in words_list):
            if (word in words_count):
                words_count[word] += 1
            else:
                words_count[word] = 1
lyrics.close()
print(words_count)
