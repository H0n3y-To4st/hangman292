import random

word_list = ['orange', 'apple', 'kiwi', 'cherry', 'melon']
word = random.choice(word_list)

guess = input("Guess a letter: ")

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input")

#print(word)