import random

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        #word_list = ['orange', 'apple', 'kiwi', 'cherry', 'melon'] #for testing
        self.word = random.choice(word_list)
        self.word_guessed = ['_', '_', '_', '_', '_']
        self.num_letters = len(self.word)
        self.num_lives = 5
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess.lower()
        if guess in self.word:
            print('Good guess! {} is in the word'.format(guess))
        for letter in self.word:
            if letter == guess:
                self.word_guessed[self.word.index(letter)] = guess
        else:
         self.num_lives -= 1
         print('Sorry, {} is not in the word'.format(guess))
         print('You have {} lives left'.format(self.num_lives))
         print(' '.join(self.word_guessed))

    def ask_for_input(self):
        while True:
            guess = input('Guess a letter: ')
            if guess.isalpha() == False and len(guess) != 1:
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

fruit_list = ['orange', 'apple', 'kiwi', 'cherry', 'melon']
hangman = Hangman(fruit_list, 5)
Hangman.ask_for_input(hangman)