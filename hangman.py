"""
CodeAlpha Internship Project
Project : Hangman game
Author : Krishna Pandey
Description : A console-based hangman game using python.
"""

import random

# list of predefined words
words = ["python", "coding", "letter", "github", "doctor"]

# Function to select a random word
def select_word():
    return random.choice(words)

# Function to display the word
def display_word(display):
    return " ".join(display)

# Function to process the guess
def process_guess(guess, word, display):
    if guess in word:
        print("Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
               display[i] = guess
        return True
    else:
        print("Wrong guess!")
        return False

# Main game function 
def play_game():

    # select a random word
    word = select_word()

    # Hide the word
    display = ["_"] * len(word)

    # Maximum incorrect guesses
    attempts = 6

    # Store guessed letters
    guessed_letters = set()

    # Game heading
    print("_" * 40)
    print("        HANGMAN GAME")
    print("_" * 40)
    print()
    print("Attempts remaining: ", attempts)

    # Main game loop
    while "_" in display and attempts > 0:
        guess = input("Enter a letter: ")

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter only one letter.")
            continue

        # Convert uppercase to lowercase
        guess = guess.lower()

        # Check repeated guess
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

       # Store the guess
        guessed_letters.add(guess)

       # Process the guess
        correct = process_guess(guess, word, display)

       # Reduce attempt if wrong
        if not correct:
            attempts -= 1

       # Display current status
        print()
        print("word:", display_word(display))
        print("Attempts remaining", attempts)
        print("Guessed letters", ", ".join(sorted(guessed_letters)) )
        print()

      # Final result
    if "_" not in display:
        print("\nCongratulations, You Won!")
        print("The word was:", word)

    else:
        print("\nGame Over!")
        print("The word was:", word)

# start the game
play_game()  
     