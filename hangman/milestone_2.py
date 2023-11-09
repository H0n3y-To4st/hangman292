import random

def random_fruit():
    word_list = ['orange', 'apple', 'kiwi', 'cherry', 'melon']
    word = random.choice(word_list)
    return word

guess = input("Guess a letter: ")

def letter_guesser(guess):
    if len(guess) == 1 and guess.isalpha():
        print("Good guess!")
    else:
        print("Oops! That is not a valid input")

#print(word)