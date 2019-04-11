#  Word bank to random a word
#  User guesses the letters of the selected word
#  Generate empty spaces equal to the length of the selected word

import random
import string

lives = 10

word_bank = ['grim dawn', 'path of exile', 'talesweaver', 'maplestory', 'ragnarok online']

selected_word = list(random.choice(word_bank))
letters = list(string.ascii_letters + ' ')

#  marker for filling the correctly guessed letters
correct_answers = []
used_words = []

for x in range(1, len(selected_word)):
    correct_answers.append('_')
    print(correct_answers)


while lives != 0:

    #  answer key, depends on the length of the selected word

    print(''.join(selected_word))

    guess = str(input('Guess the letter: '))

    if guess in selected_word:
        letters.remove(guess)
        used_words.append(guess)
        correct_answers[position] = guess
        print(letters)
        print(used_words)

        if used_words == selected_word:
            print('You Won!')
            break

    elif guess not in selected_word:
        lives -= 1
        print(lives)
        print(letters)

    elif lives == 0:
        print('Game Over!')


