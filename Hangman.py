import random

def draw_hangman(incorrect_guesses):
    stages = [
        # 0
        """
           +---+
           |   |
               |
               |
               |
               |
        =========""",
        # 1
        """
           +---+
           |   |
           O   |
               |
               |
               |
        =========""",
        # 2
        """
           +---+
           |   |
           O   |
           |   |
               |
               |
        =========""",
        # 3
        """
           +---+
           |   |
           O   |
          /|   |
               |
               |
        =========""",
        # 4
        """
           +---+
           |   |
           O   |
          /|\  |
               |
               |
        =========""",
        # 5
        """
           +---+
           |   |
           O   |
          /|\  |
          /    |
               |
        =========""",
        # 6
        """
           +---+
           |   |
           O   |
          /|\  |
          / \  |
               |
        ========="""
    ]
    return stages[incorrect_guesses]

def choose_random_word():
    words = ["hangman", "python", "programming", "computer", "keyboard", "mouse", "monitor", "software"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def hangman():
    print("Welcome to Hangman!")
    word_to_guess = choose_random_word()
    guessed_letters = []
    incorrect_guesses = 0

    while incorrect_guesses < 6:
        print(draw_hangman(incorrect_guesses))
        print("Word:", display_word(word_to_guess, guessed_letters))

        if "_" not in display_word(word_to_guess, guessed_letters):
            print("Congratulations! You guessed the word:", word_to_guess)
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            incorrect_guesses += 1

    if incorrect_guesses == 6:
        print(draw_hangman(incorrect_guesses))
        print("Game Over. The word was:", word_to_guess)

if __name__ == "__main__":
    hangman()
