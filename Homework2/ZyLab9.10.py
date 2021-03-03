# Kyle Dela Pena
# 2038252

import csv

# Type your code here.
Frequency_of_words = {}

with open(input(), 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        for word in row:
            if word not in Frequency_of_words.keys():
                Frequency_of_words[word] = 1
            else:
                Frequency_of_words[word] += 1

for key in Frequency_of_words.keys():
    print(key + " " + str(Frequency_of_words[key]))
