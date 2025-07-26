import random

# List of predefined words
words = ["apple", "mango", "grape", "peach", "lemon"]

# Randomly select a word
word = random.choice(words)
guessed_word = ["_"] * len(word)
attempts = 6
guessed_letters = []

print("🎯 Welcome to Hangman Game!")
print("Guess the fruit name!")
print("You have", attempts, "lives.\n")

while attempts > 0 and "_" in guessed_word:
    print("Current word:", " ".join(guessed_word))
    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter. Try again.\n")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        print("✅ Good guess!\n")
    else:
        attempts -= 1
        print("❌ Wrong guess. Attempts left:", attempts, "\n")

if "_" not in guessed_word:
    print("🎉 Congrats! You guessed the word:", word)
else:
    print("💀 Game Over! The word was:", word)