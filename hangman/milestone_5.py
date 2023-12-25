import random


class Hangman:
    '''
    This class is the final milestone where the basic game logic is completed.

    Attributes:
        word_list (list[str]): the list of words the game will choose at random.
        num_lives (int): the number of lives the player has at the start.

    '''
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for i in range(len(self.word))]
        self.list_of_guesses = []

    def check_guess(self, guess):
        '''
        This function checks if the letter is in the word or not.

        Args:
            guess (str): the letter the user has inputted to guess.
        '''
        guess = guess.lower()
        if guess in self.word:
            print('Good guess! {} is in the word'.format(guess))
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
        else:
                self.num_lives -= 1
                print('Sorry, {} is not in the word'.format(guess))
                print('You have {} lives left'.format(self.num_lives))
        print(' '.join(self.word_guessed))

    def ask_for_input(self):
        '''
        This function asks the user for a letter and checks if it is valid.

        Attributes:
            guess (str): the letter the user has inputted
        '''
        while True:
            guess = input('Guess a letter: ')
            if guess.isalpha() == False or len(guess) != 1:
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

    def play_game(self):
        '''
        This function checks if the user has won the game
        '''
        while True:
            if self.num_lives == 0:
                print('You lost!')
                break
            elif '_' in self.word_guessed:
                self.ask_for_input()
            else:
                print('Congratulations. You won the game!')
                break

fruit_list = ['orange', 'apple', 'kiwi', 'cherry', 'melon', 'banana']
hangman = Hangman(fruit_list, 5)
hangman.play_game()