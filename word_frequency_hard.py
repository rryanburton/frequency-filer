import re

def word_frequency(text):
    return {"hello": 1}

# open file sample.txt and read in the words
# orig_text = str("""Project Gutenberg's The Hound of the Baskervilles, by A. Conan Doyle
#
# This eBook is for the use of anyone anywhere at no cost and with
# almost no restrictions whatsoever.  You may copy it, give it away or
# re-use it under the terms of the Project Gutenberg License included
# with this eBook or online at www.gutenberg.org
#
#
# Title: The Hound of the Baskervilles
#
# Author: A. Conan Doyle
#
# Posting Date: December 8, 2008 [EBook #2852]
# Release Date: October, 2001
#
# Language: English
#
#
# """

with open('sample.txt') as g:
    orig_text = g.read()

# split text into individual words
#word_list= orig_text.lower().split()
word_list = re.sub(r'[0-9,.!-?]', "", orig_text).lower().split()

# make word list into another list with unique words
unique_words = []

for word in word_list:
    if word in ignore_words:
        continue
    if word not in unique_words:
        unique_words.append(word)


#make a list of tuples w/(unique word: count)

word_counts = []

for unique in unique_words:
    count = 0
    for word in word_list:
        if word == unique:
            count += 1
    word_counts.append((unique, count))

#print(word_counts)
# sort tuples from highest to lowest
sorted_word_counts= sorted(word_counts, key=lambda s: s[1], reverse=True)

#print(unique_words)
print(sorted_word_counts)[:20]

#take top   20 words and output their count(s) to screen
