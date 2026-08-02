import random

def hangman_game():
    # List of 5 predefined words
    words = ["python", "coding", "alpha", "github", "program"]
    secret_word = random.choice(words)
    guessed_letters = []
    attempts_remaining = 6

    print("--- Welcome to the Hangman Game! ---")
    print(f"The computer has guessed a word with {len(secret_word)} letters.")

    # Game Loop
    while attempts_remaining > 0:
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print("\nCurrent word: ", display_word)
        print(f"Attempts remaining: {attempts_remaining}")
        
        # Check if user won
        if "_" not in display_word:
            print(f"🎉 Congratulations! You guessed the word correctly: '{secret_word}'")
            break

        guess = input("Guess a letter: ").lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue

        guessed_letters.append(guess)

        # Check if letter is in the secret word
        if guess in secret_word:
            print("Good job! That letter is in the word.")
        else:
            print("Wrong! That letter is not in the word.")
            attempts_remaining -= 1

    # Check if user lost
    if attempts_remaining == 0:
        print(f"\n😢 Game Over! You ran out of attempts.")
        print(f"The correct word was: '{secret_word}'")

if __name__ == "__main__":
    hangman_game()
