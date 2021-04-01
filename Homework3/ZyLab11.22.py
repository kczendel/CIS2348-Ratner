# Kyle Dela Pena
# 2038252

input_words = input().split()
for word in input_words:
    frequency = 0
    for same_word in input_words:
        if same_word == word:
            frequency += 1
    print(word, frequency)