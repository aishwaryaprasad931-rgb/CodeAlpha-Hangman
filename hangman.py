import random

# List of 5 predefined words
words = ["python", "computer", "coding", "program", "developer"]

# Select a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of incorrect guesses allowed
incorrect_guesses = 6

print("Welcome to Hangman Game!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.")

# Create blanks for the word
display = ["_"] * len(word)

while incorrect_guesses > 0 and "_" in display:

    print("\nWord:", " ".join(display))
    
    guess = input("Enter a letter: ").lower()

    # Check if the letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check whether the letter is in the word
    if guess in word:
        print("Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess

    else:
        incorrect_guesses -= 1
        print("Wrong guess!")
        print("Remaining chances:", incorrect_guesses)

# Check the result
if "_" not in display:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over!")
    print("The word was:", word)