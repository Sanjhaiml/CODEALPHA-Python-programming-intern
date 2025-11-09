import random

# --- Step 1: Predefined list of 5 words ---
words = ["apple", "banana", "grapes", "orange", "mango"]

# --- Step 2: Randomly choose one word from the list ---
word = random.choice(words)

# --- Step 3: Initialize variables ---
guessed_word = ["_"] * len(word)
attempts = 6
guessed_letters = []

print(" Welcome to Hangman Game!")
print("Guess the word (fruit name):")

# --- Step 4: Game loop ---
while attempts > 0 and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Guessed letters:", ", ".join(guessed_letters))
    print(f"Remaining attempts: {attempts}")

    guess = input("Enter a letter: ").lower()

    # --- Step 5: Validate input ---
    if len(guess) != 1 or not guess.isalpha():
        print(" Please enter a single alphabet letter!")
        continue

    if guess in guessed_letters:
        print(" You already guessed that letter. Try again.")
        continue

    guessed_letters.append(guess)

    # --- Step 6: Check if guess is correct ---
    if guess in word:
        print("Good guess!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print(" Wrong guess!")
        attempts -= 1

# --- Step 7: End of game ---
if "_" not in guessed_word:
    print("\n Congratulations! You guessed the word:", word)
else:
    print("\n Game Over! The correct word was:", word)
