import milestone_2 as m2

word = m2.random_fruit()

def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print("Good guess! {} is in the word.".format(guess))
    else:
        print("Sorry, {} is not in the word. Try again.".format(guess))

def ask_for_input():
    while(True):
        guess = input("Guess a letter: ")
        if guess.isalpha() and len(guess) == 1:
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)

result = ask_for_input()
print(result)