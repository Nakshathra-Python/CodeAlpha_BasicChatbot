import random

words = ["apple", "mango", "grapes", "orange", "banana"]

secret_word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_guesses = 6

print("Welcome to Hangman Game!")

while wrong_guesses < max_guesses:

    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("Congratulations! You guessed the word!")
        break

    guess = input("Guess a letter: ").lower()

    if guess in secret_word:
        guessed_letters.append(guess)
        print("Correct Guess!")

    else:
        wrong_guesses += 1
        print("Wrong Guess!")
        print("Remaining guesses:", max_guesses - wrong_guesses)

if wrong_guesses == max_guesses:
    print("\nGame Over!")
    print("The word was:", secret_word)