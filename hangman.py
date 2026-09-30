import random

# List of predefined words
words = ["python", "computer", "programming", "developer", "college"]

# Select a random word
word = random.choice(words)

# Create blanks for the word
guessed_word = ["_"] * len(word)

# Number of incorrect guesses allowed
attempts = 6

# Store letters already guessed
guessed_letters = []

print("================================")
print("       🎯 HANGMAN GAME")
print("================================")

print("Guess the word one letter at a time!")
print("You have", attempts, "incorrect guesses.")

while attempts > 0 and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Guessed letters:", " ".join(guessed_letters))
    print("Attempts remaining:", attempts)

    guess = input("Enter a letter: ").lower()

    # Check if input is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check whether the letter exists
    if guess in word:

        print("✅ Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess

    else:
        attempts -= 1
        print("❌ Wrong guess!")

# Final result
if "_" not in guessed_word:
    print("\n🎉 Congratulations!")
    print("You guessed the word:", word)
else:
    print("\n😢 Game Over!")
    print("The word was:", word)