import random, sys
import string

word_list = ['path of exile', 'talesweaver', 'maplestory','ragnarok online',
             'diablo 2', 'starcraft', 'warcraft 3','age of empire 2', 'grim dawn'
             ]

correct_answers = []
used_words = []
selected_word = list(random.choice(word_list))
letters = list(string.ascii_lowercase + ' ' + '1234567890')


def length_display():
    """Display's the length of the secret word to the player."""
    for char in selected_word:
        correct_answers.append(' ')
    print('The secret word is', len(selected_word), 'characters in length.\n' + str(correct_answers))
    print(selected_word, 'Answer, temporarily')


def game():
    """Main loop for the game where player inputs a character and see if it matches the secret word."""
    lives = 10

    while lives != 0:
        guess = input('Choose a letter: \n')
        if guess not in letters:
            print('Only use letters in the alphabet (a-z), numbers (0-9) or space')
        elif guess in used_words:
            print('You already tried this character. Try another!')
        else:
            used_words.append(guess)
            if correct_answers == selected_word:
                print('Congratz! You Won!')
                break
            elif guess in selected_word:
                print('Correct! Keep it up!')
                x = [i for i, e in enumerate(selected_word) if e == guess]
                for num in x:
                    correct_answers[num] = str(guess)
                    if correct_answers == selected_word:
                        print('Congratz! You Won!')
                print(correct_answers)
            else:
                print('This character is not part of the secret word! Try another!')
                lives -= 1
                print('You have', lives, 'remaining')
                print(correct_answers)
                if lives == 0:
                    print('You have no more lives! - Game Over -')


if __name__ == "__main__":
    length_display()
    game()
