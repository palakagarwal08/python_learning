import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "camel"]

# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#  Set 'lives' to equal 6.

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

lives = 6

placeholder_array = list(placeholder)
print(placeholder_array)
while '_' in placeholder_array:
    if lives == 0:
        print("You lose!")
        break
    guess = input("Guess a letter: ").lower()
    i = 0
    for letter in chosen_word:
        if letter == guess:
            placeholder_array[i] = letter
        else:
            if placeholder_array[i] == '_':
                placeholder_array[i] = '_'
        i+=1
    if guess not in placeholder_array:
        lives = lives - 1
        print(stages[lives-1])

placeholder = "".join(placeholder_array)
if '_' not in placeholder:
    print("You win!")

