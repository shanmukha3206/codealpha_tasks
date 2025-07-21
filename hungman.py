import random  # to pick a random word

#Define a list
words = ["game", "special", "friend", "snake", "family","occasion","education" ,"girl"]

#Pick a random word from the list
word_to_guess = random.choice(words)

#Set variables
guessed_word = ["_"] * len(word_to_guess)  # blanks for each letter
guessed_letters = []  # store guessed letters
incorrect_guesses = 0
max_guesses = 6

#using while loop
while incorrect_guesses < max_guesses and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Guessed letters:", guessed_letters)
    guess = input("Guess a letter: ").lower()

    #Check if guessed letter is valid and new
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    guessed_letters.append(guess)

    #Check if guessed letter is in word
    if guess in word_to_guess:
        print("Good guess!")
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == guess:
                guessed_word[i] = guess
    else:
        print("Wrong guess.")
        incorrect_guesses += 1
        print(f"Incorrect guesses: {incorrect_guesses}/{max_guesses}")

#last step of game
if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", word_to_guess)
else:
    print("\nYou lost! The word was:", word_to_guess)
