import random
word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter : ")
guess = guess.lower()

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.

def check_letter(chosen_word, guess):
    letter_exist = False
    for letter in chosen_word:
        if letter == guess:
            letter_exist = True
            return letter_exist
        else:
            letter_exist = False
    return letter_exist


if check_letter(chosen_word, guess):
    print("Right")
else:
    print("Wrong")